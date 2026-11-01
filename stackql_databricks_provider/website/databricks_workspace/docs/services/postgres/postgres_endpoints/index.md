---
title: postgres_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_endpoints
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

Creates, updates, deletes, gets or lists a <code>postgres_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_endpoints" /></td></tr>
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
    "description": "Output only. The full resource path of the endpoint. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;"
  },
  {
    "name": "endpoint_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The branch containing this endpoint (API resource hierarchy). Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the compute endpoint configuration, including autoscaling limits, suspend timeout, and disabled state.",
    "children": [
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either ``read_write`` or ``read_only``. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units. The maximum value is 64. The difference between the minimum and maximum Compute Units (max - min) must not exceed 16."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units. Minimum value is 0.5."
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for optional HA configuration of the endpoint. If unspecified, the endpoint defaults to non HA settings, with a single compute backing the endpoint (and no readable secondaries for Read/Write endpoints).",
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
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current operational status of the compute endpoint.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": ""
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units."
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "endpoint_id",
        "type": "string",
        "description": "Part of the resource name."
      },
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either ``read_write`` or ``read_only``. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "group",
        "type": "object",
        "description": "Details on the HA configuration of the endpoint.",
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
            "description": "Whether read-only connections to read-write endpoints are allowed. Only relevant if read replicas are configured by specifying size.max &gt; 1."
          }
        ]
      },
      {
        "name": "hosts",
        "type": "object",
        "description": "Contains host information for connecting to the endpoint.",
        "children": [
          {
            "name": "host",
            "type": "string",
            "description": "The hostname to connect to this endpoint. For read-write endpoints, this is a read-write hostname which connects to the primary compute. For read-only endpoints, this is a read-only hostname which allows read-only operations."
          },
          {
            "name": "read_only_host",
            "type": "string",
            "description": "An optionally defined read-only host for the endpoint, without pooling. For read-only endpoints, this attribute is always defined and is equivalent to host. For read-write endpoints, this attribute is defined if the enclosing endpoint is a group with greater than 1 computes configured, and has readable secondaries enabled."
          },
          {
            "name": "read_only_pooled_host",
            "type": "string",
            "description": "The read-only hostname of the compute endpoint, with pooling. This attribute is always defined for read-only endpoints, and may be defined for read-write endpoints if configured with read replicas and allow read-only connections."
          },
          {
            "name": "read_write_pooled_host",
            "type": "string",
            "description": "The read-write hostname of the compute endpoint, with pooling. This attribute is only defined for read-write endpoints."
          }
        ]
      },
      {
        "name": "last_active_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the compute endpoint was last active."
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the endpoint."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute endpoint was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the endpoint. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;"
  },
  {
    "name": "endpoint_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The branch containing this endpoint (API resource hierarchy). Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the compute endpoint configuration, including autoscaling limits, suspend timeout, and disabled state.",
    "children": [
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either ``read_write`` or ``read_only``. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": "The maximum number of Compute Units. The maximum value is 64. The difference between the minimum and maximum Compute Units (max - min) must not exceed 16."
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units. Minimum value is 0.5."
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "group",
        "type": "object",
        "description": "Settings for optional HA configuration of the endpoint. If unspecified, the endpoint defaults to non HA settings, with a single compute backing the endpoint (and no readable secondaries for Read/Write endpoints).",
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
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended. If specified should be between 60s and 604800s (1 minute to 1 week). Mutually exclusive with ``no_suspension``."
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current operational status of the compute endpoint.",
    "children": [
      {
        "name": "autoscaling_limit_max_cu",
        "type": "number",
        "description": ""
      },
      {
        "name": "autoscaling_limit_min_cu",
        "type": "number",
        "description": "The minimum number of Compute Units."
      },
      {
        "name": "current_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "disabled",
        "type": "boolean",
        "description": "Whether to restrict connections to the compute endpoint. Enabling this option schedules a suspend compute operation. A disabled compute endpoint cannot be enabled by a connection or console action."
      },
      {
        "name": "endpoint_id",
        "type": "string",
        "description": "Part of the resource name."
      },
      {
        "name": "endpoint_type",
        "type": "string",
        "description": "The compute endpoint type. Either ``read_write`` or ``read_only``. (ENDPOINT_TYPE_READ_ONLY, ENDPOINT_TYPE_READ_WRITE)"
      },
      {
        "name": "group",
        "type": "object",
        "description": "Details on the HA configuration of the endpoint.",
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
            "description": "Whether read-only connections to read-write endpoints are allowed. Only relevant if read replicas are configured by specifying size.max &gt; 1."
          }
        ]
      },
      {
        "name": "hosts",
        "type": "object",
        "description": "Contains host information for connecting to the endpoint.",
        "children": [
          {
            "name": "host",
            "type": "string",
            "description": "The hostname to connect to this endpoint. For read-write endpoints, this is a read-write hostname which connects to the primary compute. For read-only endpoints, this is a read-only hostname which allows read-only operations."
          },
          {
            "name": "read_only_host",
            "type": "string",
            "description": "An optionally defined read-only host for the endpoint, without pooling. For read-only endpoints, this attribute is always defined and is equivalent to host. For read-write endpoints, this attribute is defined if the enclosing endpoint is a group with greater than 1 computes configured, and has readable secondaries enabled."
          },
          {
            "name": "read_only_pooled_host",
            "type": "string",
            "description": "The read-only hostname of the compute endpoint, with pooling. This attribute is always defined for read-only endpoints, and may be defined for read-write endpoints if configured with read replicas and allow read-only connections."
          },
          {
            "name": "read_write_pooled_host",
            "type": "string",
            "description": "The read-write hostname of the compute endpoint, with pooling. This attribute is only defined for read-write endpoints."
          }
        ]
      },
      {
        "name": "last_active_time",
        "type": "string (date-time)",
        "description": "A timestamp indicating when the compute endpoint was last active."
      },
      {
        "name": "pending_state",
        "type": "string",
        "description": "The state of the compute endpoint. (ACTIVE, DEGRADED, IDLE, INIT)"
      },
      {
        "name": "settings",
        "type": "object",
        "description": "A collection of settings for a compute endpoint.",
        "children": [
          {
            "name": "pg_settings",
            "type": "object",
            "description": "A raw representation of Postgres settings."
          }
        ]
      },
      {
        "name": "suspend_timeout_duration",
        "type": "string",
        "description": "Duration of inactivity after which the compute endpoint is automatically suspended."
      }
    ]
  },
  {
    "name": "uid",
    "type": "string",
    "description": "System-generated unique ID for the endpoint."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "A timestamp indicating when the compute endpoint was last updated."
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information about the specified compute endpoint, including its connection details and</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of compute endpoints in the branch.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-replace_existing"><code>replace_existing</code></a></td>
    <td>Creates a new compute endpoint in the branch.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Updates the specified compute endpoint. You can update autoscaling limits, suspend timeout, or</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-endpoint_id"><code>endpoint_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes the specified compute endpoint.</td>
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
    <td>The `branch_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;`). The full resource path of the endpoint to delete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-endpoint_id">
    <td><CopyableCode code="endpoint_id" /></td>
    <td><code>string</code></td>
    <td>The `endpoint_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;`). The full resource path of the endpoint to delete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;`). The full resource path of the endpoint to delete. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/endpoints/&#123;endpoint_id&#125;</td>
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
<tr id="parameter-replace_existing">
    <td><CopyableCode code="replace_existing" /></td>
    <td><code>boolean</code></td>
    <td>If true, update the endpoint if it already exists instead of returning an error.</td>
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

Retrieves information about the specified compute endpoint, including its connection details and

```sql
SELECT
name,
endpoint_id,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_endpoints
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
AND endpoint_id = '{{ endpoint_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of compute endpoints in the branch.

