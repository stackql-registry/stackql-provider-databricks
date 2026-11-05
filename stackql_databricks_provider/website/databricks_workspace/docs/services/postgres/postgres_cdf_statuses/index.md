---
title: postgres_cdf_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_cdf_statuses
  - postgres
  - databricks_workspace
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_workspace resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_workspace-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>postgres_cdf_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_cdf_statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_cdf_statuses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource name of the CdfStatus. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;/cdf-statuses/&#123;cdf_status&#125; The &#123;cdf_status&#125; segment is the Postgres table name."
  },
  {
    "name": "committed_lsn",
    "type": "string",
    "description": "The high-watermark Log Sequence Number (LSN) committed to Delta Lake."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When replication for this table was first established."
  },
  {
    "name": "last_sync_time",
    "type": "string (date-time)",
    "description": "The last time changes for this table were written to Delta Lake."
  },
  {
    "name": "postgres_table",
    "type": "string",
    "description": "The Postgres table being replicated."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current replication state of this table. (CDF_STATE_SKIPPED, CDF_STATE_SNAPSHOTTING, CDF_STATE_STREAMING, CDF_STATE_TERMINATED)"
  },
  {
    "name": "status_detail",
    "type": "string",
    "description": "Human-readable detail for the current state (e.g. the skip/error reason). Empty for healthy states."
  },
  {
    "name": "uc_table",
    "type": "string",
    "description": "The Unity Catalog table receiving replicated data."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource name of the CdfStatus. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;/cdf-statuses/&#123;cdf_status&#125; The &#123;cdf_status&#125; segment is the Postgres table name."
  },
  {
    "name": "committed_lsn",
    "type": "string",
    "description": "The high-watermark Log Sequence Number (LSN) committed to Delta Lake."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When replication for this table was first established."
  },
  {
    "name": "last_sync_time",
    "type": "string (date-time)",
    "description": "The last time changes for this table were written to Delta Lake."
  },
  {
    "name": "postgres_table",
    "type": "string",
    "description": "The Postgres table being replicated."
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current replication state of this table. (CDF_STATE_SKIPPED, CDF_STATE_SNAPSHOTTING, CDF_STATE_STREAMING, CDF_STATE_TERMINATED)"
  },
  {
    "name": "status_detail",
    "type": "string",
    "description": "Human-readable detail for the current state (e.g. the skip/error reason). Empty for healthy states."
  },
  {
    "name": "uc_table",
    "type": "string",
    "description": "The Unity Catalog table receiving replicated data."
  }
]} />
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-cdf_config"><code>cdf_config</code></a>, <a href="#parameter-cdf_status"><code>cdf_status</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get the CDF status of a single table within a Lakebase CDF configuration, including its current state</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-cdf_config"><code>cdf_config</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List the per-table CDF statuses within a Lakebase CDF configuration. Each status shows whether a</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-branch">
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The `branch` segment of the `parent` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The parent CdfConfig to list CdfStatuses for. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-cdf_config">
    <td><CopyableCode code="cdf_config" /></td>
    <td><code>string</code></td>
    <td>The `cdf_config` segment of the `parent` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The parent CdfConfig to list CdfStatuses for. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-cdf_status">
    <td><CopyableCode code="cdf_status" /></td>
    <td><code>string</code></td>
    <td>The `cdf_status` segment of the `name` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;/cdf-statuses/&#123;cdf_status&#125;`). The resource name of the CdfStatus to retrieve. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;/cdf-statuses/&#123;cdf_status&#125;</td>
</tr>
<tr id="parameter-database">
    <td><CopyableCode code="database" /></td>
    <td><code>string</code></td>
    <td>The `database` segment of the `parent` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The parent CdfConfig to list CdfStatuses for. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project">
    <td><CopyableCode code="project" /></td>
    <td><code>string</code></td>
    <td>The `project` segment of the `parent` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The parent CdfConfig to list CdfStatuses for. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of CdfStatuses to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token returned by a previous ListCdfStatuses call. Empty on the first page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the CDF status of a single table within a Lakebase CDF configuration, including its current state

```sql
SELECT
name,
committed_lsn,
create_time,
last_sync_time,
postgres_table,
state,
status_detail,
uc_table
FROM databricks_workspace.postgres.postgres_cdf_statuses
WHERE project = '{{ project }}' -- required
AND branch = '{{ branch }}' -- required
AND database = '{{ database }}' -- required
AND cdf_config = '{{ cdf_config }}' -- required
AND cdf_status = '{{ cdf_status }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the per-table CDF statuses within a Lakebase CDF configuration. Each status shows whether a

```sql
SELECT
name,
committed_lsn,
create_time,
last_sync_time,
postgres_table,
state,
status_detail,
uc_table
FROM databricks_workspace.postgres.postgres_cdf_statuses
WHERE project = '{{ project }}' -- required
AND branch = '{{ branch }}' -- required
AND database = '{{ database }}' -- required
AND cdf_config = '{{ cdf_config }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>
