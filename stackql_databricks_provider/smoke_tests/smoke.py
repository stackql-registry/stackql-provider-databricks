"""
Authenticated smoke tests for the StackQL Databricks providers.

Three layers, in order:

1. Resource queries - the SELECTs most people run first (workspaces, account
   groups, the current user, clusters, SQL warehouses, secret scopes), each
   asserted to return rows with the documented columns.
2. Lifecycles - cheap, self-cleaning mutations through the SQL verbs: an
   account SCIM group (exists / INSERT / exports / DELETE, the stackql-deploy
   shape) and a workspace secret scope (INSERT / SELECT / EXEC delete). Both
   are free of charge: no compute is created. Everything is named
   ``stackql-smoke-<stamp>`` and removed again; ``--read-only`` skips them.
3. Views - SELECT * against every view under ``views/{account,workspace}``,
   asserting the documented columns.

Modes:
  local (default) - tests the locally generated provider in ``stackql-provider/``
                    via a ``file://`` registry (run after ``make providers``)
  --live          - pulls the latest published providers from the public StackQL
                    registry and tests those instead

Both modes are authenticated: set DATABRICKS_ACCOUNT_ID, DATABRICKS_CLIENT_ID
and DATABRICKS_CLIENT_SECRET (or put them in ``stackql_databricks_provider/.env``;
``--env-file`` points at another file, e.g. ``.env.azure``). The cloud is
selected the way the provider selects it: DATABRICKS_CLOUD = aws (default) |
azure | gcp (``--cloud`` sets it for the run) and the optional
DATABRICKS_ACCOUNT_HOST override. DATABRICKS_DEPLOYMENT_NAME is optional; when
unset the workspace deployment name is derived from
``databricks_account.provisioning.workspaces``.

Usage:
  python smoke_tests/smoke.py [--live] [--cloud aws|azure|gcp] [--env-file PATH]
                              [--read-only] [--scope account|workspace|all]
                              [--view SUBSTR] [--verbose]
"""

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("pyyaml is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

PROVIDER_DIR = Path(__file__).resolve().parent.parent
VIEWS_DIR = PROVIDER_DIR / "views"
REGISTRY_DIR = PROVIDER_DIR / "stackql-provider"
QUERY_TIMEOUT_SECONDS = 240

REQUIRED_ENV = ["DATABRICKS_ACCOUNT_ID", "DATABRICKS_CLIENT_ID", "DATABRICKS_CLIENT_SECRET"]

PROVIDER_BY_SCOPE = {"account": "databricks_account", "workspace": "databricks_workspace"}

# Named ANSI-less status labels keep output greppable in CI logs.
PASS, EMPTY, FAIL, SKIP = "PASS", "EMPTY", "FAIL", "SKIP"

# Views over APIs that exist only on some clouds. Databricks answers with an
# HTML page (Azure) or 503 TEMPORARILY_UNAVAILABLE (GCP) rather than a clean
# 404, so the harness skips them up front instead of reporting a failure.
# Keys are "<scope>.<service>.<view>", values the clouds that lack the API.
NOT_APPLICABLE_VIEWS = {
    "account.provisioning.vw_networks": {"azure"},
    "account.provisioning.vw_network_errors": {"azure"},
    "account.provisioning.vw_network_warnings": {"azure"},
    "account.provisioning.vw_credentials": {"azure", "gcp"},
    "account.provisioning.vw_storage_configurations": {"azure"},
    "account.provisioning.vw_vpc_endpoints": {"azure"},
}

# stackql exits 0 on planning, transport and HTTP errors and only writes them to
# stderr, so an empty stdout is classified EMPTY only when stderr shows none of
# these. The transport patterns (an unexpandable token URL, a server variable
# that reached the host name unbound) matter because they carry no "error" word.
ERROR_LINE_PATTERN = (
    r"error|unsatisfied|cannot find|unauthorized|status code: [45]\d\d"
    r"|no host in request url|invalid character|^parse \""
)
FATAL_STDERR_PATTERN = (
    r"http response status code|cannot fetch token|unsatisfied required|unauthorized"
    r"|no host in request url|invalid character|^parse \""
)


def load_dotenv(path, override=False):
    """Load KEY=VALUE pairs from a .env file.

    The default ``.env`` never overrides the environment; a file the caller
    named explicitly (``--env-file``, ``make smoke CLOUD=azure``) does, so a
    shell that still exports the AWS credentials cannot leak into an Azure run.
    """
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and (override or key not in os.environ):
            os.environ[key] = value


def find_stackql(cli_arg):
    """Resolve the stackql binary: --stackql-bin, STACKQL_BIN, repo-local, PATH."""
    candidates = []
    if cli_arg:
        candidates.append(cli_arg)
    if os.environ.get("STACKQL_BIN"):
        candidates.append(os.environ["STACKQL_BIN"])
    exe = "stackql.exe" if platform.system() == "Windows" else "stackql"
    candidates.append(str(PROVIDER_DIR / exe))
    which = shutil.which("stackql")
    if which:
        candidates.append(which)
    for c in candidates:
        if c and Path(c).exists():
            return str(Path(c).resolve())
    return None


def discover_views(views_dir, scope_filter, name_filter):
    """Yield dicts describing each view found under views/{scope}/{service}/views.yaml."""
    views = []
    for path in sorted(views_dir.glob("*/*/views.yaml")):
        scope, service = path.parent.parent.name, path.parent.name
        if scope_filter != "all" and scope != scope_filter:
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for view_name, view_def in doc.items():
            if name_filter and name_filter not in view_name:
                continue
            docs_cfg = (view_def.get("config", {}) or {}).get("docs", {}) or {}
            fields = [f["name"] for f in docs_cfg.get("fields", []) if isinstance(f, dict) and "name" in f]
            params = [p["name"] for p in docs_cfg.get("requiredParams", []) if isinstance(p, dict) and "name" in p]
            views.append(
                {
                    "scope": scope,
                    "service": service,
                    "name": view_name,
                    "fields": fields,
                    "params": params,
                }
            )
    return views


class StackQLRunner:
    def __init__(self, binary, live, verbose):
        self.binary = binary
        self.live = live
        self.verbose = verbose
        approot = PROVIDER_DIR / (".stackql-smoke-live" if live else ".stackql-smoke")
        approot.mkdir(exist_ok=True)
        self.base_args = [binary, "--approot", str(approot)]
        if not live:
            reg_path = REGISTRY_DIR.resolve().as_posix()
            reg = {
                "url": f"file://{reg_path}",
                "localDocRoot": reg_path,
                "verifyConfig": {"nopVerify": True},
            }
            self.base_args += ["--registry", json.dumps(reg)]

    def exec(self, sql, output="json"):
        """Run one statement; returns (ok, rows_or_None, message)."""
        cmd = self.base_args + ["exec", "-o", output, sql]
        if self.verbose:
            print(f"    $ stackql exec: {sql}")
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True, timeout=QUERY_TIMEOUT_SECONDS
            )
        except subprocess.TimeoutExpired:
            return False, None, f"timed out after {QUERY_TIMEOUT_SECONDS}s"
        stdout, stderr = proc.stdout.strip(), proc.stderr.strip()
        err_line = next(
            (l for l in stderr.splitlines() if "error" in l.lower() and "http response" in l.lower()),
            "",
        )
        # stackql exits 0 on a planning or HTTP error and reports it on stderr,
        # so a mutation is only ok when nothing on stderr looks like one.
        stderr_error = next(
            (l for l in stderr.splitlines()
             if re.search(ERROR_LINE_PATTERN, l, re.I)),
            "",
        )
        if output != "json":
            ok = proc.returncode == 0 and not stderr_error
            return ok, None, stdout if ok else (err_line or stderr_error or stderr or stdout)
        # An HTTP or token failure on stderr makes any rows on stdout suspect
        # (a COUNT(*) over a failed read still prints 0).
        fatal = re.search(FATAL_STDERR_PATTERN, stderr, re.I | re.M)
        if stdout and not fatal:
            try:
                rows = json.loads(stdout)
                if isinstance(rows, list):
                    return True, rows, ""
            except json.JSONDecodeError:
                pass
        # No parseable JSON: an empty result set or a genuine error.
        blob = (stdout + "\n" + stderr).lower()
        if proc.returncode == 0 and not fatal and "error" not in blob and "cannot find" not in blob and "unauthorized" not in blob:
            return True, [], ""
        return False, None, (err_line or stderr or stdout or f"exit code {proc.returncode}")

    def pull(self, provider):
        return self.exec(f"REGISTRY PULL {provider};", output="text")


