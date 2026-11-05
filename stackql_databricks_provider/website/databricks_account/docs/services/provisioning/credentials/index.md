---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="credentials_get"
    values={[
        { label: 'credentials_get', value: 'credentials_get' },
        { label: 'credentials_list', value: 'credentials_list' }
    ]}
>
<TabItem value="credentials_get">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "Databricks credential configuration ID."
  },
  {
    "name": "credentials_name",
    "type": "string",
    "description": "The human-readable name of the credential configuration object."
  },
  {
    "name": "aws_credentials",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "sts_role",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "role_arn",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the credential was created."
  }
]} />
</TabItem>
<TabItem value="credentials_list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "credentials_id",
    "type": "string",
    "description": "Databricks credential configuration ID."
  },
  {
    "name": "credentials_name",
    "type": "string",
    "description": "The human-readable name of the credential configuration object."
  },
  {
    "name": "aws_credentials",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "sts_role",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "role_arn",
            "type": "string",
            "description": ""
          }
        ]
      }
    ]
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Time in epoch milliseconds when the credential was created."
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
    <td><a href="#credentials_get"><CopyableCode code="credentials_get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-credentials_id"><code>credentials_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Gets a Databricks credential configuration object for an account, both specified by ID.</td>
</tr>
<tr>
    <td><a href="#credentials_list"><CopyableCode code="credentials_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>List Databricks credential configuration objects for an account, specified by ID.</td>
</tr>
<tr>
    <td><a href="#credentials_create"><CopyableCode code="credentials_create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-credentials_name"><code>credentials_name</code></a>, <a href="#parameter-aws_credentials"><code>aws_credentials</code></a></td>
    <td></td>
    <td>Creates a Databricks credential configuration that represents cloud cross-account credentials for a</td>
</tr>
<tr>
    <td><a href="#credentials_delete"><CopyableCode code="credentials_delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-credentials_id"><code>credentials_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot</td>
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
<tr id="parameter-credentials_id">
    <td><CopyableCode code="credentials_id" /></td>
    <td><code>string</code></td>
    <td>Databricks Account API credential configuration ID</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="credentials_get"
    values={[
        { label: 'credentials_get', value: 'credentials_get' },
        { label: 'credentials_list', value: 'credentials_list' }
    ]}
>
<TabItem value="credentials_get">

Gets a Databricks credential configuration object for an account, both specified by ID.

```sql
SELECT
account_id,
credentials_id,
credentials_name,
aws_credentials,
creation_time
FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}' -- required
AND credentials_id = '{{ credentials_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="credentials_list">

List Databricks credential configuration objects for an account, specified by ID.

```sql
SELECT
account_id,
credentials_id,
credentials_name,
aws_credentials,
creation_time
FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="credentials_create"
    values={[
        { label: 'credentials_create', value: 'credentials_create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="credentials_create">

Creates a Databricks credential configuration that represents cloud cross-account credentials for a

```sql
INSERT INTO databricks_account.provisioning.credentials (
credentials_name,
aws_credentials,
account_id,
account_host
)
SELECT 
'{{ credentials_name }}' /* required */,
'{{ aws_credentials }}' /* required */,
'{{ account_id }}',
'{{ account_host }}'
RETURNING
account_id,
credentials_id,
credentials_name,
aws_credentials,
creation_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: credentials
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the credentials resource.
    - name: account_host
      value: "{{ account_host }}"
      description: Required parameter for the credentials resource.
    - name: credentials_name
      value: "{{ credentials_name }}"
      description: |
        The human-readable name of the credential configuration object.
    - name: aws_credentials
      value:
        sts_role:
          role_arn: "{{ role_arn }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="credentials_delete"
    values={[
        { label: 'credentials_delete', value: 'credentials_delete' }
    ]}
>
<TabItem value="credentials_delete">

Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot

```sql
DELETE FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}' --required
AND credentials_id = '{{ credentials_id }}' --required
AND account_host = '{{ account_host }}' --required
;
```
</TabItem>
</Tabs>
