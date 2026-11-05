---
title: catalog_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_configs
  - dataclassification
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

Creates, updates, deletes, gets or lists a <code>catalog_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="catalog_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dataclassification.catalog_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Resource name in the format: catalogs/&#123;catalog_name&#125;/config."
  },
  {
    "name": "auto_tag_configs",
    "type": "array",
    "description": "List of auto-tagging configurations for this catalog. Empty list means no auto-tagging is enabled.",
    "children": [
      {
        "name": "classification_tag",
        "type": "string",
        "description": "The Classification Tag. For built-in classes this is a system tag (e.g., \"class.name\", \"class.location\"); for custom classes it is a user-defined governance tag key."
      },
      {
        "name": "auto_tagging_mode",
        "type": "string",
        "description": "Whether auto-tagging is enabled or disabled for this classification tag. (AUTO_TAGGING_DISABLED, AUTO_TAGGING_ENABLED)"
      }
    ]
  },
  {
    "name": "excluded_schemas",
    "type": "object",
    "description": "Schemas to exclude from the scan, each named relative to the parent catalog. If specified, all schemas except the specified ones will be scanned. Mutually exclusive with ``included_schemas``: only one may be set per request. If neither ``included_schemas`` nor ``excluded_schemas`` is set, all schemas are scanned.",
    "children": [
      {
        "name": "names",
        "type": "array",
        "description": "Schema names, each relative to the parent catalog. Must not be empty."
      }
    ]
  },
  {
    "name": "included_schemas",
    "type": "object",
    "description": "Schemas to include in the scan, each named relative to the parent catalog. If specified, only listed schemas will be scanned. Mutually exclusive with ``excluded_schemas``: only one may be set per request. If neither ``included_schemas`` nor ``excluded_schemas`` is set, all schemas are scanned.",
    "children": [
      {
        "name": "names",
        "type": "array",
        "description": "Schema names, each relative to the parent catalog. Must not be empty."
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
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Get the Data Classification configuration for a catalog.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Create Data Classification configuration for a catalog.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Update the Data Classification configuration for a catalog.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-catalog_name"><code>catalog_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Delete Data Classification configuration for a catalog.</td>
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
    <td>The `catalog_name` segment of the `name` resource name (`catalogs/&#123;catalog_name&#125;/config`). Resource name in the format: catalogs/&#123;catalog_name&#125;/config</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Field mask specifying which fields to update.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the Data Classification configuration for a catalog.

```sql
SELECT
name,
auto_tag_configs,
excluded_schemas,
included_schemas
FROM databricks_workspace.dataclassification.catalog_configs
WHERE catalog_name = '{{ catalog_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
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

Create Data Classification configuration for a catalog.

```sql
INSERT INTO databricks_workspace.dataclassification.catalog_configs (
auto_tag_configs,
excluded_schemas,
included_schemas,
name,
catalog_name,
deployment_name,
workspace_domain
)
SELECT 
'{{ auto_tag_configs }}',
'{{ excluded_schemas }}',
'{{ included_schemas }}',
'{{ name }}',
'{{ catalog_name }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
auto_tag_configs,
excluded_schemas,
included_schemas
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: catalog_configs
  props:
    - name: catalog_name
      value: "{{ catalog_name }}"
      description: Required parameter for the catalog_configs resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the catalog_configs resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the catalog_configs resource.
    - name: auto_tag_configs
      description: |
        List of auto-tagging configurations for this catalog. Empty list means no auto-tagging is enabled.
      value:
        - classification_tag: "{{ classification_tag }}"
          auto_tagging_mode: "{{ auto_tagging_mode }}"
    - name: excluded_schemas
      description: |
        Schemas to exclude from the scan, each named relative to the parent catalog. If specified, all schemas except the specified ones will be scanned. Mutually exclusive with \`\`included_schemas\`\`: only one may be set per request. If neither \`\`included_schemas\`\` nor \`\`excluded_schemas\`\` is set, all schemas are scanned.
      value:
        names:
          - "{{ names }}"
    - name: included_schemas
      description: |
        Schemas to include in the scan, each named relative to the parent catalog. If specified, only listed schemas will be scanned. Mutually exclusive with \`\`excluded_schemas\`\`: only one may be set per request. If neither \`\`included_schemas\`\` nor \`\`excluded_schemas\`\` is set, all schemas are scanned.
      value:
        names:
          - "{{ names }}"
    - name: name
      value: "{{ name }}"
      description: |
        Resource name in the format: catalogs/{catalog_name}/config.
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

Update the Data Classification configuration for a catalog.

```sql
UPDATE databricks_workspace.dataclassification.catalog_configs
SET 
auto_tag_configs = '{{ auto_tag_configs }}',
excluded_schemas = '{{ excluded_schemas }}',
included_schemas = '{{ included_schemas }}',
name = '{{ name }}'
WHERE 
catalog_name = '{{ catalog_name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
RETURNING
name,
auto_tag_configs,
excluded_schemas,
included_schemas;
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

Delete Data Classification configuration for a catalog.

```sql
DELETE FROM databricks_workspace.dataclassification.catalog_configs
WHERE catalog_name = '{{ catalog_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
