---
title: tools
hide_title: false
hide_table_of_contents: false
keywords:
  - tools
  - supervisoragents
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

Creates, updates, deletes, gets or lists a <code>tools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tools" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.supervisoragents.tools" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "Deprecated: Use tool_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;"
  },
  {
    "name": "tool_id",
    "type": "string",
    "description": "User specified id of the Tool."
  },
  {
    "name": "app",
    "type": "object",
    "description": "Databricks app. Supported app: custom mcp, custom agent.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "App name"
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this tool does (user-facing)."
  },
  {
    "name": "genie_space",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "knowledge_assistant",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "knowledge_assistant_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "serving_endpoint_name",
        "type": "string",
        "description": "Deprecated: use knowledge_assistant_id instead."
      }
    ]
  },
  {
    "name": "tool_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "uc_connection",
    "type": "object",
    "description": "Databricks UC connection. Supported connection: external mcp server.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_function",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "volume",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Deprecated: Use tool_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;"
  },
  {
    "name": "tool_id",
    "type": "string",
    "description": "User specified id of the Tool."
  },
  {
    "name": "app",
    "type": "object",
    "description": "Databricks app. Supported app: custom mcp, custom agent.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "App name"
      }
    ]
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this tool does (user-facing)."
  },
  {
    "name": "genie_space",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "id",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "knowledge_assistant",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "knowledge_assistant_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "serving_endpoint_name",
        "type": "string",
        "description": "Deprecated: use knowledge_assistant_id instead."
      }
    ]
  },
  {
    "name": "tool_type",
    "type": "string",
    "description": ""
  },
  {
    "name": "uc_connection",
    "type": "object",
    "description": "Databricks UC connection. Supported connection: external mcp server.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "uc_function",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "volume",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-tool_id"><code>tool_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a Tool.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists Tools under a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-tool_id"><code>tool_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-tool_type"><code>tool_type</code></a></td>
    <td></td>
    <td>Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-tool_id"><code>tool_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-tool_type"><code>tool_type</code></a></td>
    <td></td>
    <td>Updates a Tool. Only the ``description`` field can be updated. To change immutable fields such as tool</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-tool_id"><code>tool_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a Tool.</td>
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
<tr id="parameter-supervisor_agent_id">
    <td><CopyableCode code="supervisor_agent_id" /></td>
    <td><code>string</code></td>
    <td>The `supervisor_agent_id` segment of the `name` resource name (`supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;`). The resource name of the Tool. Format: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;</td>
</tr>
<tr id="parameter-tool_id">
    <td><CopyableCode code="tool_id" /></td>
    <td><code>string</code></td>
    <td>The `tool_id` segment of the `name` resource name (`supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;`). The resource name of the Tool. Format: supervisor-agents/&#123;supervisor_agent_id&#125;/tools/&#123;tool_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Field mask for fields to be updated.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
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

Gets a Tool.

```sql
SELECT
id,
name,
tool_id,
app,
description,
genie_space,
knowledge_assistant,
tool_type,
uc_connection,
uc_function,
volume
FROM databricks_workspace.supervisoragents.tools
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' -- required
AND tool_id = '{{ tool_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Tools under a Supervisor Agent.

```sql
SELECT
id,
name,
tool_id,
app,
description,
genie_space,
knowledge_assistant,
tool_type,
uc_connection,
uc_function,
volume
FROM databricks_workspace.supervisoragents.tools
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' -- required
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

Creates a Tool under a Supervisor Agent. Specify one of "genie_space", "knowledge_assistant",

```sql
INSERT INTO databricks_workspace.supervisoragents.tools (
tool_type,
app,
description,
genie_space,
id,
knowledge_assistant,
name,
tool_id,
uc_connection,
uc_function,
volume,
supervisor_agent_id,
tool_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ tool_type }}' /* required */,
'{{ app }}',
'{{ description }}',
'{{ genie_space }}',
'{{ id }}',
'{{ knowledge_assistant }}',
'{{ name }}',
'{{ tool_id }}',
'{{ uc_connection }}',
'{{ uc_function }}',
'{{ volume }}',
'{{ supervisor_agent_id }}',
'{{ tool_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
id,
name,
tool_id,
app,
description,
genie_space,
knowledge_assistant,
tool_type,
uc_connection,
uc_function,
volume
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tools
  props:
    - name: supervisor_agent_id
      value: "{{ supervisor_agent_id }}"
      description: Required parameter for the tools resource.
    - name: tool_id
      value: "{{ tool_id }}"
      description: Required parameter for the tools resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the tools resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the tools resource.
    - name: tool_type
      value: "{{ tool_type }}"
    - name: app
      description: |
        Databricks app. Supported app: custom mcp, custom agent.
      value:
        name: "{{ name }}"
    - name: description
      value: "{{ description }}"
      description: |
        Description of what this tool does (user-facing).
    - name: genie_space
      value:
        id: "{{ id }}"
    - name: id
      value: "{{ id }}"
      description: |
        Deprecated: Use tool_id instead.
    - name: knowledge_assistant
      value:
        knowledge_assistant_id: "{{ knowledge_assistant_id }}"
        serving_endpoint_name: "{{ serving_endpoint_name }}"
    - name: name
      value: "{{ name }}"
      description: |
        Full resource name: supervisor-agents/{supervisor_agent_id}/tools/{tool_id}
    - name: tool_id
      value: "{{ tool_id }}"
      description: |
        User specified id of the Tool.
    - name: uc_connection
      description: |
        Databricks UC connection. Supported connection: external mcp server.
      value:
        name: "{{ name }}"
    - name: uc_function
      value:
        name: "{{ name }}"
    - name: volume
      value:
        name: "{{ name }}"
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

Updates a Tool. Only the ``description`` field can be updated. To change immutable fields such as tool

```sql
UPDATE databricks_workspace.supervisoragents.tools
SET 
tool_type = '{{ tool_type }}',
app = '{{ app }}',
description = '{{ description }}',
genie_space = '{{ genie_space }}',
id = '{{ id }}',
knowledge_assistant = '{{ knowledge_assistant }}',
name = '{{ name }}',
tool_id = '{{ tool_id }}',
uc_connection = '{{ uc_connection }}',
uc_function = '{{ uc_function }}',
volume = '{{ volume }}'
WHERE 
supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND tool_id = '{{ tool_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND tool_type = '{{ tool_type }}' --required
RETURNING
id,
name,
tool_id,
app,
description,
genie_space,
knowledge_assistant,
tool_type,
uc_connection,
uc_function,
volume;
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

Deletes a Tool.

```sql
DELETE FROM databricks_workspace.supervisoragents.tools
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND tool_id = '{{ tool_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
