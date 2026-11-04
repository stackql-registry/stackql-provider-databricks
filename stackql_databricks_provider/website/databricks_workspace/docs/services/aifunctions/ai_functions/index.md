---
title: ai_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_functions
  - aifunctions
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

Creates, updates, deletes, gets or lists an <code>ai_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_functions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.aifunctions.ai_functions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#ai_classify"><CopyableCode code="ai_classify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-content"><code>content</code></a>, <a href="#parameter-labels"><code>labels</code></a></td>
    <td></td>
    <td>Classifies content according to a set of provided labels. For REST API requests, the default rate</td>
</tr>
<tr>
    <td><a href="#ai_decide"><CopyableCode code="ai_decide" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-state"><code>state</code></a>, <a href="#parameter-questions"><code>questions</code></a></td>
    <td></td>
    <td>Turn text and structured data into decisions your application can use. Define questions and criteria</td>
</tr>
<tr>
    <td><a href="#ai_extract"><CopyableCode code="ai_extract" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-content"><code>content</code></a>, <a href="#parameter-schema"><code>schema</code></a></td>
    <td></td>
    <td>Extracts structured data from text and documents according to a provided schema. For REST API</td>
</tr>
<tr>
    <td><a href="#ai_parse_document"><CopyableCode code="ai_parse_document" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-content"><code>content</code></a></td>
    <td></td>
    <td>Parse structured content from unstructured documents.</td>
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
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="ai_classify"
    values={[
        { label: 'ai_classify', value: 'ai_classify' },
        { label: 'ai_decide', value: 'ai_decide' },
        { label: 'ai_extract', value: 'ai_extract' },
        { label: 'ai_parse_document', value: 'ai_parse_document' }
    ]}
>
<TabItem value="ai_classify">

Classifies content according to a set of provided labels. For REST API requests, the default rate

```sql
EXEC databricks_workspace.aifunctions.ai_functions.ai_classify 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"content": "{{ content }}", 
"labels": "{{ labels }}", 
"options": "{{ options }}"
}'
;
```
</TabItem>
<TabItem value="ai_decide">

Turn text and structured data into decisions your application can use. Define questions and criteria

```sql
EXEC databricks_workspace.aifunctions.ai_functions.ai_decide 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"state": "{{ state }}", 
"questions": "{{ questions }}", 
"options": "{{ options }}"
}'
;
```
</TabItem>
<TabItem value="ai_extract">

Extracts structured data from text and documents according to a provided schema. For REST API

```sql
EXEC databricks_workspace.aifunctions.ai_functions.ai_extract 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"content": "{{ content }}", 
"schema": "{{ schema }}", 
"options": "{{ options }}"
}'
;
```
</TabItem>
<TabItem value="ai_parse_document">

Parse structured content from unstructured documents.

```sql
EXEC databricks_workspace.aifunctions.ai_functions.ai_parse_document 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"content": "{{ content }}", 
"options": "{{ options }}"
}'
;
```
</TabItem>
</Tabs>
