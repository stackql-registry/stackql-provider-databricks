---
title: postgres_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_projects
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

Creates, updates, deletes, gets or lists a <code>postgres_projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_projects" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_projects" /></td></tr>
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
    "description": "Output only. The full resource path of the project. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "project_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "delete_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was soft-deleted. Empty if the project is not deleted, otherwise set to a timestamp in the past."
  },
  {
    "name": "initial_branch_spec",
    "type": "object",
    "description": "Configuration for the initial default branch created as part of project creation. Allows overriding branch protection. These settings only apply at creation time and do not affect resources created after project creation.",
    "children": [
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the initial default branch should be protected from deletion."
      }
    ]
  },
  {
    "name": "initial_endpoint_spec",
    "type": "object",
    "description": "Configuration settings for the initial Read/Write endpoint created inside the initial branch for a newly created project. If omitted, the initial endpoint created will have default settings, without high availability configured. This field does not apply to any endpoints created after project creation. Use spec.default_endpoint_settings to configure default settings for endpoints created after project creation.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units for the initial endpoint."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units for the initial endpoint."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for HA configuration of the endpoint.",
        "children": [
          {
            "name": "min",
            "type": "integer",
            "description": ""
          },
          {
            "name": "max",
            "type": "integer",
            "description": "The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an endpoint group, set disabled to true on the EndpointSpec."
          },
          {
            "name": "enable_readable_secondaries",
            "type": "boolean",
            "description": "Whether to allow read-only connections to read-write endpoints. Only relevant for read-write endpoints where size.max &gt; 1."
          }
        ]
      },
      {
        "name": "no_suspension",
        "type": "boolean",
        "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the initial endpoint is automatically suspended. If specified, should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
      }
    ]
  },
  {
    "name": "purge_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project is scheduled for permanent deletion. Empty if the project is not deleted, otherwise set to a timestamp in the future."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the project configuration, including display_name, pg_version (Postgres version), history_retention_duration, and default_endpoint_settings.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "Custom tags to associate with the project. Forwarded to LBM for billing and cost tracking. To update tags, provide the new tag list and include \"spec.custom_tags\" in the update_mask. To clear all tags, provide an empty list and include \"spec.custom_tags\" in the update_mask. To preserve existing tags, omit this field from the update_mask (or use wildcard \"*\" which auto-excludes empty tags).",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path for the default branch of the project Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "Human-readable project name. Length should be between 1 and 256 characters."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project. Defaults to false."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The number of seconds to retain the shared history for point in time recovery for all branches in this project. Value should be between 172800s (2 days) and 3024000s (35 days)."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The major Postgres version number. The set of supported versions may vary; consult the API documentation for currently accepted values."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Project.",
    "children": [
      {
        "name": "branch_logical_size_limit_bytes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": "The budget policy that is applied to the project."
      },
      {
        "name": "compute_last_active_time",
        "type": "string (date-time)",
        "description": "The most recent time when any endpoint of this project was active."
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "The effective custom tags associated with the project.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path of the default branch of the project"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "The effective human-readable project name."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The effective number of seconds to retain the shared history for point in time recovery."
      },
      {
        "name": "owner",
        "type": "string",
        "description": "The email of the project owner."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The effective major Postgres version number."
      },
      {
        "name": "project_id",
        "type": "string",
        "description": "Part of the resource name."
      },
      {
        "name": "synthetic_storage_size_bytes",
        "type": "integer",
        "description": "The current space occupied by the project in storage."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the project."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the project. Format: projects/&#123;project_id&#125;"
  },
  {
    "name": "project_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "delete_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was soft-deleted. Empty if the project is not deleted, otherwise set to a timestamp in the past."
  },
  {
    "name": "initial_branch_spec",
    "type": "object",
    "description": "Configuration for the initial default branch created as part of project creation. Allows overriding branch protection. These settings only apply at creation time and do not affect resources created after project creation.",
    "children": [
      {
        "name": "is_protected",
        "type": "boolean",
        "description": "Whether the initial default branch should be protected from deletion."
      }
    ]
  },
  {
    "name": "initial_endpoint_spec",
    "type": "object",
    "description": "Configuration settings for the initial Read/Write endpoint created inside the initial branch for a newly created project. If omitted, the initial endpoint created will have default settings, without high availability configured. This field does not apply to any endpoints created after project creation. Use spec.default_endpoint_settings to configure default settings for endpoints created after project creation.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units for the initial endpoint."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units for the initial endpoint."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for HA configuration of the endpoint.",
        "children": [
          {
            "name": "min",
            "type": "integer",
            "description": ""
          },
          {
            "name": "max",
            "type": "integer",
            "description": "The maximum number of computes in the endpoint group. Currently, this must be equal to min. Set to 1 for single compute endpoints, to disable HA. To manually suspend all computes in an endpoint group, set disabled to true on the EndpointSpec."
          },
          {
            "name": "enable_readable_secondaries",
            "type": "boolean",
            "description": "Whether to allow read-only connections to read-write endpoints. Only relevant for read-write endpoints where size.max &gt; 1."
          }
        ]
      },
      {
        "name": "no_suspension",
        "type": "boolean",
        "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the initial endpoint is automatically suspended. If specified, should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
      }
    ]
  },
  {
    "name": "purge_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project is scheduled for permanent deletion. Empty if the project is not deleted, otherwise set to a timestamp in the future."
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the project configuration, including display_name, pg_version (Postgres version), history_retention_duration, and default_endpoint_settings.",
    "children": [
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": ""
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "Custom tags to associate with the project. Forwarded to LBM for billing and cost tracking. To update tags, provide the new tag list and include \"spec.custom_tags\" in the update_mask. To clear all tags, provide an empty list and include \"spec.custom_tags\" in the update_mask. To preserve existing tags, omit this field from the update_mask (or use wildcard \"*\" which auto-excludes empty tags).",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path for the default branch of the project Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "Human-readable project name. Length should be between 1 and 256 characters."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project. Defaults to false."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The number of seconds to retain the shared history for point in time recovery for all branches in this project. Value should be between 172800s (2 days) and 3024000s (35 days)."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The major Postgres version number. The set of supported versions may vary; consult the API documentation for currently accepted values."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The current status of a Project.",
    "children": [
      {
        "name": "branch_logical_size_limit_bytes",
        "type": "integer",
        "description": ""
      },
      {
        "name": "budget_policy_id",
        "type": "string",
        "description": "The budget policy that is applied to the project."
      },
      {
        "name": "compute_last_active_time",
        "type": "string (date-time)",
        "description": "The most recent time when any endpoint of this project was active."
      },
      {
        "name": "custom_tags",
        "type": "array",
        "description": "The effective custom tags associated with the project.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the custom tag."
          }
        ]
      },
      {
        "name": "default_branch",
        "type": "string",
        "description": "The full resource path of the default branch of the project"
      },
      {
        "name": "default_endpoint_settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "autoscaling_limit_max_cu",
            "type": "number",
            "description": "The maximum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "autoscaling_limit_min_cu",
            "type": "number",
            "description": "The minimum number of Compute Units. Minimum value is 0.5."
          },
          {
            "name": "no_suspension",
            "type": "boolean",
            "description": "When set to true, explicitly disables automatic suspension (never suspend). Should be set to true when provided. Mutually exclusive with ``suspend_timeout_duration``."
          },
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          },
          {
            "name": "suspend_timeout_duration",
            "type": "string",
            "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
          }
        ]
      },
      {
        "name": "display_name",
        "type": "string",
        "description": "The effective human-readable project name."
      },
      {
        "name": "enable_pg_native_login",
        "type": "boolean",
        "description": "Whether to enable PG native password login on all endpoints in this project."
      },
      {
        "name": "history_retention_duration",
        "type": "string",
        "description": "The effective number of seconds to retain the shared history for point in time recovery."
      },
      {
        "name": "owner",
        "type": "string",
        "description": "The email of the project owner."
      },
      {
        "name": "pg_version",
        "type": "integer",
        "description": "The effective major Postgres version number."
      },
      {
        "name": "project_id",
        "type": "string",
        "description": "Part of the resource name."
      },
      {
        "name": "synthetic_storage_size_bytes",
        "type": "integer",
        "description": "The current space occupied by the project in storage."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the project."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the project was last updated."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information about the specified database project.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-show_deleted"><code>show_deleted</code></a></td>
    <td>Returns a paginated list of database projects in the workspace that the user has permission to access.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-project"><code>project</code></a></td>
    <td></td>
    <td>Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-project"><code>project</code></a></td>
    <td></td>
    <td>Updates the specified database project.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-purge"><code>purge</code></a></td>
    <td>Deletes the specified database project.</td>
</tr>
<tr>
    <td><a href="#undelete"><CopyableCode code="undelete" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Undeletes a soft-deleted project.</td>
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
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;`). The full resource path of the project to undelete. Format: projects/&#123;project_id&#125;</td>
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
    <td>Upper bound for items returned. Cannot be negative. The maximum value is 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-purge">
    <td><CopyableCode code="purge" /></td>
    <td><code>boolean</code></td>
    <td>If true, permanently deletes the project (hard delete). If false or unset, performs a soft delete.</td>
</tr>
<tr id="parameter-show_deleted">
    <td><CopyableCode code="show_deleted" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include soft-deleted projects in the response. When true, soft-deleted projects are included alongside active projects. Hard-deleted and already-purged projects are never returned.</td>
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

Retrieves information about the specified database project.

```sql
SELECT
name,
project_id,
create_time,
delete_time,
initial_branch_spec,
initial_endpoint_spec,
purge_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_projects
WHERE project_id = '{{ project_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of database projects in the workspace that the user has permission to access.

```sql
SELECT
name,
project_id,
create_time,
delete_time,
initial_branch_spec,
initial_endpoint_spec,
purge_time,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_projects
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

Creates a new Lakebase Autoscaling Postgres database project, which contains branches and compute

```sql
INSERT INTO databricks_workspace.postgres.postgres_projects (
project,
project_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ project }}' /* required */,
'{{ project_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_projects
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_projects resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_projects resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_projects resource.
    - name: project
      description: |
        The Project to create.
      value:
        create_time: "{{ create_time }}"
        delete_time: "{{ delete_time }}"
        initial_branch_spec:
          is_protected: {{ is_protected }}
        initial_endpoint_spec:
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          no_suspension: {{ no_suspension }}
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        name: "{{ name }}"
        project_id: "{{ project_id }}"
        purge_time: "{{ purge_time }}"
        spec:
          budget_policy_id: "{{ budget_policy_id }}"
          custom_tags:
            - key: "{{ key }}"
              value: "{{ value }}"
          default_branch: "{{ default_branch }}"
          default_endpoint_settings:
            autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
            autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
            no_suspension: {{ no_suspension }}
            pg_settings: "{{ pg_settings }}"
            suspend_timeout_duration: "{{ suspend_timeout_duration }}"
          display_name: "{{ display_name }}"
          enable_pg_native_login: {{ enable_pg_native_login }}
          history_retention_duration: "{{ history_retention_duration }}"
          pg_version: {{ pg_version }}
        status:
          branch_logical_size_limit_bytes: {{ branch_logical_size_limit_bytes }}
          budget_policy_id: "{{ budget_policy_id }}"
          compute_last_active_time: "{{ compute_last_active_time }}"
          custom_tags:
            - key: "{{ key }}"
              value: "{{ value }}"
          default_branch: "{{ default_branch }}"
          default_endpoint_settings:
            autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
            autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
            no_suspension: {{ no_suspension }}
            pg_settings: "{{ pg_settings }}"
            suspend_timeout_duration: "{{ suspend_timeout_duration }}"
          display_name: "{{ display_name }}"
          enable_pg_native_login: {{ enable_pg_native_login }}
          history_retention_duration: "{{ history_retention_duration }}"
          owner: "{{ owner }}"
          pg_version: {{ pg_version }}
          project_id: "{{ project_id }}"
          synthetic_storage_size_bytes: {{ synthetic_storage_size_bytes }}
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
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

Updates the specified database project.

```sql
UPDATE databricks_workspace.postgres.postgres_projects
SET 
project = '{{ project }}'
WHERE 
project_id = '{{ project_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND project = '{{ project }}' --required;
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

Deletes the specified database project.

```sql
DELETE FROM databricks_workspace.postgres.postgres_projects
WHERE project_id = '{{ project_id }}' --required
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

Undeletes a soft-deleted project.

```sql
EXEC databricks_workspace.postgres.postgres_projects.undelete 
@project_id='{{ project_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
