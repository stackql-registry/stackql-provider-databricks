---
title: memory_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - memory_stores
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

Creates, updates, deletes, gets or lists a <code>memory_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="memory_stores" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.memory_stores" /></td></tr>
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
    "description": "Resource name in the form ``memory-stores/&#123;managed_memory_store_id&#125;``."
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "Workspace-local user ID of the authenticated principal that created the store. This is immutable server-set attribution and does not grant access; authorization is evaluated from the authenticated request context."
  },
  {
    "name": "owner_user_id",
    "type": "string",
    "description": "Deprecated alias for ``creator_user_id``. This identifies the original creator, not a transferable owner. Use ``creator_user_id`` instead."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "Workspace that owns the memory store."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Deprecated compatibility alias for the caller-provided memory store ID. Canonical clients provide the ID through ``CreateMemoryStoreRequest.managed_memory_store_id`` and use ``name`` as the resource identifier."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the store was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the memory store."
  },
  {
    "name": "storage_backend",
    "type": "object",
    "description": "Service-managed storage backing this memory store.",
    "children": [
      {
        "name": "backend_id",
        "type": "string",
        "description": "Backend-specific identifier. For Lakebase, this is the project ID."
      },
      {
        "name": "backend_type",
        "type": "string",
        "description": "Type of the storage backend. (STORAGE_BACKEND_TYPE_LAKEBASE)"
      }
    ]
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
    "description": "Resource name in the form ``memory-stores/&#123;managed_memory_store_id&#125;``."
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "Workspace-local user ID of the authenticated principal that created the store. This is immutable server-set attribution and does not grant access; authorization is evaluated from the authenticated request context."
  },
  {
    "name": "owner_user_id",
    "type": "string",
    "description": "Deprecated alias for ``creator_user_id``. This identifies the original creator, not a transferable owner. Use ``creator_user_id`` instead."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "Workspace that owns the memory store."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Deprecated compatibility alias for the caller-provided memory store ID. Canonical clients provide the ID through ``CreateMemoryStoreRequest.managed_memory_store_id`` and use ``name`` as the resource identifier."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the store was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the memory store."
  },
  {
    "name": "storage_backend",
    "type": "object",
    "description": "Service-managed storage backing this memory store.",
    "children": [
      {
        "name": "backend_id",
        "type": "string",
        "description": "Backend-specific identifier. For Lakebase, this is the project ID."
      },
      {
        "name": "backend_type",
        "type": "string",
        "description": "Type of the storage backend. (STORAGE_BACKEND_TYPE_LAKEBASE)"
      }
    ]
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
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist in the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists memory stores in the caller's workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a memory store in the caller's workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Updates a memory store's description and metadata.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist in the</td>
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
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-managed_memory_store_id">
    <td><CopyableCode code="managed_memory_store_id" /></td>
    <td><code>string</code></td>
    <td>The `managed_memory_store_id` segment of the `name` resource name (`memory-stores/&#123;managed_memory_store_id&#125;`). Resource name in the form ``memory-stores/&#123;managed_memory_store_id&#125;``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Only ``description`` and ``metadata`` may be updated. Selecting ``metadata`` replaces the entire map.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of stores to return. The service may return fewer stores than requested. Defaults to 10; must be between 1 and 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous ListManagedMemoryStores response.</td>
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

Retrieves a memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist in the

```sql
SELECT
name,
creator_user_id,
owner_user_id,
workspace_id,
display_name,
create_time,
description,
storage_backend,
update_time
FROM databricks_workspace.agentkit.memory_stores
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists memory stores in the caller's workspace.

```sql
SELECT
name,
creator_user_id,
owner_user_id,
workspace_id,
display_name,
create_time,
description,
storage_backend,
update_time
FROM databricks_workspace.agentkit.memory_stores
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

Creates a memory store in the caller's workspace.

```sql
INSERT INTO databricks_workspace.agentkit.memory_stores (
create_time,
creator_user_id,
description,
display_name,
name,
owner_user_id,
storage_backend,
update_time,
workspace_id,
managed_memory_store_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ create_time }}',
'{{ creator_user_id }}',
'{{ description }}',
'{{ display_name }}',
'{{ name }}',
'{{ owner_user_id }}',
'{{ storage_backend }}',
'{{ update_time }}',
{{ workspace_id }},
'{{ managed_memory_store_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
creator_user_id,
owner_user_id,
workspace_id,
display_name,
create_time,
description,
storage_backend,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: memory_stores
  props:
    - name: managed_memory_store_id
      value: "{{ managed_memory_store_id }}"
      description: Required parameter for the memory_stores resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the memory_stores resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the memory_stores resource.
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
        Human-readable description of the memory store.
    - name: display_name
      value: "{{ display_name }}"
      description: |
        Deprecated compatibility alias for the caller-provided memory store ID. Canonical clients provide the ID through \`\`CreateMemoryStoreRequest.managed_memory_store_id\`\` and use \`\`name\`\` as the resource identifier.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name in the form \`\`memory-stores/{managed_memory_store_id}\`\`.
    - name: owner_user_id
      value: "{{ owner_user_id }}"
      description: |
        Deprecated alias for \`\`creator_user_id\`\`. This identifies the original creator, not a transferable owner. Use \`\`creator_user_id\`\` instead.
    - name: storage_backend
      description: |
        Service-managed storage backing this memory store.
      value:
        backend_id: "{{ backend_id }}"
        backend_type: "{{ backend_type }}"
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time when the store was last updated.
    - name: workspace_id
      value: {{ workspace_id }}
      description: |
        Workspace that owns the memory store.
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

Updates a memory store's description and metadata.

```sql
UPDATE databricks_workspace.agentkit.memory_stores
SET 
create_time = '{{ create_time }}',
creator_user_id = '{{ creator_user_id }}',
description = '{{ description }}',
display_name = '{{ display_name }}',
name = '{{ name }}',
owner_user_id = '{{ owner_user_id }}',
storage_backend = '{{ storage_backend }}',
update_time = '{{ update_time }}',
workspace_id = {{ workspace_id }}
WHERE 
managed_memory_store_id = '{{ managed_memory_store_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
RETURNING
name,
creator_user_id,
owner_user_id,
workspace_id,
display_name,
create_time,
description,
storage_backend,
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

Deletes a memory store by resource name. Returns ``NOT_FOUND`` when the store does not exist in the

```sql
DELETE FROM databricks_workspace.agentkit.memory_stores
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
