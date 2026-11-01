---
title: feature_engineering
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_engineering
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

Creates, updates, deletes, gets or lists a <code>feature_engineering</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_engineering" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.feature_engineering" /></td></tr>
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
    "description": "Name of the feature, extracted from the full three-part name (catalog.schema.name)."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent schema relative to its parent catalog."
  },
  {
    "name": "created_at",
    "type": "string (date-time)",
    "description": "Time at which this feature was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of the feature creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the feature."
  },
  {
    "name": "entities",
    "type": "array",
    "description": "The entity columns for the feature, used as aggregation keys and for query-time lookup. Optional since entities are not set for RequestSource features or on-demand calculated features.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "filter_condition",
    "type": "string",
    "description": ""
  },
  {
    "name": "function",
    "type": "object",
    "description": "The function by which the feature is computed.",
    "children": [
      {
        "name": "aggregation_function",
        "type": "object",
        "description": "An aggregation function applied over a time window.",
        "children": [
          {
            "name": "approx_count_distinct",
            "type": "object",
            "description": "Computes the approximate count of distinct values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the approximate count of distinct values is computed."
              },
              {
                "name": "relative_error",
                "type": "number",
                "description": "The error the user accepts, as a fraction of the count, between 0.02 (by default) and 0.3. This is one standard error of the estimate, the same meaning as Spark's relativeSD: 0.02 means the result is within ±2% of the true count about 68% of the time (one standard deviation covers 68% of the region). Feature Store picks the sketch size that gives this relative error. If neither relative_error nor relative_sd is set, 0.02 is default chosen at feature creation."
              },
              {
                "name": "relative_sd",
                "type": "number",
                "description": "The maximum relative standard deviation allowed (default defined by Spark). Deprecated: use relative_error. When relative_error is set, reads return the same value here for clients that don't have relative_error, and a request may only send that value."
              }
            ]
          },
          {
            "name": "approx_percentile",
            "type": "object",
            "description": "Computes the approximate percentile of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the approximate percentile is computed."
              },
              {
                "name": "percentile",
                "type": "number",
                "description": "The percentile value to compute (between 0 and 1)."
              },
              {
                "name": "accuracy",
                "type": "integer",
                "description": "The accuracy parameter (higher is more accurate but slower). Deprecated: use relative_error. When relative_error is set, reads return ceil(1 / relative_error) here for clients that don't have relative_error, and a request may only send that value."
              },
              {
                "name": "relative_error",
                "type": "number",
                "description": "The error the user accepts, as a fraction of rank, between 0.01 (by default) and 0.3. The result is within this rank error with 99% confidence: at 0.01, the value returned for p95 is between the true p94 and p96 at least 99% of the time. Feature Store picks the sketch size that gives this error. If neither relative_error nor accuracy is set, 0.01 is default chosen at feature creation."
              }
            ]
          },
          {
            "name": "avg",
            "type": "object",
            "description": "Computes the average of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the average is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "count_function",
            "type": "object",
            "description": "Computes the count of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the count is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "first",
            "type": "object",
            "description": "Returns the first value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first value is returned."
              }
            ]
          },
          {
            "name": "first_distinct",
            "type": "object",
            "description": "Returns the first N distinct values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first N distinct values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of distinct values to return."
              }
            ]
          },
          {
            "name": "first_n",
            "type": "object",
            "description": "Returns the first N values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first N values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of values to return."
              }
            ]
          },
          {
            "name": "last",
            "type": "object",
            "description": "Returns the last value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last value is returned."
              }
            ]
          },
          {
            "name": "last_distinct",
            "type": "object",
            "description": "Returns the last N distinct values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last N distinct values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of distinct values to return."
              }
            ]
          },
          {
            "name": "last_n",
            "type": "object",
            "description": "Returns the last N values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last N values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of values to return."
              }
            ]
          },
          {
            "name": "max",
            "type": "object",
            "description": "Computes the maximum value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the maximum is computed."
              }
            ]
          },
          {
            "name": "min",
            "type": "object",
            "description": "Computes the minimum value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the minimum is computed."
              }
            ]
          },
          {
            "name": "stddev_pop",
            "type": "object",
            "description": "Computes the population standard deviation.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the population standard deviation is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "stddev_samp",
            "type": "object",
            "description": "Computes the sample standard deviation.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sample standard deviation is computed."
              }
            ]
          },
          {
            "name": "sum",
            "type": "object",
            "description": "Computes the sum of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sum is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "time_window",
            "type": "object",
            "description": "The time window over which the aggregation is computed.",
            "children": [
              {
                "name": "continuous",
                "type": "object",
                "description": ""
              },
              {
                "name": "rolling",
                "type": "object",
                "description": "A rolling time window with an optional non-negative delay."
              },
              {
                "name": "sawtooth",
                "type": "object",
                "description": "A sawtooth window served via the hybrid batch + streaming path."
              },
              {
                "name": "sliding",
                "type": "object",
                "description": ""
              },
              {
                "name": "start_time",
                "type": "string (date-time)",
                "description": "Earliest event-time boundary at which the Feature may emit an output. This gates outputs, not the historical inputs read by a window. For example, a 365-day window with start_time=2026-01-01 begins emitting partial-window values on that date instead of waiting for 365 days of data; a lifetime window produces no output before start_time. If unset, tumbling and fixed-duration sliding windows first emit at an offset-aligned boundary after a full window can be formed. If unset, lifetime sliding windows and rolling windows emit as soon as eligible source data exists. For sawtooth windows, start_time must not be later than the time the Feature is created. Not supported for rolling windows on Features with a stream source."
              },
              {
                "name": "tumbling",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "var_pop",
            "type": "object",
            "description": "Computes the population variance.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the population variance is computed."
              }
            ]
          },
          {
            "name": "var_samp",
            "type": "object",
            "description": "Computes the sample variance.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sample variance is computed."
              }
            ]
          }
        ]
      },
      {
        "name": "column_selection",
        "type": "object",
        "description": "Selects the latest value of a single column in a data source",
        "children": [
          {
            "name": "column",
            "type": "string",
            "description": "Column name from source to select as the feature value."
          }
        ]
      },
      {
        "name": "custom_udf",
        "type": "object",
        "description": "Applies a registered Unity Catalog function row-wise to source columns.",
        "children": [
          {
            "name": "function_path",
            "type": "string",
            "description": "Fully qualified 3-part Unity Catalog path of the function to apply."
          },
          {
            "name": "input_bindings",
            "type": "array",
            "description": "Binds each UC function parameter to a source column. May be empty for zero-argument functions (e.g. a timestamp generator).",
            "children": [
              {
                "name": "parameter",
                "type": "string",
                "description": "Name of the UC function parameter."
              },
              {
                "name": "column",
                "type": "string",
                "description": "Source column whose value is passed for this parameter at execution time."
              }
            ]
          }
        ]
      },
      {
        "name": "extra_parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the parameter."
          }
        ]
      },
      {
        "name": "function_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (APPROX_COUNT_DISTINCT, APPROX_PERCENTILE, AVG, COUNT, FIRST, FUNCTION_TYPE_UNSPECIFIED, LAST, MAX, MIN, STDDEV_POP, STDDEV_SAMP, SUM, VAR_POP, VAR_SAMP)"
      }
    ]
  },
  {
    "name": "inputs",
    "type": "array",
    "description": ""
  },
  {
    "name": "lineage_context",
    "type": "object",
    "description": "Lineage context information for this feature. WARNING: This field is primarily intended for internal use by Databricks systems and is automatically populated when features are created through Databricks notebooks or jobs. Users should not manually set this field as incorrect values may lead to inaccurate lineage tracking or unexpected behavior. This field will be set by feature-engineering client and should be left unset by SDK and terraform users.",
    "children": [
      {
        "name": "job_context",
        "type": "object",
        "description": "Job context information including job ID and run ID.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "job_run_id",
            "type": "integer",
            "description": "The job run ID where this API was invoked."
          }
        ]
      },
      {
        "name": "notebook_id",
        "type": "integer",
        "description": "The notebook ID where this API was invoked."
      }
    ]
  },
  {
    "name": "source",
    "type": "object",
    "description": "The data source of the feature.",
    "children": [
      {
        "name": "delta_table_source",
        "type": "object",
        "description": "A Delta table data source.",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
          },
          {
            "name": "entity_columns",
            "type": "array",
            "description": ""
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "Single WHERE clause to filter delta table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
          },
          {
            "name": "timeseries_column",
            "type": "string",
            "description": ""
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "A single SQL SELECT expression applied after filter_condition. Should contains all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the delta table are present in the DataSource dataframe."
          }
        ]
      },
      {
        "name": "feature_view_source",
        "type": "object",
        "description": "A data source composed from registered upstream Features.",
        "children": [
          {
            "name": "feature_references",
            "type": "array",
            "description": "The upstream Features this source reads. Must include at least one feature.",
            "children": [
              {
                "name": "feature",
                "type": "string",
                "description": "The three-part full name of the upstream Feature."
              }
            ]
          }
        ]
      },
      {
        "name": "kafka_source",
        "type": "object",
        "description": "A Kafka stream data source.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_column_identifiers",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "The filter condition applied to the source data before aggregation."
          },
          {
            "name": "timeseries_column_identifier",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "lateness",
        "type": "object",
        "description": "Completeness timing for this Feature's use of the source. This configuration is part of the Feature definition; it does not modify the underlying table or stream.",
        "children": [
          {
            "name": "settling_delay",
            "type": "string",
            "description": "Non-negative time to wait after a window ends before treating its source data as complete. Training shifts the eligible evaluation time backwards by this duration so it does not join data that would still have been settling online. Materialization waits for the duration to elapse before publishing the window. If unset, source data is considered settled immediately."
          }
        ]
      },
      {
        "name": "request_source",
        "type": "object",
        "description": "A request-time data source.",
        "children": [
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "A schema containing scalar or nested fields, in Spark StructType JSON format (from df.schema.json()). This preserves field, array-element, and map-value nullability."
          },
          {
            "name": "flat_schema",
            "type": "object",
            "description": "A flat schema with scalar-typed fields only.",
            "children": [
              {
                "name": "fields",
                "type": "array",
                "description": "The list of fields in this schema."
              }
            ]
          }
        ]
      },
      {
        "name": "sdp_source",
        "type": "object",
        "description": "A Spark Declarative Pipeline data source.",
        "children": [
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "Single WHERE clause to filter the pipeline's output table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
          },
          {
            "name": "input_tables",
            "type": "array",
            "description": "The full three-part names of the tables the pipeline reads from. Required to materialize this feature with a TableTrigger, which starts a run when these tables update. Each table must exist when the feature is created. Feature Store doesn't confirm that the pipeline reads from these tables. At most 100 tables."
          },
          {
            "name": "output_table",
            "type": "string",
            "description": "The full three-part (catalog, schema, table) name of the pipeline's output table to read from. The table doesn't need to exist until the pipeline first runs. Required."
          },
          {
            "name": "pipeline_id",
            "type": "string",
            "description": "The ID of the Spark Declarative Pipeline that Feature Store runs to produce this source, before each materialization or backfill. The pipeline must already exist when the feature is created, and you need CAN_RUN, CAN_MANAGE, or owner permission on it. It doesn't need to have run yet. Deleting the feature doesn't delete the pipeline. If the pipeline is deleted, this field reads back empty. Required."
          },
          {
            "name": "pipeline_state",
            "type": "string",
            "description": "State tracking pipeline execution and output table validation. PENDING until the pipeline has run at least once and created the output table; then RESOLVED on success, or ERROR on failure. (ERROR, PENDING, RESOLVED)"
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "A single SQL SELECT expression applied after filter_condition. Should contain all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the pipeline's output table are present in the DataSource dataframe."
          }
        ]
      },
      {
        "name": "stream_source",
        "type": "object",
        "description": "A Stream data source.",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": "Three-part full name of the Stream (catalog.schema.stream)."
          },
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Any subsequent functions operate against this dataframe."
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "The filter condition applied to the source data before aggregation."
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "The pipeline runs these SQL statements immediately after conversion into the schema specified on the Stream object."
          }
        ]
      }
    ]
  },
  {
    "name": "time_window",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "continuous",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "offset",
            "type": "string",
            "description": "The offset of the continuous window (must be non-positive)."
          }
        ]
      },
      {
        "name": "rolling",
        "type": "object",
        "description": "A rolling time window with an optional non-negative delay.",
        "children": [
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the rolling window. Must be positive when set; absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "sawtooth",
        "type": "object",
        "description": "A sawtooth window served via the hybrid batch + streaming path.",
        "children": [
          {
            "name": "delay",
            "type": "string",
            "description": "Delay is not currently supported for Sawtooth windows."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the window. Must be positive and span more than two days when set, so that both the batch (N-1 day) and stale-path (N-2 day) partial aggregates are well defined. The duration need not be a whole number of days (e.g. 3 days 15 minutes is allowed). Absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "sliding",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "slide_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "offset",
            "type": "string",
            "description": "Non-negative phase shift from the default midnight UTC alignment. For example, offset=22h on a 24h slide produces boundaries at 22:00 UTC (17:00 New York in standard time) instead of midnight UTC. If unset, the offset is zero. Must be shorter than slide_duration (and therefore window_duration)."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the sliding window. Must be positive when set; absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "start_time",
        "type": "string (date-time)",
        "description": "Earliest event-time boundary at which the Feature may emit an output. This gates outputs, not the historical inputs read by a window. For example, a 365-day window with start_time=2026-01-01 begins emitting partial-window values on that date instead of waiting for 365 days of data; a lifetime window produces no output before start_time. If unset, tumbling and fixed-duration sliding windows first emit at an offset-aligned boundary after a full window can be formed. If unset, lifetime sliding windows and rolling windows emit as soon as eligible source data exists. For sawtooth windows, start_time must not be later than the time the Feature is created. Not supported for rolling windows on Features with a stream source."
      },
      {
        "name": "tumbling",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "offset",
            "type": "string",
            "description": "Non-negative phase shift from the default midnight UTC alignment. For example, offset=22h on a 24h window produces boundaries at 22:00 UTC (17:00 New York in standard time) instead of midnight UTC. If unset, the offset is zero. Must be shorter than window_duration."
          }
        ]
      }
    ]
  },
  {
    "name": "timeseries_column",
    "type": "object",
    "description": "Column recording time, used for point-in-time joins, backfills, and aggregations. Optional since a timeseries column is not set for RequestSource features or on-demand calculated features.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
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
    "description": "Name of the feature, extracted from the full three-part name (catalog.schema.name)."
  },
  {
    "name": "catalog_name",
    "type": "string",
    "description": "Name of parent catalog."
  },
  {
    "name": "full_name",
    "type": "string",
    "description": ""
  },
  {
    "name": "schema_name",
    "type": "string",
    "description": "Name of parent schema relative to its parent catalog."
  },
  {
    "name": "created_at",
    "type": "string (date-time)",
    "description": "Time at which this feature was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Username of the feature creator."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the feature."
  },
  {
    "name": "entities",
    "type": "array",
    "description": "The entity columns for the feature, used as aggregation keys and for query-time lookup. Optional since entities are not set for RequestSource features or on-demand calculated features.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      }
    ]
  },
  {
    "name": "filter_condition",
    "type": "string",
    "description": ""
  },
  {
    "name": "function",
    "type": "object",
    "description": "The function by which the feature is computed.",
    "children": [
      {
        "name": "aggregation_function",
        "type": "object",
        "description": "An aggregation function applied over a time window.",
        "children": [
          {
            "name": "approx_count_distinct",
            "type": "object",
            "description": "Computes the approximate count of distinct values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the approximate count of distinct values is computed."
              },
              {
                "name": "relative_error",
                "type": "number",
                "description": "The error the user accepts, as a fraction of the count, between 0.02 (by default) and 0.3. This is one standard error of the estimate, the same meaning as Spark's relativeSD: 0.02 means the result is within ±2% of the true count about 68% of the time (one standard deviation covers 68% of the region). Feature Store picks the sketch size that gives this relative error. If neither relative_error nor relative_sd is set, 0.02 is default chosen at feature creation."
              },
              {
                "name": "relative_sd",
                "type": "number",
                "description": "The maximum relative standard deviation allowed (default defined by Spark). Deprecated: use relative_error. When relative_error is set, reads return the same value here for clients that don't have relative_error, and a request may only send that value."
              }
            ]
          },
          {
            "name": "approx_percentile",
            "type": "object",
            "description": "Computes the approximate percentile of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the approximate percentile is computed."
              },
              {
                "name": "percentile",
                "type": "number",
                "description": "The percentile value to compute (between 0 and 1)."
              },
              {
                "name": "accuracy",
                "type": "integer",
                "description": "The accuracy parameter (higher is more accurate but slower). Deprecated: use relative_error. When relative_error is set, reads return ceil(1 / relative_error) here for clients that don't have relative_error, and a request may only send that value."
              },
              {
                "name": "relative_error",
                "type": "number",
                "description": "The error the user accepts, as a fraction of rank, between 0.01 (by default) and 0.3. The result is within this rank error with 99% confidence: at 0.01, the value returned for p95 is between the true p94 and p96 at least 99% of the time. Feature Store picks the sketch size that gives this error. If neither relative_error nor accuracy is set, 0.01 is default chosen at feature creation."
              }
            ]
          },
          {
            "name": "avg",
            "type": "object",
            "description": "Computes the average of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the average is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "count_function",
            "type": "object",
            "description": "Computes the count of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the count is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "first",
            "type": "object",
            "description": "Returns the first value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first value is returned."
              }
            ]
          },
          {
            "name": "first_distinct",
            "type": "object",
            "description": "Returns the first N distinct values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first N distinct values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of distinct values to return."
              }
            ]
          },
          {
            "name": "first_n",
            "type": "object",
            "description": "Returns the first N values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the first N values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of values to return."
              }
            ]
          },
          {
            "name": "last",
            "type": "object",
            "description": "Returns the last value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last value is returned."
              }
            ]
          },
          {
            "name": "last_distinct",
            "type": "object",
            "description": "Returns the last N distinct values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last N distinct values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of distinct values to return."
              }
            ]
          },
          {
            "name": "last_n",
            "type": "object",
            "description": "Returns the last N values, ordered by the feature's timeseries column.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the last N values are returned."
              },
              {
                "name": "n",
                "type": "integer",
                "description": "The number of values to return."
              }
            ]
          },
          {
            "name": "max",
            "type": "object",
            "description": "Computes the maximum value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the maximum is computed."
              }
            ]
          },
          {
            "name": "min",
            "type": "object",
            "description": "Computes the minimum value.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the minimum is computed."
              }
            ]
          },
          {
            "name": "stddev_pop",
            "type": "object",
            "description": "Computes the population standard deviation.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the population standard deviation is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "stddev_samp",
            "type": "object",
            "description": "Computes the sample standard deviation.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sample standard deviation is computed."
              }
            ]
          },
          {
            "name": "sum",
            "type": "object",
            "description": "Computes the sum of values.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sum is computed. For Kafka sources, use dot-prefixed path notation (e.g., \"value.amount\"). For nested fields, the leaf node name is used. Colon-prefixed notation (e.g., \"value:amount\") is supported for backwards compatibility but is deprecated; migrate to dot notation."
              }
            ]
          },
          {
            "name": "time_window",
            "type": "object",
            "description": "The time window over which the aggregation is computed.",
            "children": [
              {
                "name": "continuous",
                "type": "object",
                "description": ""
              },
              {
                "name": "rolling",
                "type": "object",
                "description": "A rolling time window with an optional non-negative delay."
              },
              {
                "name": "sawtooth",
                "type": "object",
                "description": "A sawtooth window served via the hybrid batch + streaming path."
              },
              {
                "name": "sliding",
                "type": "object",
                "description": ""
              },
              {
                "name": "start_time",
                "type": "string (date-time)",
                "description": "Earliest event-time boundary at which the Feature may emit an output. This gates outputs, not the historical inputs read by a window. For example, a 365-day window with start_time=2026-01-01 begins emitting partial-window values on that date instead of waiting for 365 days of data; a lifetime window produces no output before start_time. If unset, tumbling and fixed-duration sliding windows first emit at an offset-aligned boundary after a full window can be formed. If unset, lifetime sliding windows and rolling windows emit as soon as eligible source data exists. For sawtooth windows, start_time must not be later than the time the Feature is created. Not supported for rolling windows on Features with a stream source."
              },
              {
                "name": "tumbling",
                "type": "object",
                "description": ""
              }
            ]
          },
          {
            "name": "var_pop",
            "type": "object",
            "description": "Computes the population variance.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the population variance is computed."
              }
            ]
          },
          {
            "name": "var_samp",
            "type": "object",
            "description": "Computes the sample variance.",
            "children": [
              {
                "name": "input",
                "type": "string",
                "description": "The input column from which the sample variance is computed."
              }
            ]
          }
        ]
      },
      {
        "name": "column_selection",
        "type": "object",
        "description": "Selects the latest value of a single column in a data source",
        "children": [
          {
            "name": "column",
            "type": "string",
            "description": "Column name from source to select as the feature value."
          }
        ]
      },
      {
        "name": "custom_udf",
        "type": "object",
        "description": "Applies a registered Unity Catalog function row-wise to source columns.",
        "children": [
          {
            "name": "function_path",
            "type": "string",
            "description": "Fully qualified 3-part Unity Catalog path of the function to apply."
          },
          {
            "name": "input_bindings",
            "type": "array",
            "description": "Binds each UC function parameter to a source column. May be empty for zero-argument functions (e.g. a timestamp generator).",
            "children": [
              {
                "name": "parameter",
                "type": "string",
                "description": "Name of the UC function parameter."
              },
              {
                "name": "column",
                "type": "string",
                "description": "Source column whose value is passed for this parameter at execution time."
              }
            ]
          }
        ]
      },
      {
        "name": "extra_parameters",
        "type": "array",
        "description": "",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": ""
          },
          {
            "name": "value",
            "type": "string",
            "description": "The value of the parameter."
          }
        ]
      },
      {
        "name": "function_type",
        "type": "string",
        "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (APPROX_COUNT_DISTINCT, APPROX_PERCENTILE, AVG, COUNT, FIRST, FUNCTION_TYPE_UNSPECIFIED, LAST, MAX, MIN, STDDEV_POP, STDDEV_SAMP, SUM, VAR_POP, VAR_SAMP)"
      }
    ]
  },
  {
    "name": "inputs",
    "type": "array",
    "description": ""
  },
  {
    "name": "lineage_context",
    "type": "object",
    "description": "Lineage context information for this feature. WARNING: This field is primarily intended for internal use by Databricks systems and is automatically populated when features are created through Databricks notebooks or jobs. Users should not manually set this field as incorrect values may lead to inaccurate lineage tracking or unexpected behavior. This field will be set by feature-engineering client and should be left unset by SDK and terraform users.",
    "children": [
      {
        "name": "job_context",
        "type": "object",
        "description": "Job context information including job ID and run ID.",
        "children": [
          {
            "name": "job_id",
            "type": "integer",
            "description": ""
          },
          {
            "name": "job_run_id",
            "type": "integer",
            "description": "The job run ID where this API was invoked."
          }
        ]
      },
      {
        "name": "notebook_id",
        "type": "integer",
        "description": "The notebook ID where this API was invoked."
      }
    ]
  },
  {
    "name": "source",
    "type": "object",
    "description": "The data source of the feature.",
    "children": [
      {
        "name": "delta_table_source",
        "type": "object",
        "description": "A Delta table data source.",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
          },
          {
            "name": "entity_columns",
            "type": "array",
            "description": ""
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "Single WHERE clause to filter delta table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
          },
          {
            "name": "timeseries_column",
            "type": "string",
            "description": ""
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "A single SQL SELECT expression applied after filter_condition. Should contains all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the delta table are present in the DataSource dataframe."
          }
        ]
      },
      {
        "name": "feature_view_source",
        "type": "object",
        "description": "A data source composed from registered upstream Features.",
        "children": [
          {
            "name": "feature_references",
            "type": "array",
            "description": "The upstream Features this source reads. Must include at least one feature.",
            "children": [
              {
                "name": "feature",
                "type": "string",
                "description": "The three-part full name of the upstream Feature."
              }
            ]
          }
        ]
      },
      {
        "name": "kafka_source",
        "type": "object",
        "description": "A Kafka stream data source.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "entity_column_identifiers",
            "type": "array",
            "description": "",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "The filter condition applied to the source data before aggregation."
          },
          {
            "name": "timeseries_column_identifier",
            "type": "object",
            "description": "",
            "children": [
              {
                "name": "variant_expr_path",
                "type": "string",
                "description": ""
              }
            ]
          }
        ]
      },
      {
        "name": "lateness",
        "type": "object",
        "description": "Completeness timing for this Feature's use of the source. This configuration is part of the Feature definition; it does not modify the underlying table or stream.",
        "children": [
          {
            "name": "settling_delay",
            "type": "string",
            "description": "Non-negative time to wait after a window ends before treating its source data as complete. Training shifts the eligible evaluation time backwards by this duration so it does not join data that would still have been settling online. Materialization waits for the duration to elapse before publishing the window. If unset, source data is considered settled immediately."
          }
        ]
      },
      {
        "name": "request_source",
        "type": "object",
        "description": "A request-time data source.",
        "children": [
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "A schema containing scalar or nested fields, in Spark StructType JSON format (from df.schema.json()). This preserves field, array-element, and map-value nullability."
          },
          {
            "name": "flat_schema",
            "type": "object",
            "description": "A flat schema with scalar-typed fields only.",
            "children": [
              {
                "name": "fields",
                "type": "array",
                "description": "The list of fields in this schema."
              }
            ]
          }
        ]
      },
      {
        "name": "sdp_source",
        "type": "object",
        "description": "A Spark Declarative Pipeline data source.",
        "children": [
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Required if transformation_sql is specified. Example: &#123;\"type\":\"struct\",\"fields\":[&#123;\"name\":\"col_a\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;,&#123;\"name\":\"col_c\",\"type\":\"integer\",\"nullable\":true,\"metadata\":&#123;&#125;&#125;]&#125;"
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "Single WHERE clause to filter the pipeline's output table before applying transformations. Will be row-wise evaluated, so should only include conditionals and projections."
          },
          {
            "name": "input_tables",
            "type": "array",
            "description": "The full three-part names of the tables the pipeline reads from. Required to materialize this feature with a TableTrigger, which starts a run when these tables update. Each table must exist when the feature is created. Feature Store doesn't confirm that the pipeline reads from these tables. At most 100 tables."
          },
          {
            "name": "output_table",
            "type": "string",
            "description": "The full three-part (catalog, schema, table) name of the pipeline's output table to read from. The table doesn't need to exist until the pipeline first runs. Required."
          },
          {
            "name": "pipeline_id",
            "type": "string",
            "description": "The ID of the Spark Declarative Pipeline that Feature Store runs to produce this source, before each materialization or backfill. The pipeline must already exist when the feature is created, and you need CAN_RUN, CAN_MANAGE, or owner permission on it. It doesn't need to have run yet. Deleting the feature doesn't delete the pipeline. If the pipeline is deleted, this field reads back empty. Required."
          },
          {
            "name": "pipeline_state",
            "type": "string",
            "description": "State tracking pipeline execution and output table validation. PENDING until the pipeline has run at least once and created the output table; then RESOLVED on success, or ERROR on failure. (ERROR, PENDING, RESOLVED)"
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "A single SQL SELECT expression applied after filter_condition. Should contain all the columns needed (eg. \"SELECT *, col_a + col_b AS col_c FROM x.y.z WHERE col_a &gt; 0\" would have ``transformation_sql`` \"*, col_a + col_b AS col_c\") If transformation_sql is not provided, all columns of the pipeline's output table are present in the DataSource dataframe."
          }
        ]
      },
      {
        "name": "stream_source",
        "type": "object",
        "description": "A Stream data source.",
        "children": [
          {
            "name": "full_name",
            "type": "string",
            "description": "Three-part full name of the Stream (catalog.schema.stream)."
          },
          {
            "name": "dataframe_schema",
            "type": "string",
            "description": "Schema of the resulting dataframe after transformations, in Spark StructType JSON format (from df.schema.json()). Any subsequent functions operate against this dataframe."
          },
          {
            "name": "filter_condition",
            "type": "string",
            "description": "The filter condition applied to the source data before aggregation."
          },
          {
            "name": "transformation_sql",
            "type": "string",
            "description": "The pipeline runs these SQL statements immediately after conversion into the schema specified on the Stream object."
          }
        ]
      }
    ]
  },
  {
    "name": "time_window",
    "type": "object",
    "description": "",
    "children": [
      {
        "name": "continuous",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "offset",
            "type": "string",
            "description": "The offset of the continuous window (must be non-positive)."
          }
        ]
      },
      {
        "name": "rolling",
        "type": "object",
        "description": "A rolling time window with an optional non-negative delay.",
        "children": [
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the rolling window. Must be positive when set; absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "sawtooth",
        "type": "object",
        "description": "A sawtooth window served via the hybrid batch + streaming path.",
        "children": [
          {
            "name": "delay",
            "type": "string",
            "description": "Delay is not currently supported for Sawtooth windows."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the window. Must be positive and span more than two days when set, so that both the batch (N-1 day) and stale-path (N-2 day) partial aggregates are well defined. The duration need not be a whole number of days (e.g. 3 days 15 minutes is allowed). Absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "sliding",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "slide_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "offset",
            "type": "string",
            "description": "Non-negative phase shift from the default midnight UTC alignment. For example, offset=22h on a 24h slide produces boundaries at 22:00 UTC (17:00 New York in standard time) instead of midnight UTC. If unset, the offset is zero. Must be shorter than slide_duration (and therefore window_duration)."
          },
          {
            "name": "window_duration",
            "type": "string",
            "description": "The duration of the sliding window. Must be positive when set; absent means lifetime (aggregate over the entity's entire history)."
          }
        ]
      },
      {
        "name": "start_time",
        "type": "string (date-time)",
        "description": "Earliest event-time boundary at which the Feature may emit an output. This gates outputs, not the historical inputs read by a window. For example, a 365-day window with start_time=2026-01-01 begins emitting partial-window values on that date instead of waiting for 365 days of data; a lifetime window produces no output before start_time. If unset, tumbling and fixed-duration sliding windows first emit at an offset-aligned boundary after a full window can be formed. If unset, lifetime sliding windows and rolling windows emit as soon as eligible source data exists. For sawtooth windows, start_time must not be later than the time the Feature is created. Not supported for rolling windows on Features with a stream source."
      },
      {
        "name": "tumbling",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "window_duration",
            "type": "string",
            "description": ""
          },
          {
            "name": "delay",
            "type": "string",
            "description": "Non-negative analytic lag that evaluates the window this far in the past. Use this for timing variations unrelated to source lateness, such as a 30-day count as of one week ago. If unset, the analytic lag is zero. It composes with source.lateness when both are set."
          },
          {
            "name": "offset",
            "type": "string",
            "description": "Non-negative phase shift from the default midnight UTC alignment. For example, offset=22h on a 24h window produces boundaries at 22:00 UTC (17:00 New York in standard time) instead of midnight UTC. If unset, the offset is zero. Must be shorter than window_duration."
          }
        ]
      }
    ]
  },
  {
    "name": "timeseries_column",
    "type": "object",
    "description": "Column recording time, used for point-in-time joins, backfills, and aggregations. Optional since a timeseries column is not set for RequestSource features or on-demand calculated features.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
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
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a Feature.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-schema_name"><code>schema_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Features.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-feature"><code>feature</code></a></td>
    <td></td>
    <td>Create a Feature.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-feature"><code>feature</code></a></td>
    <td></td>
    <td>Update a Feature.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete a Feature.</td>
</tr>
<tr>
    <td><a href="#backfill_features"><CopyableCode code="backfill_features" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-feature_full_names"><code>feature_full_names</code></a>, <a href="#parameter-backfill_ranges"><code>backfill_ranges</code></a></td>
    <td></td>
    <td>Backfill features.</td>
</tr>
<tr>
    <td><a href="#purge_feature_entities"><CopyableCode code="purge_feature_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-features"><code>features</code></a>, <a href="#parameter-entities_table"><code>entities_table</code></a></td>
    <td></td>
    <td>Purge materialized feature values for specified entities.</td>
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
<tr id="parameter-catalog_name">
    <td><CopyableCode code="catalog_name" /></td>
    <td><code>string</code></td>
    <td>Name of parent catalog for features of interest.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>Name of the feature to delete.</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Name of parent schema relative to its parent catalog.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>string</code></td>
    <td>Fields to update. The only supported path is description.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of results to return.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page based on a previous query.</td>
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

Get a Feature.

```sql
SELECT
name,
catalog_name,
full_name,
schema_name,
created_at,
created_by,
description,
entities,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window,
timeseries_column
FROM databricks_workspace.ml.feature_engineering
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Features.

```sql
SELECT
name,
catalog_name,
full_name,
schema_name,
created_at,
created_by,
description,
entities,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window,
timeseries_column
FROM databricks_workspace.ml.feature_engineering
WHERE catalog_name = '{{ catalog_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
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

Create a Feature.

```sql
INSERT INTO databricks_workspace.ml.feature_engineering (
feature,
deployment_name,
workspace_domain
)
SELECT 
'{{ feature }}' /* required */,
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
catalog_name,
full_name,
schema_name,
created_at,
created_by,
description,
entities,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window,
timeseries_column
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_engineering
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the feature_engineering resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the feature_engineering resource.
    - name: feature
      description: |
        Feature to create.
      value:
        full_name: "{{ full_name }}"
        source:
          delta_table_source:
            full_name: "{{ full_name }}"
            dataframe_schema: "{{ dataframe_schema }}"
            entity_columns:
              - "{{ entity_columns }}"
            filter_condition: "{{ filter_condition }}"
            timeseries_column: "{{ timeseries_column }}"
            transformation_sql: "{{ transformation_sql }}"
          feature_view_source:
            feature_references:
              - feature: "{{ feature }}"
          kafka_source:
            name: "{{ name }}"
            entity_column_identifiers:
              - variant_expr_path: "{{ variant_expr_path }}"
            filter_condition: "{{ filter_condition }}"
            timeseries_column_identifier:
              variant_expr_path: "{{ variant_expr_path }}"
          lateness:
            settling_delay: "{{ settling_delay }}"
          request_source:
            dataframe_schema: "{{ dataframe_schema }}"
            flat_schema:
              fields:
                - name: "{{ name }}"
                  data_type: "{{ data_type }}"
          sdp_source:
            dataframe_schema: "{{ dataframe_schema }}"
            filter_condition: "{{ filter_condition }}"
            input_tables:
              - "{{ input_tables }}"
            output_table: "{{ output_table }}"
            pipeline_id: "{{ pipeline_id }}"
            pipeline_state: "{{ pipeline_state }}"
            transformation_sql: "{{ transformation_sql }}"
          stream_source:
            full_name: "{{ full_name }}"
            dataframe_schema: "{{ dataframe_schema }}"
            filter_condition: "{{ filter_condition }}"
            transformation_sql: "{{ transformation_sql }}"
        function:
          aggregation_function:
            approx_count_distinct:
              input: "{{ input }}"
              relative_error: {{ relative_error }}
              relative_sd: {{ relative_sd }}
            approx_percentile:
              input: "{{ input }}"
              percentile: {{ percentile }}
              accuracy: {{ accuracy }}
              relative_error: {{ relative_error }}
            avg:
              input: "{{ input }}"
            count_function:
              input: "{{ input }}"
            first:
              input: "{{ input }}"
            first_distinct:
              input: "{{ input }}"
              n: {{ n }}
            first_n:
              input: "{{ input }}"
              n: {{ n }}
            last:
              input: "{{ input }}"
            last_distinct:
              input: "{{ input }}"
              n: {{ n }}
            last_n:
              input: "{{ input }}"
              n: {{ n }}
            max:
              input: "{{ input }}"
            min:
              input: "{{ input }}"
            stddev_pop:
              input: "{{ input }}"
            stddev_samp:
              input: "{{ input }}"
            sum:
              input: "{{ input }}"
            time_window:
              continuous:
                window_duration: "{{ window_duration }}"
                offset: "{{ offset }}"
              rolling:
                delay: "{{ delay }}"
                window_duration: "{{ window_duration }}"
              sawtooth:
                delay: "{{ delay }}"
                window_duration: "{{ window_duration }}"
              sliding:
                slide_duration: "{{ slide_duration }}"
                delay: "{{ delay }}"
                offset: "{{ offset }}"
                window_duration: "{{ window_duration }}"
              start_time: "{{ start_time }}"
              tumbling:
                window_duration: "{{ window_duration }}"
                delay: "{{ delay }}"
                offset: "{{ offset }}"
            var_pop:
              input: "{{ input }}"
            var_samp:
              input: "{{ input }}"
          column_selection:
            column: "{{ column }}"
          custom_udf:
            function_path: "{{ function_path }}"
            input_bindings:
              - parameter: "{{ parameter }}"
                column: "{{ column }}"
          extra_parameters:
            - key: "{{ key }}"
              value: "{{ value }}"
          function_type: "{{ function_type }}"
        catalog_name: "{{ catalog_name }}"
        created_at: "{{ created_at }}"
        created_by: "{{ created_by }}"
        description: "{{ description }}"
        entities:
          - name: "{{ name }}"
        filter_condition: "{{ filter_condition }}"
        inputs:
          - "{{ inputs }}"
        lineage_context:
          job_context:
            job_id: {{ job_id }}
            job_run_id: {{ job_run_id }}
          notebook_id: {{ notebook_id }}
        name: "{{ name }}"
        schema_name: "{{ schema_name }}"
        time_window:
          continuous:
            window_duration: "{{ window_duration }}"
            offset: "{{ offset }}"
          rolling:
            delay: "{{ delay }}"
            window_duration: "{{ window_duration }}"
          sawtooth:
            delay: "{{ delay }}"
            window_duration: "{{ window_duration }}"
          sliding:
            slide_duration: "{{ slide_duration }}"
            delay: "{{ delay }}"
            offset: "{{ offset }}"
            window_duration: "{{ window_duration }}"
          start_time: "{{ start_time }}"
          tumbling:
            window_duration: "{{ window_duration }}"
            delay: "{{ delay }}"
            offset: "{{ offset }}"
        timeseries_column:
          name: "{{ name }}"
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

Update a Feature.

```sql
UPDATE databricks_workspace.ml.feature_engineering
SET 
feature = '{{ feature }}'
WHERE 
full_name = '{{ full_name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND feature = '{{ feature }}' --required
RETURNING
name,
catalog_name,
full_name,
schema_name,
created_at,
created_by,
description,
entities,
filter_condition,
function,
inputs,
lineage_context,
source,
time_window,
timeseries_column;
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

Delete a Feature.

```sql
DELETE FROM databricks_workspace.ml.feature_engineering
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="backfill_features"
    values={[
        { label: 'backfill_features', value: 'backfill_features' },
        { label: 'purge_feature_entities', value: 'purge_feature_entities' }
    ]}
>
<TabItem value="backfill_features">

Backfill features.

```sql
EXEC databricks_workspace.ml.feature_engineering.backfill_features 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"feature_full_names": "{{ feature_full_names }}", 
"backfill_ranges": "{{ backfill_ranges }}", 
"budget_policy_id": "{{ budget_policy_id }}", 
"request_id": "{{ request_id }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
<TabItem value="purge_feature_entities">

Purge materialized feature values for specified entities.

```sql
EXEC databricks_workspace.ml.feature_engineering.purge_feature_entities 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"features": "{{ features }}", 
"entities_table": "{{ entities_table }}", 
"budget_policy_id": "{{ budget_policy_id }}", 
"delete_rows": {{ delete_rows }}, 
"request_id": "{{ request_id }}", 
"tags": "{{ tags }}"
}'
;
```
</TabItem>
</Tabs>
