# StackQL Databricks Provider - OpenAPI Schema Generator

A library of modular, testable functions to parse the Databricks Python SDK and extract components for generating OpenAPI specifications.

## Features

- **Small, modular functions** - Each function has a single, well-defined responsibility
- **Comprehensive logging** - Detailed logging at INFO and DEBUG levels to track anomalies
- **Type-safe** - Full type hints throughout
- **Well-tested** - Unit tests for all core functionality
- **Incremental design** - Built to be extended without creating a monolith
- **Account/Workspace separation** - Specs are organized by scope based on the SDK's `AccountClient` and `WorkspaceClient` definitions

## Project Structure

```
stackql_databricks_provider/
├── __init__.py              # Public API (get_resources, get_operations, etc.)
├── extract.py               # Core extraction functions (routes, schemas, params, resource-name expansion)
├── registry.py              # Service registry (account vs workspace classification)
├── generate.py              # OpenAPI spec generation and CLI entry point
├── inventory_gen.py         # CSV inventory generator (operation mapping files)
├── resource_name_templates.json  # Curated `name`/`parent` templates the SDK does not document
├── spec_overrides.json      # Post-extraction JSON-path overrides on the specs
├── provider-config/         # The hosts, auth and pagination config (the only place hosts are written)
│   ├── account_servers.json     # servers block: account_host selected by DATABRICKS_CLOUD
│   ├── workspace_servers.json   # servers block: deployment_name + workspace_domain
│   ├── provider_config.json     # provider.yaml config.auth (OAuth M2M token_url + variables)
│   └── service_config.json      # x-stackQL-config (pagination) for every service
├── Makefile                 # The operator surface (make help)
├── .env.aws.example         # Smoke-test credential templates per cloud: copy to .env.<cloud> (gitignored)
├── .env.azure.example
├── .env.gcp.example
├── README.md                # This file
├── tests/
│   ├── __init__.py
│   ├── test_extract.py      # Tests for extraction functions
│   ├── test_registry.py     # Tests for service registry
│   ├── test_generate.py     # Tests for spec generation
│   ├── test_inventory_gen.py # Tests for CSV inventory generator
│   └── test_multicloud.py   # Snapshot + resolution of the AWS/Azure/GCP host selection
├── smoke_tests/smoke.py     # Live smoke harness (resource queries, lifecycles, views)
├── views/                   # SQL views merged into the providers (also the smoke surface)
├── inventory/               # CSV operation inventories (the mapping masters)
│   ├── account/             # One CSV per account-level service + all_services.csv
│   └── workspace/           # One CSV per workspace-level service + all_services.csv
├── openapi_generated/       # Generated specs (after running the generator)
│   ├── account/             # 10 account-level service specs (billing ... settingsv2, networking)
│   └── workspace/           # 36 workspace-level service specs (agentbricks ... workspace)
├── stackql-provider/        # Generated providers (after make providers)
└── website/                 # Docusaurus microsites (after make docs)
```

## Setup

Install the project and its dependencies from the repository root:

```bash
pip install -e ".[dev]"
```

## How to Run

### Generate all specs

```bash
python -m stackql_databricks_provider.generate
```

This produces OpenAPI 3.0 JSON files under `stackql_databricks_provider/openapi_generated/`, organized into `account/` and `workspace/` subdirectories.

### Generate a single service

```bash
python -m stackql_databricks_provider.generate -s compute
```

### Custom output directory

```bash
python -m stackql_databricks_provider.generate -o /path/to/output
```

### Verbose/debug logging

```bash
python -m stackql_databricks_provider.generate -v
```

### Generate CSV operation inventories

After generating the OpenAPI specs, generate the CSV inventory files:

```bash
python -m stackql_databricks_provider.inventory_gen
```

This produces one CSV per service under `stackql_databricks_provider/inventory/{account,workspace}/`.

**Important:** The inventory generator respects existing CSV files. If a CSV already exists for a service, only *new* operations (by `filename::path::verb` key) are appended. Existing rows are preserved as-is, so any manual edits to `stackql_resource_name`, `stackql_method_name`, `stackql_verb`, or `stackql_object_key` are not overwritten.

