---
title: postgres_branches
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_branches
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres_branches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_branches" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_branches" /></td></tr>
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
    "description": "Output only. The full resource path of the branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "branch_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the branch was created."
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The project containing this branch (API resource hierarchy). Format: projects/&#123;project_id&#125; Note: This field indicates where the branch exists in the resource hierarchy. For point-in-time branching from another branch, see ``status.source_branch``."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the branch configuration.",
    "children": [
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": ""
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "When set to true, protects the branch from deletion and reset. Associated compute endpoints and the project cannot be deleted while the branch is protected."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "Explicitly disable expiration. When set to true, the branch will not expire. If set to false, the request is invalid; provide either ttl or expire_time instead. Mutually exclusive with ``expire_time`` and ``ttl``."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created (data lineage for point-in-time recovery). If not specified, defaults to the project's default branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "source_snapshot",
        "type": "string",
        "description": "The snapshot this branch was created from. When set, the branch's data comes from the snapshot rather than a source branch, so source_branch, source_branch_lsn, and source_branch_time must be empty. The snapshot must be AVAILABLE and belong to this branch's project. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Relative time-to-live duration. When set, the branch will expire at creation_time + ttl. Mutually exclusive with ``expire_time`` and ``no_expiry``."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Branch.",
    "children": [
      {
        "name": "branch_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The branch's state, indicating if it is initializing, ready for use, or archived. (ARCHIVED, DELETED, IMPORTING, INIT, READY, RESETTING)"
      },
      {
        "name": "default",
        "type": "boolean",
        "description": "Whether the branch is the project's default branch."
      },
      {
        "name": "delete_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the branch was deleted. Empty if the branch is not deleted."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute expiration time for the branch. Empty if expiration is disabled."
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the branch is protected."
      },
      {
        "name": "logical_size_bytes",
        "type": "integer",
        "description": "The logical size of the branch."
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The pending state of the branch, if a state transition is in progress. (ARCHIVED, DELETED, IMPORTING, INIT, READY, RESETTING)"
      },
      {
        "name": "purge_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the branch is scheduled to be purged. Empty if the branch is not deleted, otherwise set to a timestamp in the future."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "source_snapshot",
        "type": "string",
        "description": "The snapshot this branch was restored from. Set only for branches created by restoring a snapshot; unset for all other branches. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
      },
      {
        "name": "state_change_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the ``current_state`` began."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the branch."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the branch was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "branch_id",
    "type": "string",
    "description": ""
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the branch was created."
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The project containing this branch (API resource hierarchy). Format: projects/&#123;project_id&#125; Note: This field indicates where the branch exists in the resource hierarchy. For point-in-time branching from another branch, see ``status.source_branch``."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the branch configuration.",
    "children": [
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": ""
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "When set to true, protects the branch from deletion and reset. Associated compute endpoints and the project cannot be deleted while the branch is protected."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "Explicitly disable expiration. When set to true, the branch will not expire. If set to false, the request is invalid; provide either ttl or expire_time instead. Mutually exclusive with ``expire_time`` and ``ttl``."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created (data lineage for point-in-time recovery). If not specified, defaults to the project's default branch. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "source_snapshot",
        "type": "string",
        "description": "The snapshot this branch was created from. When set, the branch's data comes from the snapshot rather than a source branch, so source_branch, source_branch_lsn, and source_branch_time must be empty. The snapshot must be AVAILABLE and belong to this branch's project. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Relative time-to-live duration. When set, the branch will expire at creation_time + ttl. Mutually exclusive with ``expire_time`` and ``no_expiry``."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Branch.",
    "children": [
      {
        "name": "branch_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The branch's state, indicating if it is initializing, ready for use, or archived. (ARCHIVED, DELETED, IMPORTING, INIT, READY, RESETTING)"
      },
      {
        "name": "default",
        "type": "boolean",
        "description": "Whether the branch is the project's default branch."
      },
      {
        "name": "delete_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the branch was deleted. Empty if the branch is not deleted."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute expiration time for the branch. Empty if expiration is disabled."
      },
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the branch is protected."
      },
      {
        "name": "logical_size_bytes",
        "type": "integer",
        "description": "The logical size of the branch."
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The pending state of the branch, if a state transition is in progress. (ARCHIVED, DELETED, IMPORTING, INIT, READY, RESETTING)"
      },
      {
        "name": "purge_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the branch is scheduled to be purged. Empty if the branch is not deleted, otherwise set to a timestamp in the future."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The name of the source branch from which this branch was created. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "The Log Sequence Number (LSN) on the source branch from which this branch was created."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "The point in time on the source branch from which this branch was created."
      },
      {
        "name": "source_snapshot",
        "type": "string",
        "description": "The snapshot this branch was restored from. Set only for branches created by restoring a snapshot; unset for all other branches. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
      },
      {
        "name": "state_change_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the ``current_state`` began."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the branch."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the branch was last updated."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information about the specified database branch.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-show_deleted"><code>show_deleted</code></a></td>
    <td>Returns a paginated list of database branches in the project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-replace_existing"><code>replace_existing</code></a></td>
    <td>Creates a new database branch in the project.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Updates the specified database branch. You can set this branch as the project's default branch, or</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-purge"><code>purge</code></a></td>
    <td>Deletes the specified database branch.</td>
</tr>
<tr>
    <td><a href="#undelete"><CopyableCode code="undelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Undeletes the specified database branch.</td>
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
<tr id="parameter-branch_id">
    <td><CopyableCode code="branch_id" /></td>
    <td><code>string</code></td>
    <td>The `branch_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;`). The full resource path of the branch to undelete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;`). The full resource path of the branch to undelete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-purge">
    <td><CopyableCode code="purge" /></td>
    <td><code>boolean</code></td>
    <td>If true, permanently delete the branch; if false, soft delete.</td>
</tr>
<tr id="parameter-replace_existing">
    <td><CopyableCode code="replace_existing" /></td>
    <td><code>boolean</code></td>
    <td>If true, update the branch if it already exists instead of returning an error.</td>
</tr>
<tr id="parameter-show_deleted">
    <td><CopyableCode code="show_deleted" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include soft-deleted branches in the response. When true, deleted branches are included alongside active branches. Purged branches are never returned.</td>
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

Retrieves information about the specified database branch.

```sql
SELECT
name,
branch_id,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_branches
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of database branches in the project.

```sql
SELECT
name,
branch_id,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_branches
WHERE project_id = '{{ project_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND show_deleted = '{{ show_deleted }}'
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

Creates a new database branch in the project.

```sql
INSERT INTO databricks_workspace.postgres.postgres_branches (
branch_id,
create_time,
name,
parent,
spec,
status,
uid,
update_time,
project_id,
branch_id,
deployment_name,
workspace_domain,
replace_existing
)
SELECT 
'{{ branch_id }}',
'{{ create_time }}',
'{{ name }}',
'{{ parent }}',
'{{ spec }}',
'{{ status }}',
'{{ uid }}',
'{{ update_time }}',
'{{ project_id }}',
'{{ branch_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ replace_existing }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_branches
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_branches resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the postgres_branches resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_branches resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_branches resource.
    - name: branch_id
      value: "{{ branch_id }}"
    - name: create_time
      value: "{{ create_time }}"
      description: |
        A timestamp indicating when the branch was created.
    - name: name
      value: "{{ name }}"
      description: |
        Output only. The full resource path of the branch. Format: projects/{project_id}/branches/{branch_id}
    - name: parent
      value: "{{ parent }}"
      description: |
        The project containing this branch (API resource hierarchy). Format: projects/{project_id} Note: This field indicates where the branch exists in the resource hierarchy. For point-in-time branching from another branch, see \`\`status.source_branch\`\`.
    - name: spec
      description: |
        The spec contains the branch configuration.
      value:
        expire_time: "{{ expire_time }}"
        is_protected: {{ is_protected }}
        no_expiry: {{ no_expiry }}
        source_branch: "{{ source_branch }}"
        source_branch_lsn: "{{ source_branch_lsn }}"
        source_branch_time: "{{ source_branch_time }}"
        source_snapshot: "{{ source_snapshot }}"
        ttl: "{{ ttl }}"
    - name: status
      description: |
        The current status of a Branch.
      value:
        branch_id: "{{ branch_id }}"
        current_state: "{{ current_state }}"
        default: {{ default }}
        delete_time: "{{ delete_time }}"
        expire_time: "{{ expire_time }}"
        is_protected: {{ is_protected }}
        logical_size_bytes: {{ logical_size_bytes }}
        pending_state: "{{ pending_state }}"
        purge_time: "{{ purge_time }}"
        source_branch: "{{ source_branch }}"
        source_branch_lsn: "{{ source_branch_lsn }}"
        source_branch_time: "{{ source_branch_time }}"
        source_snapshot: "{{ source_snapshot }}"
        state_change_time: "{{ state_change_time }}"
    - name: uid
      value: "{{ uid }}"
      description: |
        System-generated unique ID for the branch.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        A timestamp indicating when the branch was last updated.
    - name: replace_existing
      value: {{ replace_existing }}
      description: If true, update the branch if it already exists instead of returning an error.
      description: If true, update the branch if it already exists instead of returning an error.
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

Updates the specified database branch. You can set this branch as the project's default branch, or

```sql
UPDATE databricks_workspace.postgres.postgres_branches
SET 
branch_id = '{{ branch_id }}',
create_time = '{{ create_time }}',
name = '{{ name }}',
parent = '{{ parent }}',
spec = '{{ spec }}',
status = '{{ status }}',
uid = '{{ uid }}',
update_time = '{{ update_time }}'
WHERE 
project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required;
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

Deletes the specified database branch.

```sql
DELETE FROM databricks_workspace.postgres.postgres_branches
WHERE project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND purge = '{{ purge }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undelete"
    values={[
        { label: 'undelete', value: 'undelete' }
    ]}
>
<TabItem value="undelete">

Undeletes the specified database branch.

```sql
EXEC databricks_workspace.postgres.postgres_branches.undelete 
@project_id='{{ project_id }}' --required, 
@branch_id='{{ branch_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
