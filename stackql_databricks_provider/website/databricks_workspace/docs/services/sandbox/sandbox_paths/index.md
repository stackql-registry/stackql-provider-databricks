---
title: sandbox_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_paths
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

Creates, updates, deletes, gets or lists a <code>sandbox_paths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sandbox_paths" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sandbox.sandbox_paths" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "file",
    "type": "object",
    "description": "Metadata for a sandbox filesystem entry, describing a final symlink itself.",
    "children": [
      {
        "name": "file_type",
        "type": "string",
        "description": "Type of a sandbox filesystem entry without following its final symlink. (SANDBOX_FILE_TYPE_DIRECTORY, SANDBOX_FILE_TYPE_FILE, SANDBOX_FILE_TYPE_OTHER, SANDBOX_FILE_TYPE_SYMLINK)"
      },
      {
        "name": "group",
        "type": "string",
        "description": ""
      },
      {
        "name": "mode",
        "type": "integer",
        "description": ""
      },
      {
        "name": "modify_time",
        "type": "string (date-time)",
        "description": "Nanosecond precision is preserved on the wire."
      },
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "owner",
        "type": "string",
        "description": ""
      },
      {
        "name": "path",
        "type": "string",
        "description": ""
      },
      {
        "name": "permissions",
        "type": "string",
        "description": ""
      },
      {
        "name": "size",
        "type": "integer",
        "description": ""
      },
      {
        "name": "symlink_target",
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
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Returns metadata for a path without following its final symlink.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a file, symlink, or empty directory, with an option for recursive deletion. Succeeds if the</td>
</tr>
<tr>
    <td><a href="#rename"><CopyableCode code="rename" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-source"><code>source</code></a>, <a href="#parameter-destination"><code>destination</code></a></td>
    <td></td>
    <td>Renames a path within a sandbox. The destination must be absent and on the same filesystem.</td>
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
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Absolute UTF-8 path of the entry to inspect.</td>
</tr>
<tr id="parameter-sandbox_id">
    <td><CopyableCode code="sandbox_id" /></td>
    <td><code>string</code></td>
    <td>The `sandbox_id` segment of the `parent` resource name (`sandboxes/&#123;sandbox_id&#125;`). Sandbox resource name, for example ``sandboxes/my-sandbox``.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Returns metadata for a path without following its final symlink.

```sql
SELECT
file
FROM databricks_workspace.sandbox.sandbox_paths
WHERE sandbox_id = '{{ sandbox_id }}' -- required
AND path = '{{ path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
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

Deletes a file, symlink, or empty directory, with an option for recursive deletion. Succeeds if the

```sql
DELETE FROM databricks_workspace.sandbox.sandbox_paths
WHERE sandbox_id = '{{ sandbox_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename"
    values={[
        { label: 'rename', value: 'rename' }
    ]}
>
<TabItem value="rename">

Renames a path within a sandbox. The destination must be absent and on the same filesystem.

```sql
EXEC databricks_workspace.sandbox.sandbox_paths.rename 
@sandbox_id='{{ sandbox_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"source": "{{ source }}", 
"destination": "{{ destination }}"
}'
;
```
</TabItem>
</Tabs>
