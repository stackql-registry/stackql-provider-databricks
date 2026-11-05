"""Multi-cloud host resolution for the generated providers (AWS, Azure, GCP).

Two layers are pinned here:

1. A snapshot of what the generated ``provider.yaml`` and every service's
   ``servers`` block declare: the token URL, the server URL templates and the
   ``x-stackQL-envVar`` / ``x-stackQL-envVarSelector`` annotations. This is
   the contract the stackql host resolves against.
2. A reference implementation of the resolution rules (the same order the
   omnisdk ``ServerVariableSpec.Resolve`` function applies: verbatim env var,
   else selector entry for its env var, else selector default) applied to
   those declarations, asserting the resolved token URL and base URLs with no
   environment (byte-for-byte the published AWS values), with
   ``DATABRICKS_CLOUD`` set to ``azure`` / ``gcp``, and with the explicit
   ``DATABRICKS_ACCOUNT_HOST`` override.

The generated output must exist (``make providers``); the tests are skipped
otherwise.
"""

import json
import re
from pathlib import Path

import pytest
import yaml

PROVIDER_DIR = Path(__file__).resolve().parent.parent
OUTPUT = PROVIDER_DIR / "stackql-provider" / "src"
CONFIG = PROVIDER_DIR / "provider-config"
VERSION = "v00.00.00000"

ACCOUNT_HOSTS = {
    "aws": "accounts.cloud.databricks.com",
    "azure": "accounts.azuredatabricks.net",
    "gcp": "accounts.gcp.databricks.com",
}
WORKSPACE_DOMAINS = {
    "aws": "cloud.databricks.com",
    "azure": "azuredatabricks.net",
    "gcp": "gcp.databricks.com",
}
PUBLISHED_TOKEN_URL = (
    "https://accounts.cloud.databricks.com/oidc/accounts/{{ .__env__DATABRICKS_ACCOUNT_ID }}/v1/token"
)
PUBLISHED_ACCOUNT_BASE_URL = "https://accounts.cloud.databricks.com"
PUBLISHED_WORKSPACE_BASE_URL = "https://{deployment_name}.cloud.databricks.com"


def provider_yaml(provider):
    path = OUTPUT / provider / VERSION / "provider.yaml"
    if not path.exists():
        pytest.skip(f"{path} not generated (run make providers)")
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def service_files(provider):
    services = sorted((OUTPUT / provider / VERSION / "services").glob("*.yaml"))
    if not services:
        pytest.skip(f"no services generated for {provider} (run make providers)")
    return services


def servers_of(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))["servers"]


# ---------------------------------------------------------------------------
# Reference resolver (mirrors omnisdk aot.ServerVariableSpec.Resolve)
# ---------------------------------------------------------------------------


def resolve_variable(name, spec, env):
    """Return the variable's value from ``env`` or raise when unresolvable."""
    verbatim = spec.get("x-stackQL-envVar")
    if verbatim and env.get(verbatim, "").strip():
        return env[verbatim].strip().rstrip("/")
    selector = spec.get("x-stackQL-envVarSelector")
    if not selector:
        raise LookupError(f"{name} requires a query predicate")
    key = env.get(selector["envVar"], "").strip() or selector.get("default", "")
    if key not in selector["values"]:
        raise ValueError(f"{selector['envVar']}={key!r} is not one of {sorted(selector['values'])}")
    return selector["values"][key]


def resolve_url(template, variables, env, bindings=None):
    """Substitute every declared variable; ``bindings`` are query predicates."""
    out = template
    for name, spec in variables.items():
        if bindings and name in bindings:
            value = bindings[name]
        else:
            value = resolve_variable(name, spec, env)
        out = out.replace("{" + name + "}", value)
    return out


# ---------------------------------------------------------------------------
# Snapshot of the generated declarations
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("provider", ["databricks_account", "databricks_workspace"])
def test_token_url_declares_cloud_selected_account_host(provider):
    auth = provider_yaml(provider)["config"]["auth"]
    assert auth["type"] == "oauth2"
    assert auth["grant_type"] == "client_credentials"
    assert auth["client_id_env_var"] == "DATABRICKS_CLIENT_ID"
    assert auth["client_secret_env_var"] == "DATABRICKS_CLIENT_SECRET"
    assert auth["scopes"] == ["all-apis"]
    # YAML folding may rewrap the template; the env lookup keeps the {{ .__env__NAME }} convention
    token_url = re.sub(r"\s+", " ", auth["token_url"])
    assert token_url == "https://{account_host}/oidc/accounts/{{ .__env__DATABRICKS_ACCOUNT_ID }}/v1/token"
    host = auth["variables"]["account_host"]
    assert host["default"] == ACCOUNT_HOSTS["aws"]
    assert host["x-stackQL-envVar"] == "DATABRICKS_ACCOUNT_HOST"
    assert host["x-stackQL-envVarSelector"] == {
        "envVar": "DATABRICKS_CLOUD",
        "default": "aws",
        "values": ACCOUNT_HOSTS,
    }
    assert auth == yaml.safe_load(json.dumps(json.load((CONFIG / "provider_config.json").open())["auth"]))


def test_every_account_service_declares_the_same_servers():
    expected = json.load((CONFIG / "account_servers.json").open(encoding="utf-8"))
    for path in service_files("databricks_account"):
        assert servers_of(path) == expected, path.name
    (server,) = expected
    assert server["url"] == "https://{account_host}"
    assert server["variables"]["account_host"]["x-stackQL-envVarSelector"]["values"] == ACCOUNT_HOSTS


