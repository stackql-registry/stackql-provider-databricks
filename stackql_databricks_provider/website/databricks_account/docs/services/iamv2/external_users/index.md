---
title: external_users
hide_title: false
hide_table_of_contents: false
keywords:
  - external_users
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

Creates, updates, deletes, gets or lists an <code>external_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="external_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.external_users" /></td></tr>
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
    "name": "name",
    "type": "string",
    "description": "The resource name of the external user. The format depends on the API that returned it: - Account-scoped: accounts/&#123;account_id&#125;/external-users/&#123;external_user_id&#125; - Workspace-scoped: external-users/&#123;external_user_id&#125;"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": "The parent account ID, from Databricks."
  },
  {
    "name": "external_user_id",
    "type": "string",
    "description": "The external ID of the user in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal userId of the user in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the user from the customer's IdP."
  },
  {
    "name": "full_name",
    "type": "object",
    "description": "The full name of the user, from the customer's IdP.",
    "children": [
      {
        "name": "family_name",
        "type": "string",
        "description": "The family (last) name of the user, from the customer's IdP."
      },
      {
        "name": "given_name",
        "type": "string",
        "description": "The given (first) name of the user, from the customer's IdP."
      }
    ]
  },
  {
    "name": "account_user_status",
    "type": "string",
    "description": "The activity status of the user in the Databricks account. (ACTIVE, INACTIVE)"
  },
  {
    "name": "username",
    "type": "string",
    "description": "Username/email of the user, from Databricks."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-external_user_id"><code>external_user_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Retrieves an external user with the given external ID from the customer's IdP. If the user does not</td>
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
    <td>The `account_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/external-users/&#123;external_user_id&#125;`). Required. The resource name of the external user. Format: accounts/&#123;account_id&#125;/external-users/&#123;external_user_id&#125;</td>
</tr>
<tr id="parameter-external_user_id">
    <td><CopyableCode code="external_user_id" /></td>
    <td><code>string</code></td>
    <td>The `external_user_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/external-users/&#123;external_user_id&#125;`). Required. The resource name of the external user. Format: accounts/&#123;account_id&#125;/external-users/&#123;external_user_id&#125;</td>
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

Retrieves an external user with the given external ID from the customer's IdP. If the user does not

```sql
SELECT
name,
account_id,
external_user_id,
internal_id,
display_name,
full_name,
account_user_status,
username
FROM databricks_account.iamv2.external_users
WHERE account_id = '{{ account_id }}' -- required
AND external_user_id = '{{ external_user_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
</Tabs>
