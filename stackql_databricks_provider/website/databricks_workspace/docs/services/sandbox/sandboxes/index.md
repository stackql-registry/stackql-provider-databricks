---
title: sandboxes
hide_title: false
hide_table_of_contents: false
keywords:
  - sandboxes
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

Creates, updates, deletes, gets or lists a <code>sandboxes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sandboxes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sandbox.sandboxes" /></td></tr>
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
    "description": "The sandbox resource name, in the form ``sandboxes/&#123;sandbox_id&#125;``. Derived from ``sandbox_id``; any value supplied in a create or update request body is ignored."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display label for the sandbox. At most 256 characters."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Output only. The creation time of the sandbox."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Metadata associated with the sandbox.",
    "children": [
      {
        "name": "custom_tags",
        "type": "object",
        "description": "Key-value tags associated with the sandbox. Supports up to 54 tags. Keys must be between 1 and 512 characters, and values must not exceed 256 characters."
      }
    ]
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The desired configuration of the sandbox, supplied by the caller at creation time.",
    "children": [
      {
        "name": "compute",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "inactivity_timeout",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "environment",
        "type": "object",
        "description": "The execution environment to use for the sandbox.",
        "children": [
          {
            "name": "image_uri",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The observed runtime state of the sandbox, populated by the server.",
    "children": [
      {
        "name": "state",
        "type": "string",
        "description": "Lifecycle state of a Sandbox resource. STOPPING is the transient state while the sandbox is<br />being stopped -- by a Stop request or inactivity auto-termination -- and settles to STOPPED once<br />the operation completes. (SANDBOX_STATE_PENDING, SANDBOX_STATE_RUNNING, SANDBOX_STATE_STOPPED, SANDBOX_STATE_STOPPING)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Output only. The last update time of the sandbox metadata and spec."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The sandbox resource name, in the form ``sandboxes/&#123;sandbox_id&#125;``. Derived from ``sandbox_id``; any value supplied in a create or update request body is ignored."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display label for the sandbox. At most 256 characters."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Output only. The creation time of the sandbox."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Metadata associated with the sandbox.",
    "children": [
      {
        "name": "custom_tags",
        "type": "object",
        "description": "Key-value tags associated with the sandbox. Supports up to 54 tags. Keys must be between 1 and 512 characters, and values must not exceed 256 characters."
      }
    ]
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The desired configuration of the sandbox, supplied by the caller at creation time.",
    "children": [
      {
        "name": "compute",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "inactivity_timeout",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "environment",
        "type": "object",
        "description": "The execution environment to use for the sandbox.",
        "children": [
          {
            "name": "image_uri",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The observed runtime state of the sandbox, populated by the server.",
    "children": [
      {
        "name": "state",
        "type": "string",
        "description": "Lifecycle state of a Sandbox resource. STOPPING is the transient state while the sandbox is<br />being stopped -- by a Stop request or inactivity auto-termination -- and settles to STOPPED once<br />the operation completes. (SANDBOX_STATE_PENDING, SANDBOX_STATE_RUNNING, SANDBOX_STATE_STOPPED, SANDBOX_STATE_STOPPING)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Output only. The last update time of the sandbox metadata and spec."
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
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a Sandbox by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all Sandboxes.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-sandbox"><code>sandbox</code></a></td>
    <td></td>
    <td>Creates a new Sandbox.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-sandbox"><code>sandbox</code></a></td>
    <td></td>
    <td>Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today: display_name,</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a Sandbox.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Starts a previously stopped Sandbox under the same sandbox name. Returns NOT_FOUND if there is no</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Stops a running Sandbox, preserving it so it can later be restarted with a Start request.</td>
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
<tr id="parameter-sandbox_id">
    <td><CopyableCode code="sandbox_id" /></td>
    <td><code>string</code></td>
    <td>The `sandbox_id` segment of the `name` resource name (`sandboxes/&#123;sandbox_id&#125;`). Resource name of the sandbox to stop, in the form ``sandboxes/&#123;sandbox_id&#125;``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Field paths to update. Must be a non-empty subset of: - display_name - spec.compute.inactivity_timeout Any other path returns INVALID_PARAMETER_VALUE.</td>
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

Retrieves a Sandbox by name.

```sql
SELECT
name,
display_name,
create_time,
metadata,
spec,
status,
update_time
FROM databricks_workspace.sandbox.sandboxes
WHERE sandbox_id = '{{ sandbox_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all Sandboxes.

```sql
SELECT
name,
display_name,
create_time,
metadata,
spec,
status,
update_time
FROM databricks_workspace.sandbox.sandboxes
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

Creates a new Sandbox.

```sql
INSERT INTO databricks_workspace.sandbox.sandboxes (
sandbox,
sandbox_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ sandbox }}' /* required */,
'{{ sandbox_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
display_name,
create_time,
metadata,
spec,
status,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sandboxes
  props:
    - name: sandbox_id
      value: "{{ sandbox_id }}"
      description: Required parameter for the sandboxes resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the sandboxes resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the sandboxes resource.
    - name: sandbox
      description: |
        The sandbox to create.
      value:
        create_time: "{{ create_time }}"
        display_name: "{{ display_name }}"
        metadata:
          custom_tags: "{{ custom_tags }}"
        name: "{{ name }}"
        spec:
          compute:
            inactivity_timeout: "{{ inactivity_timeout }}"
          environment:
            image_uri: "{{ image_uri }}"
        status:
          state: "{{ state }}"
        update_time: "{{ update_time }}"
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

Updates mutable fields on an existing Sandbox. Allowlisted update_mask paths today: display_name,

```sql
UPDATE databricks_workspace.sandbox.sandboxes
SET 
sandbox = '{{ sandbox }}'
WHERE 
sandbox_id = '{{ sandbox_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND sandbox = '{{ sandbox }}' --required
RETURNING
name,
display_name,
create_time,
metadata,
spec,
status,
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

Deletes a Sandbox.

```sql
DELETE FROM databricks_workspace.sandbox.sandboxes
WHERE sandbox_id = '{{ sandbox_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Starts a previously stopped Sandbox under the same sandbox name. Returns NOT_FOUND if there is no

```sql
EXEC databricks_workspace.sandbox.sandboxes.start 
@sandbox_id='{{ sandbox_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops a running Sandbox, preserving it so it can later be restarted with a Start request.

```sql
EXEC databricks_workspace.sandbox.sandboxes.stop 
@sandbox_id='{{ sandbox_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
