---
title: private_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - private_network_gateways
  - networking
  - databricks_account
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage databricks_account resources using SQL
custom_edit_url: null
image: /img/stackql-databricks_account-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SchemaTable from '@site/src/components/SchemaTable/SchemaTable';

Creates, updates, deletes, gets or lists a <code>private_network_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="private_network_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.networking.private_network_gateways" /></td></tr>
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
    "description": "The canonical resource name of the gateway, in the form ``accounts/&#123;account_id&#125;/network-connectivity-configs/&#123;ncc_id&#125;/private-network-gateways/&#123;gateway_id&#125;``."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The human-readable name of the gateway."
  },
  {
    "name": "aws_cloud_connection",
    "type": "object",
    "description": "The AWS connection used by the gateway.",
    "children": [
      {
        "name": "gateway_subnets",
        "type": "array",
        "description": "The subnets where the gateway establishes connectivity.",
        "children": [
          {
            "name": "subnet_id",
            "type": "string",
            "description": "The AWS subnet ID."
          }
        ]
      },
      {
        "name": "cross_account_role",
        "type": "object",
        "description": "The IAM role that Databricks assumes to manage gateway resources.",
        "children": [
          {
            "name": "role_arn",
            "type": "string",
            "description": "The ARN of the IAM role."
          }
        ]
      },
      {
        "name": "security_group_ids",
        "type": "array",
        "description": "The security groups attached to the gateway network interface."
      }
    ]
  },
  {
    "name": "azure_cloud_connection",
    "type": "object",
    "description": "The Azure connection used by the gateway.",
    "children": [
      {
        "name": "gateway_subnet",
        "type": "object",
        "description": "The subnet where the gateway establishes connectivity.",
        "children": [
          {
            "name": "resource_id",
            "type": "string",
            "description": "The full Azure resource ID of the subnet."
          }
        ]
      }
    ]
  },
  {
    "name": "bandwidth_tier_gigabits_per_second",
    "type": "integer",
    "description": "The provisioned bandwidth tier for an Azure gateway, in gigabits per second. Required when creating an Azure gateway."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The time when the gateway was created."
  },
  {
    "name": "destinations",
    "type": "array",
    "description": "The destinations routed through this gateway.",
    "children": [
      {
        "name": "destination_type",
        "type": "string",
        "description": "The destination type. (DNS_NAME)"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The destination value."
      }
    ]
  },
  {
    "name": "error_message",
    "type": "string",
    "description": "The failure reason when the gateway is in the FAILED state."
  },
  {
    "name": "private_dns_resolvers",
    "type": "array",
    "description": "The DNS resolvers used for private name resolution.",
    "children": [
      {
        "name": "resolver_type",
        "type": "string",
        "description": "The resolver type. (IP_ADDRESS)"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The resolver value."
      }
    ]
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current lifecycle state of the gateway. (CREATING, DELETING, ESTABLISHED, FAILED)"
  },
  {
    "name": "traffic_mode",
    "type": "string",
    "description": "The traffic routed through this gateway. (ALL_TRAFFIC, SPECIFIC_DESTINATIONS)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The time when the gateway was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "The canonical resource name of the gateway, in the form ``accounts/&#123;account_id&#125;/network-connectivity-configs/&#123;ncc_id&#125;/private-network-gateways/&#123;gateway_id&#125;``."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The human-readable name of the gateway."
  },
  {
    "name": "aws_cloud_connection",
    "type": "object",
    "description": "The AWS connection used by the gateway.",
    "children": [
      {
        "name": "gateway_subnets",
        "type": "array",
        "description": "The subnets where the gateway establishes connectivity.",
        "children": [
          {
            "name": "subnet_id",
            "type": "string",
            "description": "The AWS subnet ID."
          }
        ]
      },
      {
        "name": "cross_account_role",
        "type": "object",
        "description": "The IAM role that Databricks assumes to manage gateway resources.",
        "children": [
          {
            "name": "role_arn",
            "type": "string",
            "description": "The ARN of the IAM role."
          }
        ]
      },
      {
        "name": "security_group_ids",
        "type": "array",
        "description": "The security groups attached to the gateway network interface."
      }
    ]
  },
  {
    "name": "azure_cloud_connection",
    "type": "object",
    "description": "The Azure connection used by the gateway.",
    "children": [
      {
        "name": "gateway_subnet",
        "type": "object",
        "description": "The subnet where the gateway establishes connectivity.",
        "children": [
          {
            "name": "resource_id",
            "type": "string",
            "description": "The full Azure resource ID of the subnet."
          }
        ]
      }
    ]
  },
  {
    "name": "bandwidth_tier_gigabits_per_second",
    "type": "integer",
    "description": "The provisioned bandwidth tier for an Azure gateway, in gigabits per second. Required when creating an Azure gateway."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The time when the gateway was created."
  },
  {
    "name": "destinations",
    "type": "array",
    "description": "The destinations routed through this gateway.",
    "children": [
      {
        "name": "destination_type",
        "type": "string",
        "description": "The destination type. (DNS_NAME)"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The destination value."
      }
    ]
  },
  {
    "name": "error_message",
    "type": "string",
    "description": "The failure reason when the gateway is in the FAILED state."
  },
  {
    "name": "private_dns_resolvers",
    "type": "array",
    "description": "The DNS resolvers used for private name resolution.",
    "children": [
      {
        "name": "resolver_type",
        "type": "string",
        "description": "The resolver type. (IP_ADDRESS)"
      },
      {
        "name": "value",
        "type": "string",
        "description": "The resolver value."
      }
    ]
  },
  {
    "name": "state",
    "type": "string",
    "description": "The current lifecycle state of the gateway. (CREATING, DELETING, ESTABLISHED, FAILED)"
  },
  {
    "name": "traffic_mode",
    "type": "string",
    "description": "The traffic routed through this gateway. (ALL_TRAFFIC, SPECIFIC_DESTINATIONS)"
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The time when the gateway was last updated."
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
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ncc_id"><code>ncc_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Gets a private network gateway.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ncc_id"><code>ncc_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td><a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists private network gateways under a network connectivity configuration.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ncc_id"><code>ncc_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-private_network_gateway"><code>private_network_gateway</code></a></td>
    <td><a href="#parameter-request_id"><code>request_id</code></a></td>
    <td>Creates a private network gateway.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ncc_id"><code>ncc_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-account_host"><code>account_host</code></a>, <a href="#parameter-private_network_gateway"><code>private_network_gateway</code></a></td>
    <td></td>
    <td>Updates a private network gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-account_id"><code>account_id</code></a>, <a href="#parameter-ncc_id"><code>ncc_id</code></a>, <a href="#parameter-gateway_id"><code>gateway_id</code></a>, <a href="#parameter-account_host"><code>account_host</code></a></td>
    <td></td>
    <td>Permanently deletes a private network gateway.</td>
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
<tr id="parameter-account_host">
    <td><CopyableCode code="account_host" /></td>
    <td><code>string</code></td>
    <td>The Databricks account console host. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws), or set explicitly with DATABRICKS_ACCOUNT_HOST (bare host, no scheme). (default: accounts.cloud.databricks.com, x-stackQL-envVar: DATABRICKS_ACCOUNT_HOST, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"accounts.cloud.databricks.com","azure":"accounts.azuredatabricks.net","gcp":"accounts.gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-account_id">
    <td><CopyableCode code="account_id" /></td>
    <td><code>string</code></td>
    <td>The `account_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/network-connectivity-configs/&#123;ncc_id&#125;/private-network-gateways/&#123;gateway_id&#125;`). The canonical resource name of the gateway.</td>
