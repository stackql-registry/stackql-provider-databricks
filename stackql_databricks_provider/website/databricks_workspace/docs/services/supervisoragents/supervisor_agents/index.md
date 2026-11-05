---
title: supervisor_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - supervisor_agents
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

Creates, updates, deletes, gets or lists a <code>supervisor_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="supervisor_agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.supervisoragents.supervisor_agents" /></td></tr>
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
    "description": "Deprecated: Use supervisor_agent_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the SupervisorAgent. Format: supervisor-agents/&#123;supervisor_agent_id&#125;"
  },
  {
    "name": "experiment_id",
    "type": "string",
    "description": "The MLflow experiment ID."
  },
  {
    "name": "supervisor_agent_id",
    "type": "string",
    "description": "The universally unique identifier (UUID) of the Supervisor Agent."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the supervisor agent's serving endpoint."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Creation timestamp."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The creator of the Supervisor Agent."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this agent can do (user-facing)."
  },
  {
    "name": "instructions",
    "type": "string",
    "description": "Optional natural-language instructions for the supervisor agent."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Deprecated: Use supervisor_agent_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the SupervisorAgent. Format: supervisor-agents/&#123;supervisor_agent_id&#125;"
  },
  {
    "name": "experiment_id",
    "type": "string",
    "description": "The MLflow experiment ID."
  },
  {
    "name": "supervisor_agent_id",
    "type": "string",
    "description": "The universally unique identifier (UUID) of the Supervisor Agent."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the supervisor agent's serving endpoint."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Creation timestamp."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The creator of the Supervisor Agent."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this agent can do (user-facing)."
  },
  {
    "name": "instructions",
    "type": "string",
    "description": "Optional natural-language instructions for the supervisor agent."
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
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists Supervisor Agents.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-display_name"><code>display_name</code></a></td>
    <td></td>
    <td>Creates a new Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-display_name"><code>display_name</code></a></td>
    <td></td>
    <td>Updates a Supervisor Agent. The fields that are required depend on the paths specified in</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a Supervisor Agent.</td>
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
    <td>The `supervisor_agent_id` segment of the `name` resource name (`supervisor-agents/&#123;supervisor_agent_id&#125;`). The resource name of the Supervisor Agent. Format: supervisor-agents/&#123;supervisor_agent_id&#125;</td>
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
    <td>The maximum number of supervisor agents to return. If unspecified, at most 100 supervisor agents will be returned. The maximum value is 100; values above 100 will be coerced to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListSupervisorAgents`` call. Provide this to retrieve the subsequent page. If unspecified, the first page will be returned.</td>
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

Gets a Supervisor Agent.

```sql
SELECT
id,
name,
experiment_id,
supervisor_agent_id,
display_name,
endpoint_name,
create_time,
creator,
description,
instructions
FROM databricks_workspace.supervisoragents.supervisor_agents
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Supervisor Agents.

```sql
SELECT
id,
name,
experiment_id,
supervisor_agent_id,
display_name,
endpoint_name,
create_time,
creator,
description,
instructions
FROM databricks_workspace.supervisoragents.supervisor_agents
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

Creates a new Supervisor Agent.

```sql
INSERT INTO databricks_workspace.supervisoragents.supervisor_agents (
display_name,
create_time,
creator,
description,
endpoint_name,
experiment_id,
id,
instructions,
name,
supervisor_agent_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ display_name }}' /* required */,
'{{ create_time }}',
'{{ creator }}',
'{{ description }}',
'{{ endpoint_name }}',
'{{ experiment_id }}',
'{{ id }}',
'{{ instructions }}',
'{{ name }}',
'{{ supervisor_agent_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
id,
name,
experiment_id,
supervisor_agent_id,
display_name,
endpoint_name,
create_time,
creator,
description,
instructions
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: supervisor_agents
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the supervisor_agents resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the supervisor_agents resource.
    - name: display_name
      value: "{{ display_name }}"
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Creation timestamp.
    - name: creator
      value: "{{ creator }}"
      description: |
        The creator of the Supervisor Agent.
    - name: description
      value: "{{ description }}"
      description: |
        Description of what this agent can do (user-facing).
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: |
        The name of the supervisor agent's serving endpoint.
    - name: experiment_id
      value: "{{ experiment_id }}"
      description: |
        The MLflow experiment ID.
    - name: id
      value: "{{ id }}"
      description: |
        Deprecated: Use supervisor_agent_id instead.
    - name: instructions
      value: "{{ instructions }}"
      description: |
        Optional natural-language instructions for the supervisor agent.
    - name: name
      value: "{{ name }}"
      description: |
        The resource name of the SupervisorAgent. Format: supervisor-agents/{supervisor_agent_id}
    - name: supervisor_agent_id
      value: "{{ supervisor_agent_id }}"
      description: |
        The universally unique identifier (UUID) of the Supervisor Agent.
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

Updates a Supervisor Agent. The fields that are required depend on the paths specified in

```sql
UPDATE databricks_workspace.supervisoragents.supervisor_agents
SET 
display_name = '{{ display_name }}',
create_time = '{{ create_time }}',
creator = '{{ creator }}',
description = '{{ description }}',
endpoint_name = '{{ endpoint_name }}',
experiment_id = '{{ experiment_id }}',
id = '{{ id }}',
instructions = '{{ instructions }}',
name = '{{ name }}',
supervisor_agent_id = '{{ supervisor_agent_id }}'
WHERE 
supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND display_name = '{{ display_name }}' --required
RETURNING
id,
name,
experiment_id,
supervisor_agent_id,
display_name,
endpoint_name,
create_time,
creator,
description,
instructions;
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

Deletes a Supervisor Agent.

```sql
DELETE FROM databricks_workspace.supervisoragents.supervisor_agents
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
