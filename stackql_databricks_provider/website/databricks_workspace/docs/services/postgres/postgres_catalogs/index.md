---
title: postgres_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_catalogs
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

Creates, updates, deletes, gets or lists a <code>postgres_catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_catalogs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_catalogs" /></td></tr>
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
    "description": "Output only. The full resource path of the catalog. Format: \"catalogs/&#123;catalog_id&#125;\"."
  },
  {
    "name": "catalog_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the catalog was created."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The desired state of the Catalog.",
    "children": [
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The name of the Postgres database inside the specified Lakebase project and branch to be associated with the UC catalog. This database must already exist, unless create_database_if_missing is set to true on creation. A database can only be registered with one UC catalog at a time. To re-register a database with a different catalog, the existing catalog must be deleted first. A child branch inherits the fact of parent's registration. This means the same-named database in a child branch cannot be registered with a second catalog while the parent's registration exists. To allow registering the database of a child branch, drop and recreate the database on the child branch. This removes the fact of parent's registration from this branch only. Doing Point In Time Restore (PITR) prior to the moment before the Postgres DB was registered in the Catalog drops the fact of registration of the database. So the user should avoid doing so."
      },
      {
        "name": "branch",
        "type": "string",
        "description": "The resource path of the branch associated with the catalog. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;."
      },
      {
        "name": "create_database_if_missing",
        "type": "boolean",
        "description": "If set to true, the specified postgres_database is created on behalf of the calling user if it does not already exist. In this case, the calling user has a role created for them in Postgres if they do not already have one. Defaults to false, meaning that the request fails if the specified postgres_database does not already exist."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The observed state of the Catalog.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "The resource path of the branch associated with the catalog. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;."
      },
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The name of the Postgres database associated with the catalog."
      },
      {
        "name": "project",
        "type": "string",
        "description": "The resource path of the project associated with the catalog. Format: projects/&#123;project_id&#125;."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique identifier for the catalog."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the catalog was last updated."
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
    <td><a href="#parameter-catalog_id"><code>catalog_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a Database Catalog.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-catalog_id"><code>catalog_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-catalog"><code>catalog</code></a></td>
    <td></td>
    <td>Register a Postgres database in the Unity Catalog.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-catalog_id"><code>catalog_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete a Database Catalog.</td>
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
<tr id="parameter-catalog_id">
    <td><CopyableCode code="catalog_id" /></td>
    <td><code>string</code></td>
    <td>The `catalog_id` segment of the `name` resource name (`catalogs/&#123;catalog_id&#125;`). The full resource path of the catalog to delete. Format: "catalogs/&#123;catalog_id&#125;".</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
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

Get a Database Catalog.

```sql
SELECT
name,
catalog_id,
create_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_catalogs
WHERE catalog_id = '{{ catalog_id }}' -- required
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

Register a Postgres database in the Unity Catalog.

```sql
INSERT INTO databricks_workspace.postgres.postgres_catalogs (
catalog,
catalog_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ catalog }}' /* required */,
'{{ catalog_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_catalogs
  props:
    - name: catalog_id
      value: "{{ catalog_id }}"
      description: Required parameter for the postgres_catalogs resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_catalogs resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_catalogs resource.
    - name: catalog
      value:
        catalog_id: "{{ catalog_id }}"
        create_time: "{{ create_time }}"
        name: "{{ name }}"
        spec:
          postgres_database: "{{ postgres_database }}"
          branch: "{{ branch }}"
          create_database_if_missing: {{ create_database_if_missing }}
        status:
          branch: "{{ branch }}"
          postgres_database: "{{ postgres_database }}"
          project: "{{ project }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
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

Delete a Database Catalog.

```sql
DELETE FROM databricks_workspace.postgres.postgres_catalogs
WHERE catalog_id = '{{ catalog_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
