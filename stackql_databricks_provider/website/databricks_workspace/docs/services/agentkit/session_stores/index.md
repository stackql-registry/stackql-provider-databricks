---
title: session_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - session_stores
  - agentkit
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

Creates, updates, deletes, gets or lists a <code>session_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="session_stores" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.session_stores" /></td></tr>
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
    "description": "Resource name in the form ``session-stores/&#123;session_store_id&#125;``."
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "Workspace-local user ID of the authenticated principal that created the store. This is immutable server-set attribution and does not grant access; authorization is evaluated from the authenticated request context."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the store was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the session store."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Mutable caller-defined string labels."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time when the store was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name in the form ``session-stores/&#123;session_store_id&#125;``."
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "Workspace-local user ID of the authenticated principal that created the store. This is immutable server-set attribution and does not grant access; authorization is evaluated from the authenticated request context."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the store was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the session store."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Mutable caller-defined string labels."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time when the store was last updated."
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
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a session store by resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists session stores.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a session store.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Updates a session store's description and metadata.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a session store, its sessions and items, and its service-managed storage. Memory entries</td>
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
<tr id="parameter-session_store_id">
    <td><CopyableCode code="session_store_id" /></td>
    <td><code>string</code></td>
    <td>The `session_store_id` segment of the `name` resource name (`session-stores/&#123;session_store_id&#125;`). Resource name in the form ``session-stores/&#123;session_store_id&#125;``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Only ``description`` and ``metadata`` are mutable; any other path returns ``INVALID_PARAMETER_VALUE``.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of session stores to return. Defaults to 10; must be between 1 and 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token returned by a previous list request.</td>
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

Gets a session store by resource name.

```sql
SELECT
name,
creator_user_id,
create_time,
description,
metadata,
update_time
FROM databricks_workspace.agentkit.session_stores
WHERE session_store_id = '{{ session_store_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists session stores.

```sql
SELECT
name,
creator_user_id,
create_time,
description,
metadata,
update_time
FROM databricks_workspace.agentkit.session_stores
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a session store.

```sql
INSERT INTO databricks_workspace.agentkit.session_stores (
create_time,
creator_user_id,
description,
metadata,
name,
update_time,
session_store_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ create_time }}',
'{{ creator_user_id }}',
'{{ description }}',
'{{ metadata }}',
'{{ name }}',
'{{ update_time }}',
'{{ session_store_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
creator_user_id,
create_time,
description,
metadata,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: session_stores
  props:
    - name: session_store_id
      value: "{{ session_store_id }}"
      description: Required parameter for the session_stores resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the session_stores resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the session_stores resource.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time when the store was created.
    - name: creator_user_id
      value: "{{ creator_user_id }}"
      description: |
        Workspace-local user ID of the authenticated principal that created the store. This is immutable server-set attribution and does not grant access; authorization is evaluated from the authenticated request context.
    - name: description
      value: "{{ description }}"
      description: |
        Human-readable description of the session store.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        Mutable caller-defined string labels.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name in the form \`\`session-stores/{session_store_id}\`\`.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time when the store was last updated.
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

Updates a session store's description and metadata.

```sql
UPDATE databricks_workspace.agentkit.session_stores
SET 
create_time = '{{ create_time }}',
creator_user_id = '{{ creator_user_id }}',
description = '{{ description }}',
metadata = '{{ metadata }}',
name = '{{ name }}',
update_time = '{{ update_time }}'
WHERE 
session_store_id = '{{ session_store_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
RETURNING
name,
creator_user_id,
create_time,
description,
metadata,
update_time;
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

Deletes a session store, its sessions and items, and its service-managed storage. Memory entries

```sql
DELETE FROM databricks_workspace.agentkit.session_stores
WHERE session_store_id = '{{ session_store_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
