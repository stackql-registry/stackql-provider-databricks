---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.bundledeployments.deployments" /></td></tr>
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
    "description": "Resource name of the deployment. Format: deployments/&#123;deployment_id&#125;"
  },
  {
    "name": "last_successful_version_id",
    "type": "string",
    "description": "The version_id of the most recent version that completed successfully. Unset until a version has completed successfully. Unlike last_version_id, it is not advanced when a version fails, so it always points at the last known-good deployment state (or is unset if there has never been one)."
  },
  {
    "name": "last_version_id",
    "type": "string",
    "description": "The version_id of the most recent deployment version."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable name for the deployment, up to 256 characters."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "The bundle target name associated with this deployment."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the deployment was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the deployment (email or principal name). Empty if authoritative deployment metadata does not identify a creator or the principal cannot be resolved."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production). (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "destroy_time",
    "type": "string (date-time)",
    "description": "When deletion was recorded. Unset if deletion has not been recorded. This response metadata does not determine the deployment's lifecycle status."
  },
  {
    "name": "destroyed_by",
    "type": "string",
    "description": "The user who destroyed the deployment (email or principal name). Unset if the deployment has not been destroyed."
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the deployment's source, derived from the latest version.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Branch the source was deployed from."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Commit SHA of the deployed source."
      },
      {
        "name": "origin_url",
        "type": "string",
        "description": "URL of the git remote the source was deployed from."
      }
    ]
  },
  {
    "name": "initial_parent_path",
    "type": "string",
    "description": "The workspace path of the existing folder where the deployment is initially created. Must be absolute and canonical, with single separators, no ``.`` or ``..`` segments, and no trailing slash unless the path is ``/``. It may contain at most 24 path segments, excluding an optional leading ``/Workspace`` segment. The complete path may contain up to 1,024 characters, and each segment may contain up to 511 characters. This field is input only and is not returned in create, get, or list responses."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Current status of the deployment. (DEPLOYMENT_STATUS_ACTIVE, DEPLOYMENT_STATUS_DELETED, DEPLOYMENT_STATUS_FAILED, DEPLOYMENT_STATUS_IN_PROGRESS)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the deployment was last updated."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The user who most recently updated the deployment (email or principal name). Empty if authoritative deployment metadata does not identify a modifier or the principal cannot be resolved."
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment.",
    "children": [
      {
        "name": "bundle_root_path",
        "type": "string",
        "description": "Path of the bundle root (the directory containing databricks.yml) relative to git_folder_path. Empty when the deployment is not from a Databricks Git folder."
      },
      {
        "name": "file_path",
        "type": "string",
        "description": "Absolute workspace path where the deployed bundle files live. Mirrors the workspace.file_path field in DABs bundle config."
      },
      {
        "name": "git_folder_path",
        "type": "string",
        "description": "When deployed from a Databricks Git folder, the absolute workspace path of that folder; empty for local deploys."
      },
      {
        "name": "root_path",
        "type": "string",
        "description": "Absolute workspace path of the deployment root — the base path the deployed files live under. Mirrors workspace.root_path in the DABs bundle config; file_path is its files subdirectory."
      },
      {
        "name": "source_linked",
        "type": "boolean",
        "description": "Whether files are served directly from the source sync root instead of being copied into file_path."
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
    "description": "Resource name of the deployment. Format: deployments/&#123;deployment_id&#125;"
  },
  {
    "name": "last_successful_version_id",
    "type": "string",
    "description": "The version_id of the most recent version that completed successfully. Unset until a version has completed successfully. Unlike last_version_id, it is not advanced when a version fails, so it always points at the last known-good deployment state (or is unset if there has never been one)."
  },
  {
    "name": "last_version_id",
    "type": "string",
    "description": "The version_id of the most recent deployment version."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable name for the deployment, up to 256 characters."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "The bundle target name associated with this deployment."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the deployment was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the deployment (email or principal name). Empty if authoritative deployment metadata does not identify a creator or the principal cannot be resolved."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production). (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "destroy_time",
    "type": "string (date-time)",
    "description": "When deletion was recorded. Unset if deletion has not been recorded. This response metadata does not determine the deployment's lifecycle status."
  },
  {
    "name": "destroyed_by",
    "type": "string",
    "description": "The user who destroyed the deployment (email or principal name). Unset if the deployment has not been destroyed."
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the deployment's source, derived from the latest version.",
    "children": [
      {
        "name": "branch",
        "type": "string",
        "description": "Branch the source was deployed from."
      },
      {
        "name": "commit",
        "type": "string",
        "description": "Commit SHA of the deployed source."
      },
      {
        "name": "origin_url",
        "type": "string",
        "description": "URL of the git remote the source was deployed from."
      }
    ]
  },
  {
    "name": "initial_parent_path",
    "type": "string",
    "description": "The workspace path of the existing folder where the deployment is initially created. Must be absolute and canonical, with single separators, no ``.`` or ``..`` segments, and no trailing slash unless the path is ``/``. It may contain at most 24 path segments, excluding an optional leading ``/Workspace`` segment. The complete path may contain up to 1,024 characters, and each segment may contain up to 511 characters. This field is input only and is not returned in create, get, or list responses."
  },
  {
    "name": "status",
    "type": "string",
    "description": "Current status of the deployment. (DEPLOYMENT_STATUS_ACTIVE, DEPLOYMENT_STATUS_DELETED, DEPLOYMENT_STATUS_FAILED, DEPLOYMENT_STATUS_IN_PROGRESS)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the deployment was last updated."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "The user who most recently updated the deployment (email or principal name). Empty if authoritative deployment metadata does not identify a modifier or the principal cannot be resolved."
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment.",
    "children": [
      {
        "name": "bundle_root_path",
        "type": "string",
        "description": "Path of the bundle root (the directory containing databricks.yml) relative to git_folder_path. Empty when the deployment is not from a Databricks Git folder."
      },
      {
        "name": "file_path",
        "type": "string",
        "description": "Absolute workspace path where the deployed bundle files live. Mirrors the workspace.file_path field in DABs bundle config."
      },
      {
        "name": "git_folder_path",
        "type": "string",
        "description": "When deployed from a Databricks Git folder, the absolute workspace path of that folder; empty for local deploys."
      },
      {
        "name": "root_path",
        "type": "string",
        "description": "Absolute workspace path of the deployment root — the base path the deployed files live under. Mirrors workspace.root_path in the DABs bundle config; file_path is its files subdirectory."
      },
      {
        "name": "source_linked",
        "type": "boolean",
        "description": "Whether files are served directly from the source sync root instead of being copied into file_path."
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
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a deployment by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-show_deleted"><code>show_deleted</code></a></td>
    <td>Lists deployments in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-deployment"><code>deployment</code></a></td>
    <td></td>
    <td>Creates a new deployment in the workspace.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-deployment"><code>deployment</code></a></td>
    <td></td>
    <td>Updates a deployment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a deployment.</td>
</tr>
<tr>
    <td><a href="#heartbeat"><CopyableCode code="heartbeat" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Sends a heartbeat to renew the lock held by a version.</td>
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
    <td>The `deployment_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;`). The version whose lock to renew. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The fields to update; supported paths are ``display_name``, ``deployment_mode``, ``target_name``, and ``workspace_info``. An empty mask or any other path returns INVALID_PARAMETER_VALUE.</td>
</tr>
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td>The `version_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;`). The version whose lock to renew. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 20 deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListDeployments`` call. Provide this to retrieve the subsequent page.</td>
</tr>
<tr id="parameter-show_deleted">
    <td><CopyableCode code="show_deleted" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include soft-deleted deployments in the response. Defaults to false. When true, returns both live and soft-deleted deployments visible to the caller, subject to the filter. Soft-deleted deployments have status ``DEPLOYMENT_STATUS_DELETED``.</td>
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

Retrieves a deployment by its resource name.

```sql
SELECT
name,
last_successful_version_id,
last_version_id,
display_name,
target_name,
create_time,
created_by,
deployment_mode,
destroy_time,
destroyed_by,
git_info,
initial_parent_path,
status,
update_time,
updated_by,
workspace_info
FROM databricks_workspace.bundledeployments.deployments
WHERE deployment_id = '{{ deployment_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists deployments in the workspace.

```sql
SELECT
name,
last_successful_version_id,
last_version_id,
display_name,
target_name,
create_time,
created_by,
deployment_mode,
destroy_time,
destroyed_by,
git_info,
initial_parent_path,
status,
update_time,
updated_by,
workspace_info
FROM databricks_workspace.bundledeployments.deployments
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a new deployment in the workspace.

```sql
INSERT INTO databricks_workspace.bundledeployments.deployments (
deployment,
deployment_name,
workspace_domain
)
SELECT 
'{{ deployment }}' /* required */,
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
last_successful_version_id,
last_version_id,
display_name,
target_name,
create_time,
created_by,
deployment_mode,
destroy_time,
destroyed_by,
git_info,
initial_parent_path,
status,
update_time,
updated_by,
workspace_info
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployments
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the deployments resource.
    - name: deployment
      description: |
        The deployment to create. \`\`initial_parent_path\`\` is required. \`\`display_name\`\`, \`\`target_name\`\`, \`\`deployment_mode\`\`, and \`\`workspace_info\`\` may be set; every other field is assigned by the service and ignored on input.
      value:
        create_time: "{{ create_time }}"
        created_by: "{{ created_by }}"
        deployment_mode: "{{ deployment_mode }}"
        destroy_time: "{{ destroy_time }}"
        destroyed_by: "{{ destroyed_by }}"
        display_name: "{{ display_name }}"
        git_info:
          branch: "{{ branch }}"
          commit: "{{ commit }}"
          origin_url: "{{ origin_url }}"
        initial_parent_path: "{{ initial_parent_path }}"
        last_successful_version_id: "{{ last_successful_version_id }}"
        last_version_id: "{{ last_version_id }}"
        name: "{{ name }}"
        status: "{{ status }}"
        target_name: "{{ target_name }}"
        update_time: "{{ update_time }}"
        updated_by: "{{ updated_by }}"
        workspace_info:
          bundle_root_path: "{{ bundle_root_path }}"
          file_path: "{{ file_path }}"
          git_folder_path: "{{ git_folder_path }}"
          root_path: "{{ root_path }}"
          source_linked: {{ source_linked }}
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

Updates a deployment.

```sql
UPDATE databricks_workspace.bundledeployments.deployments
SET 
deployment = '{{ deployment }}'
WHERE 
deployment_id = '{{ deployment_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND deployment = '{{ deployment }}' --required
RETURNING
name,
last_successful_version_id,
last_version_id,
display_name,
target_name,
create_time,
created_by,
deployment_mode,
destroy_time,
destroyed_by,
git_info,
initial_parent_path,
status,
update_time,
updated_by,
workspace_info;
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

Deletes a deployment.

```sql
DELETE FROM databricks_workspace.bundledeployments.deployments
WHERE deployment_id = '{{ deployment_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="heartbeat"
    values={[
        { label: 'heartbeat', value: 'heartbeat' }
    ]}
>
<TabItem value="heartbeat">

Sends a heartbeat to renew the lock held by a version.

```sql
EXEC databricks_workspace.bundledeployments.deployments.heartbeat 
@deployment_id='{{ deployment_id }}' --required, 
@version_id='{{ version_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
