---
title: feature_materialization_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_materialization_sets
  - ml
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

Creates, updates, deletes, gets or lists a <code>feature_materialization_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_materialization_sets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_materialization_sets" /></td></tr>
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
    "name": "materialization_set_id",
    "type": "string",
    "description": "Server-assigned unique identifier for the materialization set."
  },
  {
    "name": "materialized_features",
    "type": "array",
    "description": "The materialized features in this set. Order is not significant. Updating the set with a materialized feature removed from this set will cause it to be deleted.",
    "children": [
      {
        "name": "feature_name",
        "type": "string",
        "description": "The full name of the feature in Unity Catalog."
      },
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": "The ID of the budget policy used to attribute the serverless compute cost of this materialization. If not specified, a default budget policy may be applied."
      },
      {
        "name": "cron_schedule",
        "type": "string",
        "description": ""
      },
      {
        "name": "cron_schedule_trigger",
        "type": "object",
        "description": "A cron-based schedule trigger for the materialization pipeline.",
        "children": [
          {
            "name": "cron_expression",
            "type": "string",
            "description": "The cron expression defining the schedule (e.g., \"0 0 * * *\" for daily at midnight). The schedule is interpreted in timezone_id (defaults to UTC). Required when mode is MANUAL (or unset). Left empty when mode is DERIVED, where the service computes it (aligned to UTC) from the features' window timing and fills it in on the response."
          },
          {
            "name": "mode",
            "type": "string",
            "description": "How the schedule is determined. Defaults to MANUAL when unset. (DERIVED, MANUAL)"
          },
          {
            "name": "timezone_id",
            "type": "string",
            "description": "A Java timezone ID. The schedule is resolved with respect to this timezone. Defaults to UTC when omitted. Can only be configured for MANUAL schedules; DERIVED schedules are always aligned to UTC."
          }
        ]
      },
      {
        "name": "is_online",
        "type": "boolean",
        "description": "True if this is an online materialized feature. False if it is an offline materialized feature."
      },
      {
        "name": "job_id",
        "type": "integer",
        "description": "The ID of the job that materializes the feature. This is present for both batch and streaming features."
      },
      {
        "name": "last_materialization_time",
        "type": "string",
        "description": "The timestamp when the pipeline last ran and updated the materialized feature values. If the pipeline has not run yet, this field will be null."
      },
      {
        "name": "latest_backfill_operation",
        "type": "string",
        "description": "Name of the latest backfill operation on this materialized feature. Format: operations/&#123;operation_id&#125;."
      },
      {
        "name": "materialization_set_id",
        "type": "string",
        "description": "The materialization set this materialized feature was created for, through DABs or direct-engine creation. Unset for a materialized feature that was not created as part of a set."
      },
      {
        "name": "materialized_feature_id",
        "type": "string",
        "description": "Server-assigned unique identifier for the materialized feature."
      },
      {
        "name": "notifications",
        "type": "object",
        "description": "Notification configuration around the materialization job or pipeline lifecycle. They are applied to every job and pipeline that materializes this feature. Features which are materialized in the same pipeline will share the same notification.",
        "children": [
          {
            "name": "on_failure",
            "type": "object",
            "description": "Who to notify when a run fails, and on which attempts.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "IDs of the notification destinations (for example Slack, Microsoft Teams, PagerDuty, or a generic webhook) to notify. Not supported for streaming materialized features."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "Email addresses to notify."
              },
              {
                "name": "final_attempt_only",
                "type": "boolean",
                "description": "If true, notify only when the final attempt of a run fails. If false or unset, notify on every failed attempt, including attempts that will be retried. Batch materialization does not retry failures that need a fix on your side, such as missing permissions or invalid configuration, so the first attempt is the final one. Other batch failures are retried up to twice. Streaming materialization restarts a failed update indefinitely unless the error cannot be retried. With this set, a streaming materialized feature notifies only on errors that cannot be retried, and never on failures that are restarted."
              }
            ]
          },
          {
            "name": "on_success",
            "type": "object",
            "description": "Who to notify when a run succeeds.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "IDs of the notification destinations (for example Slack, Microsoft Teams, PagerDuty, or a generic webhook) to notify. Not supported for streaming materialized features."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "Email addresses to notify."
              }
            ]
          }
        ]
      },
      {
        "name": "offline_store_config",
        "type": "object",
        "description": "Destination for writing feature values to an offline Delta table. The resulting table is returned as ``table_name``.",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": "The Unity Catalog catalog name."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The Unity Catalog schema name."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a table with this prefix and a generated postfix."
          }
        ]
      },
      {
        "name": "online_store_config",
        "type": "object",
        "description": "Destination for writing feature values to an online Lakebase table. The resulting table is returned as ``table_name``.",
        "children": [
          {
            "name": "catalog_name",
            "type": "string",
            "description": "The Unity Catalog catalog name. This name is also used as the Lakebase logical database name. Quoting is handled by the backend where needed, do not pre-quote it."
          },
          {
            "name": "schema_name",
            "type": "string",
            "description": "The Unity Catalog schema name. This name is also used as the Lakebase schema name under the database. Quoting is handled by the backend where needed, do not pre-quote it."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix for Unity Catalog table name. The materialized feature will be stored in a Lakebase table with this prefix and a generated postfix."
          },
          {
            "name": "online_store_name",
            "type": "string",
            "description": "The name of the target online store."
          }
        ]
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "The ID of the pipeline that materializes this feature. This is only present for streaming features."
      },
      {
        "name": "pipeline_schedule_state",
        "type": "string",
        "description": "The schedule state of the materialization pipeline. Hidden from GraphQL: being deprecated, so not exposed to Catalog Explorer. (ACTIVE, PAUSED, SNAPSHOT)"
      },
      {
        "name": "streaming_mode",
        "type": "object",
        "description": "The Structured Streaming trigger mode used for materialization. Real-time mode (RTM) targets sub-second latency for operational workloads; micro-batch mode (MBM) favors cost efficiency for ETL and analytics workloads.",
        "children": [
          {
            "name": "freshness_target",
            "type": "string",
            "description": "The desired data freshness for feature materialization, expressed as a duration string (e.g. \"1 minute\")."
          },
          {
            "name": "mode",
            "type": "string",
            "description": "The type of streaming mode used by the materialization pipeline. (STREAMING_MODE_TYPE_MBM, STREAMING_MODE_TYPE_RTM)"
          },
          {
            "name": "shuffle_partitions",
            "type": "integer",
            "description": "Number of shuffle partitions for streaming materialization of this feature. Higher values process high-throughput features with more parallelism at higher compute cost. Materialized features which are computed together will use the largest value set among them."
          }
        ]
      },
      {
        "name": "table_name",
        "type": "string",
        "description": "The fully qualified Unity Catalog path to the table containing the materialized feature (Delta table or Lakebase table). Output only."
      },
      {
        "name": "table_trigger",
        "type": "object",
        "description": "A trigger that fires when the upstream source table changes.",
        "children": [
          {
            "name": "condition",
            "type": "string",
            "description": "Which source table updates trigger a materialization run. If not set, any source table update triggers a run. (TABLE_TRIGGER_CONDITION_ALL_UPDATED, TABLE_TRIGGER_CONDITION_ANY_UPDATED)"
          },
          {
            "name": "min_time_between_triggers",
            "type": "string",
            "description": "The minimum time between two triggered runs, so a frequently updated source table does not trigger runs too often. If not set, a feature with a sliding window uses half its slide_duration and a feature with a tumbling window uses half its window_duration, clamped to between 5 minutes and 1 hour. Other features have no minimum."
          },
          {
            "name": "wait_after_last_change",
            "type": "string",
            "description": "How long the source table must go without updates before a run starts, so a series of updates settles before the run. If not set, a run starts as soon as the source table updates."
          }
        ]
      },
      {
        "name": "tags",
        "type": "object",
        "description": "Custom tags to associate with this materialization. They are applied to the materialization job (for batch features) or pipeline (for streaming features) and forwarded to the underlying compute as cluster tags, so materialization cost can be attributed in the billing system tables. These tags apply only to the materialization compute; they are not applied to the Unity Catalog Feature resource itself, whose tags are managed separately through the Unity Catalog tagging API. A maximum of 25 tags is supported; keys and values are subject to the same limitations as cluster tags."
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
    <td><a href="#parameter-materialization_set_id"><code>materialization_set_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a materialization set and the materialized features in it. A set whose materialized feature</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-request_id"><code>request_id</code></a></td>
    <td>Create a materialization set.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-materialization_set_id"><code>materialization_set_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-request_id"><code>request_id</code></a></td>
    <td>Update the materialization set's state to match the supplied materialization set. Changes are applied</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-materialization_set_id"><code>materialization_set_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-allow_missing"><code>allow_missing</code></a>, <a href="#parameter-request_id"><code>request_id</code></a></td>
    <td>Delete a materialization set and every materialized feature in it. The set is gone afterwards, so a</td>
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
<tr id="parameter-materialization_set_id">
    <td><CopyableCode code="materialization_set_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the materialization set to delete.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The fields to update. Only 'materialized_features' or '*' is supported.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-allow_missing">
    <td><CopyableCode code="allow_missing" /></td>
    <td><code>boolean</code></td>
    <td>Return success instead of NOT_FOUND when the set does not exist, so a repeated destroy is idempotent.</td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td>Idempotency token for the request. A second request carrying a token that has already been used returns the operation the first one created, whatever state it reached, and deletes nothing further. The token is not checked against the rest of the request. Omit it and each request deletes independently.</td>
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

Get a materialization set and the materialized features in it. A set whose materialized feature

```sql
SELECT
materialization_set_id,
materialized_features
FROM databricks_workspace.ml.feature_materialization_sets
WHERE materialization_set_id = '{{ materialization_set_id }}' -- required
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

Create a materialization set.

```sql
INSERT INTO databricks_workspace.ml.feature_materialization_sets (
materialization_set_id,
materialized_features,
deployment_name,
workspace_domain,
request_id
)
SELECT 
'{{ materialization_set_id }}',
'{{ materialized_features }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ request_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_materialization_sets
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the feature_materialization_sets resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the feature_materialization_sets resource.
    - name: materialization_set_id
      value: "{{ materialization_set_id }}"
      description: |
        Server-assigned unique identifier for the materialization set.
    - name: materialized_features
      description: |
        The materialized features in this set. Order is not significant. Updating the set with a materialized feature removed from this set will cause it to be deleted.
      value:
        - feature_name: "{{ feature_name }}"
          budget_policy_id: "{{ budget_policy_id }}"
          cron_schedule: "{{ cron_schedule }}"
          cron_schedule_trigger:
            cron_expression: "{{ cron_expression }}"
            mode: "{{ mode }}"
            timezone_id: "{{ timezone_id }}"
          is_online: {{ is_online }}
          job_id: {{ job_id }}
          last_materialization_time: "{{ last_materialization_time }}"
          latest_backfill_operation: "{{ latest_backfill_operation }}"
          materialization_set_id: "{{ materialization_set_id }}"
          materialized_feature_id: "{{ materialized_feature_id }}"
          notifications:
            on_failure:
              destination_ids:
                - "{{ destination_ids }}"
              email_addresses:
                - "{{ email_addresses }}"
              final_attempt_only: {{ final_attempt_only }}
            on_success:
              destination_ids:
                - "{{ destination_ids }}"
              email_addresses:
                - "{{ email_addresses }}"
          offline_store_config:
            catalog_name: "{{ catalog_name }}"
            schema_name: "{{ schema_name }}"
            table_name_prefix: "{{ table_name_prefix }}"
          online_store_config:
            catalog_name: "{{ catalog_name }}"
            schema_name: "{{ schema_name }}"
            table_name_prefix: "{{ table_name_prefix }}"
            online_store_name: "{{ online_store_name }}"
          pipeline_id: "{{ pipeline_id }}"
          pipeline_schedule_state: "{{ pipeline_schedule_state }}"
          streaming_mode:
            freshness_target: "{{ freshness_target }}"
            mode: "{{ mode }}"
            shuffle_partitions: {{ shuffle_partitions }}
          table_name: "{{ table_name }}"
          table_trigger:
            condition: "{{ condition }}"
            min_time_between_triggers: "{{ min_time_between_triggers }}"
            wait_after_last_change: "{{ wait_after_last_change }}"
          tags: "{{ tags }}"
    - name: request_id
      value: "{{ request_id }}"
      description: Idempotency token for the request. A second request carrying a token that has already been used returns the operation the first one created, whatever state it reached, and creates no second set. The token is not checked against the rest of the request, so reusing one for a different set returns the original operation rather than an error. Omit it and each request creates its own set.
      description: Idempotency token for the request. A second request carrying a token that has already been used returns the operation the first one created, whatever state it reached, and creates no second set. The token is not checked against the rest of the request, so reusing one for a different set returns the original operation rather than an error. Omit it and each request creates its own set.
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

Update the materialization set's state to match the supplied materialization set. Changes are applied

```sql
UPDATE databricks_workspace.ml.feature_materialization_sets
SET 
materialization_set_id = '{{ materialization_set_id }}',
materialized_features = '{{ materialized_features }}'
WHERE 
materialization_set_id = '{{ materialization_set_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND request_id = '{{ request_id}}';
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

Delete a materialization set and every materialized feature in it. The set is gone afterwards, so a

```sql
DELETE FROM databricks_workspace.ml.feature_materialization_sets
WHERE materialization_set_id = '{{ materialization_set_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND allow_missing = '{{ allow_missing }}'
AND request_id = '{{ request_id }}'
;
```
</TabItem>
</Tabs>
