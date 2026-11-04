---
title: workspace_access_details
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_access_details
  - iamv2
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

Creates, updates, deletes, gets or lists a <code>workspace_access_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_access_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.workspace_access_details" /></td></tr>
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
    "name": "account_id",
    "type": "string",
    "description": "The account ID parent of the workspace where the principal has access."
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal has access."
  },
  {
    "name": "access_type",
    "type": "string",
    "description": "The type of access the principal has to the workspace. (DIRECT, INDIRECT)"
  },
  {
    "name": "permissions",
    "type": "array",
    "description": "The permissions granted to the principal in the workspace."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
  },
  {
    "name": "status",
    "type": "string",
    "description": "The activity status of the principal in the workspace. Not applicable for groups at the moment. (ACTIVE, INACTIVE)"
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
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-view"><code>view</code></a></td>
    <td>Returns the access details for a principal in the current workspace. Allows for checking access</td>
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
<tr id="parameter-principal_id">
    <td><CopyableCode code="principal_id" /></td>
    <td><code>integer</code></td>
    <td>Required. The internal ID of the principal (user/sp/group) for which the access details are being requested.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>Controls what fields are returned.</td>
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

Returns the access details for a principal in the current workspace. Allows for checking access

```sql
SELECT
account_id,
principal_id,
workspace_id,
access_type,
permissions,
principal_type,
status
FROM databricks_workspace.iamv2.workspace_access_details
WHERE principal_id = '{{ principal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND view = '{{ view }}'
;
```
</TabItem>
</Tabs>
