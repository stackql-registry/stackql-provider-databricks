---
title: ai_gateway_model_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_model_services
  - catalog
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_model_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_model_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_model_services" /></td></tr>
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
    "description": "Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the model service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Destinations, routing, rate limits, and payload logging configuration. Required on Create. On Update, provide this field when ``update_mask`` contains ``config`` or one of its subpaths.",
    "children": [
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table configuration for payload logging.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent Unity Catalog schema where the inference table is created, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required when configuring an inference table. After the inference table is created, this field cannot be changed."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced inference table has been deleted. The configuration remains visible so you can identify the broken dependency. Payload logging cannot continue until the table is restored or the configuration is updated."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix used to form the inference table's registered name. AI Gateway appends ``_payload``; for example, ``table_name_prefix = \"orders\"`` creates ``orders_payload``. If unset, the prefix defaults to the service name. Read ``table`` from the response for the resulting resource name. After the inference table is created, this field cannot be changed."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits applied to requests routed through this model service.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope of the rate limit. Depending on this value, the limit applies to a principal, the service as a whole, or each user by default. (RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required when ``key`` applies to a user, group, or service principal; otherwise it must be unset."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Maximum requests allowed in one renewal period. Leave unset for no request limit. Set to ``0`` to deny all requests."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Maximum tokens allowed in one renewal period. Leave unset for no token limit. Set to ``0`` to deny all requests."
          }
        ]
      },
      {
        "name": "routing",
        "type": "object",
        "description": "Routing configuration: destinations and fallback.",
        "children": [
          {
            "name": "destinations",
            "type": "array",
            "description": "Primary routing destinations. At most 10 are allowed. At least one is required on Create. On Update, provide this list when replacing the full ``config`` or updating ``config.routing.destinations``; other granular routing updates do not require resending destinations. The intermediate ``config.routing`` mask path is not supported.",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": "User-facing label for this destination, used in routing references."
              },
              {
                "name": "destination_type",
                "type": "string",
                "description": "Backing-model category. Provide the matching type-specific configuration and leave the other type-specific configurations unset. (DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL, DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL, DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL)"
              },
              {
                "name": "external_model_config",
                "type": "object",
                "description": "Configuration for an external model reached through a model provider service."
              },
              {
                "name": "is_deleted",
                "type": "boolean",
                "description": "Whether the destination's backing model or model provider service has been deleted. The destination remains visible so you can identify the broken dependency. Requests cannot use this destination until the backing resource is restored or the destination is replaced."
              },
              {
                "name": "pay_per_token_config",
                "type": "object",
                "description": "Configuration for a pay-per-token Databricks foundation model."
              },
              {
                "name": "provisioned_throughput_config",
                "type": "object",
                "description": "Configuration for a provisioned-throughput Databricks foundation model."
              },
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": "Percentage of primary traffic sent to this destination, from 0 to 100. Required when there is more than one primary destination, in which case the primary percentages must sum to 100; a single primary destination receives all traffic. Fallback destinations are ordered and do not use this field."
              }
            ]
          },
          {
            "name": "fallback",
            "type": "object",
            "description": "Fallback routing applied after a primary destination fails. Fallback destinations are tried in the listed order.",
            "children": [
              {
                "name": "destinations",
                "type": "array",
                "description": "Fallback destinations, tried in the listed order. At most 5 are allowed."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the model service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the model service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "supported_api_types",
    "type": "array",
    "description": "API types supported across this service's destinations, such as ``openai/v1/chat/completions``, ``openai/v1/embeddings``, and ``mlflow/v1/chat/completions``. Derived from the backing models and providers at read time."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the model service was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Identity of the last updater."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the model service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Destinations, routing, rate limits, and payload logging configuration. Required on Create. On Update, provide this field when ``update_mask`` contains ``config`` or one of its subpaths.",
    "children": [
      {
        "name": "inference_table",
        "type": "object",
        "description": "Inference table configuration for payload logging.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent Unity Catalog schema where the inference table is created, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required when configuring an inference table. After the inference table is created, this field cannot be changed."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced inference table has been deleted. The configuration remains visible so you can identify the broken dependency. Payload logging cannot continue until the table is restored or the configuration is updated."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix used to form the inference table's registered name. AI Gateway appends ``_payload``; for example, ``table_name_prefix = \"orders\"`` creates ``orders_payload``. If unset, the prefix defaults to the service name. Read ``table`` from the response for the resulting resource name. After the inference table is created, this field cannot be changed."
          }
        ]
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits applied to requests routed through this model service.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope of the rate limit. Depending on this value, the limit applies to a principal, the service as a whole, or each user by default. (RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required when ``key`` applies to a user, group, or service principal; otherwise it must be unset."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Maximum requests allowed in one renewal period. Leave unset for no request limit. Set to ``0`` to deny all requests."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Maximum tokens allowed in one renewal period. Leave unset for no token limit. Set to ``0`` to deny all requests."
          }
        ]
      },
      {
        "name": "routing",
        "type": "object",
        "description": "Routing configuration: destinations and fallback.",
        "children": [
          {
            "name": "destinations",
            "type": "array",
            "description": "Primary routing destinations. At most 10 are allowed. At least one is required on Create. On Update, provide this list when replacing the full ``config`` or updating ``config.routing.destinations``; other granular routing updates do not require resending destinations. The intermediate ``config.routing`` mask path is not supported.",
            "children": [
              {
                "name": "name",
                "type": "string",
                "description": "User-facing label for this destination, used in routing references."
              },
              {
                "name": "destination_type",
                "type": "string",
                "description": "Backing-model category. Provide the matching type-specific configuration and leave the other type-specific configurations unset. (DESTINATION_TYPE_EXTERNAL_FOUNDATION_MODEL, DESTINATION_TYPE_PAY_PER_TOKEN_FOUNDATION_MODEL, DESTINATION_TYPE_PROVISIONED_THROUGHPUT_FOUNDATION_MODEL)"
              },
              {
                "name": "external_model_config",
                "type": "object",
                "description": "Configuration for an external model reached through a model provider service."
              },
              {
                "name": "is_deleted",
                "type": "boolean",
                "description": "Whether the destination's backing model or model provider service has been deleted. The destination remains visible so you can identify the broken dependency. Requests cannot use this destination until the backing resource is restored or the destination is replaced."
              },
              {
                "name": "pay_per_token_config",
                "type": "object",
                "description": "Configuration for a pay-per-token Databricks foundation model."
              },
              {
                "name": "provisioned_throughput_config",
                "type": "object",
                "description": "Configuration for a provisioned-throughput Databricks foundation model."
              },
              {
                "name": "traffic_percentage",
                "type": "integer",
                "description": "Percentage of primary traffic sent to this destination, from 0 to 100. Required when there is more than one primary destination, in which case the primary percentages must sum to 100; a single primary destination receives all traffic. Fallback destinations are ordered and do not use this field."
              }
            ]
          },
          {
            "name": "fallback",
            "type": "object",
            "description": "Fallback routing applied after a primary destination fails. Fallback destinations are tried in the listed order.",
            "children": [
              {
                "name": "destinations",
                "type": "array",
                "description": "Fallback destinations, tried in the listed order. At most 5 are allowed."
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the model service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the model service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "supported_api_types",
    "type": "array",
    "description": "API types supported across this service's destinations, such as ``openai/v1/chat/completions``, ``openai/v1/embeddings``, and ``mlflow/v1/chat/completions``. Derived from the backing models and providers at read time."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the model service was last modified."
  },
  {
    "name": "updated_by",
    "type": "string",
    "description": "Identity of the last updater."
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
    <td>Returns the model service identified by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists the model services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-model_service_id"><code>model_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a model service in a Unity Catalog schema. A model service is a governed AI Gateway endpoint</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Updates a model service. Only the fields named in ``update_mask`` are changed; the resource name is</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the</td>
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
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The `full_name` segment of the `name` resource name (`model-services/&#123;full_name&#125;`). Resource name of the model service. Format: ``model-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-model_service_id">
    <td><CopyableCode code="model_service_id" /></td>
    <td><code>string</code></td>
    <td>Name for the model service, e.g. "my_model_service".</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Use ``config`` to replace the entire configuration. The replacement must include every required field; any optional field you omit is cleared. To preserve sibling fields, use one or more granular paths: ``comment``, ``config.routing.destinations``, ``config.routing.fallback.destinations``, ``config.rate_limits``, or ``config.inference_table``. Intermediate paths such as ``config.routing`` and ``config.routing.fallback`` are not supported.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-etag">
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Optimistic concurrency token from the most recent read. When set, the delete succeeds only if the resource has not changed. Leave unset for an unconditional delete. For REST requests, URL-encode the base64 string returned by the API when setting the ``etag`` query parameter.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of model services to return. Defaults to 200 when unset or 0; the maximum is 1000 for ``view = BASIC`` and 200 for ``view = FULL``. Use ``page_token`` to retrieve additional pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from the previous response.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent schema to list within, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>Fields to return for each service. ``FULL`` includes destinations, inference-table details, and rate-limit principal names. ``BASIC`` omits destinations and inference-table details and omits principal names from rate limits. Defaults to ``BASIC`` when unset.</td>
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

Returns the model service identified by its resource name.

```sql
SELECT
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
supported_api_types,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the model services in a Unity Catalog schema. Provide ``parent`` as

```sql
SELECT
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
supported_api_types,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent = '{{ parent }}'
AND view = '{{ view }}'
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

Creates a model service in a Unity Catalog schema. A model service is a governed AI Gateway endpoint

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_model_services (
comment,
config,
create_time,
created_by,
effective_owner,
etag,
metastore_id,
name,
supported_api_types,
update_time,
updated_by,
parent,
model_service_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ comment }}',
'{{ config }}',
'{{ create_time }}',
'{{ created_by }}',
'{{ effective_owner }}',
'{{ etag }}',
'{{ metastore_id }}',
'{{ name }}',
'{{ supported_api_types }}',
'{{ update_time }}',
'{{ updated_by }}',
'{{ parent }}',
'{{ model_service_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
supported_api_types,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_model_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: model_service_id
      value: "{{ model_service_id }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the ai_gateway_model_services resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided description.
    - name: config
      description: |
        Destinations, routing, rate limits, and payload logging configuration. Required on Create. On Update, provide this field when \`\`update_mask\`\` contains \`\`config\`\` or one of its subpaths.
      value:
        inference_table:
          parent: "{{ parent }}"
          is_deleted: {{ is_deleted }}
          table: "{{ table }}"
          table_name_prefix: "{{ table_name_prefix }}"
        rate_limits:
          - key: "{{ key }}"
            renewal_period: "{{ renewal_period }}"
            principal: "{{ principal }}"
            requests: {{ requests }}
            tokens: {{ tokens }}
        routing:
          destinations:
            - name: "{{ name }}"
              destination_type: "{{ destination_type }}"
              external_model_config:
                model_provider_service: "{{ model_provider_service }}"
                target:
                  model: "{{ model }}"
                  endpoint_route: "{{ endpoint_route }}"
                  native_api_types: "{{ native_api_types }}"
              is_deleted: {{ is_deleted }}
              pay_per_token_config:
                model: "{{ model }}"
              provisioned_throughput_config:
                model_serving_endpoint: "{{ model_serving_endpoint }}"
                model: "{{ model }}"
              traffic_percentage: {{ traffic_percentage }}
          fallback:
            destinations:
              - name: "{{ name }}"
                destination_type: "{{ destination_type }}"
                external_model_config:
                  model_provider_service: "{{ model_provider_service }}"
                  target: "{{ target }}"
                is_deleted: {{ is_deleted }}
                pay_per_token_config:
                  model: "{{ model }}"
                provisioned_throughput_config:
                  model_serving_endpoint: "{{ model_serving_endpoint }}"
                  model: "{{ model }}"
                traffic_percentage: {{ traffic_percentage }}
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time the model service was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        Creator identity.
    - name: effective_owner
      value: "{{ effective_owner }}"
      description: |
        Owner of the model service.
    - name: etag
      value: "{{ etag }}"
      description: |
        Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's \`\`etag\`\` field. In REST responses, this value is a base64 string; URL-encode it when setting the \`\`etag\`\` query parameter.
    - name: metastore_id
      value: "{{ metastore_id }}"
      description: |
        Metastore hosting the model service.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name of the model service. Format: \`\`model-services/{catalog}.{schema}.{model_service}\`\`. Each \`\`{...}\`\` component is capped at 255 characters individually. Server-derived on Create from \`\`parent\`\` + \`\`model_service_id\`\`; required and immutable on Update/Get/Delete.
    - name: supported_api_types
      value:
        - "{{ supported_api_types }}"
      description: |
        API types supported across this service's destinations, such as \`\`openai/v1/chat/completions\`\`, \`\`openai/v1/embeddings\`\`, and \`\`mlflow/v1/chat/completions\`\`. Derived from the backing models and providers at read time.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time the model service was last modified.
    - name: updated_by
      value: "{{ updated_by }}"
      description: |
        Identity of the last updater.
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

Updates a model service. Only the fields named in ``update_mask`` are changed; the resource name is

```sql
UPDATE databricks_workspace.catalog.ai_gateway_model_services
SET 
comment = '{{ comment }}',
config = '{{ config }}',
create_time = '{{ create_time }}',
created_by = '{{ created_by }}',
effective_owner = '{{ effective_owner }}',
etag = '{{ etag }}',
metastore_id = '{{ metastore_id }}',
name = '{{ name }}',
supported_api_types = '{{ supported_api_types }}',
update_time = '{{ update_time }}',
updated_by = '{{ updated_by }}'
WHERE 
full_name = '{{ full_name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND etag = '{{ etag}}'
RETURNING
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
supported_api_types,
update_time,
updated_by;
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

Deletes the model service identified by its resource name. Optionally supply an ``etag`` to make the

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_model_services
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>
