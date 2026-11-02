---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
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

Creates, updates, deletes, gets or lists a <code>sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sessions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.sessions" /></td></tr>
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
    "description": "Resource name in the form ``session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;``."
  },
  {
    "name": "actor_id",
    "type": "string",
    "description": "Opaque caller-provided identifier for the application actor associated with the session. This is application data and has no Databricks authentication or authorization semantics. Use the same value as the Managed Memory Entry ``actor_id`` when storing memories associated with this actor. Every session must set it. A child session must use the same value as its parent."
  },
  {
    "name": "parent_session_id",
    "type": "string",
    "description": "Immediate parent session ID. Set only at creation for child sessions, immutable thereafter, and restricted to the same store."
  },
  {
    "name": "root_session_id",
    "type": "string",
    "description": "Top-level session ID in the spawn tree. This equals ``session_id`` for a root or fork and is inherited transitively by child sessions."
  },
  {
    "name": "session_id",
    "type": "string",
    "description": "Unique session ID. The service generates a UUID unless the caller supplies ``CreateSessionRequest.session_id``."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the session was created."
  },
  {
    "name": "last_activity_time",
    "type": "string (date-time)",
    "description": "Time when the session's item history was last mutated."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Mutable caller-defined string labels."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time when session resource fields last changed."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name in the form ``session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;``."
  },
  {
    "name": "actor_id",
    "type": "string",
    "description": "Opaque caller-provided identifier for the application actor associated with the session. This is application data and has no Databricks authentication or authorization semantics. Use the same value as the Managed Memory Entry ``actor_id`` when storing memories associated with this actor. Every session must set it. A child session must use the same value as its parent."
  },
  {
    "name": "parent_session_id",
    "type": "string",
    "description": "Immediate parent session ID. Set only at creation for child sessions, immutable thereafter, and restricted to the same store."
  },
  {
    "name": "root_session_id",
    "type": "string",
    "description": "Top-level session ID in the spawn tree. This equals ``session_id`` for a root or fork and is inherited transitively by child sessions."
  },
  {
    "name": "session_id",
    "type": "string",
    "description": "Unique session ID. The service generates a UUID unless the caller supplies ``CreateSessionRequest.session_id``."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time when the session was created."
  },
  {
    "name": "last_activity_time",
    "type": "string (date-time)",
    "description": "Time when the session's item history was last mutated."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Mutable caller-defined string labels."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time when session resource fields last changed."
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
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a session by resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists sessions within a session store.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a></td>
    <td><a href="#parameter-session_id"><code>session_id</code></a></td>
    <td>Creates a session within a session store.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a></td>
    <td></td>
    <td>Updates a session's mutable fields.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a session, its items, and any descendant sessions recursively. Independently retained memory</td>
</tr>
<tr>
    <td><a href="#extract_memories"><CopyableCode code="extract_memories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-memory_store"><code>memory_store</code></a></td>
    <td></td>
    <td>Synchronously extracts memories from a single session into the given memory store, returning the</td>
</tr>
<tr>
    <td><a href="#fork"><CopyableCode code="fork" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-source_session_id"><code>source_session_id</code></a>, <a href="#parameter-actor_id"><code>actor_id</code></a></td>
    <td></td>
    <td>Forks a session into an independent top-level copy.</td>
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
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>Identifier of the session whose transcript is distilled into memories.</td>
</tr>
<tr id="parameter-session_store_id">
    <td><CopyableCode code="session_store_id" /></td>
    <td><code>string</code></td>
    <td>The `session_store_id` segment of the `parent` resource name (`session-stores/&#123;session_store_id&#125;`). Resource name of the containing session store, in the form ``session-stores/&#123;session_store_id&#125;``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Only ``metadata`` is mutable; any other path returns ``INVALID_PARAMETER_VALUE``.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Filter expression. Supported fields include ``actor_id`` and ``metadata``; for example, ``actor_id = "support-customer-123"``.</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Sort order. Defaults to ``last_activity_time desc``. Page-token continuation is exactly-once when ordering by ``create_time`` (immutable); ordering by ``last_activity_time`` is best-effort, because that value changes as a session gains activity, so a session updated between page requests may be repeated or skipped. To enumerate every session exactly once, order by ``create_time``.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of sessions to return. Defaults to 10; must be between 1 and 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Token returned by a previous list request.</td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>Optional caller-selected session ID. The service generates a UUID when this field is omitted. The ID must be unique; a collision returns ``ALREADY_EXISTS``.</td>
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

Gets a session by resource name.

```sql
SELECT
name,
actor_id,
parent_session_id,
root_session_id,
session_id,
create_time,
last_activity_time,
metadata,
update_time
FROM databricks_workspace.agentkit.sessions
WHERE session_store_id = '{{ session_store_id }}' -- required
AND session_id = '{{ session_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists sessions within a session store.

```sql
SELECT
name,
actor_id,
parent_session_id,
root_session_id,
session_id,
create_time,
last_activity_time,
metadata,
update_time
FROM databricks_workspace.agentkit.sessions
WHERE session_store_id = '{{ session_store_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND filter = '{{ filter }}'
AND order_by = '{{ order_by }}'
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

Creates a session within a session store.

```sql
INSERT INTO databricks_workspace.agentkit.sessions (
actor_id,
create_time,
last_activity_time,
metadata,
name,
parent_session_id,
root_session_id,
session_id,
update_time,
session_store_id,
deployment_name,
workspace_domain,
session_id
)
SELECT 
'{{ actor_id }}' /* required */,
'{{ create_time }}',
'{{ last_activity_time }}',
'{{ metadata }}',
'{{ name }}',
'{{ parent_session_id }}',
'{{ root_session_id }}',
'{{ session_id }}',
'{{ update_time }}',
'{{ session_store_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ session_id }}'
RETURNING
name,
actor_id,
parent_session_id,
root_session_id,
session_id,
create_time,
last_activity_time,
metadata,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sessions
  props:
    - name: session_store_id
      value: "{{ session_store_id }}"
      description: Required parameter for the sessions resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the sessions resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the sessions resource.
    - name: actor_id
      value: "{{ actor_id }}"
      description: |
        Opaque caller-provided identifier for the application actor associated with the session. This is application data and has no Databricks authentication or authorization semantics. Use the same value as the Managed Memory Entry \`\`actor_id\`\` when storing memories associated with this actor. Every session must set it. A child session must use the same value as its parent.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time when the session was created.
    - name: last_activity_time
      value: "{{ last_activity_time }}"
      description: |
        Time when the session's item history was last mutated.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        Mutable caller-defined string labels.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name in the form \`\`session-stores/{session_store_id}/sessions/{session_id}\`\`.
    - name: parent_session_id
      value: "{{ parent_session_id }}"
      description: |
        Immediate parent session ID. Set only at creation for child sessions, immutable thereafter, and restricted to the same store.
    - name: root_session_id
      value: "{{ root_session_id }}"
      description: |
        Top-level session ID in the spawn tree. This equals \`\`session_id\`\` for a root or fork and is inherited transitively by child sessions.
    - name: session_id
      value: "{{ session_id }}"
      description: |
        Unique session ID. The service generates a UUID unless the caller supplies \`\`CreateSessionRequest.session_id\`\`.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time when session resource fields last changed.
    - name: session_id
      value: "{{ session_id }}"
      description: Optional caller-selected session ID. The service generates a UUID when this field is omitted. The ID must be unique; a collision returns \`\`ALREADY_EXISTS\`\`.
      description: Optional caller-selected session ID. The service generates a UUID when this field is omitted. The ID must be unique; a collision returns \`\`ALREADY_EXISTS\`\`.
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

Updates a session's mutable fields.

```sql
UPDATE databricks_workspace.agentkit.sessions
SET 
actor_id = '{{ actor_id }}',
create_time = '{{ create_time }}',
last_activity_time = '{{ last_activity_time }}',
metadata = '{{ metadata }}',
name = '{{ name }}',
parent_session_id = '{{ parent_session_id }}',
root_session_id = '{{ root_session_id }}',
session_id = '{{ session_id }}',
update_time = '{{ update_time }}'
WHERE 
session_store_id = '{{ session_store_id }}' --required
AND session_id = '{{ session_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND actor_id = '{{ actor_id }}' --required
RETURNING
name,
actor_id,
parent_session_id,
root_session_id,
session_id,
create_time,
last_activity_time,
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

Deletes a session, its items, and any descendant sessions recursively. Independently retained memory

```sql
DELETE FROM databricks_workspace.agentkit.sessions
WHERE session_store_id = '{{ session_store_id }}' --required
AND session_id = '{{ session_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="extract_memories"
    values={[
        { label: 'extract_memories', value: 'extract_memories' },
        { label: 'fork', value: 'fork' }
    ]}
>
<TabItem value="extract_memories">

Synchronously extracts memories from a single session into the given memory store, returning the

```sql
EXEC databricks_workspace.agentkit.sessions.extract_memories 
@session_store_id='{{ session_store_id }}' --required, 
@session_id='{{ session_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"memory_store": "{{ memory_store }}", 
"dry_run": {{ dry_run }}, 
"instructions": "{{ instructions }}"
}'
;
```
</TabItem>
<TabItem value="fork">

Forks a session into an independent top-level copy.

```sql
EXEC databricks_workspace.agentkit.sessions.fork 
@session_store_id='{{ session_store_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"source_session_id": "{{ source_session_id }}", 
"actor_id": "{{ actor_id }}", 
"metadata": "{{ metadata }}", 
"session_id": "{{ session_id }}", 
"up_to_item_id": "{{ up_to_item_id }}"
}'
;
```
</TabItem>
</Tabs>
