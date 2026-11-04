---
title: sandbox_directory_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_directory_entries
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

Creates, updates, deletes, gets or lists a <code>sandbox_directory_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sandbox_directory_entries" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sandbox.sandbox_directory_entries" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": ""
  },
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
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists a directory's immediate children in UTF-8 name order. Later pages may reflect concurrent</td>
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
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Absolute UTF-8 path of the directory.</td>
</tr>
<tr id="parameter-sandbox_id">
    <td><CopyableCode code="sandbox_id" /></td>
    <td><code>string</code></td>
    <td>The `sandbox_id` segment of the `parent` resource name (`sandboxes/&#123;sandbox_id&#125;`).</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Zero uses the default of 1000; values above 1000 are clamped to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>The token from a prior response. Keep parent and path unchanged between pages.</td>
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

Lists a directory's immediate children in UTF-8 name order. Later pages may reflect concurrent

```sql
SELECT
name,
file_type,
group,
mode,
modify_time,
owner,
path,
permissions,
size,
symlink_target
FROM databricks_workspace.sandbox.sandbox_directory_entries
WHERE sandbox_id = '{{ sandbox_id }}' -- required
AND path = '{{ path }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>