def derive_seed_params(runner, account_id):
    """Best-effort derivation of parameters needed by multi-param views."""
    seeds = {"account_id": account_id}
    if os.environ.get("DATABRICKS_DEPLOYMENT_NAME"):
        seeds["deployment_name"] = os.environ["DATABRICKS_DEPLOYMENT_NAME"]
    if os.environ.get("DATABRICKS_METASTORE_ID"):
        seeds["metastore_id"] = os.environ["DATABRICKS_METASTORE_ID"]

    if "deployment_name" not in seeds or "workspace_id" not in seeds:
        ok, rows, _ = runner.exec(
            "SELECT workspace_id, deployment_name FROM databricks_account.provisioning.workspaces "
            f"WHERE account_id = '{account_id}' AND workspace_status = 'RUNNING' LIMIT 1"
        )
        if ok and rows:
            seeds.setdefault("deployment_name", str(rows[0].get("deployment_name", "")))
            seeds.setdefault("workspace_id", str(rows[0].get("workspace_id", "")))

    if "metastore_id" not in seeds:
        ok, rows, _ = runner.exec(
            "SELECT metastore_id FROM databricks_account.catalog.metastores "
            f"WHERE account_id = '{account_id}' LIMIT 1"
        )
        if ok and rows and rows[0].get("metastore_id"):
            seeds["metastore_id"] = str(rows[0]["metastore_id"])

    return {k: v for k, v in seeds.items() if v}


