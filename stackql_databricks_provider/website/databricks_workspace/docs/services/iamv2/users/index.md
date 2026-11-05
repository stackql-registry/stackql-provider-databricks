---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.users" /></td></tr>
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
    "name": "account_id",
    "type": "string",
    "description": "The accountId parent of the user in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the user in the customer's IdP."
  },
  {
    "name": "user_id",
    "type": "string",
    "description": "Internal userId of the user in Databricks."
  },
  {
    "name": "full_name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "family_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "given_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "account_user_status",
    "type": "string",
    "description": "The activity status of a user in a Databricks account. (ACTIVE, INACTIVE)"
  },
  {
    "name": "username",
    "type": "string",
    "description": "Username/email of the user."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The accountId parent of the user in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the user in the customer's IdP."
  },
  {
    "name": "user_id",
    "type": "string",
    "description": "Internal userId of the user in Databricks."
  },
  {
    "name": "full_name",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "family_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "given_name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "account_user_status",
    "type": "string",
    "description": "The activity status of a user in a Databricks account. (ACTIVE, INACTIVE)"
  },
  {
    "name": "username",
    "type": "string",
    "description": "Username/email of the user."
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Fetches a user by its internal ID from the Databricks account that parents the calling workspace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the users in the Databricks account that parents the calling workspace, returning one page per</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-username"><code>username</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-account_user_status"><code>account_user_status</code></a></td>
    <td></td>
    <td>Creates a local user in the Databricks account that parents the calling workspace and returns the</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-username"><code>username</code></a>, <a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-account_user_status"><code>account_user_status</code></a></td>
    <td></td>
    <td>Updates an existing user in the Databricks account that parents the calling workspace and returns the</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a user by its internal ID from the Databricks account that parents the calling workspace.</td>
</tr>
<tr>
    <td><a href="#resolve"><CopyableCode code="resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it</td>
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
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Required. The list of fields to update.</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>Required. Internal ID of the user in Databricks.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Optional. Allows filtering users by username or external id.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of users to return. The service may return fewer than this value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum are clamped to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListUsers call. Provide this to retrieve the subsequent page.</td>
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

Fetches a user by its internal ID from the Databricks account that parents the calling workspace.

```sql
SELECT
account_id,
external_id,
user_id,
full_name,
account_user_status,
username
FROM databricks_workspace.iamv2.users
WHERE user_id = '{{ user_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the users in the Databricks account that parents the calling workspace, returning one page per

```sql
SELECT
account_id,
external_id,
user_id,
full_name,
account_user_status,
username
FROM databricks_workspace.iamv2.users
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND filter = '{{ filter }}'
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

Creates a local user in the Databricks account that parents the calling workspace and returns the

```sql
INSERT INTO databricks_workspace.iamv2.users (
username,
full_name,
account_user_status,
account_id,
external_id,
user_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ username }}' /* required */,
'{{ full_name }}' /* required */,
'{{ account_user_status }}' /* required */,
'{{ account_id }}',
'{{ external_id }}',
'{{ user_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
account_id,
external_id,
user_id,
full_name,
account_user_status,
username
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: users
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the users resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the users resource.
    - name: username
      value: "{{ username }}"
      description: |
        Username/email of the user.
    - name: full_name
      value:
        family_name: "{{ family_name }}"
        given_name: "{{ given_name }}"
    - name: account_user_status
      value: "{{ account_user_status }}"
      description: |
        The activity status of a user in a Databricks account.
    - name: account_id
      value: "{{ account_id }}"
      description: |
        The accountId parent of the user in Databricks.
    - name: external_id
      value: "{{ external_id }}"
      description: |
        ExternalId of the user in the customer's IdP.
    - name: user_id
      value: "{{ user_id }}"
      description: |
        Internal userId of the user in Databricks.
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

Updates an existing user in the Databricks account that parents the calling workspace and returns the

```sql
UPDATE databricks_workspace.iamv2.users
SET 
username = '{{ username }}',
full_name = '{{ full_name }}',
account_user_status = '{{ account_user_status }}',
account_id = '{{ account_id }}',
external_id = '{{ external_id }}',
user_id = '{{ user_id }}'
WHERE 
user_id = '{{ user_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND username = '{{ username }}' --required
AND full_name = '{{ full_name }}' --required
AND account_user_status = '{{ account_user_status }}' --required
RETURNING
account_id,
external_id,
user_id,
full_name,
account_user_status,
username;
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

Deletes a user by its internal ID from the Databricks account that parents the calling workspace.

```sql
DELETE FROM databricks_workspace.iamv2.users
WHERE user_id = '{{ user_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resolve"
    values={[
        { label: 'resolve', value: 'resolve' }
    ]}
>
<TabItem value="resolve">

Resolves a user with the given external ID from the customer's IdP. If the user does not exist, it

```sql
EXEC databricks_workspace.iamv2.users.resolve 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
</Tabs>
