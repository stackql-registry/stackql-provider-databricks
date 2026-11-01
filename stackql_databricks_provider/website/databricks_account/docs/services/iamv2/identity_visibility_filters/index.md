---
title: identity_visibility_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_visibility_filters
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

Creates, updates, deletes, gets or lists an <code>identity_visibility_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identity_visibility_filters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iamv2.identity_visibility_filters" /></td></tr>
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
    "description": "The resource name of the identity-visibility filter. Format: accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;"
  },
  {
    "name": "exact",
    "type": "object",
    "description": "Exact match on the group's external ID from the identity provider.",
    "children": [
      {
        "name": "external_id",
        "type": "string",
        "description": "The identity provider's external ID for the group to match. This is not the Databricks group ID. The value must be non-empty and is matched exactly, including case."
      }
    ]
  },
  {
    "name": "prefix",
    "type": "object",
    "description": "Case-sensitive starts-with match on the group's display name.",
    "children": [
      {
        "name": "display_name_prefix",
        "type": "string",
        "description": "The display-name prefix to match. Must contain at least one non-whitespace character. Leading and trailing whitespace are preserved, and matching is case-sensitive."
      }
    ]
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of principal this rule applies to. Set to ``GROUP`` when creating a filter. Other principal types are not supported for creation. (GROUP, SERVICE_PRINCIPAL, USER)"
  },
  {
    "name": "regex",
    "type": "object",
    "description": "Full, case-sensitive RE2 match on the identity's display name.",
    "children": [
      {
        "name": "display_name_regex",
        "type": "string",
        "description": "The RE2 regular expression matched against the complete display name."
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
    "description": "The resource name of the identity-visibility filter. Format: accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;"
  },
  {
    "name": "exact",
    "type": "object",
    "description": "Exact match on the group's external ID from the identity provider.",
    "children": [
      {
        "name": "external_id",
        "type": "string",
        "description": "The identity provider's external ID for the group to match. This is not the Databricks group ID. The value must be non-empty and is matched exactly, including case."
      }
    ]
  },
  {
    "name": "prefix",
    "type": "object",
    "description": "Case-sensitive starts-with match on the group's display name.",
    "children": [
      {
        "name": "display_name_prefix",
        "type": "string",
        "description": "The display-name prefix to match. Must contain at least one non-whitespace character. Leading and trailing whitespace are preserved, and matching is case-sensitive."
      }
    ]
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of principal this rule applies to. Set to ``GROUP`` when creating a filter. Other principal types are not supported for creation. (GROUP, SERVICE_PRINCIPAL, USER)"
  },
  {
    "name": "regex",
    "type": "object",
    "description": "Full, case-sensitive RE2 match on the identity's display name.",
    "children": [
      {
        "name": "display_name_regex",
        "type": "string",
        "description": "The RE2 regular expression matched against the complete display name."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identity_visibility_filter_id"><code>identity_visibility_filter_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Gets a group visibility filter by its resource name. Requires account admin privileges. Returns the</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists group visibility filters in the account, returning one page per call. Requires account admin</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-identity_visibility_filter"><code>identity_visibility_filter</code></a></td>
    <td><a href="#parameter-identity_visibility_filter_id"><code>identity_visibility_filter_id</code></a></td>
    <td>Creates a group visibility filter in the account. Requires account admin privileges. Set</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-identity_visibility_filter_id"><code>identity_visibility_filter_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Deletes a group visibility filter by its resource name. Requires account admin privileges. Deleting a</td>
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
    <td>The `account_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;`). Required. The resource name of the filter. Format: accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;</td>
</tr>
<tr id="parameter-identity_visibility_filter_id">
    <td><CopyableCode code="identity_visibility_filter_id" /></td>
    <td><code>string</code></td>
    <td>The `identity_visibility_filter_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;`). Required. The resource name of the filter. Format: accounts/&#123;account_id&#125;/identity-visibility-filters/&#123;identity_visibility_filter_id&#125;</td>
</tr>
<tr id="parameter-identity_visibility_filter_id">
    <td><CopyableCode code="identity_visibility_filter_id" /></td>
    <td><code>string</code></td>
    <td>Optional. The ID to use for the filter, which becomes the final component of its resource name. If not specified or empty, the server generates one. Must not contain ``/``.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of filters to return. The service may return fewer than this value. If omitted or non-positive, defaults to 100. Values above 1000 are reduced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ListIdentityVisibilityFilters call. Provide this to retrieve the subsequent page.</td>
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

Gets a group visibility filter by its resource name. Requires account admin privileges. Returns the

```sql
SELECT
name,
exact,
prefix,
principal_type,
regex
FROM databricks_account.iamv2.identity_visibility_filters
WHERE account_id = '{{ account_id }}' -- required
AND identity_visibility_filter_id = '{{ identity_visibility_filter_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists group visibility filters in the account, returning one page per call. Requires account admin

```sql
SELECT
name,
exact,
prefix,
principal_type,
regex
FROM databricks_account.iamv2.identity_visibility_filters
WHERE account_id = '{{ account_id }}' -- required
AND account_host = '{{ account_host }}' -- required
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

Creates a group visibility filter in the account. Requires account admin privileges. Set

```sql
INSERT INTO databricks_account.iamv2.identity_visibility_filters (
identity_visibility_filter,
account_id,
account_host,
identity_visibility_filter_id
)
SELECT 
'{{ identity_visibility_filter }}' /* required */,
'{{ account_id }}',
'{{ account_host }}',
'{{ identity_visibility_filter_id }}'
RETURNING
name,
exact,
prefix,
principal_type,
regex
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: identity_visibility_filters
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the identity_visibility_filters resource.
    - name: account_host
      value: "{{ account_host }}"
      description: Required parameter for the identity_visibility_filters resource.
    - name: identity_visibility_filter
      description: |
        Required. The filter to create. Set \`\`principal_type\`\` to \`\`GROUP\`\` and specify exactly one of \`\`exact\`\`, \`\`prefix\`\`, or \`\`regex\`\`. The server assigns the resource name; any supplied \`\`name\`\` is ignored.
      value:
        principal_type: "{{ principal_type }}"
        exact:
          external_id: "{{ external_id }}"
        name: "{{ name }}"
        prefix:
          display_name_prefix: "{{ display_name_prefix }}"
        regex:
          display_name_regex: "{{ display_name_regex }}"
    - name: identity_visibility_filter_id
      value: "{{ identity_visibility_filter_id }}"
      description: Optional. The ID to use for the filter, which becomes the final component of its resource name. If not specified or empty, the server generates one. Must not contain \`\`/\`\`.
      description: Optional. The ID to use for the filter, which becomes the final component of its resource name. If not specified or empty, the server generates one. Must not contain \`\`/\`\`.
`}</CodeBlock>

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

Deletes a group visibility filter by its resource name. Requires account admin privileges. Deleting a

```sql
DELETE FROM databricks_account.iamv2.identity_visibility_filters
WHERE account_id = '{{ account_id }}' --required
AND identity_visibility_filter_id = '{{ identity_visibility_filter_id }}' --required
AND account_host = '{{ account_host }}' --required
;
```
</TabItem>
</Tabs>
