---
title: postgres_synced_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_synced_tables
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

Creates, updates, deletes, gets or lists a <code>postgres_synced_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_synced_tables" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_synced_tables" /></td></tr>
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
    "description": "Output only. The Full resource name of the synced table in Postgres where (catalog, schema, table) are the UC entity names. Format \"synced_tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;\" For the corresponding source table in the Unity catalog look for the \"source_table_full_name\" attribute."
  },
  {
    "name": "synced_table_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "spec",
    "type": "object",
    "description": "Configuration details of the synced table, such as the source table, scheduling policy, etc.",
    "children": [
      {
        "name": "accelerated_sync",
        "type": "boolean",
        "description": ""
      },
      {
        "name": "branch",
        "type": "string",
        "description": "The full resource name the branch associated with the table. Format: \"projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;\"."
      },
      {
        "name": "create_database_objects_if_missing",
        "type": "boolean",
        "description": "If true, the synced table's logical database and schema resources in PG will be created if they do not already exist. The request will fail if this is false and the database/schema do not exist. Defaults to true if omitted."
      },
      {
        "name": "existing_pipeline_id",
        "type": "string",
        "description": "ID of an existing pipeline to bin-pack this synced table into. At most one of existing_pipeline_id and new_pipeline_spec should be defined. The pipeline used for the synced table is returned via the top level pipeline_id attribute."
      },
      {
        "name": "extra_columns",
        "type": "array",
        "description": "Extra PostgreSQL-only columns to add to the synced table.",
        "children": [
          {
            "name": "column_name",
            "type": "string",
            "description": "Name of the column."
          },
          {
            "name": "column_type",
            "type": "string",
            "description": "PostgreSQL type of the column, for example \"tsvector\" or \"vector(1024)\"."
          },
          {
            "name": "compute",
            "type": "string",
            "description": "SQL expression used to compute the column's value, for example \"to_tsvector('english', content)\"."
          },
          {
            "name": "maintenance",
            "type": "string",
            "description": "How the column's value is populated and kept up to date. (STORED_GENERATED)"
          }
        ]
      },
      {
        "name": "new_pipeline_spec",
        "type": "object",
        "description": "Specification for creating a new pipeline. At most one of existing_pipeline_id and new_pipeline_spec should be defined. The pipeline used for the synced table is returned via the top level pipeline_id attribute.",
        "children": [
          {
            "name": "budget_policy_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "pipeline_channel",
            "type": "string",
            "description": "Release channel of the underlying pipeline's runtime. Some source table configurations (e.g., read-time CDF) require PREVIEW. Defaults to CURRENT if not specified. (CURRENT, PREVIEW)"
          },
          {
            "name": "storage_catalog",
            "type": "string",
            "description": "UC catalog for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be a standard catalog where the user has permissions to create Delta tables."
          },
          {
            "name": "storage_schema",
            "type": "string",
            "description": "UC schema for the pipeline to store intermediate files (checkpoints, event logs etc). This needs to be in the standard catalog where the user has permissions to create Delta tables."
          }
        ]
      },
      {
        "name": "postgres_database",
        "type": "string",
        "description": "The Postgres database name where the synced table will be created in. If this synced table is created inside a Lakebase Catalog, this attribute can be omitted on creation and is inferred from the postgres_database associated with the Lakebase Catalog. If specified when inside a Lakebase Catalog, the value must match. A value must be specified when creating a synced table inside a Standard Catalog."
      },
      {
        "name": "primary_key_columns",
        "type": "array",
        "description": "Primary Key columns to be used for data insert/update in the destination."
      },
      {
        "name": "scheduling_policy",
        "type": "string",
        "description": "Scheduling policy of the underlying pipeline. (CONTINUOUS, SNAPSHOT, TRIGGERED)"
      },
      {
        "name": "source_table_full_name",
        "type": "string",
        "description": "Three-part (catalog, schema, table) name of the source Delta table. For the corresponding destination table, use any of the two: - synced_table_id used at the creation of the SyncedTable - \"name\" consisting of \"synced_tables/\" prefix and the full name of the destination table."
      },
      {
        "name": "timeseries_key",
        "type": "string",
        "description": "Time series key to deduplicate (tie-break) rows with the same primary key."
      },
      {
        "name": "type_overrides",
        "type": "array",
        "description": "Override the default Delta-&gt;PG type mapping for specific columns. A TypeOverride with PG_SPECIFIC_TYPE_UNSPECIFIED is rejected; a valid pg_type must be set.",
        "children": [
          {
            "name": "column_name",
            "type": "string",
            "description": "Name of the source column whose target PostgreSQL type should be overridden."
          },
          {
            "name": "pg_type",
            "type": "string",
            "description": "PostgreSQL-specific target type to use for the column. (PG_SPECIFIC_TYPE_HALFVEC, PG_SPECIFIC_TYPE_VARCHAR, PG_SPECIFIC_TYPE_VECTOR)"
          },
          {
            "name": "size",
            "type": "integer",
            "description": "Size parameter for the target type, for types that take one (e.g. vector dimension, varchar length). Required when the chosen pg_type needs a size."
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Synced Table data synchronization status.",
    "children": [
      {
        "name": "detailed_state",
        "type": "string",
        "description": "The state of a synced table. (SYNCED_TABLE_OFFLINE, SYNCED_TABLE_OFFLINE_FAILED, SYNCED_TABLE_ONLINE, SYNCED_TABLE_ONLINE_CONTINUOUS_UPDATE, SYNCED_TABLE_ONLINE_NO_PENDING_UPDATE, SYNCED_TABLE_ONLINE_PIPELINE_FAILED, SYNCED_TABLE_ONLINE_TRIGGERED_UPDATE, SYNCED_TABLE_ONLINE_UPDATING_PIPELINE_RESOURCES, SYNCED_TABLE_PROVISIONING, SYNCED_TABLE_PROVISIONING_INITIAL_SNAPSHOT, SYNCED_TABLE_PROVISIONING_PIPELINE_RESOURCES)"
      },
      {
        "name": "last_processed_commit_version",
        "type": "integer",
        "description": "The last source table Delta version that was successfully synced to the synced table."
      },
      {
        "name": "last_sync",
        "type": "object",
        "description": "Summary of the last successful synchronization from source to destination.",
        "children": [
          {
            "name": "delta_table_sync_info",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "delta_commit_time",
                "type": "string (date-time)",
                "description": ""
              },
              {
                "name": "delta_commit_version",
                "type": "integer",
                "description": "The Delta Lake commit version that was last successfully synced."
              }
            ]
          },
          {
            "name": "sync_end_time",
            "type": "string (date-time)",
            "description": "The end timestamp of the most recent successful synchronization. This is the time when the data is available in the synced table."
          },
          {
            "name": "sync_start_time",
            "type": "string (date-time)",
            "description": "The starting timestamp of the most recent successful synchronization from the source table to the destination (synced) table. Note this is the starting timestamp of the sync operation, not the end time. E.g., for a batch, this is the time when the sync operation started."
          }
        ]
      },
      {
        "name": "last_sync_time",
        "type": "string (date-time)",
        "description": "The end timestamp of the last time any data was synchronized from the source table to the synced table. This is when the data is available in the synced table."
      },
      {
        "name": "message",
        "type": "string",
        "description": "A text description of the current state of the synced table."
      },
      {
        "name": "ongoing_sync_progress",
        "type": "object",
        "description": "Progress information of the Synced Table data synchronization pipeline.",
        "children": [
          {
            "name": "estimated_completion_time_seconds",
            "type": "number",
            "description": "The estimated time remaining to complete this update in seconds."
          },
          {
            "name": "latest_version_currently_processing",
            "type": "integer",
            "description": "The source table Delta version that was last processed by the pipeline. The pipeline may not have completely processed this version yet."
          },
          {
            "name": "sync_progress_completion",
            "type": "number",
            "description": "The completion ratio of this update. This is a number between 0 and 1."
          },
          {
            "name": "synced_row_count",
            "type": "integer",
            "description": "The number of rows that have been synced in this update."
          },
          {
            "name": "total_row_count",
            "type": "integer",
            "description": "The total number of rows that need to be synced in this update. This number may be an estimate."
          }
        ]
      },
      {
        "name": "pipeline_id",
        "type": "string",
        "description": "ID of the associated pipeline."
      },
      {
        "name": "project",
        "type": "string",
        "description": "The full resource name of the project associated with the table. Format: \"projects/&#123;project_id&#125;\"."
      },
      {
        "name": "provisioning_phase",
        "type": "string",
        "description": "The current phase of the data synchronization pipeline. (PROVISIONING_PHASE_INDEX_SCAN, PROVISIONING_PHASE_INDEX_SORT, PROVISIONING_PHASE_MAIN)"
      },
      {
        "name": "unity_catalog_provisioning_state",
        "type": "string",
        "description": "The provisioning state of the synced table entity in Unity Catalog. (ACTIVE, DEGRADED, DELETING, FAILED, PROVISIONING, UPDATING)"
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "The Unity Catalog table ID for this synced table."
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
    <td>Get a Synced Table.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-synced_table_id"><code>synced_table_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Create a Synced Table.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete a Synced Table.</td>
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
    <td>The `full_name` segment of the `name` resource name (`synced_tables/&#123;full_name&#125;`). The Full resource name of the synced table, of the format "synced_tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;", where (catalog, schema, table) are the UC entity names.</td>
</tr>
<tr id="parameter-synced_table_id">
    <td><CopyableCode code="synced_table_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Synced Table. This becomes the final component of the SyncedTable's resource name. ID is required and is the synced table name, containing (catalog, schema, table) tuple. Elements of the tuple are the UC entity names. Example: "&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;" synced_table_id represents both of the following: 1. An online VIEW virtual table in the Unity Catalog accessible via the Lakehouse Federation. 2. Postgres table named "&#123;table&#125;" in schema "&#123;schema&#125;" in the connected Postgres database</td>
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

Get a Synced Table.

```sql
SELECT
name,
synced_table_id,
create_time,
spec,
status,
uid
FROM databricks_workspace.postgres.postgres_synced_tables
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

Create a Synced Table.

```sql
INSERT INTO databricks_workspace.postgres.postgres_synced_tables (
create_time,
name,
spec,
status,
synced_table_id,
uid,
synced_table_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ create_time }}',
'{{ name }}',
'{{ spec }}',
'{{ status }}',
'{{ synced_table_id }}',
'{{ uid }}',
'{{ synced_table_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_synced_tables
  props:
    - name: synced_table_id
      value: "{{ synced_table_id }}"
      description: Required parameter for the postgres_synced_tables resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_synced_tables resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_synced_tables resource.
    - name: create_time
      value: "{{ create_time }}"
    - name: name
      value: "{{ name }}"
      description: |
        Output only. The Full resource name of the synced table in Postgres where (catalog, schema, table) are the UC entity names. Format "synced_tables/{catalog}.{schema}.{table}" For the corresponding source table in the Unity catalog look for the "source_table_full_name" attribute.
    - name: spec
      description: |
        Configuration details of the synced table, such as the source table, scheduling policy, etc.
      value:
        accelerated_sync: {{ accelerated_sync }}
        branch: "{{ branch }}"
        create_database_objects_if_missing: {{ create_database_objects_if_missing }}
        existing_pipeline_id: "{{ existing_pipeline_id }}"
        extra_columns:
          - column_name: "{{ column_name }}"
            column_type: "{{ column_type }}"
            compute: "{{ compute }}"
            maintenance: "{{ maintenance }}"
        new_pipeline_spec:
          budget_policy_id: "{{ budget_policy_id }}"
          pipeline_channel: "{{ pipeline_channel }}"
          storage_catalog: "{{ storage_catalog }}"
          storage_schema: "{{ storage_schema }}"
        postgres_database: "{{ postgres_database }}"
        primary_key_columns:
          - "{{ primary_key_columns }}"
        scheduling_policy: "{{ scheduling_policy }}"
        source_table_full_name: "{{ source_table_full_name }}"
        timeseries_key: "{{ timeseries_key }}"
        type_overrides:
          - column_name: "{{ column_name }}"
            pg_type: "{{ pg_type }}"
            size: {{ size }}
    - name: status
      description: |
        Synced Table data synchronization status.
      value:
        detailed_state: "{{ detailed_state }}"
        last_processed_commit_version: {{ last_processed_commit_version }}
        last_sync:
          delta_table_sync_info:
            delta_commit_time: "{{ delta_commit_time }}"
            delta_commit_version: {{ delta_commit_version }}
          sync_end_time: "{{ sync_end_time }}"
          sync_start_time: "{{ sync_start_time }}"
        last_sync_time: "{{ last_sync_time }}"
        message: "{{ message }}"
        ongoing_sync_progress:
          estimated_completion_time_seconds: {{ estimated_completion_time_seconds }}
          latest_version_currently_processing: {{ latest_version_currently_processing }}
          sync_progress_completion: {{ sync_progress_completion }}
          synced_row_count: {{ synced_row_count }}
          total_row_count: {{ total_row_count }}
        pipeline_id: "{{ pipeline_id }}"
        project: "{{ project }}"
        provisioning_phase: "{{ provisioning_phase }}"
        unity_catalog_provisioning_state: "{{ unity_catalog_provisioning_state }}"
    - name: synced_table_id
      value: "{{ synced_table_id }}"
      description: |
        The part of the name, chosen by the user when the resource was created.
    - name: uid
      value: "{{ uid }}"
      description: |
        The Unity Catalog table ID for this synced table.
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

Delete a Synced Table.

```sql
DELETE FROM databricks_workspace.postgres.postgres_synced_tables
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
