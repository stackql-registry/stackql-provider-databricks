---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.bundledeployments.versions" /></td></tr>
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
    "description": "Resource name of the version. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;"
  },
  {
    "name": "previous_version_id",
    "type": "string",
    "description": "The version_id this version was created on top of — the deployment's most recent version at creation time. Leave unset when creating the first version (the deployment has no prior versions). Set by the client on creation and immutable thereafter. Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's current most-recent version (and to be unset when the deployment has no versions) and returns ``INVALID_PARAMETER_VALUE`` on mismatch, so a deploy racing against a concurrent deploy is rejected rather than silently overwriting it."
  },
  {
    "name": "version_id",
    "type": "string",
    "description": "Version identifier within the parent deployment, assigned by the client on creation. A numeric string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version IDs are strictly increasing within a deployment but are not required to start at 1 or to be contiguous."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name for the deployment, captured at the time of this version. Up to 256 characters. When present, creating the version updates the deployment display name. An empty value clears it; an absent value leaves the current deployment display name unchanged."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "Target name of the deployment, captured at the time of this version."
  },
  {
    "name": "cli_version",
    "type": "string",
    "description": "CLI version used to initiate the version."
  },
  {
    "name": "complete_time",
    "type": "string (date-time)",
    "description": "When the version completed. Unset while the version is in progress."
  },
  {
    "name": "completed_by",
    "type": "string",
    "description": "The user who completed the version (email or principal name). May differ from ``created_by`` when another user force-completes the version."
  },
  {
    "name": "completion_reason",
    "type": "string",
    "description": "Why the version was completed. Unset while in progress. Set when status transitions to COMPLETED. (VERSION_COMPLETE_FAILURE, VERSION_COMPLETE_FORCE_ABORT, VERSION_COMPLETE_LEASE_EXPIRED, VERSION_COMPLETE_SUCCESS)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the version was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the version (email or principal name)."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production), captured at the time of this version. (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the source, captured at the time of this version.",
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
    "name": "operations",
    "type": "array",
    "description": "The full operation plan for this version: one PENDING operation per entry, recorded in the same transaction. Input only -- supplied on create and never returned by create/get/list; read the recorded operations via ListOperations.",
    "children": [
      {
        "name": "resource_key",
        "type": "string",
        "description": "The key identifying the resource this operation applies to (e.g. \"jobs.foo\", \"pipelines.bar\"). Becomes the final component of the operation's name and must be unique among the operations in the version."
      },
      {
        "name": "action_type",
        "type": "string",
        "description": "The type of operation planned for this resource. (OPERATION_ACTION_TYPE_BIND, OPERATION_ACTION_TYPE_BIND_AND_UPDATE, OPERATION_ACTION_TYPE_CREATE, OPERATION_ACTION_TYPE_DELETE, OPERATION_ACTION_TYPE_INITIAL_REGISTER, OPERATION_ACTION_TYPE_RECREATE, OPERATION_ACTION_TYPE_RESIZE, OPERATION_ACTION_TYPE_UNBIND, OPERATION_ACTION_TYPE_UPDATE, OPERATION_ACTION_TYPE_UPDATE_WITH_ID)"
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the version: IN_PROGRESS or COMPLETED. (VERSION_STATUS_COMPLETED, VERSION_STATUS_IN_PROGRESS)"
  },
  {
    "name": "version_type",
    "type": "string",
    "description": "Type of version (deploy or destroy). (VERSION_TYPE_DEPLOY, VERSION_TYPE_DESTROY)"
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment, captured at the time of this version.",
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
    "description": "Resource name of the version. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;"
  },
  {
    "name": "previous_version_id",
    "type": "string",
    "description": "The version_id this version was created on top of — the deployment's most recent version at creation time. Leave unset when creating the first version (the deployment has no prior versions). Set by the client on creation and immutable thereafter. Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's current most-recent version (and to be unset when the deployment has no versions) and returns ``INVALID_PARAMETER_VALUE`` on mismatch, so a deploy racing against a concurrent deploy is rejected rather than silently overwriting it."
  },
  {
    "name": "version_id",
    "type": "string",
    "description": "Version identifier within the parent deployment, assigned by the client on creation. A numeric string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version IDs are strictly increasing within a deployment but are not required to start at 1 or to be contiguous."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name for the deployment, captured at the time of this version. Up to 256 characters. When present, creating the version updates the deployment display name. An empty value clears it; an absent value leaves the current deployment display name unchanged."
  },
  {
    "name": "target_name",
    "type": "string",
    "description": "Target name of the deployment, captured at the time of this version."
  },
  {
    "name": "cli_version",
    "type": "string",
    "description": "CLI version used to initiate the version."
  },
  {
    "name": "complete_time",
    "type": "string (date-time)",
    "description": "When the version completed. Unset while the version is in progress."
  },
  {
    "name": "completed_by",
    "type": "string",
    "description": "The user who completed the version (email or principal name). May differ from ``created_by`` when another user force-completes the version."
  },
  {
    "name": "completion_reason",
    "type": "string",
    "description": "Why the version was completed. Unset while in progress. Set when status transitions to COMPLETED. (VERSION_COMPLETE_FAILURE, VERSION_COMPLETE_FORCE_ABORT, VERSION_COMPLETE_LEASE_EXPIRED, VERSION_COMPLETE_SUCCESS)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the version was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The user who created the version (email or principal name)."
  },
  {
    "name": "deployment_mode",
    "type": "string",
    "description": "Bundle target deployment mode (development or production), captured at the time of this version. (DEPLOYMENT_MODE_DEVELOPMENT, DEPLOYMENT_MODE_PRODUCTION)"
  },
  {
    "name": "git_info",
    "type": "object",
    "description": "Git provenance of the source, captured at the time of this version.",
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
    "name": "operations",
    "type": "array",
    "description": "The full operation plan for this version: one PENDING operation per entry, recorded in the same transaction. Input only -- supplied on create and never returned by create/get/list; read the recorded operations via ListOperations.",
    "children": [
      {
        "name": "resource_key",
        "type": "string",
        "description": "The key identifying the resource this operation applies to (e.g. \"jobs.foo\", \"pipelines.bar\"). Becomes the final component of the operation's name and must be unique among the operations in the version."
      },
      {
        "name": "action_type",
        "type": "string",
        "description": "The type of operation planned for this resource. (OPERATION_ACTION_TYPE_BIND, OPERATION_ACTION_TYPE_BIND_AND_UPDATE, OPERATION_ACTION_TYPE_CREATE, OPERATION_ACTION_TYPE_DELETE, OPERATION_ACTION_TYPE_INITIAL_REGISTER, OPERATION_ACTION_TYPE_RECREATE, OPERATION_ACTION_TYPE_RESIZE, OPERATION_ACTION_TYPE_UNBIND, OPERATION_ACTION_TYPE_UPDATE, OPERATION_ACTION_TYPE_UPDATE_WITH_ID)"
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "Status of the version: IN_PROGRESS or COMPLETED. (VERSION_STATUS_COMPLETED, VERSION_STATUS_IN_PROGRESS)"
  },
  {
    "name": "version_type",
    "type": "string",
    "description": "Type of version (deploy or destroy). (VERSION_TYPE_DEPLOY, VERSION_TYPE_DESTROY)"
  },
  {
    "name": "workspace_info",
    "type": "object",
    "description": "Workspace location of the deployment, captured at the time of this version.",
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
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a version by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists versions under a deployment, ordered numerically by version_id descending (most recent first).</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-cli_version"><code>cli_version</code></a>, <a href="#parameter-version_type"><code>version_type</code></a></td>
    <td></td>
    <td>Creates a new version under a deployment.</td>
</tr>
<tr>
    <td><a href="#complete"><CopyableCode code="complete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_id"><code>deployment_id</code></a>, <a href="#parameter-version_id"><code>version_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-completion_reason"><code>completion_reason</code></a></td>
    <td></td>
    <td>Marks a version as complete and releases the deployment lock.</td>
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
    <td>The `deployment_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;`). The name of the version to complete. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-version_id">
    <td><CopyableCode code="version_id" /></td>
    <td><code>string</code></td>
    <td>The `version_id` segment of the `name` resource name (`deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;`). The name of the version to complete. Format: deployments/&#123;deployment_id&#125;/versions/&#123;version_id&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 20 versions will be returned. The maximum value is 100; values above 100 will be coerced to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListVersions`` call. Provide this to retrieve the subsequent page.</td>
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

Retrieves a version by its resource name.

```sql
SELECT
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
operations,
status,
version_type,
workspace_info
FROM databricks_workspace.bundledeployments.versions
WHERE deployment_id = '{{ deployment_id }}' -- required
AND version_id = '{{ version_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists versions under a deployment, ordered numerically by version_id descending (most recent first).

```sql
SELECT
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
operations,
status,
version_type,
workspace_info
FROM databricks_workspace.bundledeployments.versions
WHERE deployment_id = '{{ deployment_id }}' -- required
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

Creates a new version under a deployment.

```sql
INSERT INTO databricks_workspace.bundledeployments.versions (
cli_version,
version_type,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
display_name,
git_info,
name,
operations,
previous_version_id,
status,
target_name,
version_id,
workspace_info,
deployment_id,
version_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ cli_version }}' /* required */,
'{{ version_type }}' /* required */,
'{{ complete_time }}',
'{{ completed_by }}',
'{{ completion_reason }}',
'{{ create_time }}',
'{{ created_by }}',
'{{ deployment_mode }}',
'{{ display_name }}',
'{{ git_info }}',
'{{ name }}',
'{{ operations }}',
'{{ previous_version_id }}',
'{{ status }}',
'{{ target_name }}',
'{{ version_id }}',
'{{ workspace_info }}',
'{{ deployment_id }}',
'{{ version_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
previous_version_id,
version_id,
display_name,
target_name,
cli_version,
complete_time,
completed_by,
completion_reason,
create_time,
created_by,
deployment_mode,
git_info,
operations,
status,
version_type,
workspace_info
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: versions
  props:
    - name: deployment_id
      value: "{{ deployment_id }}"
      description: Required parameter for the versions resource.
    - name: version_id
      value: "{{ version_id }}"
      description: Required parameter for the versions resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the versions resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the versions resource.
    - name: cli_version
      value: "{{ cli_version }}"
      description: |
        CLI version used to initiate the version.
    - name: version_type
      value: "{{ version_type }}"
      description: |
        Type of version (deploy or destroy).
    - name: complete_time
      value: "{{ complete_time }}"
      description: |
        When the version completed. Unset while the version is in progress.
    - name: completed_by
      value: "{{ completed_by }}"
      description: |
        The user who completed the version (email or principal name). May differ from \`\`created_by\`\` when another user force-completes the version.
    - name: completion_reason
      value: "{{ completion_reason }}"
      description: |
        Why the version was completed. Unset while in progress. Set when status transitions to COMPLETED.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        When the version was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        The user who created the version (email or principal name).
    - name: deployment_mode
      value: "{{ deployment_mode }}"
      description: |
        Bundle target deployment mode (development or production), captured at the time of this version.
    - name: display_name
      value: "{{ display_name }}"
      description: |
        Display name for the deployment, captured at the time of this version. Up to 256 characters. When present, creating the version updates the deployment display name. An empty value clears it; an absent value leaves the current deployment display name unchanged.
    - name: git_info
      description: |
        Git provenance of the source, captured at the time of this version.
      value:
        branch: "{{ branch }}"
        commit: "{{ commit }}"
        origin_url: "{{ origin_url }}"
    - name: name
      value: "{{ name }}"
      description: |
        Resource name of the version. Format: deployments/{deployment_id}/versions/{version_id}
    - name: operations
      description: |
        The full operation plan for this version: one PENDING operation per entry, recorded in the same transaction. Input only -- supplied on create and never returned by create/get/list; read the recorded operations via ListOperations.
      value:
        - resource_key: "{{ resource_key }}"
          action_type: "{{ action_type }}"
    - name: previous_version_id
      value: "{{ previous_version_id }}"
      description: |
        The version_id this version was created on top of — the deployment's most recent version at creation time. Leave unset when creating the first version (the deployment has no prior versions). Set by the client on creation and immutable thereafter. Acts as an optimistic-concurrency precondition: the server requires it to equal the deployment's current most-recent version (and to be unset when the deployment has no versions) and returns \`\`INVALID_PARAMETER_VALUE\`\` on mismatch, so a deploy racing against a concurrent deploy is rejected rather than silently overwriting it.
    - name: status
      value: "{{ status }}"
      description: |
        Status of the version: IN_PROGRESS or COMPLETED.
    - name: target_name
      value: "{{ target_name }}"
      description: |
        Target name of the deployment, captured at the time of this version.
    - name: version_id
      value: "{{ version_id }}"
      description: |
        Version identifier within the parent deployment, assigned by the client on creation. A numeric string (base-10, fits in a signed 64-bit integer) that is greater than or equal to 1. Version IDs are strictly increasing within a deployment but are not required to start at 1 or to be contiguous.
    - name: workspace_info
      description: |
        Workspace location of the deployment, captured at the time of this version.
      value:
        bundle_root_path: "{{ bundle_root_path }}"
        file_path: "{{ file_path }}"
        git_folder_path: "{{ git_folder_path }}"
        root_path: "{{ root_path }}"
        source_linked: {{ source_linked }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="complete"
    values={[
        { label: 'complete', value: 'complete' }
    ]}
>
<TabItem value="complete">

Marks a version as complete and releases the deployment lock.

```sql
EXEC databricks_workspace.bundledeployments.versions.complete 
@deployment_id='{{ deployment_id }}' --required, 
@version_id='{{ version_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"completion_reason": "{{ completion_reason }}", 
"force": {{ force }}
}'
;
```
</TabItem>
</Tabs>
