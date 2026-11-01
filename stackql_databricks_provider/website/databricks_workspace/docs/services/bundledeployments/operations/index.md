---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - bundledeployments
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

Creates, updates, deletes, gets or lists an <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.bundledeployments.operations" /></td></tr>
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
    "description": "Resource name of the operation. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;"
  },
  {
    "name": "resource_id",
    "type": "string",
    "description": "ID of the actual resource in the workspace (e.g. the job ID, pipeline ID). Required whenever ``state`` is set, because state records a resource that exists. A CREATE or RECREATE that has not produced its resource yet records neither. Mutable: may be filled in (or corrected) later via UpdateOperation once the ID is known."
  },
  {
    "name": "sequence_id",
    "type": "integer",
    "description": "Monotonically increasing revision used for optimistic concurrency control (the AIP-154 concurrency token for this resource, realized as a sequence number rather than an opaque etag). The server assigns 0 when the operation is created and increments it on every successful UpdateOperation, so a never-updated operation is at 0 and the first successful update makes it 1. It is OPTIONAL rather than OUTPUT_ONLY because it is dual-purpose: GetOperation returns the current value, and UpdateOperation reads the caller-supplied value as a precondition. The caller must echo the value it last observed; if it no longer matches the server's value, the update is rejected with ABORTED so the caller can re-read and retry."
  },
  {
    "name": "action_type",
    "type": "string",
    "description": "The type of operation performed on this resource. Set when the version is created and immutable thereafter. (OPERATION_ACTION_TYPE_BIND, OPERATION_ACTION_TYPE_BIND_AND_UPDATE, OPERATION_ACTION_TYPE_CREATE, OPERATION_ACTION_TYPE_DELETE, OPERATION_ACTION_TYPE_INITIAL_REGISTER, OPERATION_ACTION_TYPE_RECREATE, OPERATION_ACTION_TYPE_RESIZE, OPERATION_ACTION_TYPE_UNBIND, OPERATION_ACTION_TYPE_UPDATE, OPERATION_ACTION_TYPE_UPDATE_WITH_ID)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the operation was recorded."
  },
  {
    "name": "dashboard_metadata",
    "type": "object",
    "description": "Dashboard-specific metadata; set only for dashboard resources. Mutable: may be set or updated via UpdateOperation as the resource is applied, and is mirrored onto the corresponding deployment-level resource.",
    "children": [
      {
        "name": "definition_path",
        "type": "string",
        "description": "Path of the file that declares this dashboard, relative to the bundle's workspace.file_path (Deployment.workspace_info.file_path) — join the two to get the file's absolute workspace path. For now this lives only on the dashboard metadata, and is a single string because it was a single string (``relative_path``) in the legacy bundle metadata.json. We may generalize it in the future: lifting it to a top-level field on Resource/Operation (every resource type has a definition location) and converting it to a repeated field, since a resource can be declared across multiple files/locations."
      },
      {
        "name": "source_path",
        "type": "string",
        "description": "Path of the dashboard's source artifact (its ``.lvdash.json``), relative to the deployment root."
      }
    ]
  },
  {
    "name": "error_message",
    "type": "string",
    "description": "Error message if the operation failed. Set when status is OPERATION_STATUS_FAILED. Captures the error encountered while applying the resource to the workspace. Mutable: may be updated after creation via UpdateOperation; setting it to an empty string clears it. After an update is applied, an operation whose status is OPERATION_STATUS_SUCCEEDED cannot carry an error_message."
  },
  {
    "name": "resource_key",
    "type": "string",
    "description": "Resource identifier within the bundle (e.g. \"jobs.foo\", \"pipelines.bar\", \"jobs.foo.permissions\", \"files.&lt;rel-path&gt;\"). Can be an arbitrary UTF-8 encoded string key. This key links the operation to the corresponding deployment-level Resource. Set when the version is created and immutable thereafter."
  },
  {
    "name": "resource_type",
    "type": "string",
    "description": "The type of the deployment resource this operation applies to. Derived from the ``resource_key`` prefix (e.g. \"jobs\" → JOB); the caller does not set this field. (DEPLOYMENT_RESOURCE_TYPE_ALERT, DEPLOYMENT_RESOURCE_TYPE_APP, DEPLOYMENT_RESOURCE_TYPE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_CLUSTER, DEPLOYMENT_RESOURCE_TYPE_CLUSTER_POLICY, DEPLOYMENT_RESOURCE_TYPE_DASHBOARD, DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE, DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT, DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION, DEPLOYMENT_RESOURCE_TYPE_GENIE_SPACE, DEPLOYMENT_RESOURCE_TYPE_INSTANCE_POOL, DEPLOYMENT_RESOURCE_TYPE_JOB, DEPLOYMENT_RESOURCE_TYPE_JOB_RUN, DEPLOYMENT_RESOURCE_TYPE_MODEL, DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_PIPELINE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_CATALOG, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_DATABASE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ROLE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_SYNCED_TABLE, DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR, DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL, DEPLOYMENT_RESOURCE_TYPE_SCHEMA, DEPLOYMENT_RESOURCE_TYPE_SECRET, DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE, DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE, DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE, DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_INDEX, DEPLOYMENT_RESOURCE_TYPE_VOLUME)"
  },
  {
    "name": "state",
    "type": "string",
    "description": "Serialized local config state after the operation. Its presence records whether the resource is still tracked by the deployment. Explicitly clearing state removes the resource from the deployment; omitting it from the update mask leaves resource state unchanged. State is stored only on Resources. UpdateOperation accepts state but omits it from its response, as do subsequent GetOperation and ListOperations. Mutable: may be updated after creation via UpdateOperation. When updating, the caller must echo the last-observed ``sequence_id`` as a concurrency precondition. The string is not parsed; it is projected onto the corresponding Resource's state. It is deliberately not google.protobuf.Value, whose only numeric case is ``double number_value``, so parsing the client's JSON into it rewrites every integer as a double - ``1`` reads back as ``1.0``, which no longer deserializes into an integer field - and silently loses precision above 2^53, which is within range for IDs the client records. A string rather than bytes: the payload is always UTF-8 JSON, and proto3 JSON maps bytes to base64, which inflates every request and response by a third and makes state unreadable in logs and API responses. Both generate the same OpenAPI schema (\"type\": \"string\"), so the SDKs are identical either way."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the operation. Starts as OPERATION_STATUS_PENDING when the version is created and moves to a terminal status once the resource is applied. Mutable: updated via UpdateOperation, e.g. when an operation recorded as failed is retried and eventually succeeds. (OPERATION_STATUS_FAILED, OPERATION_STATUS_PENDING, OPERATION_STATUS_SUCCEEDED)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the operation was last updated. Set to ``create_time`` when the operation is created and to the server timestamp on each successful UpdateOperation."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the operation. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;"
  },
  {
    "name": "resource_id",
    "type": "string",
    "description": "ID of the actual resource in the workspace (e.g. the job ID, pipeline ID). Required whenever ``state`` is set, because state records a resource that exists. A CREATE or RECREATE that has not produced its resource yet records neither. Mutable: may be filled in (or corrected) later via UpdateOperation once the ID is known."
  },
  {
    "name": "sequence_id",
    "type": "integer",
    "description": "Monotonically increasing revision used for optimistic concurrency control (the AIP-154 concurrency token for this resource, realized as a sequence number rather than an opaque etag). The server assigns 0 when the operation is created and increments it on every successful UpdateOperation, so a never-updated operation is at 0 and the first successful update makes it 1. It is OPTIONAL rather than OUTPUT_ONLY because it is dual-purpose: GetOperation returns the current value, and UpdateOperation reads the caller-supplied value as a precondition. The caller must echo the value it last observed; if it no longer matches the server's value, the update is rejected with ABORTED so the caller can re-read and retry."
  },
  {
    "name": "action_type",
    "type": "string",
    "description": "The type of operation performed on this resource. Set when the version is created and immutable thereafter. (OPERATION_ACTION_TYPE_BIND, OPERATION_ACTION_TYPE_BIND_AND_UPDATE, OPERATION_ACTION_TYPE_CREATE, OPERATION_ACTION_TYPE_DELETE, OPERATION_ACTION_TYPE_INITIAL_REGISTER, OPERATION_ACTION_TYPE_RECREATE, OPERATION_ACTION_TYPE_RESIZE, OPERATION_ACTION_TYPE_UNBIND, OPERATION_ACTION_TYPE_UPDATE, OPERATION_ACTION_TYPE_UPDATE_WITH_ID)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the operation was recorded."
  },
  {
    "name": "dashboard_metadata",
    "type": "object",
    "description": "Dashboard-specific metadata; set only for dashboard resources. Mutable: may be set or updated via UpdateOperation as the resource is applied, and is mirrored onto the corresponding deployment-level resource.",
    "children": [
      {
        "name": "definition_path",
        "type": "string",
        "description": "Path of the file that declares this dashboard, relative to the bundle's workspace.file_path (Deployment.workspace_info.file_path) — join the two to get the file's absolute workspace path. For now this lives only on the dashboard metadata, and is a single string because it was a single string (``relative_path``) in the legacy bundle metadata.json. We may generalize it in the future: lifting it to a top-level field on Resource/Operation (every resource type has a definition location) and converting it to a repeated field, since a resource can be declared across multiple files/locations."
      },
      {
        "name": "source_path",
        "type": "string",
        "description": "Path of the dashboard's source artifact (its ``.lvdash.json``), relative to the deployment root."
      }
    ]
  },
  {
    "name": "error_message",
    "type": "string",
    "description": "Error message if the operation failed. Set when status is OPERATION_STATUS_FAILED. Captures the error encountered while applying the resource to the workspace. Mutable: may be updated after creation via UpdateOperation; setting it to an empty string clears it. After an update is applied, an operation whose status is OPERATION_STATUS_SUCCEEDED cannot carry an error_message."
  },
  {
    "name": "resource_key",
    "type": "string",
    "description": "Resource identifier within the bundle (e.g. \"jobs.foo\", \"pipelines.bar\", \"jobs.foo.permissions\", \"files.&lt;rel-path&gt;\"). Can be an arbitrary UTF-8 encoded string key. This key links the operation to the corresponding deployment-level Resource. Set when the version is created and immutable thereafter."
  },
  {
    "name": "resource_type",
    "type": "string",
    "description": "The type of the deployment resource this operation applies to. Derived from the ``resource_key`` prefix (e.g. \"jobs\" → JOB); the caller does not set this field. (DEPLOYMENT_RESOURCE_TYPE_ALERT, DEPLOYMENT_RESOURCE_TYPE_APP, DEPLOYMENT_RESOURCE_TYPE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_CLUSTER, DEPLOYMENT_RESOURCE_TYPE_CLUSTER_POLICY, DEPLOYMENT_RESOURCE_TYPE_DASHBOARD, DEPLOYMENT_RESOURCE_TYPE_DATABASE_CATALOG, DEPLOYMENT_RESOURCE_TYPE_DATABASE_INSTANCE, DEPLOYMENT_RESOURCE_TYPE_EXPERIMENT, DEPLOYMENT_RESOURCE_TYPE_EXTERNAL_LOCATION, DEPLOYMENT_RESOURCE_TYPE_GENIE_SPACE, DEPLOYMENT_RESOURCE_TYPE_INSTANCE_POOL, DEPLOYMENT_RESOURCE_TYPE_JOB, DEPLOYMENT_RESOURCE_TYPE_JOB_RUN, DEPLOYMENT_RESOURCE_TYPE_MODEL, DEPLOYMENT_RESOURCE_TYPE_MODEL_SERVING_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_PIPELINE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_BRANCH, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_CATALOG, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_DATABASE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_PROJECT, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_ROLE, DEPLOYMENT_RESOURCE_TYPE_POSTGRES_SYNCED_TABLE, DEPLOYMENT_RESOURCE_TYPE_QUALITY_MONITOR, DEPLOYMENT_RESOURCE_TYPE_REGISTERED_MODEL, DEPLOYMENT_RESOURCE_TYPE_SCHEMA, DEPLOYMENT_RESOURCE_TYPE_SECRET, DEPLOYMENT_RESOURCE_TYPE_SECRET_SCOPE, DEPLOYMENT_RESOURCE_TYPE_SQL_WAREHOUSE, DEPLOYMENT_RESOURCE_TYPE_SYNCED_DATABASE_TABLE, DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_ENDPOINT, DEPLOYMENT_RESOURCE_TYPE_VECTOR_SEARCH_INDEX, DEPLOYMENT_RESOURCE_TYPE_VOLUME)"
  },
  {
    "name": "state",
    "type": "string",
    "description": "Serialized local config state after the operation. Its presence records whether the resource is still tracked by the deployment. Explicitly clearing state removes the resource from the deployment; omitting it from the update mask leaves resource state unchanged. State is stored only on Resources. UpdateOperation accepts state but omits it from its response, as do subsequent GetOperation and ListOperations. Mutable: may be updated after creation via UpdateOperation. When updating, the caller must echo the last-observed ``sequence_id`` as a concurrency precondition. The string is not parsed; it is projected onto the corresponding Resource's state. It is deliberately not google.protobuf.Value, whose only numeric case is ``double number_value``, so parsing the client's JSON into it rewrites every integer as a double - ``1`` reads back as ``1.0``, which no longer deserializes into an integer field - and silently loses precision above 2^53, which is within range for IDs the client records. A string rather than bytes: the payload is always UTF-8 JSON, and proto3 JSON maps bytes to base64, which inflates every request and response by a third and makes state unreadable in logs and API responses. Both generate the same OpenAPI schema (\"type\": \"string\"), so the SDKs are identical either way."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the operation. Starts as OPERATION_STATUS_PENDING when the version is created and moves to a terminal status once the resource is applied. Mutable: updated via UpdateOperation, e.g. when an operation recorded as failed is retried and eventually succeeds. (OPERATION_STATUS_FAILED, OPERATION_STATUS_PENDING, OPERATION_STATUS_SUCCEEDED)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the operation was last updated. Set to ``create_time`` when the operation is created and to the server timestamp on each successful UpdateOperation."
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
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-resource_key"><code>resource_key</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a resource operation by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists resource operations under a version.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-resource_key"><code>resource_key</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-operation"><code>operation</code></a></td>
    <td></td>
    <td>Updates a resource operation's mutable fields.</td>
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
<tr id="parameter-deployment_id">
    <td><CopyableCode code="deployment_id" /></td>
    <td><code>string</code></td>
    <td>The `deployment_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;`). Resource name of the operation. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-resource_key">
    <td><CopyableCode code="resource_key" /></td>
    <td><code>string</code></td>
    <td>The `resource_key` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;`). Resource name of the operation. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The set of fields to update. Required; supported paths are ``state``, ``error_message``, ``resource_id``, ``status``, and ``dashboard_metadata``. An empty mask or any other path is rejected with INVALID_PARAMETER_VALUE.</td>
</tr>
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td>The `version_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;`). Resource name of the operation. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;/operations/&#123;resource_key&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of operations to return. The service may return fewer than this value. If unspecified, at most 50 operations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListOperations`` call. Provide this to retrieve the subsequent page.</td>
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

Retrieves a resource operation by its resource name.

```sql
SELECT
name,
resource_id,
sequence_id,
action_type,
create_time,
dashboard_metadata,
error_message,
resource_key,
resource_type,
state,
status,
update_time
FROM databricks_workspace.bundledeployments.operations
WHERE deployment_id = '{{ deployment_id }}' -- required
AND version_id = '{{ version_id }}' -- required
AND resource_key = '{{ resource_key }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists resource operations under a version.

```sql
SELECT
name,
resource_id,
sequence_id,
action_type,
create_time,
dashboard_metadata,
error_message,
resource_key,
resource_type,
state,
status,
update_time
FROM databricks_workspace.bundledeployments.operations
WHERE deployment_id = '{{ deployment_id }}' -- required
AND version_id = '{{ version_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
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

Updates a resource operation's mutable fields.

```sql
UPDATE databricks_workspace.bundledeployments.operations
SET 
operation = '{{ operation }}'
WHERE 
deployment_id = '{{ deployment_id }}' --required
AND version_id = '{{ version_id }}' --required
AND resource_key = '{{ resource_key }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND operation = '{{ operation }}' --required
RETURNING
name,
resource_id,
sequence_id,
action_type,
create_time,
dashboard_metadata,
error_message,
resource_key,
resource_type,
state,
status,
update_time;
```
</TabItem>
</Tabs>