def run_view_test(runner, view, seeds):
    """Execute SELECT * against one view and classify the outcome."""
    provider = PROVIDER_BY_SCOPE[view["scope"]]
    fqn = f"{provider}.{view['service']}.{view['name']}"

    cloud = os.environ.get("DATABRICKS_CLOUD") or "aws"
    if cloud in NOT_APPLICABLE_VIEWS.get(f"{view['scope']}.{view['service']}.{view['name']}", set()):
        return SKIP, 0, f"API not available on {cloud}"

    missing = [p for p in view["params"] if p not in seeds]
    if missing:
        return SKIP, 0, f"no seed value for param(s): {', '.join(missing)}"

    where = " AND ".join(f"{p} = '{seeds[p]}'" for p in view["params"])
    sql = f"SELECT * FROM {fqn}"
    if where:
        sql += f" WHERE {where}"
    sql += " LIMIT 5"

    ok, rows, message = runner.exec(sql)
    if not ok:
        # Several Databricks list APIs return a bare {} when there is no data,
        # which stackql surfaces as an objectKey extraction error - that is an
        # empty result, not a provider defect.
        if "unknown key" in message:
            return EMPTY, 0, "upstream returned an empty response object"
        # Feature not licensed on this account (e.g. pricing tier) - environmental.
        if "required pricing tier" in message:
            return SKIP, 0, "feature not available on this account's pricing tier"
        return FAIL, 0, message[:300]
    if not rows:
        return EMPTY, 0, "query succeeded, zero rows returned"

    expected = set(view["fields"])
    actual = set(rows[0].keys())
    missing_cols = expected - actual
    if missing_cols:
        return FAIL, len(rows), f"missing expected column(s): {', '.join(sorted(missing_cols))}"
    return PASS, len(rows), ""


# ---------------------------------------------------------------------------
# Resource queries: the SELECTs most people run first on each provider.
# ``expect_rows`` marks the ones that always return data on any account.
# ---------------------------------------------------------------------------

