---
title: database_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - database_tables
  - database
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

Creates, updates, deletes, gets or lists a <code>database_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="database_tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.database.database_tables" /></td></tr>
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
    "description": ""
  },
  {
    "name": "database_instance_name",
    "type": "string",
    "description": "Name of the target database instance. This is required when creating database tables in standard catalogs. This is optional when creating database tables in registered catalogs. If this field is specified when creating database tables in registered catalogs, the database instance name MUST match that of the registered catalog (or the request will be rejected)."
  },
  {
    "name": "logical_database_name",
    "type": "string",
    "description": "Target Postgres database object (logical database) name for this table. When creating a table in a standard catalog, this field is required. In this scenario, specifying this field will allow targeting an arbitrary postgres database. Registration of database tables via /database/tables is currently only supported in standard catalogs."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a Database Table.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a Database Table. Useful for registering pre-existing PG tables in UC. See</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete a Database Table.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
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

Get a Database Table.

```sql
SELECT
name,
database_instance_name,
logical_database_name
FROM databricks_workspace.database.database_tables
WHERE name = '{{ name }}' -- required
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

Create a Database Table. Useful for registering pre-existing PG tables in UC. See

```sql
INSERT INTO databricks_workspace.database.database_tables (
name,
database_instance_name,
logical_database_name,
deployment_name,
workspace_domain
)
SELECT 
'{{ name }}' /* required */,
'{{ database_instance_name }}',
'{{ logical_database_name }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
database_instance_name,
logical_database_name
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: database_tables
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the database_tables resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the database_tables resource.
    - name: name
      value: "{{ name }}"
    - name: database_instance_name
      value: "{{ database_instance_name }}"
      description: |
        Name of the target database instance. This is required when creating database tables in standard catalogs. This is optional when creating database tables in registered catalogs. If this field is specified when creating database tables in registered catalogs, the database instance name MUST match that of the registered catalog (or the request will be rejected).
    - name: logical_database_name
      value: "{{ logical_database_name }}"
      description: |
        Target Postgres database object (logical database) name for this table. When creating a table in a standard catalog, this field is required. In this scenario, specifying this field will allow targeting an arbitrary postgres database. Registration of database tables via /database/tables is currently only supported in standard catalogs.
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

Delete a Database Table.

```sql
DELETE FROM databricks_workspace.database.database_tables
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
