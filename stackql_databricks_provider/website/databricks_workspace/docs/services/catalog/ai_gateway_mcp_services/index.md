---
title: ai_gateway_mcp_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_mcp_services
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_mcp_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_mcp_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_mcp_services" /></td></tr>
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
    "description": "Resource name of the MCP service. Format: ``mcp-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;mcp_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``mcp_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the MCP service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Connection, tool selectors, and rate limits. Required on Create. On Update, provide this field when ``update_mask`` contains ``config`` or one of its subpaths.",
    "children": [
      {
        "name": "include_tool_selectors",
        "type": "array",
        "description": "Tool names or prefix patterns to expose from the MCP server. Use exact tool names or prefix patterns such as ``read_*``. An empty list exposes all tools. At most 1,024 selectors are allowed, and each selector can contain at most 256 characters."
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits for tool invocations. Supported scopes are user, group, service principal, the service as a whole, and each user by default. Request and token limits are supported. Empty when no rate limit is configured.",
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
        "name": "source_connection",
        "type": "object",
        "description": "Unity Catalog connection referencing the MCP server. Required on Create.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Resource name of the Unity Catalog connection used to access the MCP server, in the form ``connections/&#123;catalog&#125;.&#123;schema&#125;.&#123;connection&#125;``."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced connection has been deleted. The MCP service keeps the reference so callers can identify the broken dependency; tool invocation fails until the source connection is updated."
          },
          {
            "name": "options",
            "type": "object",
            "description": "Options needed to build the U2M authorize request, returned as a flat map. When set, it includes: ``authorization_endpoint`` (OAuth authorize URL), ``token_endpoint`` (token-exchange URL), ``oauth_scope`` (space-separated scopes to request), ``client_id`` (OAuth client id), and ``oauth_provider`` (the OAuth provider)."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the MCP service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the MCP service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the MCP service was last modified."
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
    "description": "Resource name of the MCP service. Format: ``mcp-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;mcp_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``mcp_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the MCP service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Connection, tool selectors, and rate limits. Required on Create. On Update, provide this field when ``update_mask`` contains ``config`` or one of its subpaths.",
    "children": [
      {
        "name": "include_tool_selectors",
        "type": "array",
        "description": "Tool names or prefix patterns to expose from the MCP server. Use exact tool names or prefix patterns such as ``read_*``. An empty list exposes all tools. At most 1,024 selectors are allowed, and each selector can contain at most 256 characters."
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits for tool invocations. Supported scopes are user, group, service principal, the service as a whole, and each user by default. Request and token limits are supported. Empty when no rate limit is configured.",
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
        "name": "source_connection",
        "type": "object",
        "description": "Unity Catalog connection referencing the MCP server. Required on Create.",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": "Resource name of the Unity Catalog connection used to access the MCP server, in the form ``connections/&#123;catalog&#125;.&#123;schema&#125;.&#123;connection&#125;``."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced connection has been deleted. The MCP service keeps the reference so callers can identify the broken dependency; tool invocation fails until the source connection is updated."
          },
          {
            "name": "options",
            "type": "object",
            "description": "Options needed to build the U2M authorize request, returned as a flat map. When set, it includes: ``authorization_endpoint`` (OAuth authorize URL), ``token_endpoint`` (token-exchange URL), ``oauth_scope`` (space-separated scopes to request), ``client_id`` (OAuth client id), and ``oauth_provider`` (the OAuth provider)."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the MCP service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the MCP service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the MCP service was last modified."
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
    <td>Returns the MCP service identified by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists the MCP services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-mcp_service_id"><code>mcp_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates an MCP service in a Unity Catalog schema. An MCP (Model Context Protocol) service is a</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Updates an MCP service. Only the fields named in ``update_mask`` are changed; the resource name is</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the MCP service identified by its resource name. Optionally supply an ``etag`` to make the</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The `full_name` segment of the `name` resource name (`mcp-services/&#123;full_name&#125;`). Resource name of the MCP service. Format: ``mcp-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;mcp_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-mcp_service_id">
    <td><CopyableCode code="mcp_service_id" /></td>
    <td><code>string</code></td>
    <td>Name for the MCP service, e.g. "my_mcp_service".</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Use ``config`` to replace the entire configuration. The replacement must include every required field; any optional field you omit is cleared. To preserve sibling fields, use one or more granular paths: ``comment``, ``config.source_connection.name``, ``config.include_tool_selectors``, or ``config.rate_limits``.</td>
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
    <td>Maximum number of MCP services to return. Defaults to 200 when unset or 0; the maximum is 1000 for ``view = BASIC`` and 200 for ``view = FULL``. Use ``page_token`` to retrieve additional pages.</td>
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
    <td>Fields to return for each service. ``FULL`` includes source-connection details and rate-limit principal names. ``BASIC`` omits the source connection and omits principal names from rate limits. Defaults to ``BASIC`` when unset.</td>
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

Returns the MCP service identified by its resource name.

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
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_mcp_services
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the MCP services in a Unity Catalog schema. Provide ``parent`` as

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
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_mcp_services
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

Creates an MCP service in a Unity Catalog schema. An MCP (Model Context Protocol) service is a

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_mcp_services (
comment,
config,
create_time,
created_by,
effective_owner,
etag,
metastore_id,
name,
update_time,
updated_by,
parent,
mcp_service_id,
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
'{{ update_time }}',
'{{ updated_by }}',
'{{ parent }}',
'{{ mcp_service_id }}',
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
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_mcp_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_mcp_services resource.
    - name: mcp_service_id
      value: "{{ mcp_service_id }}"
      description: Required parameter for the ai_gateway_mcp_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_mcp_services resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the ai_gateway_mcp_services resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided description.
    - name: config
      description: |
        Connection, tool selectors, and rate limits. Required on Create. On Update, provide this field when \`\`update_mask\`\` contains \`\`config\`\` or one of its subpaths.
      value:
        include_tool_selectors:
          - "{{ include_tool_selectors }}"
        rate_limits:
          - key: "{{ key }}"
            renewal_period: "{{ renewal_period }}"
            principal: "{{ principal }}"
            requests: {{ requests }}
            tokens: {{ tokens }}
        source_connection:
          name: "{{ name }}"
          is_deleted: {{ is_deleted }}
          options: "{{ options }}"
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time the MCP service was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        Creator identity.
    - name: effective_owner
      value: "{{ effective_owner }}"
      description: |
        Owner of the MCP service.
    - name: etag
      value: "{{ etag }}"
      description: |
        Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's \`\`etag\`\` field. In REST responses, this value is a base64 string; URL-encode it when setting the \`\`etag\`\` query parameter.
    - name: metastore_id
      value: "{{ metastore_id }}"
      description: |
        Metastore hosting the MCP service.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name of the MCP service. Format: \`\`mcp-services/{catalog}.{schema}.{mcp_service}\`\`. Each \`\`{...}\`\` component is capped at 255 characters individually. Server-derived on Create from \`\`parent\`\` + \`\`mcp_service_id\`\`; required and immutable on Update/Get/Delete.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time the MCP service was last modified.
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

Updates an MCP service. Only the fields named in ``update_mask`` are changed; the resource name is

```sql
UPDATE databricks_workspace.catalog.ai_gateway_mcp_services
SET 
comment = '{{ comment }}',
config = '{{ config }}',
create_time = '{{ create_time }}',
created_by = '{{ created_by }}',
effective_owner = '{{ effective_owner }}',
etag = '{{ etag }}',
metastore_id = '{{ metastore_id }}',
name = '{{ name }}',
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

Deletes the MCP service identified by its resource name. Optionally supply an ``etag`` to make the

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_mcp_services
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>
