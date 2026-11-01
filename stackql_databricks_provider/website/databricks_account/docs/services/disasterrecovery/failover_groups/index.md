---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
  - disasterrecovery
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

Creates, updates, deletes, gets or lists a <code>failover_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="failover_groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.disasterrecovery.failover_groups" /></td></tr>
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
    "description": "Fully qualified resource name in the format accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time at which this failover group was created."
  },
  {
    "name": "effective_primary_region",
    "type": "string",
    "description": "Current effective primary region. Replication flows FROM workspaces in this region. Changes after a successful failover."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Opaque version string for optimistic locking. Server-generated and returned in responses."
  },
  {
    "name": "has_replication_point_blocking_errors",
    "type": "boolean",
    "description": "True if errors currently block the replication point."
  },
  {
    "name": "initial_primary_region",
    "type": "string",
    "description": "Initial primary region. Used only in Create requests to set the starting primary region. Not returned in responses."
  },
  {
    "name": "initial_replication_progress",
    "type": "object",
    "description": "Initial replication progress of all in-scope assets. Set only when the FailoverGroup is in INITIAL_REPLICATION state.",
    "children": [
      {
        "name": "completed",
        "type": "integer",
        "description": "Percent complete, 0-100."
      }
    ]
  },
  {
    "name": "regions",
    "type": "array",
    "description": "List of all regions participating in this failover group."
  },
  {
    "name": "replication_point",
    "type": "string (date-time)",
    "description": "The latest point in time to which data has been replicated."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Aggregate state of the failover group. (ACTIVE, CREATING, CREATION_FAILED, DELETING, DELETION_FAILED, FAILING_OVER, FAILOVER_FAILED, INITIAL_REPLICATION)"
  },
  {
    "name": "unity_catalog_assets",
    "type": "object",
    "description": "Unity Catalog replication configuration.",
    "children": [
      {
        "name": "catalogs",
        "type": "array",
        "description": "UC catalogs to replicate.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "The name of the UC catalog to replicate."
          }
        ]
      },
      {
        "name": "data_replication_workspace_set",
        "type": "string",
        "description": "The workspace set whose workspaces will be used for data replication of all UC catalogs' underlying storage."
      },
      {
        "name": "location_mappings",
        "type": "array",
        "description": "Location mappings - storage URI per region for each location.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Resource name for this location."
          },
          {
            "name": "uri_by_region",
            "type": "array",
            "description": "URI for each region. Each entry maps a region name to a storage URI.",
            "children": [
              {
                "name": "region",
                "type": "string",
                "description": "The region name."
              },
              {
                "name": "uri",
                "type": "string",
                "description": "The storage URI for this region."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time at which this failover group was last modified."
  },
  {
    "name": "workspace_sets",
    "type": "array",
    "description": "Workspace sets, each containing workspaces that replicate to each other.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Resource name for this workspace set."
      },
      {
        "name": "workspace_ids",
        "type": "array",
        "description": "Workspace IDs in this set. The system derives and validates regions. All workspaces must be in the Mission Critical tier."
      },
      {
        "name": "replicate_workspace_assets",
        "type": "boolean",
        "description": "Whether to enable control plane DR (notebooks, jobs, clusters, etc.) for this set. Defaults to false."
      },
      {
        "name": "stable_url_names",
        "type": "array",
        "description": "Resource names of stable URLs associated with this workspace set. Format: accounts/&#123;account_id&#125;/stable-urls/&#123;stable_url_id&#125;. The referenced stable URLs must already exist (via CreateStableUrl)."
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
    "description": "Fully qualified resource name in the format accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time at which this failover group was created."
  },
  {
    "name": "effective_primary_region",
    "type": "string",
    "description": "Current effective primary region. Replication flows FROM workspaces in this region. Changes after a successful failover."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Opaque version string for optimistic locking. Server-generated and returned in responses."
  },
  {
    "name": "has_replication_point_blocking_errors",
    "type": "boolean",
    "description": "True if errors currently block the replication point."
  },
  {
    "name": "initial_primary_region",
    "type": "string",
    "description": "Initial primary region. Used only in Create requests to set the starting primary region. Not returned in responses."
  },
  {
    "name": "initial_replication_progress",
    "type": "object",
    "description": "Initial replication progress of all in-scope assets. Set only when the FailoverGroup is in INITIAL_REPLICATION state.",
    "children": [
      {
        "name": "completed",
        "type": "integer",
        "description": "Percent complete, 0-100."
      }
    ]
  },
  {
    "name": "regions",
    "type": "array",
    "description": "List of all regions participating in this failover group."
  },
  {
    "name": "replication_point",
    "type": "string (date-time)",
    "description": "The latest point in time to which data has been replicated."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Aggregate state of the failover group. (ACTIVE, CREATING, CREATION_FAILED, DELETING, DELETION_FAILED, FAILING_OVER, FAILOVER_FAILED, INITIAL_REPLICATION)"
  },
  {
    "name": "unity_catalog_assets",
    "type": "object",
    "description": "Unity Catalog replication configuration.",
    "children": [
      {
        "name": "catalogs",
        "type": "array",
        "description": "UC catalogs to replicate.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "The name of the UC catalog to replicate."
          }
        ]
      },
      {
        "name": "data_replication_workspace_set",
        "type": "string",
        "description": "The workspace set whose workspaces will be used for data replication of all UC catalogs' underlying storage."
      },
      {
        "name": "location_mappings",
        "type": "array",
        "description": "Location mappings - storage URI per region for each location.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Resource name for this location."
          },
          {
            "name": "uri_by_region",
            "type": "array",
            "description": "URI for each region. Each entry maps a region name to a storage URI.",
            "children": [
              {
                "name": "region",
                "type": "string",
                "description": "The region name."
              },
              {
                "name": "uri",
                "type": "string",
                "description": "The storage URI for this region."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time at which this failover group was last modified."
  },
  {
    "name": "workspace_sets",
    "type": "array",
    "description": "Workspace sets, each containing workspaces that replicate to each other.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "Resource name for this workspace set."
      },
      {
        "name": "workspace_ids",
        "type": "array",
        "description": "Workspace IDs in this set. The system derives and validates regions. All workspaces must be in the Mission Critical tier."
      },
      {
        "name": "replicate_workspace_assets",
        "type": "boolean",
        "description": "Whether to enable control plane DR (notebooks, jobs, clusters, etc.) for this set. Defaults to false."
      },
      {
        "name": "stable_url_names",
        "type": "array",
        "description": "Resource names of stable URLs associated with this workspace set. Format: accounts/&#123;account_id&#125;/stable-urls/&#123;stable_url_id&#125;. The referenced stable URLs must already exist (via CreateStableUrl)."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-failover_group_id"><code>failover_group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Get a failover group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List failover groups.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-failover_group_id"><code>failover_group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-failover_group"><code>failover_group</code></a></td>
    <td><a href="#parameter-validate_only"><code>validate_only</code></a></td>
    <td>Create a new failover group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-failover_group_id"><code>failover_group_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-failover_group"><code>failover_group</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Update a failover group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-failover_group_id"><code>failover_group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Delete a failover group.</td>
</tr>
<tr>
    <td><a href="#failover"><CopyableCode code="failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-failover_group_id"><code>failover_group_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-target_primary_region"><code>target_primary_region</code></a>, <a href="#parameter-failover_type"><code>failover_type</code></a></td>
    <td></td>
    <td>Initiate a failover to a new primary region.</td>
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
    <td>The `account_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;`). The fully qualified resource name of the failover group to failover. Format: accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;.</td>
</tr>
<tr id="parameter-failover_group_id">
    <td><CopyableCode code="failover_group_id" /></td>
    <td><code>string</code></td>
    <td>The `failover_group_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;`). The fully qualified resource name of the failover group to failover. Format: accounts/&#123;account_id&#125;/failover-groups/&#123;failover_group_id&#125;.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Comma-separated list of fields to update.</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Opaque version string for optimistic locking. If provided, must match the current etag. If omitted, the delete proceeds without an etag check.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of failover groups to return per page: - when set to a value greater than 0, the page length is the minimum of this value and a server configured value; - when set to 0 or unset, the page length is set to a server configured value (recommended); - when set to a value less than 0, an invalid parameter error is returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token received from a previous ListFailoverGroups call. Provide this to retrieve the subsequent page.</td>
</tr>
<tr id="parameter-validate_only">
    <td><CopyableCode code="validate_only" /></td>
    <td><code>boolean</code></td>
    <td>When true, validates the request without creating the failover group.</td>
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

Get a failover group.

```sql
SELECT
name,
create_time,
effective_primary_region,
etag,
has_replication_point_blocking_errors,
initial_primary_region,
initial_replication_progress,
regions,
replication_point,
state,
unity_catalog_assets,
update_time,
workspace_sets
FROM databricks_account.disasterrecovery.failover_groups
WHERE account_id = '{{ account_id }}' -- required
AND failover_group_id = '{{ failover_group_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="list">

List failover groups.

```sql
SELECT
name,
create_time,
effective_primary_region,
etag,
has_replication_point_blocking_errors,
initial_primary_region,
initial_replication_progress,
regions,
replication_point,
state,
unity_catalog_assets,
update_time,
workspace_sets
FROM databricks_account.disasterrecovery.failover_groups
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

Create a new failover group.

```sql
INSERT INTO databricks_account.disasterrecovery.failover_groups (
failover_group,
account_id,
failover_group_id,
account_host,
validate_only
)
SELECT 
'{{ failover_group }}' /* required */,
'{{ account_id }}',
'{{ failover_group_id }}',
'{{ account_host }}',
'{{ validate_only }}'
RETURNING
name,
create_time,
effective_primary_region,
etag,
has_replication_point_blocking_errors,
initial_primary_region,
initial_replication_progress,
regions,
replication_point,
state,
unity_catalog_assets,
update_time,
workspace_sets
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: failover_groups
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the failover_groups resource.
    - name: failover_group_id
      value: "{{ failover_group_id }}"
      description: Required parameter for the failover_groups resource.
    - name: account_host
      value: "{{ account_host }}"
      description: Required parameter for the failover_groups resource.
    - name: failover_group
      description: |
        The failover group to create.
      value:
        regions:
          - "{{ regions }}"
        workspace_sets:
          - name: "{{ name }}"
            workspace_ids: "{{ workspace_ids }}"
            replicate_workspace_assets: {{ replicate_workspace_assets }}
            stable_url_names: "{{ stable_url_names }}"
        initial_primary_region: "{{ initial_primary_region }}"
        create_time: "{{ create_time }}"
        effective_primary_region: "{{ effective_primary_region }}"
        etag: "{{ etag }}"
        has_replication_point_blocking_errors: {{ has_replication_point_blocking_errors }}
        initial_replication_progress:
          completed: {{ completed }}
        name: "{{ name }}"
        replication_point: "{{ replication_point }}"
        state: "{{ state }}"
        unity_catalog_assets:
          catalogs:
            - name: "{{ name }}"
          data_replication_workspace_set: "{{ data_replication_workspace_set }}"
          location_mappings:
            - name: "{{ name }}"
              uri_by_region: "{{ uri_by_region }}"
        update_time: "{{ update_time }}"
    - name: validate_only
      value: {{ validate_only }}
      description: When true, validates the request without creating the failover group.
      description: When true, validates the request without creating the failover group.
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

Update a failover group.

```sql
UPDATE databricks_account.disasterrecovery.failover_groups
SET 
failover_group = '{{ failover_group }}'
WHERE 
account_id = '{{ account_id }}' --required
AND failover_group_id = '{{ failover_group_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND account_host = '{{ account_host }}' --required
AND failover_group = '{{ failover_group }}' --required
AND etag = '{{ etag}}'
RETURNING
name,
create_time,
effective_primary_region,
etag,
has_replication_point_blocking_errors,
initial_primary_region,
initial_replication_progress,
regions,
replication_point,
state,
unity_catalog_assets,
update_time,
workspace_sets;
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

Delete a failover group.

```sql
DELETE FROM databricks_account.disasterrecovery.failover_groups
WHERE account_id = '{{ account_id }}' --required
AND failover_group_id = '{{ failover_group_id }}' --required
AND account_host = '{{ account_host }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="failover"
    values={[
        { label: 'failover', value: 'failover' }
    ]}
>
<TabItem value="failover">

Initiate a failover to a new primary region.

```sql
EXEC databricks_account.disasterrecovery.failover_groups.failover 
@account_id='{{ account_id }}' --required, 
@failover_group_id='{{ failover_group_id }}' --required, 
@account_host='{{ account_host }}' --required 
@@json=
'{
"target_primary_region": "{{ target_primary_region }}", 
"failover_type": "{{ failover_type }}", 
"etag": "{{ etag }}"
}'
;
```
</TabItem>
</Tabs>