A consolidated `all_services.csv` is also generated per scope, which is the file used as input to `@stackql/provider-utils` for provider generation.

### CSV columns

| Column | Description |
|--------|-------------|
| `filename` | Spec file name (e.g. `compute.json`) |
| `path` | REST API path |
| `operationId` | Unique operation identifier (e.g. `clusters_create`) |
| `verb` | HTTP method (`get`, `post`, `put`, `patch`, `delete`) |
| `response_object` | Response schema name from `$ref` (without `#/components/schemas/`) |
| `tags` | Comma-delimited list of OpenAPI tags |
| `params` | Comma-delimited list of all parameter names |
| `summary` | Operation summary |
| `description` | Full operation description |
| `stackql_resource_name` | StackQL resource name (defaults to last tag) |
| `stackql_method_name` | StackQL method name (defaults to operationId) |
| `stackql_verb` | StackQL verb: `select`, `insert`, `replace`, `update`, `delete` |
| `stackql_object_key` | JSON path to response data array (e.g. `$.items`) |

### Generate StackQL Provider

After generating specs and inventories, use `@stackql/provider-utils` to generate the full StackQL provider. See [STACKQL_PROVIDER_GENERATION.md](STACKQL_PROVIDER_GENERATION.md) for the complete workflow.

## How to Test

Run the full test suite:

```bash
python -m pytest stackql_databricks_provider/tests/ -v
```

Run a specific test file:

```bash
python -m pytest stackql_databricks_provider/tests/test_extract.py -v
```

Run a specific test class or method:

```bash
python -m pytest stackql_databricks_provider/tests/test_extract.py::TestGetResources -v
python -m pytest stackql_databricks_provider/tests/test_extract.py::TestGetOperationDetails::test_get_operation_structure -v
```

### Live smoke tests

