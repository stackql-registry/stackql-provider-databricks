---
title: ai_gateway_mcp_service_user_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_mcp_service_user_credentials
  - catalog
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_mcp_service_user_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_mcp_service_user_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_mcp_service_user_credentials" /></td></tr>
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
    "name": "options",
    "type": "object",
    "description": "Token-expiry info for the credential, returned as a flat map: ``access_token_expiration`` (always set) and ``refresh_token_expiration`` (set when the credential has a refresh token). Both values are timestamps."
  },
  {
    "name": "provisioning_info",
    "type": "object",
    "description": "Provisioning state of the credential. ``ACTIVE`` means the caller is logged in and the credential is usable; any other state means the login has not completed.",
    "children": [
      {
        "name": "state",
        "type": "string",
        "description": "The provisioning state of the resource. (ACTIVE, DEGRADED, DELETING, FAILED, PROVISIONING, UPDATING)"
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Returns the caller's per-user OAuth login state for an MCP service. Read ``provisioning_info.state``:</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-login"><code>login</code></a></td>
    <td></td>
    <td>Logs the caller in to an MCP service: creates their per-user OAuth credential, or re-authenticates it</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Revokes (deletes) the caller's per-user OAuth credential for an MCP service (logout).</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The `full_name` segment of the `name` resource name (`mcp-services/&#123;full_name&#125;`). Resource name of the MCP service. Format: ``mcp-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;mcp_service&#125;``.</td>
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

Returns the caller's per-user OAuth login state for an MCP service. Read ``provisioning_info.state``:

```sql
SELECT
options,
provisioning_info
FROM databricks_workspace.catalog.ai_gateway_mcp_service_user_credentials
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Logs the caller in to an MCP service: creates their per-user OAuth credential, or re-authenticates it

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_mcp_service_user_credentials (
login,
full_name,
deployment_name,
workspace_domain
)
SELECT 
'{{ login }}' /* required */,
'{{ full_name }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
options,
provisioning_info
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_mcp_service_user_credentials
  props:
    - name: full_name
      value: "{{ full_name }}"
      description: Required parameter for the ai_gateway_mcp_service_user_credentials resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_mcp_service_user_credentials resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the ai_gateway_mcp_service_user_credentials resource.
    - name: login
      description: |
        Login input for an MCP service user credential. Carries the OAuth exchange fields as a flat map.
      value:
        options: "{{ options }}"
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

Revokes (deletes) the caller's per-user OAuth credential for an MCP service (logout).

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_mcp_service_user_credentials
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
