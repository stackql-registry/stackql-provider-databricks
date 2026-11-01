---
title: databricks_account
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_account
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

Account-level features, identity and provisioning for Databricks.

:::info

For Databricks workspace operations use the [__`databricks_workspace`__](https://databricks-workspace-provider.stackql.io/) provider.

:::

:::info[Provider Summary]

total services: __10__  
total resources: __94__  
source project: __[stackql-provider-databricks](https://github.com/stackql-registry/stackql-provider-databricks)__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL databricks_account;
```

## Authentication  

To use the `databricks_account` provider, you can authenticate using one of the following methods:

### OAuth2 (Service Principal) [Default]

Set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.

### Cloud selection (AWS, Azure, GCP)

The provider defaults to Databricks on AWS (`accounts.cloud.databricks.com`). The same service principal flow works on Azure Databricks (`accounts.azuredatabricks.net`) and Databricks on Google Cloud (`accounts.gcp.databricks.com`); select the cloud with one variable and both the OAuth token endpoint and the account API host follow:

- <CopyableCode code="DATABRICKS_CLOUD" /> - `aws` (default), `azure` or `gcp`
- <CopyableCode code="DATABRICKS_ACCOUNT_HOST" /> - optional, overrides the account console host (a bare host such as `accounts.azuredatabricks.net`, no scheme); wins over `DATABRICKS_CLOUD`

```bash
export DATABRICKS_CLOUD=azure
export DATABRICKS_ACCOUNT_ID=...
export DATABRICKS_CLIENT_ID=...
export DATABRICKS_CLIENT_SECRET=...
stackql exec "SELECT id, displayName FROM databricks_account.iam.account_groups WHERE account_id = '<account_id>'"
```

Queries are unchanged across clouds: `account_id` stays the only required predicate, and with no cloud variables set the provider behaves exactly as before. The service principal must be a Databricks-managed service principal with the account admin role (OAuth M2M); Entra ID and Google service-account tokens are not used for the account API.

### Personal Access Token (Bearer)

Alternatively, set <CopyableCode code="DATABRICKS_TOKEN" /> to a Databricks personal access token (see <a href="https://docs.databricks.com/en/dev-tools/auth/pat.html">Databricks personal access tokens</a>), then supply the auth config when starting the shell:
```bash
export DATABRICKS_TOKEN=xxx

# Linux/Mac
AUTH='{ "databricks_account": { "type": "bearer", "credentialsenvvar": "DATABRICKS_TOKEN" }}'
./stackql shell --auth="${AUTH}"
```
```powershell
# PowerShell
$Auth = "{ 'databricks_account': { 'type': 'bearer', 'credentialsenvvar': 'DATABRICKS_TOKEN' }}"
stackql.exe shell --auth=$Auth
```

## Example Queries

Try the following queries using `stackql shell`, or run them from a script or CI pipeline with `stackql exec`.

### Workspace inventory

Every workspace in the account, with status, region and when it was created:

```sql
SELECT
  workspace_id,
  workspace_name,
  workspace_status,
  aws_region,
  deployment_name,
  datetime(creation_time/1000, 'unixepoch') AS created
FROM databricks_account.provisioning.workspaces
WHERE account_id = '<account_id>'
ORDER BY creation_time DESC;
```

Join workspaces to their permission assignments - who can access what:

```sql
SELECT
  w.workspace_id,
  w.workspace_name,
  w.workspace_status,
  json_extract(wa.principal, '$.display_name') AS principal,
  wa.permissions
FROM databricks_account.provisioning.workspaces w
LEFT JOIN databricks_account.iam.workspace_assignment wa
ON w.workspace_id = wa.workspace_id
WHERE account_id = '<account_id>';
```

### Identity at a glance

Account users flattened to one row per role assignment, using a built-in view:

```sql
SELECT *
FROM databricks_account.iam.vw_account_user_roles
WHERE account_id = '<account_id>';
```

Find the account admins:

```sql
SELECT
  id AS user_id,
  userName AS user_name,
  displayName AS display_name
FROM databricks_account.iam.vw_account_user_roles
WHERE account_id = '<account_id>'
AND role = 'account_admin';
```

### FinOps queries

Budget policies and budget configurations:

```sql
SELECT *
FROM databricks_account.billing.vw_budget_policies
WHERE account_id = '<account_id>';

SELECT *
FROM databricks_account.billing.vw_budgets
WHERE account_id = '<account_id>';
```

Download a month of billable usage to CSV:

```bash
stackql exec -o text --hideheaders -f billable_usage.csv \
  "SELECT contents FROM databricks_account.billing.billable_usage
   WHERE start_month = '2026-06' AND end_month = '2026-07'
   AND account_id = '<account_id>'"
```

### Network and storage configuration

Audit the account's registered infrastructure - credentials, storage configurations, networks and encryption keys - using the built-in views:

```sql
SELECT * FROM databricks_account.provisioning.vw_credentials WHERE account_id = '<account_id>';
SELECT * FROM databricks_account.provisioning.vw_storage_configurations WHERE account_id = '<account_id>';
SELECT * FROM databricks_account.provisioning.vw_networks WHERE account_id = '<account_id>';
SELECT * FROM databricks_account.settings.vw_network_connectivity_configs WHERE account_id = '<account_id>';
```


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/billing/">billing</a><br />
<a href="/services/catalog/">catalog</a><br />
<a href="/services/disasterrecovery/">disasterrecovery</a><br />
<a href="/services/iam/">iam</a><br />
<a href="/services/iamv2/">iamv2</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/networking/">networking</a><br />
<a href="/services/oauth2/">oauth2</a><br />
<a href="/services/provisioning/">provisioning</a><br />
<a href="/services/settings/">settings</a><br />
<a href="/services/settingsv2/">settingsv2</a><br />
</div>
</div>
