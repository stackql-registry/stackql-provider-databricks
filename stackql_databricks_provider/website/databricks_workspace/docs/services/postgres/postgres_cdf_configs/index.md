---
title: postgres_cdf_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_cdf_configs
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

Creates, updates, deletes, gets or lists a <code>postgres_cdf_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_cdf_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_cdf_configs" /></td></tr>
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
    "description": "Output only. The full resource name of the CdfConfig. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;"
  },
  {
    "name": "cdf_config_id",
    "type": "string",
    "description": "The user-specified id; equals the final segment of ``name``. Defaults to the Postgres schema name for configs without an explicit id."
  },
  {
    "name": "catalog",
    "type": "string",
    "description": "The Unity Catalog catalog that replicated tables are written into. Set at creation; the CdfConfig is immutable."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the CdfConfig was created."
  },
  {
    "name": "postgres_schema",
    "type": "string",
    "description": "The Postgres schema this CdfConfig replicates from. Unique within the parent database. Set at creation; the CdfConfig is immutable."
  },
  {
    "name": "schema",
    "type": "string",
    "description": "The Unity Catalog schema that replicated tables are written into. Set at creation; the CdfConfig is immutable."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource name of the CdfConfig. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;"
  },
  {
    "name": "cdf_config_id",
    "type": "string",
    "description": "The user-specified id; equals the final segment of ``name``. Defaults to the Postgres schema name for configs without an explicit id."
  },
  {
    "name": "catalog",
    "type": "string",
    "description": "The Unity Catalog catalog that replicated tables are written into. Set at creation; the CdfConfig is immutable."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the CdfConfig was created."
  },
  {
    "name": "postgres_schema",
    "type": "string",
    "description": "The Postgres schema this CdfConfig replicates from. Unique within the parent database. Set at creation; the CdfConfig is immutable."
  },
  {
    "name": "schema",
    "type": "string",
    "description": "The Unity Catalog schema that replicated tables are written into. Set at creation; the CdfConfig is immutable."
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
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-cdf_config"><code>cdf_config</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a single Lakebase CDF configuration, including the source Postgres schema and target Unity Catalog</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List all CDF configurations for a Lakebase database. Each configuration maps a Postgres schema to a</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-cdf_config"><code>cdf_config</code></a></td>
    <td><a href="#parameter-cdf_config_id"><code>cdf_config_id</code></a></td>
    <td>Create a CDF configuration that materializes the change data feed for all tables in a Postgres schema</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project"><code>project</code></a>, <a href="#parameter-branch"><code>branch</code></a>, <a href="#parameter-database"><code>database</code></a>, <a href="#parameter-cdf_config"><code>cdf_config</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete a CDF configuration and stop materializing the change data feed. When force=true, also drops</td>
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
    <td>The `branch` segment of the `name` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The resource name of the CdfConfig to delete. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-cdf_config">
    <td><CopyableCode code="cdf_config" /></td>
    <td><code>string</code></td>
    <td>The `cdf_config` segment of the `name` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The resource name of the CdfConfig to delete. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-database">
    <td><CopyableCode code="database" /></td>
    <td><code>string</code></td>
    <td>The `database` segment of the `name` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The resource name of the CdfConfig to delete. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project">
    <td><CopyableCode code="project" /></td>
    <td><code>string</code></td>
    <td>The `project` segment of the `name` resource name (`projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;`). The resource name of the CdfConfig to delete. Format: projects/&#123;project&#125;/branches/&#123;branch&#125;/databases/&#123;database&#125;/cdf-configs/&#123;cdf_config&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-cdf_config_id">
    <td><CopyableCode code="cdf_config_id" /></td>
    <td><code>string</code></td>
    <td>The user-specified id for the CdfConfig, forming the final segment of its resource name. Must match the pattern ``[a-z][a-z0-9_]&#123;0,62&#125;``. Defaults to the Postgres schema name when omitted.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>When true, also drops the replicated Delta tables in Unity Catalog. When false (the default), the replicated tables are preserved at their last synced state.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of CdfConfigs to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token returned by a previous ListCdfConfigs call. Empty on the first page.</td>
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

Get a single Lakebase CDF configuration, including the source Postgres schema and target Unity Catalog

```sql
SELECT
name,
cdf_config_id,
catalog,
create_time,
postgres_schema,
schema
FROM databricks_workspace.postgres.postgres_cdf_configs
WHERE project = '{{ project }}' -- required
AND branch = '{{ branch }}' -- required
AND database = '{{ database }}' -- required
AND cdf_config = '{{ cdf_config }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all CDF configurations for a Lakebase database. Each configuration maps a Postgres schema to a

```sql
SELECT
name,
cdf_config_id,
catalog,
create_time,
postgres_schema,
schema
FROM databricks_workspace.postgres.postgres_cdf_configs
WHERE project = '{{ project }}' -- required
AND branch = '{{ branch }}' -- required
AND database = '{{ database }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a CDF configuration that materializes the change data feed for all tables in a Postgres schema

```sql
INSERT INTO databricks_workspace.postgres.postgres_cdf_configs (
cdf_config,
project,
branch,
database,
deployment_name,
workspace_domain,
cdf_config_id
)
SELECT 
'{{ cdf_config }}' /* required */,
'{{ project }}',
'{{ branch }}',
'{{ database }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ cdf_config_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_cdf_configs
  props:
    - name: project
      value: "{{ project }}"
      description: Required parameter for the postgres_cdf_configs resource.
    - name: branch
      value: "{{ branch }}"
      description: Required parameter for the postgres_cdf_configs resource.
    - name: database
      value: "{{ database }}"
      description: Required parameter for the postgres_cdf_configs resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_cdf_configs resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_cdf_configs resource.
    - name: cdf_config
      description: |
        The CdfConfig to create. The catalog, schema, and postgres_schema fields are required; service_principal is optional. All other fields are output only and ignored on input.
      value:
        catalog: "{{ catalog }}"
        schema: "{{ schema }}"
        postgres_schema: "{{ postgres_schema }}"
        cdf_config_id: "{{ cdf_config_id }}"
        create_time: "{{ create_time }}"
        name: "{{ name }}"
    - name: cdf_config_id
      value: "{{ cdf_config_id }}"
      description: The user-specified id for the CdfConfig, forming the final segment of its resource name. Must match the pattern \`\`[a-z][a-z0-9_]{0,62}\`\`. Defaults to the Postgres schema name when omitted.
      description: The user-specified id for the CdfConfig, forming the final segment of its resource name. Must match the pattern \`\`[a-z][a-z0-9_]{0,62}\`\`. Defaults to the Postgres schema name when omitted.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a CDF configuration and stop materializing the change data feed. When force=true, also drops

```sql
DELETE FROM databricks_workspace.postgres.postgres_cdf_configs
WHERE project = '{{ project }}' --required
AND branch = '{{ branch }}' --required
AND database = '{{ database }}' --required
AND cdf_config = '{{ cdf_config }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
