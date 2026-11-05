---
title: memories
hide_title: false
hide_table_of_contents: false
keywords:
  - memories
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

Creates, updates, deletes, gets or lists a <code>memories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="memories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.memories" /></td></tr>
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
    "description": "Resource name in the form ``memory-stores/&#123;managed_memory_store_id&#125;/entries/&#123;managed_memory_entry_id&#125;``. Required for updates; assigned by the service on creation."
  },
  {
    "name": "actor_id",
    "type": "string",
    "description": "Customer-provided identifier for the actor whose memory this entry represents."
  },
  {
    "name": "session_id",
    "type": "string",
    "description": "Optional identifier for the session associated with this memory entry. When omitted, the entry applies across the actor's sessions."
  },
  {
    "name": "content",
    "type": "string",
    "description": "Optional free-form memory content."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the entry was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Human-readable description of the memory entry."
  },
  {
    "name": "path",
    "type": "string",
    "description": "Absolute, case-sensitive path identifying the entry within its actor and optional session. Paths must begin with ``/`` and must not contain empty, ``.`` or ``..`` segments."
  },
  {
    "name": "source_type",
    "type": "string",
    "description": "Which writer created this entry. Caller sets this on Create; immutable after creation. (MANAGED_MEMORY_ENTRY_SOURCE_TYPE_AGENT, MANAGED_MEMORY_ENTRY_SOURCE_TYPE_DREAMER)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time when the entry was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[]} />
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
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-managed_memory_entry_id"><code>managed_memory_entry_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-view"><code>view</code></a></td>
    <td>Retrieves a memory entry by resource name. ``view`` controls whether the response includes memory</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-path_prefix"><code>path_prefix</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists memory entries for one actor. An exact ``path`` filters entries across sessions, ignoring</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td><a href="#parameter-managed_memory_entry_id"><code>managed_memory_entry_id</code></a></td>
    <td>Creates a memory entry using exclusive-create semantics. Callers may choose the entry ID; the service</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-managed_memory_entry_id"><code>managed_memory_entry_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Updates selected mutable fields on a memory entry. Identity fields are immutable.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-managed_memory_entry_id"><code>managed_memory_entry_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a memory entry by resource name. Returns ``NOT_FOUND`` when the entry does not exist in the</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a>, <a href="#parameter-query"><code>query</code></a></td>
    <td></td>
    <td>Searches memory entries by text query for one actor. Returns matching entries and scores ranked by</td>
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
<tr id="parameter-actor_id">
    <td><CopyableCode code="actor_id" /></td>
    <td><code>string</code></td>
    <td>Customer-provided identifier for the actor whose entries are listed.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-managed_memory_entry_id">
    <td><CopyableCode code="managed_memory_entry_id" /></td>
    <td><code>string</code></td>
    <td>The `managed_memory_entry_id` segment of the `name` resource name (`memory-stores/&#123;managed_memory_store_id&#125;/entries/&#123;managed_memory_entry_id&#125;`). Resource name in the form ``memory-stores/&#123;managed_memory_store_id&#125;/entries/&#123;managed_memory_entry_id&#125;``.</td>
</tr>
<tr id="parameter-managed_memory_store_id">
    <td><CopyableCode code="managed_memory_store_id" /></td>
    <td><code>string</code></td>
    <td>The `managed_memory_store_id` segment of the `parent` resource name (`memory-stores/&#123;managed_memory_store_id&#125;`). Memory store whose entries are searched, in the form ``memory-stores/&#123;managed_memory_store_id&#125;``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Only ``content`` and ``description`` may be updated.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-managed_memory_entry_id">
    <td><CopyableCode code="managed_memory_entry_id" /></td>
    <td><code>string</code></td>
    <td>Optional caller-selected memory entry ID. The service generates an ID when omitted.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of entries to return. The service may return fewer entries than requested. Defaults to 10; must be between 1 and 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous ListManagedMemoryEntries response.</td>
</tr>
<tr id="parameter-path_prefix">
    <td><CopyableCode code="path_prefix" /></td>
    <td><code>string</code></td>
    <td>Optional path prefix used to restrict entries within the actor partition.</td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>Optional session identifier. When set, only entries with this exact ``session_id`` are returned. Omitted-session (cross-session) entries are not included. Ignored when path is set.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>Controls whether each returned entry includes memory content. Defaults to ``FULL``.</td>
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

Retrieves a memory entry by resource name. ``view`` controls whether the response includes memory

```sql
SELECT
name,
actor_id,
session_id,
content,
create_time,
description,
path,
source_type,
update_time
FROM databricks_workspace.agentkit.memories
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' -- required
AND managed_memory_entry_id = '{{ managed_memory_entry_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND view = '{{ view }}'
;
```
</TabItem>
<TabItem value="list">

Lists memory entries for one actor. An exact ``path`` filters entries across sessions, ignoring

```sql
SELECT
*
FROM databricks_workspace.agentkit.memories
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' -- required
AND actor_id = '{{ actor_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND path_prefix = '{{ path_prefix }}'
AND session_id = '{{ session_id }}'
AND view = '{{ view }}'
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

Creates a memory entry using exclusive-create semantics. Callers may choose the entry ID; the service

```sql
INSERT INTO databricks_workspace.agentkit.memories (
actor_id,
path,
content,
create_time,
description,
name,
session_id,
source_type,
update_time,
managed_memory_store_id,
deployment_name,
workspace_domain,
managed_memory_entry_id
)
SELECT 
'{{ actor_id }}' /* required */,
'{{ path }}' /* required */,
'{{ content }}',
'{{ create_time }}',
'{{ description }}',
'{{ name }}',
'{{ session_id }}',
'{{ source_type }}',
'{{ update_time }}',
'{{ managed_memory_store_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ managed_memory_entry_id }}'
RETURNING
name,
actor_id,
session_id,
content,
create_time,
description,
path,
source_type,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: memories
  props:
    - name: managed_memory_store_id
      value: "{{ managed_memory_store_id }}"
      description: Required parameter for the memories resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the memories resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the memories resource.
    - name: actor_id
      value: "{{ actor_id }}"
      description: |
        Customer-provided identifier for the actor whose memory this entry represents.
    - name: path
      value: "{{ path }}"
      description: |
        Absolute, case-sensitive path identifying the entry within its actor and optional session. Paths must begin with \`\`/\`\` and must not contain empty, \`\`.\`\` or \`\`..\`\` segments.
    - name: content
      value: "{{ content }}"
      description: |
        Optional free-form memory content.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time when the entry was created.
    - name: description
      value: "{{ description }}"
      description: |
        Human-readable description of the memory entry.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name in the form \`\`memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}\`\`. Required for updates; assigned by the service on creation.
    - name: session_id
      value: "{{ session_id }}"
      description: |
        Optional identifier for the session associated with this memory entry. When omitted, the entry applies across the actor's sessions.
    - name: source_type
      value: "{{ source_type }}"
      description: |
        Which writer created this entry. Caller sets this on Create; immutable after creation.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time when the entry was last updated.
    - name: managed_memory_entry_id
      value: "{{ managed_memory_entry_id }}"
      description: Optional caller-selected memory entry ID. The service generates an ID when omitted.
      description: Optional caller-selected memory entry ID. The service generates an ID when omitted.
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

Updates selected mutable fields on a memory entry. Identity fields are immutable.

```sql
UPDATE databricks_workspace.agentkit.memories
SET 
actor_id = '{{ actor_id }}',
path = '{{ path }}',
content = '{{ content }}',
create_time = '{{ create_time }}',
description = '{{ description }}',
name = '{{ name }}',
session_id = '{{ session_id }}',
source_type = '{{ source_type }}',
update_time = '{{ update_time }}'
WHERE 
managed_memory_store_id = '{{ managed_memory_store_id }}' --required
AND managed_memory_entry_id = '{{ managed_memory_entry_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND actor_id = '{{ actor_id }}' --required
AND path = '{{ path }}' --required
RETURNING
name,
actor_id,
session_id,
content,
create_time,
description,
path,
source_type,
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

Deletes a memory entry by resource name. Returns ``NOT_FOUND`` when the entry does not exist in the

```sql
DELETE FROM databricks_workspace.agentkit.memories
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' --required
AND managed_memory_entry_id = '{{ managed_memory_entry_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="search"
    values={[
        { label: 'search', value: 'search' }
    ]}
>
<TabItem value="search">

Searches memory entries by text query for one actor. Returns matching entries and scores ranked by

```sql
EXEC databricks_workspace.agentkit.memories.search 
@managed_memory_store_id='{{ managed_memory_store_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"actor_id": "{{ actor_id }}", 
"query": "{{ query }}", 
"limit": {{ limit }}, 
"page_size": {{ page_size }}, 
"page_token": "{{ page_token }}", 
"path_prefix": "{{ path_prefix }}", 
"session_id": "{{ session_id }}", 
"view": "{{ view }}"
}'
;
```
</TabItem>
</Tabs>
