---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - iamv2
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.groups" /></td></tr>
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
    "description": "The parent account ID for group in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the group in the customer's IdP."
  },
  {
    "name": "group_id",
    "type": "string",
    "description": "Internal group ID of the group in Databricks."
  },
  {
    "name": "group_name",
    "type": "string",
    "description": "Display name of the group."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The parent account ID for group in Databricks."
  },
  {
    "name": "external_id",
    "type": "string",
    "description": "ExternalId of the group in the customer's IdP."
  },
  {
    "name": "group_id",
    "type": "string",
    "description": "Internal group ID of the group in Databricks."
  },
  {
    "name": "group_name",
    "type": "string",
    "description": "Display name of the group."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Fetches a group from the Databricks account by its internal ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists the groups in the Databricks account, returning one page per call. Supports filtering by group</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Creates a local group in the Databricks account and returns the created group. A local group is one</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Updates an existing group in the Databricks account. Only the fields named in the update mask are</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Deletes a group from the Databricks account by its internal ID.</td>
</tr>
<tr>
    <td><a href="#resolve"><CopyableCode code="resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-external_id"><code>external_id</code></a></td>
    <td></td>
    <td>Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it</td>
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
<tr id="parameter-account_host">
    <td><CopyableCode code="account_host" /></td>
    <td><code>string</code></td>
    <td>The Databricks account console host. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws), or set explicitly with DATABRICKS_ACCOUNT_HOST (bare host, no scheme). (default: accounts.cloud.databricks.com, x-stackQL-envVar: DATABRICKS_ACCOUNT_HOST, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"accounts.cloud.databricks.com","azure":"accounts.azuredatabricks.net","gcp":"accounts.gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>Required. Internal ID of the group in Databricks.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Required. The list of fields to update.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>Optional. Allows filtering groups by group name or external id.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of groups to return. The service may return fewer than this value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum are clamped to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListGroups call. Provide this to retrieve the subsequent page.</td>
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

Fetches a group from the Databricks account by its internal ID.

```sql
SELECT
account_id,
external_id,
group_id,
group_name
FROM databricks_account.iamv2.groups
WHERE account_id = '{{ account_id }}' -- required
AND group_id = '{{ group_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the groups in the Databricks account, returning one page per call. Supports filtering by group

```sql
SELECT
account_id,
external_id,
group_id,
group_name
FROM databricks_account.iamv2.groups
WHERE account_id = '{{ account_id }}' -- required
AND account_host = '{{ account_host }}' -- required
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

Creates a local group in the Databricks account and returns the created group. A local group is one

```sql
INSERT INTO databricks_account.iamv2.groups (
account_id,
external_id,
group_id,
group_name,
account_id,
account_host
)
SELECT 
'{{ account_id }}',
'{{ external_id }}',
'{{ group_id }}',
'{{ group_name }}',
'{{ account_id }}',
'{{ account_host }}'
RETURNING
account_id,
external_id,
group_id,
group_name
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the groups resource.
    - name: account_host
      value: "{{ account_host }}"
      description: Required parameter for the groups resource.
    - name: account_id
      value: "{{ account_id }}"
      description: |
        The parent account ID for group in Databricks.
    - name: external_id
      value: "{{ external_id }}"
      description: |
        ExternalId of the group in the customer's IdP.
    - name: group_id
      value: "{{ group_id }}"
      description: |
        Internal group ID of the group in Databricks.
    - name: group_name
      value: "{{ group_name }}"
      description: |
        Display name of the group.
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

Updates an existing group in the Databricks account. Only the fields named in the update mask are

```sql
UPDATE databricks_account.iamv2.groups
SET 
account_id = '{{ account_id }}',
external_id = '{{ external_id }}',
group_id = '{{ group_id }}',
group_name = '{{ group_name }}'
WHERE 
account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND account_host = '{{ account_host }}' --required
RETURNING
account_id,
external_id,
group_id,
group_name;
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

Deletes a group from the Databricks account by its internal ID.

```sql
DELETE FROM databricks_account.iamv2.groups
WHERE account_id = '{{ account_id }}' --required
AND group_id = '{{ group_id }}' --required
AND account_host = '{{ account_host }}' --required
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

Resolves a group with the given external ID from the customer's IdP. If the group does not exist, it

```sql
EXEC databricks_account.iamv2.groups.resolve 
@account_id='{{ account_id }}' --required, 
@account_host='{{ account_host }}' --required 
@@json=
'{
"external_id": "{{ external_id }}"
}'
;
```
</TabItem>
</Tabs>
