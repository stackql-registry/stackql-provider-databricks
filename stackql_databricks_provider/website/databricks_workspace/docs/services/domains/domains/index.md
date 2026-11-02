---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.domains.domains" /></td></tr>
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
    "description": "Full resource name of the domain. The primary identifier for this resource. Format: ``domains/&#123;domain_id&#125;`` Identifies the domain on get, update, and delete. Not an input on create — to choose the id, set ``CreateDomainRequest.domain_id``."
  },
  {
    "name": "domain_id",
    "type": "string",
    "description": "Unique identifier for the domain. If omitted at Create, the server generates one."
  },
  {
    "name": "parent_domain_id",
    "type": "string",
    "description": "Domain ID of the parent. If absent, this is a top-level domain. If present, this domain is a subdomain of the specified parent."
  },
  {
    "name": "business_owner_ids",
    "type": "array",
    "description": "Principal IDs of the business owners (users, groups, or service principals)."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when the domain was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Full description (max 4096 chars)"
  },
  {
    "name": "draft",
    "type": "boolean",
    "description": "Whether to mark the domain as a draft. If omitted on Create, the server applies a default; the resolved value is returned in ``effective_draft``."
  },
  {
    "name": "effective_draft",
    "type": "boolean",
    "description": "Resolved draft state of the domain."
  },
  {
    "name": "icon",
    "type": "object",
    "description": "Icon to display for the domain.",
    "children": [
      {
        "name": "color",
        "type": "string",
        "description": "Hex color code with # prefix (e.g., \"#FF5733\")."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Available icon names for a domain. (ADDRESS_BOOK, ALARM, ARROWS_IN, ATOM, BALLOON, BANK, BARRICADE, BASKET, BRIDGE, CACTUS, CALL_BELL, CARROT, CHART_PIE_SLICE, CITY, CLOUD, COINS, COMPASS_ROSE, CRANE_TOWER, CROWN, CUBE_TRANSPARENT, FADERS, FLAG_BANNER_FOLD, FLAG_CHECKERED, GAVEL, HAMBURGER, HEAD_CIRCUIT, HOURGLASS_HIGH, INTERSECT_THREE, MICROSCOPE, MOON_STARS, PACKAGE, PARACHUTE, PEPPER, PIGGY_BANK, PILL, PLANET, PLANT, PLUGS_CONNECTED, POPCORN, PRESENTATION_CHART, PUZZLE_PIECE, RAINBOW, RANKING, RECEIPT, ROCKET, RULER, SAILBOAT, SCALES, SCAN_SMILEY, SCROLL, SHIELD_CHECKERED, SNEAKER, SNOWFLAKE, SOLAR_ROOF, SPEEDOMETER, STAMP, STEPS, STRATEGY, SWORD, TELEVISION_SIMPLE, TENT, TICKET, TRACTOR, TRAFFIC_CONE, TRAIN, TREE_EVERGREEN, TREE_STRUCTURE, TROLLEY_SUITCASE, TROPHY, TRUCK_TRAILER, USERS_THREE, VECTOR_THREE)"
      }
    ]
  },
  {
    "name": "subtitle",
    "type": "string",
    "description": "Short description (max 280 chars)"
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": ""
  },
  {
    "name": "technical_owner_ids",
    "type": "array",
    "description": "Principal IDs of the technical owners (users, groups, or service principals)."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Timestamp when the domain was last updated."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name of the domain. The primary identifier for this resource. Format: ``domains/&#123;domain_id&#125;`` Identifies the domain on get, update, and delete. Not an input on create — to choose the id, set ``CreateDomainRequest.domain_id``."
  },
  {
    "name": "domain_id",
    "type": "string",
    "description": "Unique identifier for the domain. If omitted at Create, the server generates one."
  },
  {
    "name": "parent_domain_id",
    "type": "string",
    "description": "Domain ID of the parent. If absent, this is a top-level domain. If present, this domain is a subdomain of the specified parent."
  },
  {
    "name": "business_owner_ids",
    "type": "array",
    "description": "Principal IDs of the business owners (users, groups, or service principals)."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when the domain was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Full description (max 4096 chars)"
  },
  {
    "name": "draft",
    "type": "boolean",
    "description": "Whether to mark the domain as a draft. If omitted on Create, the server applies a default; the resolved value is returned in ``effective_draft``."
  },
  {
    "name": "effective_draft",
    "type": "boolean",
    "description": "Resolved draft state of the domain."
  },
  {
    "name": "icon",
    "type": "object",
    "description": "Icon to display for the domain.",
    "children": [
      {
        "name": "color",
        "type": "string",
        "description": "Hex color code with # prefix (e.g., \"#FF5733\")."
      },
      {
        "name": "name",
        "type": "string",
        "description": "Available icon names for a domain. (ADDRESS_BOOK, ALARM, ARROWS_IN, ATOM, BALLOON, BANK, BARRICADE, BASKET, BRIDGE, CACTUS, CALL_BELL, CARROT, CHART_PIE_SLICE, CITY, CLOUD, COINS, COMPASS_ROSE, CRANE_TOWER, CROWN, CUBE_TRANSPARENT, FADERS, FLAG_BANNER_FOLD, FLAG_CHECKERED, GAVEL, HAMBURGER, HEAD_CIRCUIT, HOURGLASS_HIGH, INTERSECT_THREE, MICROSCOPE, MOON_STARS, PACKAGE, PARACHUTE, PEPPER, PIGGY_BANK, PILL, PLANET, PLANT, PLUGS_CONNECTED, POPCORN, PRESENTATION_CHART, PUZZLE_PIECE, RAINBOW, RANKING, RECEIPT, ROCKET, RULER, SAILBOAT, SCALES, SCAN_SMILEY, SCROLL, SHIELD_CHECKERED, SNEAKER, SNOWFLAKE, SOLAR_ROOF, SPEEDOMETER, STAMP, STEPS, STRATEGY, SWORD, TELEVISION_SIMPLE, TENT, TICKET, TRACTOR, TRAFFIC_CONE, TRAIN, TREE_EVERGREEN, TREE_STRUCTURE, TROLLEY_SUITCASE, TROPHY, TRUCK_TRAILER, USERS_THREE, VECTOR_THREE)"
      }
    ]
  },
  {
    "name": "subtitle",
    "type": "string",
    "description": "Short description (max 280 chars)"
  },
  {
    "name": "tag_key",
    "type": "string",
    "description": ""
  },
  {
    "name": "technical_owner_ids",
    "type": "array",
    "description": "Principal IDs of the technical owners (users, groups, or service principals)."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Timestamp when the domain was last updated."
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
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get a domain by resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent_domain_id"><code>parent_domain_id</code></a></td>
    <td>List domains in the account. Set ``parent_domain_id`` to return only the direct subdomains of a given</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td>Create a domain. If ``domain_id`` is omitted, the server generates one.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-tag_key"><code>tag_key</code></a></td>
    <td></td>
    <td>Update a domain. ``update_mask`` selects which fields to modify; the domain is identified by its</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete a domain. By default the request fails if the domain still has Glossary pages; set ``force`` to</td>
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
<tr id="parameter-domain_id">
    <td><CopyableCode code="domain_id" /></td>
    <td><code>string</code></td>
    <td>The `domain_id` segment of the `name` resource name (`domains/&#123;domain_id&#125;`). Full resource name of the domain to delete. Format: ``domains/&#123;domain_id&#125;``</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g., ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-domain_id">
    <td><CopyableCode code="domain_id" /></td>
    <td><code>string</code></td>
    <td>Client-supplied resource ID for the new domain. If omitted, the server generates one.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>When false (default), DeleteDomain is rejected with FAILED_PRECONDITION if the domain still has Glossary pages. When true, those pages are deleted first and then the domain is removed.</td>
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
<tr id="parameter-parent_domain_id">
    <td><CopyableCode code="parent_domain_id" /></td>
    <td><code>string</code></td>
    <td>Filter by parent domain. - Absent: return all domains regardless of hierarchy. - Present: return only direct children of the specified domain.</td>
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

Get a domain by resource name.

```sql
SELECT
name,
domain_id,
parent_domain_id,
business_owner_ids,
create_time,
description,
draft,
effective_draft,
icon,
subtitle,
tag_key,
technical_owner_ids,
update_time
FROM databricks_workspace.domains.domains
WHERE domain_id = '{{ domain_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

List domains in the account. Set ``parent_domain_id`` to return only the direct subdomains of a given

```sql
SELECT
name,
domain_id,
parent_domain_id,
business_owner_ids,
create_time,
description,
draft,
effective_draft,
icon,
subtitle,
tag_key,
technical_owner_ids,
update_time
FROM databricks_workspace.domains.domains
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent_domain_id = '{{ parent_domain_id }}'
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

Create a domain. If ``domain_id`` is omitted, the server generates one.

```sql
INSERT INTO databricks_workspace.domains.domains (
tag_key,
business_owner_ids,
create_time,
description,
domain_id,
draft,
effective_draft,
icon,
name,
parent_domain_id,
subtitle,
technical_owner_ids,
update_time,
deployment_name,
workspace_domain,
domain_id
)
SELECT 
'{{ tag_key }}' /* required */,
'{{ business_owner_ids }}',
'{{ create_time }}',
'{{ description }}',
'{{ domain_id }}',
{{ draft }},
{{ effective_draft }},
'{{ icon }}',
'{{ name }}',
'{{ parent_domain_id }}',
'{{ subtitle }}',
'{{ technical_owner_ids }}',
'{{ update_time }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ domain_id }}'
RETURNING
name,
domain_id,
parent_domain_id,
business_owner_ids,
create_time,
description,
draft,
effective_draft,
icon,
subtitle,
tag_key,
technical_owner_ids,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: domains
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the domains resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the domains resource.
    - name: tag_key
      value: "{{ tag_key }}"
    - name: business_owner_ids
      value:
        - {{ business_owner_ids }}
      description: |
        Principal IDs of the business owners (users, groups, or service principals).
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Timestamp when the domain was created.
    - name: description
      value: "{{ description }}"
      description: |
        Full description (max 4096 chars)
    - name: domain_id
      value: "{{ domain_id }}"
      description: |
        Unique identifier for the domain. If omitted at Create, the server generates one.
    - name: draft
      value: {{ draft }}
      description: |
        Whether to mark the domain as a draft. If omitted on Create, the server applies a default; the resolved value is returned in \`\`effective_draft\`\`.
    - name: effective_draft
      value: {{ effective_draft }}
      description: |
        Resolved draft state of the domain.
    - name: icon
      description: |
        Icon to display for the domain.
      value:
        color: "{{ color }}"
        name: "{{ name }}"
    - name: name
      value: "{{ name }}"
      description: |
        Full resource name of the domain. The primary identifier for this resource. Format: \`\`domains/{domain_id}\`\` Identifies the domain on get, update, and delete. Not an input on create — to choose the id, set \`\`CreateDomainRequest.domain_id\`\`.
    - name: parent_domain_id
      value: "{{ parent_domain_id }}"
      description: |
        Domain ID of the parent. If absent, this is a top-level domain. If present, this domain is a subdomain of the specified parent.
    - name: subtitle
      value: "{{ subtitle }}"
      description: |
        Short description (max 280 chars)
    - name: technical_owner_ids
      value:
        - {{ technical_owner_ids }}
      description: |
        Principal IDs of the technical owners (users, groups, or service principals).
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Timestamp when the domain was last updated.
    - name: domain_id
      value: "{{ domain_id }}"
      description: Client-supplied resource ID for the new domain. If omitted, the server generates one.
      description: Client-supplied resource ID for the new domain. If omitted, the server generates one.
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

Update a domain. ``update_mask`` selects which fields to modify; the domain is identified by its

```sql
UPDATE databricks_workspace.domains.domains
SET 
tag_key = '{{ tag_key }}',
business_owner_ids = '{{ business_owner_ids }}',
create_time = '{{ create_time }}',
description = '{{ description }}',
domain_id = '{{ domain_id }}',
draft = {{ draft }},
effective_draft = {{ effective_draft }},
icon = '{{ icon }}',
name = '{{ name }}',
parent_domain_id = '{{ parent_domain_id }}',
subtitle = '{{ subtitle }}',
technical_owner_ids = '{{ technical_owner_ids }}',
update_time = '{{ update_time }}'
WHERE 
domain_id = '{{ domain_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND tag_key = '{{ tag_key }}' --required
RETURNING
name,
domain_id,
parent_domain_id,
business_owner_ids,
create_time,
description,
draft,
effective_draft,
icon,
subtitle,
tag_key,
technical_owner_ids,
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

Delete a domain. By default the request fails if the domain still has Glossary pages; set ``force`` to

```sql
DELETE FROM databricks_workspace.domains.domains
WHERE domain_id = '{{ domain_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>