`make smoke` (local provider), `make smoke-live` (published providers) and `make smoke-read-only` run
`smoke_tests/smoke.py`: resource queries, self-cleaning lifecycles (an account SCIM group and a workspace
secret scope, no compute, no charge) and every view. Credentials come from a gitignored env file: copy
`.env.aws.example`, `.env.azure.example` or `.env.gcp.example` to `.env.<cloud>` (or `.env` for the AWS
default) and fill in a Databricks-managed service principal with the account admin role (OAuth M2M).
`CLOUD=aws|azure|gcp` reads `.env.<cloud>` and selects the cloud, `ENV_FILE=...` names any other file (a
named file overrides the shell's environment, the default `.env` does not), `SMOKE_ARGS` passes harness
flags (`--skip-views`, `--scope account`, `--view SUBSTR`):

```bash
cp .env.azure.example .env.azure             # then fill in the credentials
make smoke                                   # AWS from .env, everything
make smoke CLOUD=azure                       # Azure account + workspace from .env.azure
make smoke-read-only CLOUD=gcp SMOKE_ARGS="--skip-views"
```

## How to Update

When the upstream Databricks Python SDK is updated with new services or API changes:

1. **Pull the latest SDK changes** into this repository (update the `databricks/` directory).

2. **Check for new service modules** - If new files appear under `databricks/sdk/service/`, add the module name to `SERVICE_MODULES` in `registry.py`.

3. **Check for new Account-level APIs** - If new API classes are added to `AccountClient.__init__()` in `databricks/sdk/__init__.py`, add the class name to `ACCOUNT_API_CLASSES` in `registry.py`.

4. **Regenerate specs**:
   ```bash
   python -m stackql_databricks_provider.generate
   ```
   A `WARNING ... no resource-name template found for path param 'name'` means a Google-style
   `/api/2.0/{name}` operation whose SDK docstring states no `Format:`; add the template to
   `resource_name_templates.json` (keyed `<service>: {"<ApiClass>.<method>.<param>": ...}`) unless it is
   a long-running-operation name, which stays `{name}` by design. An `ERROR ... path collision` means two
   SDK methods resolve to the same path and verb and one would be lost.

5. **Regenerate inventories** (existing manual edits are preserved):
   ```bash
   python -m stackql_databricks_provider.inventory_gen --refresh-response-objects
   python -m stackql_databricks_provider.inventory_gen --populate-object-keys
   python -m stackql_databricks_provider.inventory_gen
   ```
   The report lists **New Operations** (default routing: curate `stackql_resource_name`,
   `stackql_method_name`, `stackql_verb`, `stackql_object_key` in the per-service CSV), **Path Changes**
   (the operationId survived a path move, the curated mapping was carried over; nothing to do) and
   **Removed Operations** (dropped from the CSVs; a breaking change for the published provider, list them
   in the release notes).

6. **Run tests** to verify nothing broke:
   ```bash
   python -m pytest stackql_databricks_provider/tests/ -v
   ```

7. **Review the diff** in the generated files to understand what changed. `inventory/*/all_services.csv`
   is the checked-in record of every operation -> resource.method mapping; a changed resource or method
   name there is a breaking change to review, not noise.

The Databricks hosts and auth defaults are mastered in `provider-config/*.json` (read by both
`generate.py` and the Makefile's provider generation): the account host and workspace domain are selected
by `DATABRICKS_CLOUD` (`aws` default, `azure`, `gcp`), `DATABRICKS_ACCOUNT_HOST` overrides the account
host, and `DATABRICKS_DEPLOYMENT_NAME` defaults the workspace `deployment_name` predicate.
`tests/test_multicloud.py` pins the resolution (no environment is the AWS-only provider, byte for byte).

## Public API

The package exports these functions via `stackql_databricks_provider`:

### `get_resources(service_module) -> List[Tuple[str, str]]`

Extract API resource classes from a service module. Returns `(class_name, snake_case_name)` tuples.

```python
from databricks.sdk.service import compute
from stackql_databricks_provider import get_resources

resources = get_resources(compute)
# [('ClusterPoliciesAPI', 'cluster_policies'), ('ClustersAPI', 'clusters'), ...]
```

### `get_operations(service_module, class_name) -> List[str]`

Extract public method names from an API class.

```python
from stackql_databricks_provider import get_operations

ops = get_operations(compute, "ClustersAPI")
# ['create', 'delete', 'edit', 'get', 'list', ...]
```

### `get_operation_details(service_module, class_name, method_name, ...) -> Dict`

Extract a complete OpenAPI path object for a single API method, including HTTP method, path, parameters, request body, and responses.

```python
from stackql_databricks_provider import get_operation_details

details = get_operation_details(
    compute, "ClustersAPI", "get",
    service_name="compute", resource_snake_name="clusters"
)
# {"/api/2.0/clusters/get": {"get": {"operationId": "get", ...}}}
```

### `get_data_classes(service_module) -> List[Type]`

Extract all dataclass types from a service module.

### `get_schema_from_data_class(service_module, dc) -> Dict`

Generate an OpenAPI component schema from a dataclass, resolving string type annotations, nested dataclass references, enum references, and `List[...]` types.

## Architecture Notes

- **Extraction is done via source introspection** - The generator parses the Python source of each SDK method to find `self._api.do("METHOD", "/path", ...)` calls. This avoids needing to instantiate any API clients or make HTTP calls.

- **Account vs Workspace classification** - Uses a static mapping of API class names based on which classes are instantiated in `AccountClient.__init__()` vs `WorkspaceClient.__init__()`. Some service modules (e.g., `iam`, `catalog`, `settings`) contain both account and workspace APIs - these get split into separate spec files.

- **String annotation resolution** - The SDK uses `from __future__ import annotations`, which makes all type annotations strings at runtime. The generator resolves these back to actual types against the service module namespace for proper schema generation.

- **Skipped operations** - Methods that don't contain a `self._api.do()` call (e.g., `wait_*` polling helpers, `*_and_wait` convenience wrappers) are automatically skipped since they don't represent direct REST API endpoints.