</tr>
<tr id="parameter-gateway_id">
    <td><CopyableCode code="gateway_id" /></td>
    <td><code>string</code></td>
    <td>The `gateway_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/network-connectivity-configs/&#123;ncc_id&#125;/private-network-gateways/&#123;gateway_id&#125;`). The canonical resource name of the gateway.</td>
</tr>
<tr id="parameter-ncc_id">
    <td><CopyableCode code="ncc_id" /></td>
    <td><code>string</code></td>
    <td>The `ncc_id` segment of the `name` resource name (`accounts/&#123;account_id&#125;/network-connectivity-configs/&#123;ncc_id&#125;/private-network-gateways/&#123;gateway_id&#125;`). The canonical resource name of the gateway.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The fields to update.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>An opaque token returned by a previous list request.</td>
</tr>
<tr id="parameter-request_id">
    <td><CopyableCode code="request_id" /></td>
    <td><code>string</code></td>
    <td>A unique identifier for this request. The request is idempotent when this is provided.</td>
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

Gets a private network gateway.

```sql
SELECT
name,
display_name,
aws_cloud_connection,
azure_cloud_connection,
bandwidth_tier_gigabits_per_second,
create_time,
destinations,
error_message,
private_dns_resolvers,
state,
traffic_mode,
update_time
FROM databricks_account.networking.private_network_gateways
WHERE account_id = '{{ account_id }}' -- required
AND ncc_id = '{{ ncc_id }}' -- required
AND gateway_id = '{{ gateway_id }}' -- required
AND account_host = '{{ account_host }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists private network gateways under a network connectivity configuration.

```sql
SELECT
name,
display_name,
aws_cloud_connection,
azure_cloud_connection,
bandwidth_tier_gigabits_per_second,
create_time,
destinations,
error_message,
private_dns_resolvers,
state,
traffic_mode,
update_time
FROM databricks_account.networking.private_network_gateways
WHERE account_id = '{{ account_id }}' -- required
AND ncc_id = '{{ ncc_id }}' -- required
AND account_host = '{{ account_host }}' -- required
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

