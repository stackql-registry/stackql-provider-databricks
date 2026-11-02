---
title: workspace_base_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_base_environments
  - environments
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

Creates, updates, deletes, gets or lists a <code>workspace_base_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="workspace_base_environments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.environments.workspace_base_environments" /></td></tr>
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
    "description": "The resource name of the workspace base environment. Format: workspace-base-environments/&#123;workspace-base-environment&#125;"
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "User ID of the creator."
  },
  {
    "name": "last_updated_user_id",
    "type": "string",
    "description": "User ID of the last user who updated the environment."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display name for the workspace base environment."
  },
  {
    "name": "base_environment_type",
    "type": "string",
    "description": "The type of base environment (CPU or GPU). (CPU, GPU)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when the environment was created."
  },
  {
    "name": "filepath",
    "type": "string",
    "description": "The WSFS or UC Volumes path to the environment YAML file."
  },
  {
    "name": "is_default",
    "type": "boolean",
    "description": "Whether this is the default environment for the workspace."
  },
  {
    "name": "message",
    "type": "string",
    "description": "Status message providing additional details about the environment status."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The environment specification containing version and dependencies.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "List of pip dependencies, as supported by the version of pip in this environment. Each dependency is a valid pip requirements file line per https://pip.pypa.io/en/stable/reference/requirements-file-format/. Allowed dependencies include a requirement specifier, an archive URL, a local project path (such as WSFS or UC Volumes in Databricks), or a VCS project URL."
      },
      {
        "name": "environment_version",
        "type": "string",
        "description": "Environment version used by the environment. Each version comes with a specific Python version and a set of Python packages. The version is a string, consisting of an integer."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "The status of the materialized workspace base environment. (CREATED, EXPIRED, FAILED, INVALID, PENDING, REFRESHING)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Timestamp when the environment was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the workspace base environment. Format: workspace-base-environments/&#123;workspace-base-environment&#125;"
  },
  {
    "name": "creator_user_id",
    "type": "string",
    "description": "User ID of the creator."
  },
  {
    "name": "last_updated_user_id",
    "type": "string",
    "description": "User ID of the last user who updated the environment."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display name for the workspace base environment."
  },
  {
    "name": "base_environment_type",
    "type": "string",
    "description": "The type of base environment (CPU or GPU). (CPU, GPU)"
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when the environment was created."
  },
  {
    "name": "filepath",
    "type": "string",
    "description": "The WSFS or UC Volumes path to the environment YAML file."
  },
  {
    "name": "is_default",
    "type": "boolean",
    "description": "Whether this is the default environment for the workspace."
  },
  {
    "name": "message",
    "type": "string",
    "description": "Status message providing additional details about the environment status."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The environment specification containing version and dependencies.",
    "children": [
      {
        "name": "dependencies",
        "type": "array",
        "description": "List of pip dependencies, as supported by the version of pip in this environment. Each dependency is a valid pip requirements file line per https://pip.pypa.io/en/stable/reference/requirements-file-format/. Allowed dependencies include a requirement specifier, an archive URL, a local project path (such as WSFS or UC Volumes in Databricks), or a VCS project URL."
      },
      {
        "name": "environment_version",
        "type": "string",
        "description": "Environment version used by the environment. Each version comes with a specific Python version and a set of Python packages. The version is a string, consisting of an integer."
      }
    ]
  },
  {
    "name": "status",
    "type": "string",
    "description": "The status of the materialized workspace base environment. (CREATED, EXPIRED, FAILED, INVALID, PENDING, REFRESHING)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Timestamp when the environment was last updated."
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
    <td><a href="#parameter-workspace_base_environment"><code>workspace_base_environment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves a WorkspaceBaseEnvironment by its name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all WorkspaceBaseEnvironments in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-display_name"><code>display_name</code></a></td>
    <td><a href="#parameter-request_id"><code>request_id</code></a>, <a href="#parameter-workspace_base_environment_id"><code>workspace_base_environment_id</code></a></td>
    <td>Creates a new WorkspaceBaseEnvironment. This is a long-running operation. The operation will</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workspace_base_environment"><code>workspace_base_environment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Updates an existing WorkspaceBaseEnvironment. This is a long-running operation. The operation will</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workspace_base_environment"><code>workspace_base_environment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a WorkspaceBaseEnvironment. Deleting a base environment may impact linked notebooks and jobs.</td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-workspace_base_environment"><code>workspace_base_environment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Refreshes the materialized environment for a WorkspaceBaseEnvironment. This is a long-running</td>
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
<tr id="parameter-workspace_base_environment">
    <td><CopyableCode code="workspace_base_environment" /></td>
    <td><code>string</code></td>
    <td>The `workspace_base_environment` segment of the `name` resource name (`workspace-base-environments/&#123;workspace_base_environment&#125;`). Required. The resource name of the workspace base environment to delete. Format: workspace-base-environments/&#123;workspace_base_environment&#125;</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of environments to return per page. Default is 1000.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token for pagination. Received from a previous ListWorkspaceBaseEnvironments call.</td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for this request. A random UUID is recommended. This request is only idempotent if a request_id is provided.</td>
</tr>
<tr id="parameter-workspace_base_environment_id">
    <td><CopyableCode code="workspace_base_environment_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the workspace base environment, which will become the final component of the resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.</td>
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

Retrieves a WorkspaceBaseEnvironment by its name.

```sql
SELECT
name,
creator_user_id,
last_updated_user_id,
display_name,
base_environment_type,
create_time,
filepath,
is_default,
message,
spec,
status,
update_time
FROM databricks_workspace.environments.workspace_base_environments
WHERE workspace_base_environment = '{{ workspace_base_environment }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all WorkspaceBaseEnvironments in the workspace.

```sql
SELECT
name,
creator_user_id,
last_updated_user_id,
display_name,
base_environment_type,
create_time,
filepath,
is_default,
message,
spec,
status,
update_time
FROM databricks_workspace.environments.workspace_base_environments
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

Creates a new WorkspaceBaseEnvironment. This is a long-running operation. The operation will

```sql
INSERT INTO databricks_workspace.environments.workspace_base_environments (
display_name,
base_environment_type,
create_time,
creator_user_id,
filepath,
is_default,
last_updated_user_id,
message,
name,
spec,
status,
update_time,
deployment_name,
workspace_domain,
request_id,
workspace_base_environment_id
)
SELECT 
'{{ display_name }}' /* required */,
'{{ base_environment_type }}',
'{{ create_time }}',
'{{ creator_user_id }}',
'{{ filepath }}',
{{ is_default }},
'{{ last_updated_user_id }}',
'{{ message }}',
'{{ name }}',
'{{ spec }}',
'{{ status }}',
'{{ update_time }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ request_id }}',
'{{ workspace_base_environment_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: workspace_base_environments
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the workspace_base_environments resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the workspace_base_environments resource.
    - name: display_name
      value: "{{ display_name }}"
      description: |
        Human-readable display name for the workspace base environment.
    - name: base_environment_type
      value: "{{ base_environment_type }}"
      description: |
        The type of base environment (CPU or GPU).
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Timestamp when the environment was created.
    - name: creator_user_id
      value: "{{ creator_user_id }}"
      description: |
        User ID of the creator.
    - name: filepath
      value: "{{ filepath }}"
      description: |
        The WSFS or UC Volumes path to the environment YAML file.
    - name: is_default
      value: {{ is_default }}
      description: |
        Whether this is the default environment for the workspace.
    - name: last_updated_user_id
      value: "{{ last_updated_user_id }}"
      description: |
        User ID of the last user who updated the environment.
    - name: message
      value: "{{ message }}"
      description: |
        Status message providing additional details about the environment status.
    - name: name
      value: "{{ name }}"
      description: |
        The resource name of the workspace base environment. Format: workspace-base-environments/{workspace-base-environment}
    - name: spec
      description: |
        The environment specification containing version and dependencies.
      value:
        dependencies:
          - "{{ dependencies }}"
        environment_version: "{{ environment_version }}"
    - name: status
      value: "{{ status }}"
      description: |
        The status of the materialized workspace base environment.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Timestamp when the environment was last updated.
    - name: request_id
      value: "{{ request_id }}"
      description: A unique identifier for this request. A random UUID is recommended. This request is only idempotent if a request_id is provided.
      description: A unique identifier for this request. A random UUID is recommended. This request is only idempotent if a request_id is provided.
    - name: workspace_base_environment_id
      value: "{{ workspace_base_environment_id }}"
      description: The ID to use for the workspace base environment, which will become the final component of the resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.
      description: The ID to use for the workspace base environment, which will become the final component of the resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/.
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

Updates an existing WorkspaceBaseEnvironment. This is a long-running operation. The operation will

```sql
UPDATE databricks_workspace.environments.workspace_base_environments
SET 
-- No updatable properties
WHERE 
workspace_base_environment = '{{ workspace_base_environment }}' --required
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

Deletes a WorkspaceBaseEnvironment. Deleting a base environment may impact linked notebooks and jobs.

```sql
DELETE FROM databricks_workspace.environments.workspace_base_environments
WHERE workspace_base_environment = '{{ workspace_base_environment }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' }
    ]}
>
<TabItem value="refresh">

Refreshes the materialized environment for a WorkspaceBaseEnvironment. This is a long-running

```sql
EXEC databricks_workspace.environments.workspace_base_environments.refresh 
@workspace_base_environment='{{ workspace_base_environment }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
