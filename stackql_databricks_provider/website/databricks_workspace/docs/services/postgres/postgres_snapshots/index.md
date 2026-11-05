---
title: postgres_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_snapshots
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

Creates, updates, deletes, gets or lists a <code>postgres_snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_snapshots" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_snapshots" /></td></tr>
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
    "description": "The resource name of the snapshot. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
  },
  {
    "name": "snapshot_id",
    "type": "string",
    "description": "The user-chosen ID; the final segment of ``name``."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the snapshot was created."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Client-provided configuration of the snapshot.",
    "children": [
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch to snapshot. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted. Mutually exclusive with ``ttl`` and ``no_expiry``."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "If true, the snapshot never expires. Mutually exclusive with ``ttl`` and ``expire_time``."
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "LSN to snapshot from, e.g. ``16/B374D848``. Mutually exclusive with ``source_branch_time``."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "Timestamp to snapshot from. Mutually exclusive with ``source_branch_lsn``."
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Time-to-live. The snapshot expires this long after it is created. Mutually exclusive with ``expire_time`` and ``no_expiry``. Reads report the resolved absolute ``expire_time`` instead."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Server-observed state of the snapshot.",
    "children": [
      {
        "name": "diff_size_bytes",
        "type": "integer",
        "description": "Incremental storage size in bytes since the previous snapshot. Unset when the snapshot is not billed on incremental usage."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted."
      },
      {
        "name": "full_size_bytes",
        "type": "integer",
        "description": "Full logical size of the snapshot, in bytes."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "True if the snapshot never expires."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch the snapshot was taken from. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "Unique system-generated ID for the snapshot."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the snapshot. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;"
  },
  {
    "name": "snapshot_id",
    "type": "string",
    "description": "The user-chosen ID; the final segment of ``name``."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the snapshot was created."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Client-provided configuration of the snapshot.",
    "children": [
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch to snapshot. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted. Mutually exclusive with ``ttl`` and ``no_expiry``."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "If true, the snapshot never expires. Mutually exclusive with ``ttl`` and ``expire_time``."
      },
      {
        "name": "source_branch_lsn",
        "type": "string",
        "description": "LSN to snapshot from, e.g. ``16/B374D848``. Mutually exclusive with ``source_branch_time``."
      },
      {
        "name": "source_branch_time",
        "type": "string (date-time)",
        "description": "Timestamp to snapshot from. Mutually exclusive with ``source_branch_lsn``."
      },
      {
        "name": "ttl",
        "type": "string",
        "description": "Time-to-live. The snapshot expires this long after it is created. Mutually exclusive with ``expire_time`` and ``no_expiry``. Reads report the resolved absolute ``expire_time`` instead."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Server-observed state of the snapshot.",
    "children": [
      {
        "name": "diff_size_bytes",
        "type": "integer",
        "description": "Incremental storage size in bytes since the previous snapshot. Unset when the snapshot is not billed on incremental usage."
      },
      {
        "name": "expire_time",
        "type": "string (date-time)",
        "description": "Absolute time at which the snapshot is deleted."
      },
      {
        "name": "full_size_bytes",
        "type": "integer",
        "description": "Full logical size of the snapshot, in bytes."
      },
      {
        "name": "no_expiry",
        "type": "boolean",
        "description": "True if the snapshot never expires."
      },
      {
        "name": "source_branch",
        "type": "string",
        "description": "The source branch the snapshot was taken from. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "Unique system-generated ID for the snapshot."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information about the specified snapshot.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of snapshots in the project.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes the specified snapshot.</td>
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
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;`). The resource name of the snapshot to delete. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;</td>
</tr>
<tr id="parameter-snapshot_id">
    <td><CopyableCode code="snapshot_id" /></td>
    <td><code>string</code></td>
    <td>The `snapshot_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;`). The resource name of the snapshot to delete. Format: projects/&#123;project_id&#125;/snapshots/&#123;snapshot_id&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of snapshots to return per page.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response; omit for the first page.</td>
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

Retrieves information about the specified snapshot.

```sql
SELECT
name,
snapshot_id,
create_time,
spec,
status,
uid
FROM databricks_workspace.postgres.postgres_snapshots
WHERE project_id = '{{ project_id }}' -- required
AND snapshot_id = '{{ snapshot_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of snapshots in the project.

```sql
SELECT
name,
snapshot_id,
create_time,
spec,
status,
uid
FROM databricks_workspace.postgres.postgres_snapshots
WHERE project_id = '{{ project_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Creates a snapshot, an immutable point-in-time copy of a branch's data, within the project.

```sql
INSERT INTO databricks_workspace.postgres.postgres_snapshots (
create_time,
name,
snapshot_id,
spec,
status,
uid,
project_id,
snapshot_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ create_time }}',
'{{ name }}',
'{{ snapshot_id }}',
'{{ spec }}',
'{{ status }}',
'{{ uid }}',
'{{ project_id }}',
'{{ snapshot_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_snapshots
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: snapshot_id
      value: "{{ snapshot_id }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_snapshots resource.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        When the snapshot was created.
    - name: name
      value: "{{ name }}"
      description: |
        The resource name of the snapshot. Format: projects/{project_id}/snapshots/{snapshot_id}
    - name: snapshot_id
      value: "{{ snapshot_id }}"
      description: |
        The user-chosen ID; the final segment of \`\`name\`\`.
    - name: spec
      description: |
        Client-provided configuration of the snapshot.
      value:
        source_branch: "{{ source_branch }}"
        expire_time: "{{ expire_time }}"
        no_expiry: {{ no_expiry }}
        source_branch_lsn: "{{ source_branch_lsn }}"
        source_branch_time: "{{ source_branch_time }}"
        ttl: "{{ ttl }}"
    - name: status
      description: |
        Server-observed state of the snapshot.
      value:
        diff_size_bytes: {{ diff_size_bytes }}
        expire_time: "{{ expire_time }}"
        full_size_bytes: {{ full_size_bytes }}
        no_expiry: {{ no_expiry }}
        source_branch: "{{ source_branch }}"
    - name: uid
      value: "{{ uid }}"
      description: |
        Unique system-generated ID for the snapshot.
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

Deletes the specified snapshot.

```sql
DELETE FROM databricks_workspace.postgres.postgres_snapshots
WHERE project_id = '{{ project_id }}' --required
AND snapshot_id = '{{ snapshot_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