def test_every_workspace_service_declares_the_same_servers():
    expected = json.load((CONFIG / "workspace_servers.json").open(encoding="utf-8"))
    for path in service_files("databricks_workspace"):
        assert servers_of(path) == expected, path.name
    (server,) = expected
    assert server["url"] == "https://{deployment_name}.{workspace_domain}"
    deployment = server["variables"]["deployment_name"]
    assert deployment["default"] == "dbc-abcd0123-a1bc"
    assert deployment["x-stackQL-envVar"] == "DATABRICKS_DEPLOYMENT_NAME"
    assert "x-stackQL-envVarSelector" not in deployment  # stays a query predicate unless the env var is set
    domain = server["variables"]["workspace_domain"]
    assert domain["default"] == WORKSPACE_DOMAINS["aws"]
    assert domain["x-stackQL-envVarSelector"] == {
        "envVar": "DATABRICKS_CLOUD",
        "default": "aws",
        "values": WORKSPACE_DOMAINS,
    }
    assert "x-stackQL-envVar" not in domain  # DATABRICKS_CLOUD is the only switch for the suffix


# ---------------------------------------------------------------------------
# Resolution: no environment is byte-for-byte the published AWS provider
# ---------------------------------------------------------------------------


def account_servers():
    (server,) = servers_of(service_files("databricks_account")[0])
    return server


def workspace_servers():
    (server,) = servers_of(service_files("databricks_workspace")[0])
    return server


def token_url_for(provider, env):
    auth = provider_yaml(provider)["config"]["auth"]
    template = re.sub(r"\s+", " ", auth["token_url"])
    return resolve_url(template, auth["variables"], env)


@pytest.mark.parametrize("provider", ["databricks_account", "databricks_workspace"])
def test_no_environment_matches_published_token_url(provider):
    assert token_url_for(provider, {}) == PUBLISHED_TOKEN_URL


def test_no_environment_matches_published_account_base_url():
    server = account_servers()
    assert resolve_url(server["url"], server["variables"], {}) == PUBLISHED_ACCOUNT_BASE_URL


def test_no_environment_matches_published_workspace_base_url():
    server = workspace_servers()
    # deployment_name has no selector: it stays the query predicate it is today
    with pytest.raises(LookupError):
        resolve_url(server["url"], server["variables"], {})
    assert (
        resolve_url(server["url"], server["variables"], {}, bindings={"deployment_name": "{deployment_name}"})
        == PUBLISHED_WORKSPACE_BASE_URL
    )
    assert (
        resolve_url(server["url"], server["variables"], {}, bindings={"deployment_name": "dbc-abcd0123-a1bc"})
        == "https://dbc-abcd0123-a1bc.cloud.databricks.com"
    )


@pytest.mark.parametrize("cloud", ["azure", "gcp"])
@pytest.mark.parametrize("provider", ["databricks_account", "databricks_workspace"])
def test_cloud_selects_token_endpoint(provider, cloud):
    assert token_url_for(provider, {"DATABRICKS_CLOUD": cloud}) == PUBLISHED_TOKEN_URL.replace(
        ACCOUNT_HOSTS["aws"], ACCOUNT_HOSTS[cloud]
    )


@pytest.mark.parametrize("cloud", ["aws", "azure", "gcp"])
def test_cloud_selects_account_host(cloud):
    server = account_servers()
    assert resolve_url(server["url"], server["variables"], {"DATABRICKS_CLOUD": cloud}) == f"https://{ACCOUNT_HOSTS[cloud]}"


@pytest.mark.parametrize(
    "cloud, deployment",
    [("aws", "dbc-abcd0123-a1bc"), ("azure", "adb-1234567890123456.7"), ("gcp", "1234567890123456.7")],
)
def test_cloud_selects_workspace_domain(cloud, deployment):
    server = workspace_servers()
    url = resolve_url(server["url"], server["variables"], {"DATABRICKS_CLOUD": cloud}, {"deployment_name": deployment})
    assert url == f"https://{deployment}.{WORKSPACE_DOMAINS[cloud]}"
    # the env var defaults the predicate for the session
    env = {"DATABRICKS_CLOUD": cloud, "DATABRICKS_DEPLOYMENT_NAME": deployment}
    assert resolve_url(server["url"], server["variables"], env) == url


@pytest.mark.parametrize("provider", ["databricks_account", "databricks_workspace"])
def test_account_host_override_wins_over_cloud(provider):
    env = {"DATABRICKS_CLOUD": "gcp", "DATABRICKS_ACCOUNT_HOST": "accounts.example.test/"}
    assert token_url_for(provider, env) == PUBLISHED_TOKEN_URL.replace(ACCOUNT_HOSTS["aws"], "accounts.example.test")
    server = account_servers()
    assert resolve_url(server["url"], server["variables"], env) == "https://accounts.example.test"


def test_unknown_cloud_is_an_error_not_a_fallback():
    server = account_servers()
    with pytest.raises(ValueError):
        resolve_url(server["url"], server["variables"], {"DATABRICKS_CLOUD": "oci"})


def test_hosts_are_written_in_the_config_files_only():
    """The PR review checklist: the Databricks hosts live in provider-config/*.json
    (and the openapi_generated specs they override), nowhere else in the tooling."""
    sources = [p for p in PROVIDER_DIR.glob("*.py")] + [PROVIDER_DIR / "Makefile"]
    for path in sources:
        text = path.read_text(encoding="utf-8")
        for host in ("accounts.cloud.databricks.com", "azuredatabricks.net", "gcp.databricks.com"):
            assert host not in text, f"{path.name} hard-codes {host}; master it in provider-config/"