RESOURCE_QUERIES = [
    {
        "scope": "account",
        "name": "provisioning.workspaces",
        "sql": "SELECT workspace_id, workspace_name, workspace_status, deployment_name "
               "FROM databricks_account.provisioning.workspaces WHERE account_id = '{account_id}'",
        "columns": ["workspace_id", "workspace_name", "workspace_status", "deployment_name"],
        "expect_rows": True,
    },
    {
        "scope": "account",
        "name": "iam.account_groups",
        "sql": "SELECT id, displayName FROM databricks_account.iam.account_groups WHERE account_id = '{account_id}'",
        "columns": ["id", "displayName"],
        "expect_rows": False,
    },
    {
        "scope": "workspace",
        "name": "iam.current_user",
        "sql": "SELECT id, userName FROM databricks_workspace.iam.current_user WHERE deployment_name = '{deployment_name}'",
        "columns": ["id", "userName"],
        "expect_rows": True,
    },
    {
        "scope": "workspace",
        "name": "catalog.catalogs",
        "sql": "SELECT name, catalog_type FROM databricks_workspace.catalog.catalogs WHERE deployment_name = '{deployment_name}'",
        "columns": ["name", "catalog_type"],
        "expect_rows": True,
    },
    {
        "scope": "workspace",
        "name": "compute.clusters",
        "sql": "SELECT cluster_id, cluster_name, state FROM databricks_workspace.compute.clusters WHERE deployment_name = '{deployment_name}'",
        "columns": ["cluster_id", "cluster_name", "state"],
        "expect_rows": False,
    },
    {
        "scope": "workspace",
        "name": "sql.warehouses",
        "sql": "SELECT id, name, state FROM databricks_workspace.sql.warehouses WHERE deployment_name = '{deployment_name}'",
        "columns": ["id", "name", "state"],
        "expect_rows": False,
    },
    {
        "scope": "workspace",
        "name": "workspace.secret_scopes",
        "sql": "SELECT name FROM databricks_workspace.workspace.secret_scopes WHERE deployment_name = '{deployment_name}'",
        "columns": ["name"],
        "expect_rows": False,
    },
]


def run_resource_test(runner, query, seeds):
    """Run one resource SELECT and classify the outcome."""
    params = re.findall(r"\{(\w+)\}", query["sql"])
    missing = [p for p in params if p not in seeds]
    if missing:
        return SKIP, 0, f"no seed value for param(s): {', '.join(missing)}"
    ok, rows, message = runner.exec(query["sql"].format(**seeds))
    if not ok:
        if "unknown key" in message:
            return EMPTY, 0, "upstream returned an empty response object"
        if "required pricing tier" in message:
            return SKIP, 0, "feature not available on this account's pricing tier"
        return FAIL, 0, message[:300]
    if not rows:
        if query["expect_rows"]:
            return FAIL, 0, "expected at least one row"
        return EMPTY, 0, "query succeeded, zero rows returned"
    missing_cols = set(query["columns"]) - set(rows[0].keys())
    if missing_cols:
        return FAIL, len(rows), f"missing expected column(s): {', '.join(sorted(missing_cols))}"
    return PASS, len(rows), ""


# ---------------------------------------------------------------------------
# Lifecycles: self-cleaning create/read/delete through the SQL verbs. Free of
# charge (no compute). Each step is reported; a failure still runs the delete.
# ---------------------------------------------------------------------------


def smoke_name():
    return f"stackql-smoke-{time.strftime('%Y%m%d%H%M%S')}"


def lifecycle_account_group(runner, seeds, report):
    """The stackql-deploy shape: exists / create / exports / delete on an account SCIM group."""
    if "account_id" not in seeds:
        report("account.iam.account_groups lifecycle", SKIP, "no account_id")
        return
    account_id, group_name = seeds["account_id"], smoke_name()
    exists_sql = (
        "SELECT COUNT(*) as count FROM databricks_account.iam.account_groups "
        f"WHERE account_id = '{account_id}' AND displayName = '{group_name}'"
    )
    group_id = None
    try:
        ok, rows, message = runner.exec(exists_sql)
        count = int(rows[0]["count"]) if ok and rows else (0 if ok else None)
        report("account.iam.account_groups exists (before)", PASS if count == 0 else FAIL,
               message if not ok else f"count={count}")

        ok, _, message = runner.exec(
            "INSERT INTO databricks_account.iam.account_groups (account_id, displayName) "
            f"SELECT '{account_id}', '{group_name}'",
            output="text",
        )
        report("account.iam.account_groups INSERT", PASS if ok else FAIL, message if not ok else group_name)
        if not ok:
            return

        ok, rows, message = runner.exec(
            "SELECT id AS databricks_group_id FROM databricks_account.iam.account_groups "
            f"WHERE account_id = '{account_id}' AND displayName = '{group_name}'"
        )
        group_id = rows[0].get("databricks_group_id") if ok and rows else None
        report("account.iam.account_groups exports", PASS if group_id else FAIL,
               message if not ok else f"databricks_group_id={group_id}")

        ok, rows, message = runner.exec(exists_sql)
        count = int(rows[0]["count"]) if ok and rows else None
        report("account.iam.account_groups exists (after create)", PASS if count == 1 else FAIL,
               message if not ok else f"count={count}")
    finally:
        if group_id:
            ok, _, message = runner.exec(
                "DELETE FROM databricks_account.iam.account_groups "
                f"WHERE account_id = '{account_id}' AND id = '{group_id}'",
                output="text",
            )
            report("account.iam.account_groups DELETE", PASS if ok else FAIL, message if not ok else "")
            if ok:
                ok, rows, message = runner.exec(exists_sql)
                count = int(rows[0]["count"]) if ok and rows else (0 if ok else None)
                report("account.iam.account_groups exists (after delete)", PASS if count == 0 else FAIL,
                       message if not ok else f"count={count}")


