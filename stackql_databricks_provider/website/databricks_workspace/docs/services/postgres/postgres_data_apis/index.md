---
title: postgres_data_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_data_apis
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

Creates, updates, deletes, gets or lists a <code>postgres_data_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_data_apis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_data_apis" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the Data API was first enabled."
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The database containing this Data API configuration. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The desired Data API configuration.",
    "children": [
      {
        "name": "db_aggregates_enabled",
        "type": "boolean",
        "description": "Enable aggregate functions (count, sum, avg, etc.) in Data API responses. Default: true."
      },
      {
        "name": "db_extra_search_path",
        "type": "array",
        "description": "Additional schemas to include in the PostgreSQL search path. Each entry must be a valid PostgreSQL schema name."
      },
      {
        "name": "db_max_rows",
        "type": "integer",
        "description": "Maximum number of rows returned in a single Data API response. Must be a positive integer."
      },
      {
        "name": "db_schemas",
        "type": "array",
        "description": "Database schemas exposed through the Data API. Each entry must be a valid PostgreSQL schema name (1-63 chars, [a-zA-Z_][a-zA-Z0-9_$]*). Maximum 100 entries. Default: [\"public\"]."
      },
      {
        "name": "jwt_cache_max_lifetime",
        "type": "string",
        "description": "Maximum lifetime for cached JWT tokens. Zero duration disables caching."
      },
      {
        "name": "jwt_role_claim_key",
        "type": "string",
        "description": "JSON path to the role claim in JWT tokens (e.g., \".sub\"). Default: \".sub\"."
      },
      {
        "name": "openapi_mode",
        "type": "string",
        "description": "OpenAPI documentation mode for the Data API endpoint. (OPEN_API_MODE_DISABLED, OPEN_API_MODE_IGNORE_PRIVILEGES)"
      },
      {
        "name": "server_cors_allowed_origins",
        "type": "array",
        "description": "Allowed origins for CORS requests. Each entry should be a valid origin URL, or use \"*\" to allow all origins."
      },
      {
        "name": "server_timing_enabled",
        "type": "boolean",
        "description": "Enable the Server-Timing header in Data API responses."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The observed Data API state (read-only).",
    "children": [
      {
        "name": "available_schemas",
        "type": "array",
        "description": "Schemas available in the database (for reference when configuring db_schemas)."
      },
      {
        "name": "db_aggregates_enabled",
        "type": "boolean",
        "description": "Actual aggregate function setting read from the database."
      },
      {
        "name": "db_extra_search_path",
        "type": "array",
        "description": "Actual extra search path schemas read from the database."
      },
      {
        "name": "db_max_rows",
        "type": "integer",
        "description": "Actual max rows setting read from the database."
      },
      {
        "name": "db_schemas",
        "type": "array",
        "description": "Actual exposed schemas read from the database."
      },
      {
        "name": "jwt_cache_max_lifetime",
        "type": "string",
        "description": "Actual JWT cache max lifetime read from the database."
      },
      {
        "name": "jwt_role_claim_key",
        "type": "string",
        "description": "Actual JWT role claim key read from the database."
      },
      {
        "name": "openapi_mode",
        "type": "string",
        "description": "Actual OpenAPI mode read from the database. (OPEN_API_MODE_DISABLED, OPEN_API_MODE_IGNORE_PRIVILEGES)"
      },
      {
        "name": "server_cors_allowed_origins",
        "type": "array",
        "description": "Actual CORS allowed origins read from the database."
      },
      {
        "name": "server_timing_enabled",
        "type": "boolean",
        "description": "Actual Server-Timing header setting read from the database."
      },
      {
        "name": "url",
        "type": "string",
        "description": "Data API endpoint URL."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the Data API configuration was last updated."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get Data API configuration for a database.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Enable Data API for a database.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Update Data API configuration for a database.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-database_id"><code>database_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Disable Data API for a database.</td>
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
<tr id="parameter-branch_id">
    <td><CopyableCode code="branch_id" /></td>
    <td><code>string</code></td>
    <td>The `branch_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api`). Resource name: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api</td>
</tr>
<tr id="parameter-database_id">
    <td><CopyableCode code="database_id" /></td>
    <td><code>string</code></td>
    <td>The `database_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api`). Resource name: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api`). Resource name: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/databases/&#123;database_id&#125;/data-api</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get Data API configuration for a database.

```sql
SELECT
name,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_data_apis
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
AND database_id = '{{ database_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
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

Enable Data API for a database.

```sql
INSERT INTO databricks_workspace.postgres.postgres_data_apis (
create_time,
name,
parent,
spec,
status,
update_time,
project_id,
branch_id,
database_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ create_time }}',
'{{ name }}',
'{{ parent }}',
'{{ spec }}',
'{{ status }}',
'{{ update_time }}',
'{{ project_id }}',
'{{ branch_id }}',
'{{ database_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_data_apis
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: database_id
      value: "{{ database_id }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_data_apis resource.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        A timestamp indicating when the Data API was first enabled.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name: projects/{project_id}/branches/{branch_id}/databases/{database_id}/data-api
    - name: parent
      value: "{{ parent }}"
      description: |
        The database containing this Data API configuration. Format: projects/{project_id}/branches/{branch_id}/databases/{database_id}
    - name: spec
      description: |
        The desired Data API configuration.
      value:
        db_aggregates_enabled: {{ db_aggregates_enabled }}
        db_extra_search_path:
          - "{{ db_extra_search_path }}"
        db_max_rows: {{ db_max_rows }}
        db_schemas:
          - "{{ db_schemas }}"
        jwt_cache_max_lifetime: "{{ jwt_cache_max_lifetime }}"
        jwt_role_claim_key: "{{ jwt_role_claim_key }}"
        openapi_mode: "{{ openapi_mode }}"
        server_cors_allowed_origins:
          - "{{ server_cors_allowed_origins }}"
        server_timing_enabled: {{ server_timing_enabled }}
    - name: status
      description: |
        The observed Data API state (read-only).
      value:
        available_schemas:
          - "{{ available_schemas }}"
        db_aggregates_enabled: {{ db_aggregates_enabled }}
        db_extra_search_path:
          - "{{ db_extra_search_path }}"
        db_max_rows: {{ db_max_rows }}
        db_schemas:
          - "{{ db_schemas }}"
        jwt_cache_max_lifetime: "{{ jwt_cache_max_lifetime }}"
        jwt_role_claim_key: "{{ jwt_role_claim_key }}"
        openapi_mode: "{{ openapi_mode }}"
        server_cors_allowed_origins:
          - "{{ server_cors_allowed_origins }}"
        server_timing_enabled: {{ server_timing_enabled }}
        url: "{{ url }}"
    - name: update_time
      value: "{{ update_time }}"
      description: |
        A timestamp indicating when the Data API configuration was last updated.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update Data API configuration for a database.

```sql
UPDATE databricks_workspace.postgres.postgres_data_apis
SET 
create_time = '{{ create_time }}',
name = '{{ name }}',
parent = '{{ parent }}',
spec = '{{ spec }}',
status = '{{ status }}',
update_time = '{{ update_time }}'
WHERE 
project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND database_id = '{{ database_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required;
```
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

Disable Data API for a database.

```sql
DELETE FROM databricks_workspace.postgres.postgres_data_apis
WHERE project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND database_id = '{{ database_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
