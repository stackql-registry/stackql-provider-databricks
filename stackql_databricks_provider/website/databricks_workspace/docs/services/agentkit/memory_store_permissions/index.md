---
title: memory_store_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - memory_store_permissions
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

Creates, updates, deletes, gets or lists a <code>memory_store_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="memory_store_permissions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.agentkit.memory_store_permissions" /></td></tr>
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
    "name": "permission",
    "type": "string",
    "description": "The permission level. WRITE includes READ; PERMISSION_LEVEL_UNSPECIFIED means neither is available. (READ, WRITE)"
  },
  {
    "name": "principal",
    "type": "object",
    "description": "The principal whose permission is reported.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "principal_type",
        "type": "string",
        "description": "The kind of principal. Required unless the deprecated type alias is supplied. (SERVICE_PRINCIPAL, USER)"
      }
    ]
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
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists explicit memory store grants. Only the owner or a workspace admin may list permissions.</td>
</tr>
<tr>
    <td><a href="#grant"><CopyableCode code="grant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-principal"><code>principal</code></a>, <a href="#parameter-permission"><code>permission</code></a></td>
    <td></td>
    <td>Grants a READ or WRITE permission on a memory store to a principal. Only the owner or a workspace</td>
</tr>
<tr>
    <td><a href="#revoke"><CopyableCode code="revoke" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-managed_memory_store_id"><code>managed_memory_store_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-principal"><code>principal</code></a></td>
    <td></td>
    <td>Removes a principal's explicit READ and WRITE grants on a memory store. Only the owner or a workspace</td>
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
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of permissions to return. Defaults to 100; maximum is 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Continuation token from a previous response.</td>
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

Lists explicit memory store grants. Only the owner or a workspace admin may list permissions.

```sql
SELECT
permission,
principal
FROM databricks_workspace.agentkit.memory_store_permissions
WHERE managed_memory_store_id = '{{ managed_memory_store_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="grant"
    values={[
        { label: 'grant', value: 'grant' },
        { label: 'revoke', value: 'revoke' }
    ]}
>
<TabItem value="grant">

Grants a READ or WRITE permission on a memory store to a principal. Only the owner or a workspace

```sql
EXEC databricks_workspace.agentkit.memory_store_permissions.grant 
@managed_memory_store_id='{{ managed_memory_store_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"principal": "{{ principal }}", 
"permission": "{{ permission }}"
}'
;
```
</TabItem>
<TabItem value="revoke">

Removes a principal's explicit READ and WRITE grants on a memory store. Only the owner or a workspace

```sql
EXEC databricks_workspace.agentkit.memory_store_permissions.revoke 
@managed_memory_store_id='{{ managed_memory_store_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"principal": "{{ principal }}"
}'
;
```
</TabItem>
</Tabs>
