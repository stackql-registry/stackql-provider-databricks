---
title: postgres_snapshot_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_snapshot_schedules
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

Creates, updates, deletes, gets or lists a <code>postgres_snapshot_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_snapshot_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_snapshot_schedules" /></td></tr>
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
    "description": "The resource name of the branch's snapshot schedule. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/snapshot-schedule"
  },
  {
    "name": "schedule",
    "type": "array",
    "description": "The cadences at which automatic snapshots are taken. Update replaces the whole set; an empty set disables automatic snapshots. Order is not significant. When several cadences fire together, one snapshot is taken, retained for the longest of their retentions.",
    "children": [
      {
        "name": "retention",
        "type": "string",
        "description": "How long snapshots from this cadence are kept before automatic deletion. Must be at least 1 hour. Applied when a snapshot is taken; not retroactive, so changing it affects only later snapshots."
      },
      {
        "name": "daily_schedule",
        "type": "object",
        "description": "Take a snapshot once per day.",
        "children": [
          {
            "name": "hour",
            "type": "integer",
            "description": "The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."
          }
        ]
      },
      {
        "name": "monthly_schedule",
        "type": "object",
        "description": "Take a snapshot once per month.",
        "children": [
          {
            "name": "day",
            "type": "integer",
            "description": "The day of the month on which to take the snapshot, in [1, 31]. In shorter months the snapshot is taken on the last day instead (day 31 runs on Feb 28 or 29, and on Apr 30), so every month gets exactly one snapshot."
          },
          {
            "name": "hour",
            "type": "integer",
            "description": "The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."
          }
        ]
      },
      {
        "name": "weekly_schedule",
        "type": "object",
        "description": "Take a snapshot once per week.",
        "children": [
          {
            "name": "day_of_week",
            "type": "string",
            "description": "The day of the week on which to take the snapshot. (FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY)"
          },
          {
            "name": "hour",
            "type": "integer",
            "description": "The hour of the day, in UTC, at which to take the snapshot, in [0, 23]."
          }
        ]
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves the snapshot schedule for a branch. A branch with no configured schedule returns an empty</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-snapshot_schedule"><code>snapshot_schedule</code></a></td>
    <td></td>
    <td>Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty</td>
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
    <td>The `branch_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/snapshot-schedule`). The resource name of the branch's snapshot schedule. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/snapshot-schedule</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/snapshot-schedule`). The resource name of the branch's snapshot schedule. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/snapshot-schedule</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. The only updatable path is ``schedule``, which replaces the entire set of cadences.</td>
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

Retrieves the snapshot schedule for a branch. A branch with no configured schedule returns an empty

```sql
SELECT
name,
schedule
FROM databricks_workspace.postgres.postgres_snapshot_schedules
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
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

Sets the snapshot schedule for a branch. The ``schedule`` field is replaced wholesale; an empty

```sql
UPDATE databricks_workspace.postgres.postgres_snapshot_schedules
SET 
snapshot_schedule = '{{ snapshot_schedule }}'
WHERE 
project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND snapshot_schedule = '{{ snapshot_schedule }}' --required;
```
</TabItem>
</Tabs>