def lifecycle_secret_scope(runner, seeds, report):
    """INSERT / SELECT / EXEC delete on a workspace secret scope."""
    if "deployment_name" not in seeds:
        report("workspace.workspace.secret_scopes lifecycle", SKIP, "no deployment_name")
        return
    deployment, scope = seeds["deployment_name"], smoke_name()
    created = False
    try:
        ok, _, message = runner.exec(
            "INSERT INTO databricks_workspace.workspace.secret_scopes (deployment_name, scope) "
            f"SELECT '{deployment}', '{scope}'",
            output="text",
        )
        created = ok
        report("workspace.workspace.secret_scopes INSERT", PASS if ok else FAIL, message if not ok else scope)
        if not ok:
            return
        ok, rows, message = runner.exec(
            "SELECT name FROM databricks_workspace.workspace.secret_scopes "
            f"WHERE deployment_name = '{deployment}' AND name = '{scope}'"
        )
        found = ok and rows and rows[0].get("name") == scope
        report("workspace.workspace.secret_scopes SELECT", PASS if found else FAIL,
               message if not ok else ("found" if found else "scope not listed"))
    finally:
        if created:
            # Named arguments reach the body on both engines; the @@json form is
            # rejected by the any-sdk based releases (v0.12.x) for this method.
            ok, _, message = runner.exec(
                f"EXEC databricks_workspace.workspace.secret_scopes.delete "
                f"@deployment_name = '{deployment}', @scope = '{scope}'",
                output="text",
            )
            report("workspace.workspace.secret_scopes EXEC delete", PASS if ok else FAIL, message if not ok else "")
            ok, rows, message = runner.exec(
                "SELECT name FROM databricks_workspace.workspace.secret_scopes "
                f"WHERE deployment_name = '{deployment}' AND name = '{scope}'"
            )
            # A workspace with no scopes left answers {} and stackql reports the
            # missing objectKey ("unknown key scopes"): that is an empty list.
            gone = (ok and not rows) or (not ok and "unknown key" in message)
            report("workspace.workspace.secret_scopes SELECT (after delete)", PASS if gone else FAIL,
                   message if not ok and not gone else ("" if gone else f"{scope} still listed - remove it by hand"))


