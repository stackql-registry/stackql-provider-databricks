---
title: databricks_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/stackql-databricks-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources.

:::info

For Databricks account operations use the [__`databricks_account`__](https://databricks-account-provider.stackql.io/) provider.

:::

:::info[Provider Summary]

total services: __36__  
total resources: __372__  
source project: __[stackql-provider-databricks](https://github.com/stackql-registry/stackql-provider-databricks)__  

:::

See also:    [[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)   

* * *   

## Installation 

```bash 
REGISTRY PULL databricks_workspace; 
```  

## Authentication  

To use the `databricks_workspace` provider, you can authenticate using one of the following methods:

### OAuth2 (Service Principal) [Default]

Set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.

### Cloud selection (AWS, Azure, GCP)

The provider works against Databricks workspaces on AWS, Azure and Google Cloud with the same statements and the same three credential variables. It defaults to Databricks on AWS; one more variable selects another cloud, and both the OAuth token endpoint and the workspace host domain follow it:

- <CopyableCode code="DATABRICKS_CLOUD" /> - `aws` (default), `azure` or `gcp`
- <CopyableCode code="DATABRICKS_ACCOUNT_HOST" /> - optional, a bare account console host (no scheme) that issues the tokens, for accounts that are not on the standard hosts; overrides `DATABRICKS_CLOUD`
- <CopyableCode code="DATABRICKS_DEPLOYMENT_NAME" /> - optional, defaults the `deployment_name` predicate for the session

| Cloud | `DATABRICKS_CLOUD` | Workspace URL | `deployment_name` | Token endpoint host |
|-------|--------------------|---------------|-------------------|---------------------|
| AWS | `aws` (default) | `https://dbc-abcd0123-a1bc.cloud.databricks.com` | `dbc-abcd0123-a1bc` | `accounts.cloud.databricks.com` |
| Azure | `azure` | `https://adb-1234567890123456.7.azuredatabricks.net` | `adb-1234567890123456.7` | `accounts.azuredatabricks.net` |
| GCP | `gcp` | `https://1234567890123456.7.gcp.databricks.com` | `1234567890123456.7` | `accounts.gcp.databricks.com` |

`deployment_name` is the host prefix of the workspace URL on every cloud (everything before `.cloud.databricks.com`, `.azuredatabricks.net` or `.gcp.databricks.com`). The `databricks_account` provider lists it for every workspace in the account:

```sql
SELECT workspace_name, deployment_name, workspace_status
FROM databricks_account.provisioning.workspaces
WHERE account_id = '<account_id>';
```

Cloud selection needs stackql v1.0.888 or later. One cloud per process: the token endpoint follows the environment, so run a separate `stackql` process (or shell) for each cloud you work with.

```bash
# Azure Databricks workspace
export DATABRICKS_CLOUD=azure
export DATABRICKS_ACCOUNT_ID=...
export DATABRICKS_CLIENT_ID=...
export DATABRICKS_CLIENT_SECRET=...
export DATABRICKS_DEPLOYMENT_NAME=adb-1234567890123456.7
stackql exec "SELECT id, name, state, cluster_size, auto_stop_mins FROM databricks_workspace.sql.warehouses"
```

```powershell
# Databricks on Google Cloud workspace (PowerShell)
$env:DATABRICKS_CLOUD = "gcp"
$env:DATABRICKS_ACCOUNT_ID = "..."
$env:DATABRICKS_CLIENT_ID = "..."
$env:DATABRICKS_CLIENT_SECRET = "..."
stackql.exe exec "SELECT * FROM databricks_workspace.iam.current_user WHERE deployment_name = '1234567890123456.7'"
```

With no cloud variables set, queries behave exactly as before: AWS hosts and the AWS token endpoint.

#### Service principal by cloud

On every cloud the credential is a service principal with a Databricks OAuth secret, created in the account console under __User management > Service principals__ (add the principal, then __Generate secret__). Cloud identity tokens (AWS IAM, Microsoft Entra ID, Google service accounts) are not used by the provider.

| Cloud | Account console | Notes |
|-------|-----------------|-------|
| AWS | <a href="https://accounts.cloud.databricks.com">accounts.cloud.databricks.com</a> | Databricks-managed service principal (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">OAuth M2M on AWS</a>) |
| Azure | <a href="https://accounts.azuredatabricks.net">accounts.azuredatabricks.net</a> | Sign in with the Microsoft Entra ID identity that administers the Databricks account. A Databricks-managed service principal, or an Entra ID application registered as a service principal, both work when the OAuth secret is generated in the Databricks account console (see <a href="https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/oauth-m2m">OAuth M2M on Azure</a>) |
| GCP | <a href="https://accounts.gcp.databricks.com">accounts.gcp.databricks.com</a> | Databricks-managed service principal; the Google service account that Databricks itself uses is not the principal (see <a href="https://docs.databricks.com/gcp/en/dev-tools/auth/oauth-m2m">OAuth M2M on GCP</a>) |

The service principal needs access to each workspace it queries. Add it to the workspace from the account console (__Workspaces > Permissions__), or with the `databricks_account` provider, as a user, or as an admin for admin-only resources such as workspace configuration (`settings.vw_all_settings`) and other users' query history:

```sql
REPLACE databricks_account.iam.workspace_assignment
SET permissions = '["USER"]'
WHERE account_id = '<account_id>'
AND workspace_id = '<workspace_id>'
AND principal_id = '<service_principal_id>';
```

#### What differs by cloud

- The workspace APIs are the same on all three clouds, so resources, columns and statements do not change. Resources tied to one cloud's primitives exist only there (for example AWS instance profiles under `compute.instance_profiles`, or the AWS availability zones from `compute.clusters` `list_zones`); node types and Spark versions are cloud-specific values. Where a workspace's cloud or region does not offer a feature (serverless, Lakebase, some AI services), Databricks answers with an error rather than an empty list, and the provider surfaces that error as is.
- Workspace-level settings and compute policies that reference cloud storage or identities take the cloud's own identifiers (S3 paths and IAM roles on AWS, ABFSS paths and managed identities on Azure, GCS paths and service accounts on GCP); the provider passes them through verbatim.

### Personal Access Token (Bearer)

Alternatively, set <CopyableCode code="DATABRICKS_TOKEN" /> to a Databricks personal access token (see <a href="https://docs.databricks.com/en/dev-tools/auth/pat.html">Databricks personal access tokens</a>), then supply the auth config when starting the shell:
```bash
export DATABRICKS_TOKEN=xxx

# Linux/Mac
AUTH='{ "databricks_workspace": { "type": "bearer", "credentialsenvvar": "DATABRICKS_TOKEN" }}'
./stackql shell --auth="${AUTH}"
```
```powershell
# PowerShell
$Auth = "{ 'databricks_workspace': { 'type': 'bearer', 'credentialsenvvar': 'DATABRICKS_TOKEN' }}"
stackql.exe shell --auth=$Auth
```

## Example Queries

Try the following queries using `stackql shell`, or run them from a script or CI pipeline with `stackql exec`.

### Unity Catalog inventory

Catalogs in a workspace, with ownership and audit fields:

```sql
SELECT
  full_name,
  catalog_type,
  owner,
  comment,
  datetime(created_at/1000, 'unixepoch') AS created,
  created_by
FROM databricks_workspace.catalog.catalogs
WHERE deployment_name = '<deployment_name>';
```

Walk the catalog hierarchy - schemas and tables in a catalog:

```sql
SELECT full_name, table_type, data_source_format, owner
FROM databricks_workspace.catalog.tables
WHERE catalog_name = 'main'
AND schema_name = 'default'
AND deployment_name = '<deployment_name>';
```

### SQL statement execution - the full lifecycle

The Databricks SQL Statement Execution API maps naturally to SQL verbs - `INSERT` submits a statement, `SELECT` polls it, `DELETE` cancels it:

```sql
/* submit a statement to a SQL warehouse */
INSERT INTO databricks_workspace.sql.statement_execution (
  statement,
  warehouse_id,
  wait_timeout,
  deployment_name
)
SELECT
  'SELECT * FROM samples.nyctaxi.trips LIMIT 100',
  '<warehouse_id>',
  '0s',
  '<deployment_name>';

/* poll for status and results */
SELECT status, manifest, result
FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '<statement_id>'
AND deployment_name = '<deployment_name>';

/* cancel a running statement */
DELETE FROM databricks_workspace.sql.statement_execution
WHERE statement_id = '<statement_id>'
AND deployment_name = '<deployment_name>';
```

Recent query history across SQL warehouses and serverless compute:

```sql
SELECT query_id, status, query_text, user_name
FROM databricks_workspace.sql.query_history
WHERE deployment_name = '<deployment_name>';
```

### Workspace identity

Users, their groups and entitlements, flattened with built-in views:

```sql
SELECT * FROM databricks_workspace.iam.vw_users WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_user_groups WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_user_entitlements WHERE deployment_name = '<deployment_name>';
SELECT * FROM databricks_workspace.iam.vw_group_members WHERE deployment_name = '<deployment_name>';
```

### Compute estate

Clusters with their state, node types and autotermination settings:

```sql
SELECT
  cluster_id,
  cluster_name,
  state,
  node_type_id,
  autotermination_minutes,
  spark_version
FROM databricks_workspace.compute.clusters
WHERE deployment_name = '<deployment_name>';
```

SQL warehouses, sized and by state:

```sql
SELECT id, name, state, cluster_size, num_clusters, auto_stop_mins
FROM databricks_workspace.sql.warehouses
WHERE deployment_name = '<deployment_name>';
```

### Workspace settings

All workspace admin settings as key/value pairs, using a built-in view:

```sql
SELECT key, value
FROM databricks_workspace.settings.vw_all_settings
WHERE deployment_name = '<deployment_name>';
```


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/agentbricks/">agentbricks</a><br />
<a href="/services/agentkit/">agentkit</a><br />
<a href="/services/aifunctions/">aifunctions</a><br />
<a href="/services/aisearch/">aisearch</a><br />
<a href="/services/apps/">apps</a><br />
<a href="/services/bundledeployments/">bundledeployments</a><br />
<a href="/services/catalog/">catalog</a><br />
<a href="/services/cleanrooms/">cleanrooms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/dashboards/">dashboards</a><br />
<a href="/services/database/">database</a><br />
<a href="/services/dataclassification/">dataclassification</a><br />
<a href="/services/dataquality/">dataquality</a><br />
<a href="/services/domains/">domains</a><br />
<a href="/services/environments/">environments</a><br />
<a href="/services/files/">files</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/iamv2/">iamv2</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/jobs/">jobs</a><br />
<a href="/services/knowledgeassistants/">knowledgeassistants</a><br />
<a href="/services/marketplace/">marketplace</a><br />
<a href="/services/ml/">ml</a><br />
<a href="/services/oauth2/">oauth2</a><br />
<a href="/services/pipelines/">pipelines</a><br />
<a href="/services/postgres/">postgres</a><br />
<a href="/services/qualitymonitorv2/">qualitymonitorv2</a><br />
<a href="/services/sandbox/">sandbox</a><br />
<a href="/services/serving/">serving</a><br />
<a href="/services/settings/">settings</a><br />
<a href="/services/settingsv2/">settingsv2</a><br />
<a href="/services/sharing/">sharing</a><br />
<a href="/services/sql/">sql</a><br />
<a href="/services/supervisoragents/">supervisoragents</a><br />
<a href="/services/tags/">tags</a><br />
<a href="/services/vectorsearch/">vectorsearch</a><br />
<a href="/services/workspace/">workspace</a><br />
</div>
</div>
