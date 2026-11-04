---
title: workspace_assignment_details
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_assignment_details
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

Creates, updates, deletes, gets or lists a <code>workspace_assignment_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_assignment_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.workspace_assignment_details" /></td></tr>
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
    "description": "The account ID parent of the workspace where the principal is assigned"
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal is assigned."
  },
  {
    "name": "effective_entitlements",
    "type": "array",
    "description": "Every entitlement the principal holds in this workspace, whether granted directly or through group membership. Get responses populate this field. List responses leave it empty."
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements granted directly to the principal on this workspace. This is the only client-settable field. Create and update manage exactly this set, including entitlements the principal also holds through a group. List responses leave this field empty. Get a single principal to read its entitlements."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "account_id",
    "type": "string",
    "description": "The account ID parent of the workspace where the principal is assigned"
  },
  {
    "name": "principal_id",
    "type": "integer",
    "description": "The internal ID of the principal (user/sp/group) in Databricks."
  },
  {
    "name": "workspace_id",
    "type": "integer",
    "description": "The workspace ID where the principal is assigned."
  },
  {
    "name": "effective_entitlements",
    "type": "array",
    "description": "Every entitlement the principal holds in this workspace, whether granted directly or through group membership. Get responses populate this field. List responses leave it empty."
  },
  {
    "name": "entitlements",
    "type": "array",
    "description": "Entitlements granted directly to the principal on this workspace. This is the only client-settable field. Create and update manage exactly this set, including entitlements the principal also holds through a group. List responses leave this field empty. Get a single principal to read its entitlements."
  },
  {
    "name": "principal_type",
    "type": "string",
    "description": "The type of the principal (user/sp/group). (GROUP, SERVICE_PRINCIPAL, USER)"
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
    <td></td>
    <td>Returns the assignment details for a principal in the calling workspace.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists workspace assignment details for the calling workspace. The response omits the per-principal</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Creates a workspace assignment detail for a principal in the calling workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-principal_id"><code>principal_id</code></a></td>
    <td></td>
    <td>Updates the entitlements of a directly assigned principal in the calling workspace. Changes are</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-principal_id"><code>principal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a workspace assignment detail for a principal in the calling workspace, revoking all of its</td>
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
    <td>Required. ID of the principal in Databricks to delete workspace assignment for.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Required. The list of fields to update.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of workspace assignment details to return. The service may return fewer than this value. If not provided, defaults to 1000, which is also the maximum allowed. Requests for more than the maximum are clamped to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token from a previous list call. Provide this to retrieve the subsequent page.</td>
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

Returns the assignment details for a principal in the calling workspace.

```sql
SELECT
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
FROM databricks_workspace.iamv2.workspace_assignment_details
WHERE principal_id = '{{ principal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists workspace assignment details for the calling workspace. The response omits the per-principal

```sql
SELECT
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
FROM databricks_workspace.iamv2.workspace_assignment_details
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
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

Creates a workspace assignment detail for a principal in the calling workspace.

```sql
INSERT INTO databricks_workspace.iamv2.workspace_assignment_details (
principal_id,
account_id,
effective_entitlements,
entitlements,
principal_type,
workspace_id,
deployment_name,
workspace_domain
)
SELECT 
{{ principal_id }} /* required */,
'{{ account_id }}',
'{{ effective_entitlements }}',
'{{ entitlements }}',
'{{ principal_type }}',
{{ workspace_id }},
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_assignment_details
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the workspace_assignment_details resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the workspace_assignment_details resource.
    - name: principal_id
      value: {{ principal_id }}
      description: |
        The internal ID of the principal (user/sp/group) in Databricks.
    - name: account_id
      value: "{{ account_id }}"
      description: |
        The account ID parent of the workspace where the principal is assigned
    - name: effective_entitlements
      value:
        - "{{ effective_entitlements }}"
      description: |
        Every entitlement the principal holds in this workspace, whether granted directly or through group membership. Get responses populate this field. List responses leave it empty.
    - name: entitlements
      value:
        - "{{ entitlements }}"
      description: |
        Entitlements granted directly to the principal on this workspace. This is the only client-settable field. Create and update manage exactly this set, including entitlements the principal also holds through a group. List responses leave this field empty. Get a single principal to read its entitlements.
    - name: principal_type
      value: "{{ principal_type }}"
      description: |
        The type of the principal (user/sp/group).
    - name: workspace_id
      value: {{ workspace_id }}
      description: |
        The workspace ID where the principal is assigned.
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

Updates the entitlements of a directly assigned principal in the calling workspace. Changes are

```sql
UPDATE databricks_workspace.iamv2.workspace_assignment_details
SET 
principal_id = {{ principal_id }},
account_id = '{{ account_id }}',
effective_entitlements = '{{ effective_entitlements }}',
entitlements = '{{ entitlements }}',
principal_type = '{{ principal_type }}',
workspace_id = {{ workspace_id }}
WHERE 
principal_id = '{{ principal_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND principal_id = '{{ principal_id }}' --required
RETURNING
account_id,
principal_id,
workspace_id,
effective_entitlements,
entitlements,
principal_type;
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

Deletes a workspace assignment detail for a principal in the calling workspace, revoking all of its

```sql
DELETE FROM databricks_workspace.iamv2.workspace_assignment_details
WHERE principal_id = '{{ principal_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