def main():
    parser = argparse.ArgumentParser(description="Databricks provider smoke tests")
    parser.add_argument("--live", action="store_true", help="test latest published providers from the public registry")
    parser.add_argument("--cloud", choices=["aws", "azure", "gcp"], default=None,
                        help="set DATABRICKS_CLOUD for the run (default: the environment, else aws)")
    parser.add_argument("--env-file", default=None,
                        help="env file to load (default: stackql_databricks_provider/.env)")
    parser.add_argument("--read-only", action="store_true", help="skip the create/delete lifecycles")
    parser.add_argument("--skip-views", action="store_true", help="skip the view layer")
    parser.add_argument("--scope", choices=["account", "workspace", "all"], default="all")
    parser.add_argument("--view", default=None, help="only run views whose name contains this substring")
    parser.add_argument("--stackql-bin", default=None, help="path to the stackql binary")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    default_env = (PROVIDER_DIR / ".env").resolve()
    env_file = Path(args.env_file).resolve() if args.env_file else default_env
    if env_file != default_env:
        # A per-cloud file named explicitly (.env.azure, .env.gcp) must exist and wins
        # over whatever the shell still exports.
        if not env_file.exists():
            print(f"ERROR: env file not found: {env_file} (copy the matching .env.<cloud>.example)", file=sys.stderr)
            return 2
        load_dotenv(env_file, override=True)
    else:
        load_dotenv(env_file)
    if args.cloud:
        os.environ["DATABRICKS_CLOUD"] = args.cloud

    missing_env = [v for v in REQUIRED_ENV if not os.environ.get(v)]
    if missing_env:
        print(f"ERROR: missing required environment variable(s): {', '.join(missing_env)}", file=sys.stderr)
        print("Set them in the environment or in stackql_databricks_provider/.env", file=sys.stderr)
        return 2

    binary = find_stackql(args.stackql_bin)
    if not binary:
        print("ERROR: stackql binary not found (try 'make stackql' or set STACKQL_BIN)", file=sys.stderr)
        return 2

    if not args.live and not REGISTRY_DIR.exists():
        print(f"ERROR: local registry not found at {REGISTRY_DIR} (run 'make providers' first)", file=sys.stderr)
        return 2

    mode = "live (public registry)" if args.live else f"local ({REGISTRY_DIR})"
    cloud = os.environ.get("DATABRICKS_CLOUD") or "aws (default)"
    host_override = os.environ.get("DATABRICKS_ACCOUNT_HOST")
    print(f"Databricks provider smoke tests - mode: {mode}")
    print(f"stackql binary: {binary}")
    print(f"cloud: {cloud}" + (f" (DATABRICKS_ACCOUNT_HOST={host_override})" if host_override else ""))

    runner = StackQLRunner(binary, args.live, args.verbose)

    if args.live:
        for provider in ("databricks_account", "databricks_workspace"):
            ok, _, message = runner.pull(provider)
            print(f"  registry pull {provider}: {'ok' if ok else 'FAILED - ' + message[:200]}")

    account_id = os.environ["DATABRICKS_ACCOUNT_ID"]
    print("Deriving seed parameters...")
    seeds = derive_seed_params(runner, account_id)
    print(f"  seed params available: {', '.join(sorted(seeds))}")

    results = []

    def report(name, status, message="", row_count=0, elapsed=0.0):
        results.append((name, status, row_count, elapsed, message))
        note = f" ({message})" if message and status in (FAIL, SKIP) else (f" {message}" if message and args.verbose else "")
        print(f"  [{status:<5}] {name:<75} rows={row_count:<3} {elapsed:5.1f}s{note}")

    scoped = lambda scope: args.scope in ("all", scope)  # noqa: E731

    queries = [q for q in RESOURCE_QUERIES if scoped(q["scope"])]
    print(f"\nResource queries ({len(queries)})...")
    for query in queries:
        started = time.monotonic()
        status, row_count, message = run_resource_test(runner, query, seeds)
        report(f"{PROVIDER_BY_SCOPE[query['scope']]}.{query['name']}", status, message, row_count, time.monotonic() - started)

    if args.read_only:
        print("\nLifecycles skipped (--read-only)")
    else:
        print("\nLifecycles (self-cleaning, no compute)...")
        if scoped("account"):
            lifecycle_account_group(runner, seeds, report)
        if scoped("workspace"):
            lifecycle_secret_scope(runner, seeds, report)

    if args.skip_views:
        views = []
    else:
        views = discover_views(VIEWS_DIR, args.scope, args.view)
    if views:
        print(f"\nViews ({len(views)})...")
    for view in views:
        fqn = f"{PROVIDER_BY_SCOPE[view['scope']]}.{view['service']}.{view['name']}"
        started = time.monotonic()
        status, row_count, message = run_view_test(runner, view, seeds)
        report(fqn, status, message, row_count, time.monotonic() - started)

    counts = {s: sum(1 for r in results if r[1] == s) for s in (PASS, EMPTY, FAIL, SKIP)}
    print("\n" + "=" * 70)
    print(
        f"Summary: {counts[PASS]} passed, {counts[EMPTY]} empty, "
        f"{counts[FAIL]} failed, {counts[SKIP]} skipped (of {len(results)})"
    )
    if counts[FAIL]:
        print("\nFailures:")
        for fqn, status, _, _, message in results:
            if status == FAIL:
                print(f"  {fqn}: {message}")
    print("=" * 70)
    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    sys.exit(main())
