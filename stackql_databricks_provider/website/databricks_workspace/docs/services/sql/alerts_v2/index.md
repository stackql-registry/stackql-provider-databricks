---
title: alerts_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_v2
  - sql
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

Creates, updates, deletes, gets or lists an <code>alerts_v2</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts_v2" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sql.alerts_v2" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": "The canonical identifier of the alert to retrieve information about."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The run as username or application ID of service principal. On Create and Update, this field can be set to application ID of an active service principal. Setting this field requires the servicePrincipal/user role. Deprecated: Use ``run_as`` field instead. This field will be removed in a future release."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_description",
    "type": "string",
    "description": "Custom description for the alert. Interpreted according to ``custom_template_format``."
  },
  {
    "name": "custom_summary",
    "type": "string",
    "description": "Custom summary for the alert. Interpreted according to ``custom_template_format``."
  },
  {
    "name": "custom_template_format",
    "type": "string",
    "description": "The format used to interpret the ``custom_summary`` and ``custom_description`` templates. ``HTML`` treats both templates as HTML with Mustache ``&#123;&#123;VARIABLE_NAME&#125;&#125;`` placeholders. ``MARKDOWN`` treats them as Markdown with allowlisted ``@VARIABLE_NAME`` placeholders and converts them to the format each notification destination expects, so a single template renders correctly in email, Slack, and Microsoft Teams. When unset, the API applies no default. Responses omit the field unless a format is stored, and a template with no format is rendered as HTML. (HTML, MARKDOWN)"
  },
  {
    "name": "effective_run_as",
    "type": "object",
    "description": "The actual identity that will be used to execute the alert. This is an output-only field that shows the resolved run-as identity after applying permissions and defaults.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "evaluation",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "aggregation",
            "type": "string",
            "description": "If not set, the behavior is equivalent to using ``First row`` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
          },
          {
            "name": "display",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "comparison_operator",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NOT_NULL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Alert state if result is empty. Please avoid setting this field to be ``UNKNOWN`` because ``UNKNOWN`` state is planned to be deprecated. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "last_evaluated_at",
        "type": "string",
        "description": "Timestamp of the last evaluation."
      },
      {
        "name": "notification",
        "type": "object",
        "description": "User or Notification Destination to notify when alert is triggered.",
        "children": [
          {
            "name": "notify_on_ok",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "retrigger_seconds",
            "type": "integer",
            "description": "Number of seconds an alert waits after being triggered before it is allowed to send another notification. If set to 0 or omitted, the alert will not send any further notifications after the first trigger Setting this value to 1 allows the alert to send a notification on every evaluation where the condition is met, effectively making it always retrigger for notification purposes."
          },
          {
            "name": "subscriptions",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "destination_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "user_email",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "Latest state of alert evaluation. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold to user for alert evaluation, can be a column or a value.",
        "children": [
          {
            "name": "column",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "aggregation",
                "type": "string",
                "description": "If not set, the behavior is equivalent to using ``First row`` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
              },
              {
                "name": "display",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "bool_value",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "double_value",
                "type": "number",
                "description": ""
              },
              {
                "name": "string_value",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, DELETED)"
  },
  {
    "name": "parameters",
    "type": "array",
    "description": "A list of parameters to pass into the alert SQL query statement containing parameter markers. Static values only. Reference a parameter in the query text as ``:name``. Each parameter must have a unique, non-empty name. Each parameter consists of a name, a value, and optionally a type. To represent a NULL value, the ``value`` field may be omitted or set to ``null`` explicitly. If the ``type`` field is omitted, the value is interpreted as a string. If the type is given, parameters will be checked for type correctness according to the given type. A value is correct if the provided string can be converted to the requested type using the ``cast`` function. The exact semantics are described in the section `cast function <https://docs.databricks.com/sql/language-manual/functions/cast.html>`__ of the SQL language reference.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "The name of the parameter. Reference it in the query text as ``:name``. Required, must be non-empty, and must be unique across the alert's parameters."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The SQL data type of the parameter, for example ``STRING``, ``INT``, or ``DECIMAL(10, 2)``. If no type is given the type is assumed to be ``STRING``. Complex types such as ``ARRAY``, ``MAP``, and ``STRUCT`` are not supported."
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value bound to the parameter, represented as a string. If omitted, the value is interpreted as NULL."
      }
    ]
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the alert. Can only be set on create, and cannot be updated."
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as",
    "type": "object",
    "description": "Specifies the identity that will be used to run the alert. This field allows you to configure alerts to run as a specific user or service principal. - For user identity: Set ``user_name`` to the email of an active workspace user. Users can only set this to their own email. - For service principal: Set ``service_principal_name`` to the application ID. Requires the ``servicePrincipal/user`` role. If not specified, the alert will run as the request user.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_schedule",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved using this timezone. This will be combined with the quartz_cron_schedule to determine the schedule. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details."
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The canonical identifier of the alert to retrieve information about."
  },
  {
    "name": "warehouse_id",
    "type": "string",
    "description": "ID of the SQL warehouse attached to the alert."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "owner_user_name",
    "type": "string",
    "description": "The owner's username. This field is set to \"Unavailable\" if the user has been deleted."
  },
  {
    "name": "run_as_user_name",
    "type": "string",
    "description": "The run as username or application ID of service principal. On Create and Update, this field can be set to application ID of an active service principal. Setting this field requires the servicePrincipal/user role. Deprecated: Use ``run_as`` field instead. This field will be removed in a future release."
  },
  {
    "name": "create_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was created."
  },
  {
    "name": "custom_description",
    "type": "string",
    "description": "Custom description for the alert. Interpreted according to ``custom_template_format``."
  },
  {
    "name": "custom_summary",
    "type": "string",
    "description": "Custom summary for the alert. Interpreted according to ``custom_template_format``."
  },
  {
    "name": "custom_template_format",
    "type": "string",
    "description": "The format used to interpret the ``custom_summary`` and ``custom_description`` templates. ``HTML`` treats both templates as HTML with Mustache ``&#123;&#123;VARIABLE_NAME&#125;&#125;`` placeholders. ``MARKDOWN`` treats them as Markdown with allowlisted ``@VARIABLE_NAME`` placeholders and converts them to the format each notification destination expects, so a single template renders correctly in email, Slack, and Microsoft Teams. When unset, the API applies no default. Responses omit the field unless a format is stored, and a template with no format is rendered as HTML. (HTML, MARKDOWN)"
  },
  {
    "name": "effective_run_as",
    "type": "object",
    "description": "The actual identity that will be used to execute the alert. This is an output-only field that shows the resolved run-as identity after applying permissions and defaults.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "evaluation",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "source",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "aggregation",
            "type": "string",
            "description": "If not set, the behavior is equivalent to using ``First row`` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
          },
          {
            "name": "display",
            "type": "string",
            "description": ""
          }
        ]
      },
      {
        "name": "comparison_operator",
        "type": "string",
        "description": "Operator used for comparison in alert evaluation. (EQUAL, GREATER_THAN, GREATER_THAN_OR_EQUAL, IS_NOT_NULL, IS_NULL, LESS_THAN, LESS_THAN_OR_EQUAL, NOT_EQUAL)"
      },
      {
        "name": "empty_result_state",
        "type": "string",
        "description": "Alert state if result is empty. Please avoid setting this field to be ``UNKNOWN`` because ``UNKNOWN`` state is planned to be deprecated. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "last_evaluated_at",
        "type": "string",
        "description": "Timestamp of the last evaluation."
      },
      {
        "name": "notification",
        "type": "object",
        "description": "User or Notification Destination to notify when alert is triggered.",
        "children": [
          {
            "name": "notify_on_ok",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "retrigger_seconds",
            "type": "integer",
            "description": "Number of seconds an alert waits after being triggered before it is allowed to send another notification. If set to 0 or omitted, the alert will not send any further notifications after the first trigger Setting this value to 1 allows the alert to send a notification on every evaluation where the condition is met, effectively making it always retrigger for notification purposes."
          },
          {
            "name": "subscriptions",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "destination_id",
                "type": "string",
                "description": ""
              },
              {
                "name": "user_email",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "state",
        "type": "string",
        "description": "Latest state of alert evaluation. (ERROR, OK, TRIGGERED, UNKNOWN)"
      },
      {
        "name": "threshold",
        "type": "object",
        "description": "Threshold to user for alert evaluation, can be a column or a value.",
        "children": [
          {
            "name": "column",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": ""
              },
              {
                "name": "aggregation",
                "type": "string",
                "description": "If not set, the behavior is equivalent to using ``First row`` in the UI. (AVG, COUNT, COUNT_DISTINCT, MAX, MEDIAN, MIN, STDDEV, SUM)"
              },
              {
                "name": "display",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "value",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "bool_value",
                "type": "boolean",
                "description": ""
              },
              {
                "name": "double_value",
                "type": "number",
                "description": ""
              },
              {
                "name": "string_value",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "lifecycle_state",
    "type": "string",
    "description": "Indicates whether the query is trashed. (ACTIVE, DELETED)"
  },
  {
    "name": "parameters",
    "type": "array",
    "description": "A list of parameters to pass into the alert SQL query statement containing parameter markers. Static values only. Reference a parameter in the query text as ``:name``. Each parameter must have a unique, non-empty name. Each parameter consists of a name, a value, and optionally a type. To represent a NULL value, the ``value`` field may be omitted or set to ``null`` explicitly. If the ``type`` field is omitted, the value is interpreted as a string. If the type is given, parameters will be checked for type correctness according to the given type. A value is correct if the provided string can be converted to the requested type using the ``cast`` function. The exact semantics are described in the section `cast function <https://docs.databricks.com/sql/language-manual/functions/cast.html>`__ of the SQL language reference.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": "The name of the parameter. Reference it in the query text as ``:name``. Required, must be non-empty, and must be unique across the alert's parameters."
      },
      {
        "name": "type",
        "type": "string",
        "description": "The SQL data type of the parameter, for example ``STRING``, ``INT``, or ``DECIMAL(10, 2)``. If no type is given the type is assumed to be ``STRING``. Complex types such as ``ARRAY``, ``MAP``, and ``STRUCT`` are not supported."
      },
      {
        "name": "value",
        "type": "string",
        "description": "The value bound to the parameter, represented as a string. If omitted, the value is interpreted as NULL."
      }
    ]
  },
  {
    "name": "parent_path",
    "type": "string",
    "description": "The workspace path of the folder containing the alert. Can only be set on create, and cannot be updated."
  },
  {
    "name": "query_text",
    "type": "string",
    "description": "Text of the query to be run."
  },
  {
    "name": "run_as",
    "type": "object",
    "description": "Specifies the identity that will be used to run the alert. This field allows you to configure alerts to run as a specific user or service principal. - For user identity: Set ``user_name`` to the email of an active workspace user. Users can only set this to their own email. - For service principal: Set ``service_principal_name`` to the application ID. Requires the ``servicePrincipal/user`` role. If not specified, the alert will run as the request user.",
    "children": [
      {
        "name": "service_principal_name",
        "type": "string",
        "description": ""
      },
      {
        "name": "user_name",
        "type": "string",
        "description": "The email of an active workspace user. Can only set this field to their own email."
      }
    ]
  },
  {
    "name": "schedule",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "quartz_cron_schedule",
        "type": "string",
        "description": ""
      },
      {
        "name": "timezone_id",
        "type": "string",
        "description": "A Java timezone id. The schedule will be resolved using this timezone. This will be combined with the quartz_cron_schedule to determine the schedule. See https://docs.databricks.com/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set-timezone.html for details."
      },
      {
        "name": "pause_status",
        "type": "string",
        "description": "Indicate whether this schedule is paused or not. (PAUSED, UNPAUSED)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string",
    "description": "The timestamp indicating when the alert was updated."
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
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets an alert.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Gets a list of alerts accessible to the user, ordered by creation time.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-alert"><code>alert</code></a></td>
    <td></td>
    <td>Create Alert</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-alert"><code>alert</code></a></td>
    <td></td>
    <td>Update alert</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-id"><code>id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-purge"><code>purge</code></a></td>
    <td>Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer</td>
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
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g., ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-purge">
    <td><CopyableCode code="purge" /></td>
    <td><code>boolean</code></td>
    <td>Whether to permanently delete the alert. If not set, the alert will only be soft deleted.</td>
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

Gets an alert.

```sql
SELECT
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
custom_template_format,
effective_run_as,
evaluation,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as,
schedule,
update_time
FROM databricks_workspace.sql.alerts_v2
WHERE id = '{{ id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of alerts accessible to the user, ordered by creation time.

```sql
SELECT
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
custom_template_format,
effective_run_as,
evaluation,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as,
schedule,
update_time
FROM databricks_workspace.sql.alerts_v2
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

Create Alert

```sql
INSERT INTO databricks_workspace.sql.alerts_v2 (
alert,
deployment_name,
workspace_domain
)
SELECT 
'{{ alert }}' /* required */,
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
custom_template_format,
effective_run_as,
evaluation,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as,
schedule,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: alerts_v2
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the alerts_v2 resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the alerts_v2 resource.
    - name: alert
      value:
        display_name: "{{ display_name }}"
        query_text: "{{ query_text }}"
        warehouse_id: "{{ warehouse_id }}"
        evaluation:
          source:
            name: "{{ name }}"
            aggregation: "{{ aggregation }}"
            display: "{{ display }}"
          comparison_operator: "{{ comparison_operator }}"
          empty_result_state: "{{ empty_result_state }}"
          last_evaluated_at: "{{ last_evaluated_at }}"
          notification:
            notify_on_ok: {{ notify_on_ok }}
            retrigger_seconds: {{ retrigger_seconds }}
            subscriptions:
              - destination_id: "{{ destination_id }}"
                user_email: "{{ user_email }}"
          state: "{{ state }}"
          threshold:
            column:
              name: "{{ name }}"
              aggregation: "{{ aggregation }}"
              display: "{{ display }}"
            value:
              bool_value: {{ bool_value }}
              double_value: {{ double_value }}
              string_value: "{{ string_value }}"
        schedule:
          quartz_cron_schedule: "{{ quartz_cron_schedule }}"
          timezone_id: "{{ timezone_id }}"
          pause_status: "{{ pause_status }}"
        create_time: "{{ create_time }}"
        custom_description: "{{ custom_description }}"
        custom_summary: "{{ custom_summary }}"
        custom_template_format: "{{ custom_template_format }}"
        effective_run_as:
          service_principal_name: "{{ service_principal_name }}"
          user_name: "{{ user_name }}"
        id: "{{ id }}"
        lifecycle_state: "{{ lifecycle_state }}"
        owner_user_name: "{{ owner_user_name }}"
        parameters:
          - name: "{{ name }}"
            type: "{{ type }}"
            value: "{{ value }}"
        parent_path: "{{ parent_path }}"
        run_as:
          service_principal_name: "{{ service_principal_name }}"
          user_name: "{{ user_name }}"
        run_as_user_name: "{{ run_as_user_name }}"
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

Update alert

```sql
UPDATE databricks_workspace.sql.alerts_v2
SET 
alert = '{{ alert }}'
WHERE 
id = '{{ id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND alert = '{{ alert }}' --required
RETURNING
id,
warehouse_id,
display_name,
owner_user_name,
run_as_user_name,
create_time,
custom_description,
custom_summary,
custom_template_format,
effective_run_as,
evaluation,
lifecycle_state,
parameters,
parent_path,
query_text,
run_as,
schedule,
update_time;
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

Moves an alert to the trash. Trashed alerts immediately disappear from list views, and can no longer

```sql
DELETE FROM databricks_workspace.sql.alerts_v2
WHERE id = '{{ id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND purge = '{{ purge }}'
;
```
</TabItem>
</Tabs>
