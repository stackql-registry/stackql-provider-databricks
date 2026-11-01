---
title: data_quality
hide_title: false
hide_table_of_contents: false
keywords:
  - data_quality
  - dataquality
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

Creates, updates, deletes, gets or lists a <code>data_quality</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_quality" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dataquality.data_quality" /></td></tr>
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
    "name": "object_id",
    "type": "string",
    "description": "The UUID of the request object. It is ``schema_id`` for ``schema``, and ``table_id`` for ``table``. Find the ``schema_id`` from either: 1. The `schema_id <https://docs.databricks.com/api/workspace/schemas/get#schema_id>`__ of the ``Schemas`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``schema`` &gt; go to the ``Details`` tab &gt; the ``Schema ID`` field. Find the ``table_id`` from either: 1. The `table_id <https://docs.databricks.com/api/workspace/tables/get#table_id>`__ of the ``Tables`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``table`` &gt; go to the ``Details`` tab &gt; the ``Table ID`` field."
  },
  {
    "name": "anomaly_detection_config",
    "type": "object",
    "description": "Anomaly Detection Configuration, applicable to ``schema`` object types.",
    "children": [
      {
        "name": "excluded_table_full_names",
        "type": "array",
        "description": "List of fully qualified table names to exclude from anomaly detection."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Who to alert when anomaly detection finds unhealthy tables in this schema. Applicable to ``schema`` monitors only. This is the same schema alert you manage from **Manage alerts** in the Data Quality Monitoring UI, so a change made in either place shows in both. Set the recipients in ``on_unhealthy_table``; ``on_failure`` is not supported here. Only ``destination_ids`` and ``destination_user_ids`` are supported. On update, an update mask of ``*``, ``anomaly_detection_config``, or ``anomaly_detection_config.notification_settings`` replaces the alert's recipients with the ones in the request; omitting the field, or leaving both recipient lists empty, removes the alert. Other masks leave the alert unchanged.",
        "children": [
          {
            "name": "on_failure",
            "type": "object",
            "description": "Destinations to send notifications on failure/timeout.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          },
          {
            "name": "on_unhealthy_table",
            "type": "object",
            "description": "Recipients to notify when anomaly detection finds unhealthy tables in the schema. Each recipient gets one notification per important unhealthy table. Only supported on schema monitors, via ``anomaly_detection_config``.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "data_profiling_config",
    "type": "object",
    "description": "Data Profiling Configuration, applicable to ``table`` object types. Exactly one ``Analysis Configuration`` must be present.",
    "children": [
      {
        "name": "output_schema_id",
        "type": "string",
        "description": "ID of the schema where output tables are created."
      },
      {
        "name": "assets_dir",
        "type": "string",
        "description": "Field for specifying the absolute path to a custom directory to store data-monitoring assets. Normally prepopulated to a default user location via UI and Python APIs."
      },
      {
        "name": "baseline_table_name",
        "type": "string",
        "description": "Baseline table name. Baseline data is used to compute drift from the data in the monitored ``table_name``. The baseline table and the monitored table shall have the same schema."
      },
      {
        "name": "custom_metrics",
        "type": "array",
        "description": "Custom metrics.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Name of the metric in the output tables."
          },
          {
            "name": "definition",
            "type": "string",
            "description": "Jinja template for a SQL expression that specifies how to compute the metric. See `create metric definition <https://docs.databricks.com/en/lakehouse-monitoring/custom-metrics.html#create-definition>`__."
          },
          {
            "name": "input_columns",
            "type": "array",
            "description": "A list of column names in the input table the metric should be computed for. Can use ``\":table\"`` to indicate that the metric needs information from multiple columns."
          },
          {
            "name": "output_data_type",
            "type": "string",
            "description": "The output type of the custom metric."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the custom metric. (DATA_PROFILING_CUSTOM_METRIC_TYPE_AGGREGATE, DATA_PROFILING_CUSTOM_METRIC_TYPE_DERIVED, DATA_PROFILING_CUSTOM_METRIC_TYPE_DRIFT)"
          }
        ]
      },
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "Id of dashboard that visualizes the computed metrics. This can be empty if the monitor is in PENDING state."
      },
      {
        "name": "drift_metrics_table_name",
        "type": "string",
        "description": "Table that stores drift metrics data. Format: ``catalog.schema.table_name``."
      },
      {
        "name": "effective_warehouse_id",
        "type": "string",
        "description": "The warehouse for dashboard creation"
      },
      {
        "name": "inference_log",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring inference log tables.",
        "children": [
          {
            "name": "problem_type",
            "type": "string",
            "description": "Problem type the model aims to solve. (INFERENCE_PROBLEM_TYPE_CLASSIFICATION, INFERENCE_PROBLEM_TYPE_REGRESSION)"
          },
          {
            "name": "timestamp_column",
            "type": "string",
            "description": "Column for the timestamp."
          },
          {
            "name": "granularities",
            "type": "array",
            "description": "List of granularities to use when aggregating data into time windows based on their timestamp."
          },
          {
            "name": "prediction_column",
            "type": "string",
            "description": "Column for the prediction."
          },
          {
            "name": "model_id_column",
            "type": "string",
            "description": "Column for the model identifier."
          },
          {
            "name": "label_column",
            "type": "string",
            "description": "Column for the label."
          }
        ]
      },
      {
        "name": "latest_monitor_failure_message",
        "type": "string",
        "description": "The latest error message for a monitor failure."
      },
      {
        "name": "monitor_version",
        "type": "integer",
        "description": "Represents the current monitor configuration version in use. The version will be represented in a numeric fashion (1,2,3...). The field has flexibility to take on negative values, which can indicate corrupted monitor_version numbers."
      },
      {
        "name": "monitored_table_name",
        "type": "string",
        "description": "Unity Catalog table to monitor. Format: ``catalog.schema.table_name``"
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Field for specifying notification settings.",
        "children": [
          {
            "name": "on_failure",
            "type": "object",
            "description": "Destinations to send notifications on failure/timeout.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          },
          {
            "name": "on_unhealthy_table",
            "type": "object",
            "description": "Recipients to notify when anomaly detection finds unhealthy tables in the schema. Each recipient gets one notification per important unhealthy table. Only supported on schema monitors, via ``anomaly_detection_config``.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          }
        ]
      },
      {
        "name": "profile_metrics_table_name",
        "type": "string",
        "description": "Table that stores profile metrics data. Format: ``catalog.schema.table_name``."
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "The cron schedule.",
        "children": [
          {
            "name": "quartz_cron_expression",
            "type": "string",
            "description": "The expression that determines when to run the monitor. See `examples <https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html>`__."
          },
          {
            "name": "timezone_id",
            "type": "string",
            "description": "A Java timezone id. The schedule for a job will be resolved with respect to this timezone. See `Java TimeZone <http://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html>`_ for details. The timezone id (e.g., ``America/Los_Angeles``) in which to evaluate the quartz expression."
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Read only field that indicates whether the schedule is paused or not. (CRON_SCHEDULE_PAUSE_STATUS_PAUSED, CRON_SCHEDULE_PAUSE_STATUS_UNPAUSED)"
          }
        ]
      },
      {
        "name": "skip_builtin_dashboard",
        "type": "boolean",
        "description": "Whether to skip creating a default dashboard summarizing data quality metrics."
      },
      {
        "name": "slicing_exprs",
        "type": "array",
        "description": "List of column expressions to slice data with for targeted analysis. The data is grouped by each expression independently, resulting in a separate slice for each predicate and its complements. For example ``slicing_exprs=[“col_1”, “col_2 &gt; 10”]`` will generate the following slices: two slices for ``col_2 &gt; 10`` (True and False), and one slice per unique value in ``col1``. For high-cardinality columns, only the top 100 unique values by frequency will generate slices."
      },
      {
        "name": "snapshot",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring snapshot tables."
      },
      {
        "name": "status",
        "type": "string",
        "description": "The data profiling monitor status. (DATA_PROFILING_STATUS_ACTIVE, DATA_PROFILING_STATUS_DELETE_PENDING, DATA_PROFILING_STATUS_ERROR, DATA_PROFILING_STATUS_FAILED, DATA_PROFILING_STATUS_PENDING)"
      },
      {
        "name": "time_series",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring time series tables.",
        "children": [
          {
            "name": "timestamp_column",
            "type": "string",
            "description": "Column for the timestamp."
          },
          {
            "name": "granularities",
            "type": "array",
            "description": "List of granularities to use when aggregating data into time windows based on their timestamp."
          }
        ]
      },
      {
        "name": "warehouse_id",
        "type": "string",
        "description": "Optional argument to specify the warehouse for dashboard creation. If not specified, the first running warehouse will be used."
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the monitored object. Can be one of the following: ``schema`` or ``table``."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "object_id",
    "type": "string",
    "description": "The UUID of the request object. It is ``schema_id`` for ``schema``, and ``table_id`` for ``table``. Find the ``schema_id`` from either: 1. The `schema_id <https://docs.databricks.com/api/workspace/schemas/get#schema_id>`__ of the ``Schemas`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``schema`` &gt; go to the ``Details`` tab &gt; the ``Schema ID`` field. Find the ``table_id`` from either: 1. The `table_id <https://docs.databricks.com/api/workspace/tables/get#table_id>`__ of the ``Tables`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``table`` &gt; go to the ``Details`` tab &gt; the ``Table ID`` field."
  },
  {
    "name": "anomaly_detection_config",
    "type": "object",
    "description": "Anomaly Detection Configuration, applicable to ``schema`` object types.",
    "children": [
      {
        "name": "excluded_table_full_names",
        "type": "array",
        "description": "List of fully qualified table names to exclude from anomaly detection."
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Who to alert when anomaly detection finds unhealthy tables in this schema. Applicable to ``schema`` monitors only. This is the same schema alert you manage from **Manage alerts** in the Data Quality Monitoring UI, so a change made in either place shows in both. Set the recipients in ``on_unhealthy_table``; ``on_failure`` is not supported here. Only ``destination_ids`` and ``destination_user_ids`` are supported. On update, an update mask of ``*``, ``anomaly_detection_config``, or ``anomaly_detection_config.notification_settings`` replaces the alert's recipients with the ones in the request; omitting the field, or leaving both recipient lists empty, removes the alert. Other masks leave the alert unchanged.",
        "children": [
          {
            "name": "on_failure",
            "type": "object",
            "description": "Destinations to send notifications on failure/timeout.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          },
          {
            "name": "on_unhealthy_table",
            "type": "object",
            "description": "Recipients to notify when anomaly detection finds unhealthy tables in the schema. Each recipient gets one notification per important unhealthy table. Only supported on schema monitors, via ``anomaly_detection_config``.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "data_profiling_config",
    "type": "object",
    "description": "Data Profiling Configuration, applicable to ``table`` object types. Exactly one ``Analysis Configuration`` must be present.",
    "children": [
      {
        "name": "output_schema_id",
        "type": "string",
        "description": "ID of the schema where output tables are created."
      },
      {
        "name": "assets_dir",
        "type": "string",
        "description": "Field for specifying the absolute path to a custom directory to store data-monitoring assets. Normally prepopulated to a default user location via UI and Python APIs."
      },
      {
        "name": "baseline_table_name",
        "type": "string",
        "description": "Baseline table name. Baseline data is used to compute drift from the data in the monitored ``table_name``. The baseline table and the monitored table shall have the same schema."
      },
      {
        "name": "custom_metrics",
        "type": "array",
        "description": "Custom metrics.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Name of the metric in the output tables."
          },
          {
            "name": "definition",
            "type": "string",
            "description": "Jinja template for a SQL expression that specifies how to compute the metric. See `create metric definition <https://docs.databricks.com/en/lakehouse-monitoring/custom-metrics.html#create-definition>`__."
          },
          {
            "name": "input_columns",
            "type": "array",
            "description": "A list of column names in the input table the metric should be computed for. Can use ``\":table\"`` to indicate that the metric needs information from multiple columns."
          },
          {
            "name": "output_data_type",
            "type": "string",
            "description": "The output type of the custom metric."
          },
          {
            "name": "type",
            "type": "string",
            "description": "The type of the custom metric. (DATA_PROFILING_CUSTOM_METRIC_TYPE_AGGREGATE, DATA_PROFILING_CUSTOM_METRIC_TYPE_DERIVED, DATA_PROFILING_CUSTOM_METRIC_TYPE_DRIFT)"
          }
        ]
      },
      {
        "name": "dashboard_id",
        "type": "string",
        "description": "Id of dashboard that visualizes the computed metrics. This can be empty if the monitor is in PENDING state."
      },
      {
        "name": "drift_metrics_table_name",
        "type": "string",
        "description": "Table that stores drift metrics data. Format: ``catalog.schema.table_name``."
      },
      {
        "name": "effective_warehouse_id",
        "type": "string",
        "description": "The warehouse for dashboard creation"
      },
      {
        "name": "inference_log",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring inference log tables.",
        "children": [
          {
            "name": "problem_type",
            "type": "string",
            "description": "Problem type the model aims to solve. (INFERENCE_PROBLEM_TYPE_CLASSIFICATION, INFERENCE_PROBLEM_TYPE_REGRESSION)"
          },
          {
            "name": "timestamp_column",
            "type": "string",
            "description": "Column for the timestamp."
          },
          {
            "name": "granularities",
            "type": "array",
            "description": "List of granularities to use when aggregating data into time windows based on their timestamp."
          },
          {
            "name": "prediction_column",
            "type": "string",
            "description": "Column for the prediction."
          },
          {
            "name": "model_id_column",
            "type": "string",
            "description": "Column for the model identifier."
          },
          {
            "name": "label_column",
            "type": "string",
            "description": "Column for the label."
          }
        ]
      },
      {
        "name": "latest_monitor_failure_message",
        "type": "string",
        "description": "The latest error message for a monitor failure."
      },
      {
        "name": "monitor_version",
        "type": "integer",
        "description": "Represents the current monitor configuration version in use. The version will be represented in a numeric fashion (1,2,3...). The field has flexibility to take on negative values, which can indicate corrupted monitor_version numbers."
      },
      {
        "name": "monitored_table_name",
        "type": "string",
        "description": "Unity Catalog table to monitor. Format: ``catalog.schema.table_name``"
      },
      {
        "name": "notification_settings",
        "type": "object",
        "description": "Field for specifying notification settings.",
        "children": [
          {
            "name": "on_failure",
            "type": "object",
            "description": "Destinations to send notifications on failure/timeout.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          },
          {
            "name": "on_unhealthy_table",
            "type": "object",
            "description": "Recipients to notify when anomaly detection finds unhealthy tables in the schema. Each recipient gets one notification per important unhealthy table. Only supported on schema monitors, via ``anomaly_detection_config``.",
            "children": [
              {
                "name": "destination_ids",
                "type": "array",
                "description": "The notification-destination IDs (Slack / Teams / webhook) to send the notification to. The destinations must already exist in the workspace; a workspace admin creates them. A maximum of 25 destination IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "destination_user_ids",
                "type": "array",
                "description": "The IDs of the workspace users to notify by email. A maximum of 25 user IDs is supported. Only supported on schema monitors, via ``anomaly_detection_config``; rejected on table monitors."
              },
              {
                "name": "email_addresses",
                "type": "array",
                "description": "The list of email addresses to send the notification to. A maximum of 5 email addresses is supported."
              }
            ]
          }
        ]
      },
      {
        "name": "profile_metrics_table_name",
        "type": "string",
        "description": "Table that stores profile metrics data. Format: ``catalog.schema.table_name``."
      },
      {
        "name": "schedule",
        "type": "object",
        "description": "The cron schedule.",
        "children": [
          {
            "name": "quartz_cron_expression",
            "type": "string",
            "description": "The expression that determines when to run the monitor. See `examples <https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html>`__."
          },
          {
            "name": "timezone_id",
            "type": "string",
            "description": "A Java timezone id. The schedule for a job will be resolved with respect to this timezone. See `Java TimeZone <http://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html>`_ for details. The timezone id (e.g., ``America/Los_Angeles``) in which to evaluate the quartz expression."
          },
          {
            "name": "pause_status",
            "type": "string",
            "description": "Read only field that indicates whether the schedule is paused or not. (CRON_SCHEDULE_PAUSE_STATUS_PAUSED, CRON_SCHEDULE_PAUSE_STATUS_UNPAUSED)"
          }
        ]
      },
      {
        "name": "skip_builtin_dashboard",
        "type": "boolean",
        "description": "Whether to skip creating a default dashboard summarizing data quality metrics."
      },
      {
        "name": "slicing_exprs",
        "type": "array",
        "description": "List of column expressions to slice data with for targeted analysis. The data is grouped by each expression independently, resulting in a separate slice for each predicate and its complements. For example ``slicing_exprs=[“col_1”, “col_2 &gt; 10”]`` will generate the following slices: two slices for ``col_2 &gt; 10`` (True and False), and one slice per unique value in ``col1``. For high-cardinality columns, only the top 100 unique values by frequency will generate slices."
      },
      {
        "name": "snapshot",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring snapshot tables."
      },
      {
        "name": "status",
        "type": "string",
        "description": "The data profiling monitor status. (DATA_PROFILING_STATUS_ACTIVE, DATA_PROFILING_STATUS_DELETE_PENDING, DATA_PROFILING_STATUS_ERROR, DATA_PROFILING_STATUS_FAILED, DATA_PROFILING_STATUS_PENDING)"
      },
      {
        "name": "time_series",
        "type": "object",
        "description": "``Analysis Configuration`` for monitoring time series tables.",
        "children": [
          {
            "name": "timestamp_column",
            "type": "string",
            "description": "Column for the timestamp."
          },
          {
            "name": "granularities",
            "type": "array",
            "description": "List of granularities to use when aggregating data into time windows based on their timestamp."
          }
        ]
      },
      {
        "name": "warehouse_id",
        "type": "string",
        "description": "Optional argument to specify the warehouse for dashboard creation. If not specified, the first running warehouse will be used."
      }
    ]
  },
  {
    "name": "object_type",
    "type": "string",
    "description": "The type of the monitored object. Can be one of the following: ``schema`` or ``table``."
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
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Read a data quality monitor on a Unity Catalog object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>(Unimplemented) List data quality monitors.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-monitor"><code>monitor</code></a></td>
    <td></td>
    <td>Create a data quality monitor on a Unity Catalog object. The caller must provide either</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-monitor"><code>monitor</code></a></td>
    <td></td>
    <td>Update a data quality monitor on Unity Catalog object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-object_type"><code>object_type</code></a>, <a href="#parameter-object_id"><code>object_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete a data quality monitor on Unity Catalog object.</td>
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
<tr id="parameter-object_id">
    <td><CopyableCode code="object_id" /></td>
    <td><code>string</code></td>
    <td>The UUID of the request object. It is ``schema_id`` for ``schema``, and ``table_id`` for ``table``. Find the ``schema_id`` from either: 1. The `schema_id <https://docs.databricks.com/api/workspace/schemas/get#schema_id>`__ of the ``Schemas`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``schema`` &gt; go to the ``Details`` tab &gt; the ``Schema ID`` field. Find the ``table_id`` from either: 1. The `table_id <https://docs.databricks.com/api/workspace/tables/get#table_id>`__ of the ``Tables`` resource. 2. In `Catalog Explorer <https://docs.databricks.com/aws/en/catalog-explorer/>`__ &gt; select the ``table`` &gt; go to the ``Details`` tab &gt; the ``Table ID`` field.</td>
</tr>
<tr id="parameter-object_type">
    <td><CopyableCode code="object_type" /></td>
    <td><code>string</code></td>
    <td>The type of the monitored object. Can be one of the following: ``schema`` or ``table``.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>The field mask to specify which fields to update as a comma-separated list. Example value: ``data_profiling_config.custom_metrics,data_profiling_config.schedule.quartz_cron_expression``</td>
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

Read a data quality monitor on a Unity Catalog object.

```sql
SELECT
object_id,
anomaly_detection_config,
data_profiling_config,
object_type
FROM databricks_workspace.dataquality.data_quality
WHERE object_type = '{{ object_type }}' -- required
AND object_id = '{{ object_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

(Unimplemented) List data quality monitors.

```sql
SELECT
object_id,
anomaly_detection_config,
data_profiling_config,
object_type
FROM databricks_workspace.dataquality.data_quality
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

Create a data quality monitor on a Unity Catalog object. The caller must provide either

```sql
INSERT INTO databricks_workspace.dataquality.data_quality (
monitor,
deployment_name,
workspace_domain
)
SELECT 
'{{ monitor }}' /* required */,
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
object_id,
anomaly_detection_config,
data_profiling_config,
object_type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_quality
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the data_quality resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the data_quality resource.
    - name: monitor
      description: |
        The monitor to create.
      value:
        object_type: "{{ object_type }}"
        object_id: "{{ object_id }}"
        anomaly_detection_config:
          excluded_table_full_names:
            - "{{ excluded_table_full_names }}"
          notification_settings:
            on_failure:
              destination_ids:
                - "{{ destination_ids }}"
              destination_user_ids:
                - {{ destination_user_ids }}
              email_addresses:
                - "{{ email_addresses }}"
            on_unhealthy_table:
              destination_ids:
                - "{{ destination_ids }}"
              destination_user_ids:
                - {{ destination_user_ids }}
              email_addresses:
                - "{{ email_addresses }}"
        data_profiling_config:
          output_schema_id: "{{ output_schema_id }}"
          assets_dir: "{{ assets_dir }}"
          baseline_table_name: "{{ baseline_table_name }}"
          custom_metrics:
            - name: "{{ name }}"
              definition: "{{ definition }}"
              input_columns: "{{ input_columns }}"
              output_data_type: "{{ output_data_type }}"
              type: "{{ type }}"
          dashboard_id: "{{ dashboard_id }}"
          drift_metrics_table_name: "{{ drift_metrics_table_name }}"
          effective_warehouse_id: "{{ effective_warehouse_id }}"
          inference_log:
            problem_type: "{{ problem_type }}"
            timestamp_column: "{{ timestamp_column }}"
            granularities:
              - "{{ granularities }}"
            prediction_column: "{{ prediction_column }}"
            model_id_column: "{{ model_id_column }}"
            label_column: "{{ label_column }}"
          latest_monitor_failure_message: "{{ latest_monitor_failure_message }}"
          monitor_version: {{ monitor_version }}
          monitored_table_name: "{{ monitored_table_name }}"
          notification_settings:
            on_failure:
              destination_ids:
                - "{{ destination_ids }}"
              destination_user_ids:
                - {{ destination_user_ids }}
              email_addresses:
                - "{{ email_addresses }}"
            on_unhealthy_table:
              destination_ids:
                - "{{ destination_ids }}"
              destination_user_ids:
                - {{ destination_user_ids }}
              email_addresses:
                - "{{ email_addresses }}"
          profile_metrics_table_name: "{{ profile_metrics_table_name }}"
          schedule:
            quartz_cron_expression: "{{ quartz_cron_expression }}"
            timezone_id: "{{ timezone_id }}"
            pause_status: "{{ pause_status }}"
          skip_builtin_dashboard: {{ skip_builtin_dashboard }}
          slicing_exprs:
            - "{{ slicing_exprs }}"
          snapshot: "{{ snapshot }}"
          status: "{{ status }}"
          time_series:
            timestamp_column: "{{ timestamp_column }}"
            granularities:
              - "{{ granularities }}"
          warehouse_id: "{{ warehouse_id }}"
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

Update a data quality monitor on Unity Catalog object.

```sql
UPDATE databricks_workspace.dataquality.data_quality
SET 
monitor = '{{ monitor }}'
WHERE 
object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND monitor = '{{ monitor }}' --required
RETURNING
object_id,
anomaly_detection_config,
data_profiling_config,
object_type;
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

Delete a data quality monitor on Unity Catalog object.

```sql
DELETE FROM databricks_workspace.dataquality.data_quality
WHERE object_type = '{{ object_type }}' --required
AND object_id = '{{ object_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
