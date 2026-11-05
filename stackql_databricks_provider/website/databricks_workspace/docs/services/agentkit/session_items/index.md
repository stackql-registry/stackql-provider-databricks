---
title: session_items
hide_title: false
hide_table_of_contents: false
keywords:
  - session_items
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

Creates, updates, deletes, gets or lists a <code>session_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="session_items" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.session_items" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "item_id",
    "type": "string",
    "description": "Stable service-generated item ID."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Server-assigned time when the append commits. Values are nondecreasing within a session. Item listing orders by this timestamp; equal timestamps are resolved by committed append order."
  },
  {
    "name": "data",
    "type": "object",
    "description": "Complete SDK-native, JSON-compatible item. The service stores and returns this value without interpreting provider-specific fields such as ``type``, ``role``, or ``content``."
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-order_by"><code>order_by</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists items in a session.</td>
</tr>
<tr>
    <td><a href="#append"><CopyableCode code="append" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-items"><code>items</code></a></td>
    <td></td>
    <td>Appends items to a session.</td>
</tr>
<tr>
    <td><a href="#clear"><CopyableCode code="clear" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Clears all items from a session.</td>
</tr>
<tr>
    <td><a href="#pop"><CopyableCode code="pop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-session_store_id"><code>session_store_id</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Pops the newest item from a session.</td>
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
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The `session_id` segment of the `parent` resource name (`session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;`). Resource name of the containing session, in the form ``session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;``.</td>
</tr>
<tr id="parameter-session_store_id">
    <td><CopyableCode code="session_store_id" /></td>
    <td><code>string</code></td>
    <td>The `session_store_id` segment of the `parent` resource name (`session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;`). Resource name of the containing session, in the form ``session-stores/&#123;session_store_id&#125;/sessions/&#123;session_id&#125;``.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-order_by">
    <td><CopyableCode code="order_by" /></td>
    <td><code>string</code></td>
    <td>Sort order. Supported values are ``create_time asc`` and ``create_time desc``. The default is ``create_time desc``, which returns the most recently appended items first. Equal timestamps are resolved by committed append order in the requested direction.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of items to return. Defaults to 10; must be between 1 and 100.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists items in a session.

```sql
SELECT
item_id,
create_time,
data
FROM databricks_workspace.agentkit.session_items
WHERE session_store_id = '{{ session_store_id }}' -- required
AND session_id = '{{ session_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND order_by = '{{ order_by }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="append"
    values={[
        { label: 'append', value: 'append' },
        { label: 'clear', value: 'clear' },
        { label: 'pop', value: 'pop' }
    ]}
>
<TabItem value="append">

Appends items to a session.

```sql
EXEC databricks_workspace.agentkit.session_items.append 
@session_store_id='{{ session_store_id }}' --required, 
@session_id='{{ session_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"items": "{{ items }}"
}'
;
```
</TabItem>
<TabItem value="clear">

Clears all items from a session.

```sql
EXEC databricks_workspace.agentkit.session_items.clear 
@session_store_id='{{ session_store_id }}' --required, 
@session_id='{{ session_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
<TabItem value="pop">

Pops the newest item from a session.

```sql
EXEC databricks_workspace.agentkit.session_items.pop 
@session_store_id='{{ session_store_id }}' --required, 
@session_id='{{ session_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
