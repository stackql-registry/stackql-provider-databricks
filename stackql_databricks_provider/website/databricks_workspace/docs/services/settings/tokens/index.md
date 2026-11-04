---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - settings
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

Creates, updates, deletes, gets or lists a <code>tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tokens" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.tokens" /></td></tr>
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
    "name": "token_id",
    "type": "string",
    "description": "The ID of this token."
  },
  {
    "name": "autoscope_state",
    "type": "string",
    "description": ""
  },
  {
    "name": "backfill_scopes",
    "type": "array",
    "description": "Output only. Scopes inferred from offline backfill processing."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "Comment the token was created with, if applicable."
  },
  {
    "name": "creation_time",
    "type": "integer",
    "description": "Server time (in epoch milliseconds) when the token was created."
  },
  {
    "name": "expiry_time",
    "type": "integer",
    "description": "Server time (in epoch milliseconds) when the token will expire, or -1 if not applicable."
  },
  {
    "name": "inferred_scopes",
    "type": "array",
    "description": "Output only. Inferred API path scopes collected for this token when autoscope is enabled."
  },
  {
    "name": "scopes",
    "type": "array",
    "description": "Scope of the token was created with, if applicable."
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
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Lists all the valid tokens for a user-workspace pair.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates and returns a token for a user. If this call is made through token authentication, it creates</td>
</tr>
<tr>
    <td><a href="#tokens_update"><CopyableCode code="tokens_update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-token_id"><code>token_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-token"><code>token</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a></td>
    <td></td>
    <td>Updates the comment or scopes of a token.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-token_id"><code>token_id</code></a></td>
    <td></td>
    <td>Revokes an access token.</td>
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
<tr id="parameter-token_id">
    <td><CopyableCode code="token_id" /></td>
    <td><code>string</code></td>
    <td>The SHA-256 hash of the token to be updated.</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Lists all the valid tokens for a user-workspace pair.

```sql
SELECT
token_id,
autoscope_state,
backfill_scopes,
comment,
creation_time,
expiry_time,
inferred_scopes,
scopes
FROM databricks_workspace.settings.tokens
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
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

Creates and returns a token for a user. If this call is made through token authentication, it creates

```sql
INSERT INTO databricks_workspace.settings.tokens (
autoscope_enabled,
comment,
lifetime_seconds,
scopes,
deployment_name,
workspace_domain
)
SELECT 
{{ autoscope_enabled }},
'{{ comment }}',
{{ lifetime_seconds }},
'{{ scopes }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
token_info,
token_value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tokens
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the tokens resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the tokens resource.
    - name: autoscope_enabled
      value: {{ autoscope_enabled }}
      description: |
        Whether to enable autoscoping for this token. When true, the token will automatically collect inferred API path scopes as it is used.
    - name: comment
      value: "{{ comment }}"
      description: |
        Optional description to attach to the token.
    - name: lifetime_seconds
      value: {{ lifetime_seconds }}
      description: |
        The lifetime of the token, in seconds. If the lifetime is not specified, this token remains valid for 2 years.
    - name: scopes
      value:
        - "{{ scopes }}"
      description: |
        Optional scopes of the token.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="tokens_update"
    values={[
        { label: 'tokens_update', value: 'tokens_update' }
    ]}
>
<TabItem value="tokens_update">

Updates the comment or scopes of a token.

```sql
UPDATE databricks_workspace.settings.tokens
SET 
token = '{{ token }}',
update_mask = '{{ update_mask }}'
WHERE 
token_id = '{{ token_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND token = '{{ token }}' --required
AND update_mask = '{{ update_mask }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Revokes an access token.

```sql
EXEC databricks_workspace.settings.tokens.delete 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"token_id": "{{ token_id }}"
}'
;
```
</TabItem>
</Tabs>