```sql
SELECT
name,
endpoint_id,
create_time,
parent,
spec,
status,
uid,
update_time
FROM databricks_workspace.postgres.postgres_endpoints
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
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

Creates a new compute endpoint in the branch.

```sql
INSERT INTO databricks_workspace.postgres.postgres_endpoints (
endpoint,
project_id,
branch_id,
endpoint_id,
deployment_name,
workspace_domain,
replace_existing
)
SELECT 
'{{ endpoint }}' /* required */,
'{{ project_id }}',
'{{ branch_id }}',
'{{ endpoint_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ replace_existing }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_endpoints
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_endpoints resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the postgres_endpoints resource.
    - name: endpoint_id
      value: "{{ endpoint_id }}"
      description: Required parameter for the postgres_endpoints resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_endpoints resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_endpoints resource.
    - name: endpoint
      description: |
        The Endpoint to create.
      value:
        create_time: "{{ create_time }}"
        endpoint_id: "{{ endpoint_id }}"
        name: "{{ name }}"
        parent: "{{ parent }}"
        spec:
          endpoint_type: "{{ endpoint_type }}"
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          disabled: {{ disabled }}
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          no_suspension: {{ no_suspension }}
          settings:
            pg_settings: "{{ pg_settings }}"
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        status:
          autoscaling_limit_max_cu: {{ autoscaling_limit_max_cu }}
          autoscaling_limit_min_cu: {{ autoscaling_limit_min_cu }}
          current_state: "{{ current_state }}"
          disabled: {{ disabled }}
          endpoint_id: "{{ endpoint_id }}"
          endpoint_type: "{{ endpoint_type }}"
          group:
            min: {{ min }}
            max: {{ max }}
            enable_readable_secondaries: {{ enable_readable_secondaries }}
          hosts:
            host: "{{ host }}"
            read_only_host: "{{ read_only_host }}"
            read_only_pooled_host: "{{ read_only_pooled_host }}"
            read_write_pooled_host: "{{ read_write_pooled_host }}"
          last_active_time: "{{ last_active_time }}"
          pending_state: "{{ pending_state }}"
          settings:
            pg_settings: "{{ pg_settings }}"
          suspend_timeout_duration: "{{ suspend_timeout_duration }}"
        uid: "{{ uid }}"
        update_time: "{{ update_time }}"
    - name: replace_existing
      value: {{ replace_existing }}
      description: If true, update the endpoint if it already exists instead of returning an error.
      description: If true, update the endpoint if it already exists instead of returning an error.
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

Updates the specified compute endpoint. You can update autoscaling limits, suspend timeout, or

```sql
UPDATE databricks_workspace.postgres.postgres_endpoints
SET 
endpoint = '{{ endpoint }}'
WHERE 
project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND endpoint_id = '{{ endpoint_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND endpoint = '{{ endpoint }}' --required;
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

Deletes the specified compute endpoint.

```sql
DELETE FROM databricks_workspace.postgres.postgres_endpoints
WHERE project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND endpoint_id = '{{ endpoint_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
