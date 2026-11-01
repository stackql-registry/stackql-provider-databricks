# StackQL Databricks Provider

This file is the canonical, tool-neutral guidance for working in this repository. Claude Code (via `CLAUDE.md`), GitHub Copilot (via `.github/copilot-instructions.md`) and Codex (which reads `AGENTS.md` directly) all take their instructions from here. Keep project rules in this file; the tool-specific files are entry points only.

## What this repo is

This is a permanent fork of the [Databricks Python SDK](https://github.com/databricks/databricks-sdk-py) used to generate the `databricks_account` and `databricks_workspace` providers for [StackQL](https://github.com/stackql/stackql). The upstream SDK code (`databricks/`) is the source of truth for API operations; all provider tooling lives in `stackql_databricks_provider/`.

- Default branch: `stackql-provider` (the working branch with all StackQL-specific code); pull requests target this branch on `origin`
- `main` mirrors upstream and is never modified; never open PRs against upstream
- Upstream remote: `https://github.com/databricks/databricks-sdk-py.git` (see [UPSTREAM_SYNC.md](UPSTREAM_SYNC.md))
- Root `README.md`, `CONTRIBUTING.md`, `Makefile` and `CHANGELOG.md` are the upstream SDK's own files and are kept identical to `upstream/main`. They describe the upstream SDK project, not this fork; keep fork-specific changes out of them so upstream merges stay clean. The provider workflow is documented in this file and under `stackql_databricks_provider/`.
- Upstream CI is disabled (the workflows are renamed to `*.yml.upstream`). This fork has no CI, so run the Makefile checks below locally.

## How it works

The pipeline extracts OpenAPI specs from the SDK by source introspection (parsing `self._api.do("METHOD", "/path", ...)` calls in SDK methods - no clients are instantiated, no HTTP calls made), maps operations to StackQL resources/methods/verbs via CSV inventories, then generates the final provider YAML with `@stackql/provider-utils`.

```
databricks/sdk/service/*.py            (upstream SDK - source of truth)
        | generate.py                  (introspection -> OpenAPI 3.0 specs)
openapi_generated/{account,workspace}/*.json
        | inventory_gen.py             (specs -> CSV operation inventories)
inventory/{account,workspace}/*.csv    (per-service masters + all_services.csv)
        | npm run generate-provider    (@stackql/provider-utils)
stackql-provider/src/databricks_{account,workspace}/v00.00.00000/
        | add_response_transforms.py   (post-gen response transforms)
        | merge_views.py               (inject views/ into provider specs - final step)
        | npm run generate-docs + add_doc_examples.py
website/databricks_{account,workspace}/   (docusaurus microsites)
```

Key concepts:

- **Scope split**: `AccountClient` vs `WorkspaceClient` API classes in `databricks/sdk/__init__.py` determine account vs workspace scope. The mapping is static, in `stackql_databricks_provider/registry.py` (`SERVICE_MODULES`, `ACCOUNT_API_CLASSES`).
- **CSV inventories are masters**: manual edits to `stackql_resource_name`, `stackql_method_name`, `stackql_verb`, `stackql_object_key` in the per-service CSVs are preserved by `inventory_gen.py`; new operations are appended with default routing. Rows are keyed by `filename::path::verb` plus `operationId`: when an operation's path changes but its `operationId` (`<resource>_<method>`) survives, the curated columns follow it (reported as "path changed, mapping kept"); an operation that left the SDK is dropped and reported under "Removed Operations" - that is a breaking change for the published provider and goes in the release notes. `all_services.csv` per scope is regenerated from the masters, is the input to provider generation, and is the checked-in record of every operation -> resource.method mapping (a diff there is a breaking-change review, not noise).
- **Resource-name style APIs**: newer Databricks services (agentkit, domains, sandbox, knowledgeassistants, environments, dataclassification, networking, and parts of postgres, iamv2, catalog, aisearch, bundledeployments, disasterrecovery, supervisoragents) follow the Google AIP convention: the SDK method takes `name="domains/{domain_id}"` or `parent=...` and calls `/api/2.0/{name}`, so several resources share one path and the value carries slashes. `extract.py` expands those placeholders into real paths and typed path parameters from the template the SDK documents (`Format: domains/{domain_id}`, `in the form sandboxes/{sandbox_id}`; a three-level Unity Catalog name `{catalog}.{schema}.{x}` becomes one `full_name` parameter), falling back to a sibling method on the same noun, then to the unique template seen for the same path/parameter in the class. Templates the SDK never documents are curated in `resource_name_templates.json` (`<service>: {"<ApiClass>.<method>.<param>": template}`). Long-running-operation names (`get_*_operation`) are deliberately left as `{name}`. `generate.py` reports any path/verb collision as an error, so a lost operation is never silent.
- **Request bodies spread from a dataclass**: 179 SDK methods send a dataclass as the whole body (`body = network_connectivity_config.as_dict()`), so the wire body is the object's fields (`{"name": ..., "region": ...}`), not `{"network_connectivity_config": {...}}`. `extract.py` (`_extract_spread_body_param`) inlines that dataclass's schema as the request body, so the INSERT/UPDATE columns are the fields themselves; methods that assign `body["key"] = ...` field by field are unchanged. Before SDK v0.158 the generator wrapped these under the parameter name, a shape the API rejects; do not reintroduce it.
- **Views**: SQL views live in `stackql_databricks_provider/views/{account,workspace}/{service}/views.yaml` and are merged into `components.x-stackQL-resources` of the matching service spec by `merge_views.py` (must run last). Views are also the smoke test surface.
- **Auth**: both providers use OAuth2 client credentials with `DATABRICKS_ACCOUNT_ID`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET` (same vars as Terraform / the Databricks CLI). Local dev secrets can go in `stackql_databricks_provider/.env` (gitignored).
- **Multi-cloud hosts (AWS default, Azure, GCP)**: the Databricks hosts are written in exactly one place, `stackql_databricks_provider/provider-config/*.json` (`account_servers.json`, `workspace_servers.json`, `provider_config.json`, `service_config.json`); the Makefile passes them to `@stackql/provider-utils` and `generate.py` reads them for the intermediate specs. The account host (`accounts.cloud.databricks.com` / `accounts.azuredatabricks.net` / `accounts.gcp.databricks.com`) and the workspace domain suffix (`cloud.databricks.com` / `azuredatabricks.net` / `gcp.databricks.com`) are server variables (`account_host`, `workspace_domain`) selected by `DATABRICKS_CLOUD` (`aws` default, `azure`, `gcp`) through `x-stackQL-envVarSelector`; `DATABRICKS_ACCOUNT_HOST` (bare host) is a verbatim override through `x-stackQL-envVar` and also drives the OAuth `token_url` (`https://{account_host}/oidc/accounts/{{ .__env__DATABRICKS_ACCOUNT_ID }}/v1/token`, with the variable declared under `config.auth.variables`). `deployment_name` stays the workspace predicate on every cloud (the host prefix: `dbc-...` on AWS, `adb-<id>.<n>` on Azure, the workspace id on GCP) and can be defaulted with `DATABRICKS_DEPLOYMENT_NAME`. With no variables set, resolution is byte-for-byte the previous AWS-only provider (`tests/test_multicloud.py` pins this). The selector annotation is resolved by stackql's omnisdk-based host (`omnisdk` >= the version carrying `aot.ServerVariableSpec`, stackql main after 2026-11-01); the any-sdk based v0.12.x releases treat `account_host` as a required predicate, so this provider version is published together with that stackql release.
- **Doc microsites**: the docusaurus sites under `website/databricks_{account,workspace}` vendor the shared StackQL site config - `npm run build` (via `prebuild`) shallow-clones [stackql/docusaurus-config](https://github.com/stackql/docusaurus-config) into a gitignored `.shared-config/` and `docusaurus.config.js` calls its `createConfig` factory, with only `provider.js` (name/title) and a couple of overrides per site. The provider index page content (intro, auth, getting-started reference queries) is mastered in `docgen/provider-data/<provider>/headerContent{1,2}.txt` and spliced in by `generate-docs`.

## Workflow (Makefile)

All commands run from `stackql_databricks_provider/` in a POSIX shell (WSL on Windows):

```bash
cd stackql_databricks_provider
make help            # list all targets
make upstream-pull   # git fetch upstream && git merge upstream/main
make deps            # pip install -e ".[dev]" + npm install
make all             # specs -> inventory -> unit-test -> providers -> test-meta -> smoke -> docs -> docs-build
```

Individual steps: `make specs`, `make inventory`, `make unit-test`, `make providers`, `make test-meta`, `make smoke`, `make smoke-live`, `make docs`, `make docs-build`.

### After an upstream pull

1. Check for new service modules: `git diff HEAD~1 --name-status -- databricks/sdk/service/ | grep '^A'`
2. Register new modules in `SERVICE_MODULES` and new account-scoped API classes in `ACCOUNT_API_CLASSES` in `registry.py`. Only register modules whose API classes are wired into `AccountClient`/`WorkspaceClient` in `databricks/sdk/__init__.py`. Deliberately excluded: `bundle` (not wired into either client) and `_internal`. A removed account API class (billing `UsagePolicyAPI` left in SDK v0.158) is removed from `ACCOUNT_API_CLASSES` too.
3. Run `make specs inventory` and review the inventory report and the CSV diffs: "New Operations" default `stackql_resource_name` to the last tag and `stackql_verb` from the HTTP verb - curate them in the per-service CSVs (short method names `create`/`list`/`get`/`update`/`delete`, lifecycle and action POSTs such as `start`/`cancel`/`sync`/`search` to `exec`, `cancel`/`delete`-semantics POSTs to `delete`, PUT to `replace`); "Path Changes" need no action; "Removed Operations" go in the release notes. A `WARNING ... no resource-name template found` from `make specs` means a `{name}`/`{parent}` path the SDK does not document - add it to `resource_name_templates.json` unless it is a long-running-operation name.
4. `make unit-test providers test-meta smoke` to regenerate and verify.

[UPSTREAM_SYNC.md](UPSTREAM_SYNC.md) covers the git side (remotes, branch strategy, resolving merge conflicts). The "How to Update" section of [stackql_databricks_provider/README.md](stackql_databricks_provider/README.md) covers the same steps as direct `python -m` invocations without the Makefile.

## Testing

- **Unit tests**: `make unit-test` (pytest over `stackql_databricks_provider/tests/`) - covers the extraction/generation machinery, no network.
- **Meta-route tests**: `make test-meta` - starts a local stackql server against the generated registry and walks all services/resources/methods.
- **Smoke tests** (authenticated, hit real Databricks endpoints): `make smoke` tests the locally generated provider via a `file://` registry; `make smoke-live` pulls the latest *published* providers from the public StackQL registry and tests those; `make smoke-read-only` skips the mutations. Three layers: resource queries (workspaces, account groups, current user, catalogs, clusters, warehouses, secret scopes - the documented columns must come back), self-cleaning lifecycles that cost nothing (an account SCIM group through the stackql-deploy exists / `INSERT` / exports / `DELETE` shape, and a workspace secret scope through `INSERT` / `SELECT` / `EXEC` delete, all named `stackql-smoke-<stamp>`), then every view under `views/` with `SELECT *` and required params (seeded from env / derived via `databricks_account.provisioning.workspaces`). Credentials come from a gitignored env file copied from the committed templates `.env.aws.example`, `.env.azure.example`, `.env.gcp.example` (to `.env.<cloud>`, or `.env` for the AWS default); `CLOUD=aws|azure|gcp` reads `.env.<cloud>` and selects the cloud (a named file overrides the shell environment, the default `.env` does not), `ENV_FILE=...` names any other file, extra harness flags go in `SMOKE_ARGS` (e.g. `--skip-views`, `--scope account`). Implementation: `smoke_tests/smoke.py`.

## Publishing

Push the generated `stackql-provider/src/databricks_{account,workspace}` trees to `providers/src` in a feature branch of [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry). See [stackql_databricks_provider/STACKQL_PROVIDER_GENERATION.md](stackql_databricks_provider/STACKQL_PROVIDER_GENERATION.md) for the full manual workflow and example queries.

## Pull requests

PR descriptions follow the structure in [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) (Summary, Why, What changed, How is this tested). Lead with why the change exists rather than restating the diff, state explicitly when there are no behavioral changes, and always answer the testing question (use "N/A" or "Not tested" where that is the truth).

## Gotchas

- `merge_views.py` must be the final post-gen step; regenerating a provider overwrites its output including merged views and response transforms.
- The generator skips SDK methods without a `self._api.do()` call (`wait_*`, `*_and_wait` helpers) - by design.
- The SDK uses `from __future__ import annotations`; the extractor resolves string annotations against the service module namespace.
- Service-level pagination (`next_page_token`/`page_token`) is injected via `--service-config` as `x-stackQL-config` on every service. any-sdk also supports method-level `config.pagination` (operation config overrides resource, then service, then provider level - see `operation_store.go` in any-sdk). Note: pagination request tokens can only be applied as `query`, `body`, or `requestString` (full URL replace) - `path` location is not supported by any-sdk's `SetNextPage`, and relative URLs (e.g. `next_chunk_internal_link` in `sql.statement_execution`) are not resolved against the request host, so chunk-following pagination for statement results cannot be wired in the provider today; it needs an any-sdk enhancement.
- `sql.statement_execution` verb mappings: `execute` -> `insert`, `get`/`get_result_chunk` -> `select`, `cancel` -> `delete` (it is a POST on the wire, but semantically a DELETE of a running statement).

## Related docs

- [UPSTREAM_SYNC.md](UPSTREAM_SYNC.md) - remotes, branch strategy and merging upstream changes
- [stackql_databricks_provider/README.md](stackql_databricks_provider/README.md) - generator features, project structure, CSV columns, public API and update steps
- [stackql_databricks_provider/STACKQL_PROVIDER_GENERATION.md](stackql_databricks_provider/STACKQL_PROVIDER_GENERATION.md) - full manual generation, testing and publishing workflow with example queries
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) - PR description structure

## Guidance files

- `AGENTS.md` (this file) is the single source of truth. Edit project rules here.
- `CLAUDE.md` is the Claude Code entry point. It imports this file with `@AGENTS.md` and lists only Claude Code specifics (slash commands under `.claude/commands/`).
- `.github/copilot-instructions.md` is the GitHub Copilot entry point and points here. The Copilot coding agent also reads the root `AGENTS.md` directly.
- Codex reads the root `AGENTS.md` directly; no Codex-specific files are needed.
