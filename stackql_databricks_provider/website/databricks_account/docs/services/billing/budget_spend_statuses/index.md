---
title: budget_spend_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - budget_spend_statuses
  - billing
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

Creates, updates, deletes, gets or lists a <code>budget_spend_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="budget_spend_statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.billing.budget_spend_statuses" /></td></tr>
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
    "description": "The resource name of this budget spend status, of the form ``accounts/&#123;account_id&#125;/budget-spend-statuses/&#123;budget_id&#125;``."
  },
  {
    "name": "alert_spend_statuses",
    "type": "array",
    "description": "The calling user's spend against each blocking threshold on this budget, one entry per scope type and time period. A blocking threshold is a threshold that, once reached, blocks further requests through Unity Gateway.",
    "children": [
      {
        "name": "percent_consumed",
        "type": "string",
        "description": "Percentage of the threshold consumed, as a decimal string rounded down to one decimal place (for example, \"68.4\" means 68.4%). May exceed 100 when spend is over the threshold. Returns \"0.0\" if there's no spend, and is omitted if the threshold is $0. For shared thresholds, this is the only value returned; the absolute ``spend`` and ``threshold`` dollar amounts are withheld."
      },
      {
        "name": "scope_type",
        "type": "string",
        "description": "Whether the threshold is evaluated per individual user (``ALERT_CONFIGURATION_SCOPE_TYPE_PER_USER``) or on the shared spend across all users (``ALERT_CONFIGURATION_SCOPE_TYPE_SHARED``). (ALERT_CONFIGURATION_SCOPE_TYPE_PER_USER, ALERT_CONFIGURATION_SCOPE_TYPE_SHARED)"
      },
      {
        "name": "spend",
        "type": "string",
        "description": "The calling user's live spend against this threshold, in USD at list price. Returns \"0\" if the caller has no usage. Omitted for shared thresholds, where only ``percent_consumed`` is returned."
      },
      {
        "name": "threshold",
        "type": "string",
        "description": "The calling user's effective threshold, in USD at list price. The effective threshold is the actual threshold amount that applies to the user, after adjusting for any user or group overrides. Omitted for shared thresholds, where only ``percent_consumed`` is returned."
      },
      {
        "name": "time_period",
        "type": "string",
        "description": "The time window the threshold applies to, for example ``MONTH``. (MONTH)"
      }
    ]
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of this budget spend status, of the form ``accounts/&#123;account_id&#125;/budget-spend-statuses/&#123;budget_id&#125;``."
  },
  {
    "name": "alert_spend_statuses",
    "type": "array",
    "description": "The calling user's spend against each blocking threshold on this budget, one entry per scope type and time period. A blocking threshold is a threshold that, once reached, blocks further requests through Unity Gateway.",
    "children": [
      {
        "name": "percent_consumed",
        "type": "string",
        "description": "Percentage of the threshold consumed, as a decimal string rounded down to one decimal place (for example, \"68.4\" means 68.4%). May exceed 100 when spend is over the threshold. Returns \"0.0\" if there's no spend, and is omitted if the threshold is $0. For shared thresholds, this is the only value returned; the absolute ``spend`` and ``threshold`` dollar amounts are withheld."
      },
      {
        "name": "scope_type",
        "type": "string",
        "description": "Whether the threshold is evaluated per individual user (``ALERT_CONFIGURATION_SCOPE_TYPE_PER_USER``) or on the shared spend across all users (``ALERT_CONFIGURATION_SCOPE_TYPE_SHARED``). (ALERT_CONFIGURATION_SCOPE_TYPE_PER_USER, ALERT_CONFIGURATION_SCOPE_TYPE_SHARED)"
      },
      {
        "name": "spend",
        "type": "string",
        "description": "The calling user's live spend against this threshold, in USD at list price. Returns \"0\" if the caller has no usage. Omitted for shared thresholds, where only ``percent_consumed`` is returned."
      },
      {
        "name": "threshold",
        "type": "string",
        "description": "The calling user's effective threshold, in USD at list price. The effective threshold is the actual threshold amount that applies to the user, after adjusting for any user or group overrides. Omitted for shared thresholds, where only ``percent_consumed`` is returned."
      },
      {
        "name": "time_period",
        "type": "string",
        "description": "The time window the threshold applies to, for example ``MONTH``. (MONTH)"
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-budget_id"><code>budget_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Get the calling user's live spend against the blocking thresholds of a single Unity Gateway budget.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List the calling user's live spend against the blocking thresholds across the account's Unity Gateway</td>
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
    <td>The `account_id` segment of the `parent` resource name (`accounts/&#123;account_id&#125;`). The parent account whose budget spend statuses to list, of the form ``accounts/&#123;account_id&#125;``.</td>
</tr>
<tr id="parameter-budget_id">
    <td><CopyableCode code="budget_id" /></td>
    <td><code>string</code></td>
    <td>The `budget_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/budget-spend-statuses/&#123;budget_id&#125;`). The resource name of the budget spend status to read, of the form ``accounts/&#123;account_id&#125;/budget-spend-statuses/&#123;budget_id&#125;``. A ``budget_id`` that isn't a valid UUID fails with INVALID_PARAMETER_VALUE.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>A filter expression that narrows the returned budgets by workspace. Only ``workspace_id`` is supported, in lower case with numeric workspace IDs, for example ``workspace_id = 123`` or ``workspace_id IN (123, 456)``. Matches budgets that apply to any of the listed workspaces, including budgets that apply to all workspaces. Any other expression, such as an empty ``IN ()`` list, fails with INVALID_PARAMETER_VALUE. If empty, returns every budget in the account that has a blocking threshold.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of spend statuses to return per page. If unspecified or 0, at most 100 are returned. The maximum value is 100; values above 100 are coerced to 100. Negative values fail with INVALID_PARAMETER_VALUE. The server may return fewer results than requested, including zero, even when more pages remain; page until ``next_page_token`` is absent.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token from a previous ``ListBudgetSpendStatuses`` response, used to fetch the next page. Requests the first page if absent. All other request parameters except ``page_size`` must match the request that returned the token; otherwise the request fails with INVALID_PARAMETER_VALUE.</td>
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

Get the calling user's live spend against the blocking thresholds of a single Unity Gateway budget.

```sql
SELECT
name,
alert_spend_statuses
FROM databricks_account.billing.budget_spend_statuses
WHERE account_id = '{{ account_id }}' -- required
AND budget_id = '{{ budget_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the calling user's live spend against the blocking thresholds across the account's Unity Gateway

```sql
SELECT
name,
alert_spend_statuses
FROM databricks_account.billing.budget_spend_statuses
WHERE account_id = '{{ account_id }}' -- required
AND account_host = '{{ account_host }}' -- required
AND filter = '{{ filter }}'
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
;
```
</TabItem>
</Tabs>