Creates a private network gateway.

```sql
INSERT INTO databricks_account.networking.private_network_gateways (
private_network_gateway,
account_id,
ncc_id,
account_host,
request_id
)
SELECT 
'{{ private_network_gateway }}' /* required */,
'{{ account_id }}',
'{{ ncc_id }}',
'{{ account_host }}',
'{{ request_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: private_network_gateways
  props:
    - name: account_id
      value: "{{ account_id }}"
      description: Required parameter for the private_network_gateways resource.
    - name: ncc_id
      value: "{{ ncc_id }}"
      description: Required parameter for the private_network_gateways resource.
    - name: account_host
      value: "{{ account_host }}"
      description: Required parameter for the private_network_gateways resource.
    - name: private_network_gateway
      description: |
        The gateway to create.
      value:
        display_name: "{{ display_name }}"
        traffic_mode: "{{ traffic_mode }}"
        aws_cloud_connection:
          gateway_subnets:
            - subnet_id: "{{ subnet_id }}"
          cross_account_role:
            role_arn: "{{ role_arn }}"
          security_group_ids:
            - "{{ security_group_ids }}"
        azure_cloud_connection:
          gateway_subnet:
            resource_id: "{{ resource_id }}"
        bandwidth_tier_gigabits_per_second: {{ bandwidth_tier_gigabits_per_second }}
        create_time: "{{ create_time }}"
        destinations:
          - destination_type: "{{ destination_type }}"
            value: "{{ value }}"
        error_message: "{{ error_message }}"
        name: "{{ name }}"
        private_dns_resolvers:
          - resolver_type: "{{ resolver_type }}"
            value: "{{ value }}"
        state: "{{ state }}"
        update_time: "{{ update_time }}"
    - name: request_id
      value: "{{ request_id }}"
      description: A unique identifier for this request. The request is idempotent when this is provided.
      description: A unique identifier for this request. The request is idempotent when this is provided.
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

Updates a private network gateway.

```sql
UPDATE databricks_account.networking.private_network_gateways
SET 
private_network_gateway = '{{ private_network_gateway }}'
WHERE 
account_id = '{{ account_id }}' --required
AND ncc_id = '{{ ncc_id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND account_host = '{{ account_host }}' --required
AND private_network_gateway = '{{ private_network_gateway }}' --required
RETURNING
name,
display_name,
aws_cloud_connection,
azure_cloud_connection,
bandwidth_tier_gigabits_per_second,
create_time,
destinations,
error_message,
private_dns_resolvers,
state,
traffic_mode,
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

Permanently deletes a private network gateway.

```sql
DELETE FROM databricks_account.networking.private_network_gateways
WHERE account_id = '{{ account_id }}' --required
AND ncc_id = '{{ ncc_id }}' --required
AND gateway_id = '{{ gateway_id }}' --required
AND account_host = '{{ account_host }}' --required
;
```
</TabItem>
</Tabs>
