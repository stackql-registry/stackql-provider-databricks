---
title: sandbox_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_commands
  - sandbox
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

Creates, updates, deletes, gets or lists a <code>sandbox_commands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sandbox_commands" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sandbox.sandbox_commands" /></td></tr>
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
    "name": "command_id",
    "type": "string",
    "description": "Stable identifier for this command."
  },
  {
    "name": "args",
    "type": "array",
    "description": "Arguments passed to the program."
  },
  {
    "name": "cmd",
    "type": "string",
    "description": "The program that was executed."
  },
  {
    "name": "exit_code",
    "type": "integer",
    "description": "Process exit code. Only present when finished is true and the process exited normally (not killed by signal or failed to start)."
  },
  {
    "name": "finished",
    "type": "boolean",
    "description": "Whether the command has finished executing."
  },
  {
    "name": "pid",
    "type": "integer",
    "description": "PID of the spawned process. Absent if the process failed to start."
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
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the tracked command executions (running and completed) in a sandbox.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-cmd"><code>cmd</code></a></td>
    <td></td>
    <td>Runs a command in the sandbox and blocks until it exits, returning the captured stdout, stderr and</td>
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
<tr id="parameter-sandbox_id">
    <td><CopyableCode code="sandbox_id" /></td>
    <td><code>string</code></td>
    <td>The `sandbox_id` segment of the `name` resource name (`sandboxes/&#123;sandbox_id&#125;`). Resource name of the sandbox to run the command in, in the form ``sandboxes/&#123;sandbox_id&#125;``. Bound from the URL path.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of commands to return. The server may return fewer. If unspecified, the server returns all commands.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token returned by a previous ListCommands call. Use this to retrieve the next page of results.</td>
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

Lists the tracked command executions (running and completed) in a sandbox.

```sql
SELECT
command_id,
args,
cmd,
exit_code,
finished,
pid
FROM databricks_workspace.sandbox.sandbox_commands
WHERE sandbox_id = '{{ sandbox_id }}' -- required
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
    defaultValue="execute"
    values={[
        { label: 'execute', value: 'execute' }
    ]}
>
<TabItem value="execute">

Runs a command in the sandbox and blocks until it exits, returning the captured stdout, stderr and

```sql
EXEC databricks_workspace.sandbox.sandbox_commands.execute 
@sandbox_id='{{ sandbox_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"cmd": "{{ cmd }}", 
"args": "{{ args }}", 
"envs": "{{ envs }}", 
"execution_timeout": "{{ execution_timeout }}"
}'
;
```
</TabItem>
</Tabs>
