---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
  - supervisoragents
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

Creates, updates, deletes, gets or lists an <code>examples</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="examples" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.supervisoragents.examples" /></td></tr>
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
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;"
  },
  {
    "name": "example_id",
    "type": "string",
    "description": "The universally unique identifier (UUID) of the example."
  },
  {
    "name": "guidelines",
    "type": "array",
    "description": "Guidelines for answering the question."
  },
  {
    "name": "question",
    "type": "string",
    "description": "The example question."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;"
  },
  {
    "name": "example_id",
    "type": "string",
    "description": "The universally unique identifier (UUID) of the example."
  },
  {
    "name": "guidelines",
    "type": "array",
    "description": "Guidelines for answering the question."
  },
  {
    "name": "question",
    "type": "string",
    "description": "The example question."
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
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-example_id"><code>example_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets an example from a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists examples under a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-question"><code>question</code></a>, <a href="#parameter-guidelines"><code>guidelines</code></a></td>
    <td></td>
    <td>Creates an example for a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-example_id"><code>example_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-question"><code>question</code></a>, <a href="#parameter-guidelines"><code>guidelines</code></a></td>
    <td></td>
    <td>Updates an example in a Supervisor Agent.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-supervisor_agent_id"><code>supervisor_agent_id</code></a>, <a href="#parameter-example_id"><code>example_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes an example from a Supervisor Agent.</td>
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
<tr id="parameter-example_id">
    <td><CopyableCode code="example_id" /></td>
    <td><code>string</code></td>
    <td>The `example_id` segment of the `name` resource name (`supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;`). The resource name of the example to delete. Format: supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;</td>
</tr>
<tr id="parameter-supervisor_agent_id">
    <td><CopyableCode code="supervisor_agent_id" /></td>
    <td><code>string</code></td>
    <td>The `supervisor_agent_id` segment of the `name` resource name (`supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;`). The resource name of the example to delete. Format: supervisor-agents/&#123;supervisor_agent_id&#125;/examples/&#123;example_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Comma-delimited list of fields to update on the example. Allowed values: ``question``, ``guidelines``. Examples: - ``question`` - ``question,guidelines``</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of examples to return. If unspecified, at most 100 examples will be returned. The maximum value is 100; values above 100 will be coerced to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListExamples`` call. Provide this to retrieve the subsequent page. If unspecified, the first page will be returned.</td>
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

Gets an example from a Supervisor Agent.

```sql
SELECT
name,
example_id,
guidelines,
question
FROM databricks_workspace.supervisoragents.examples
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' -- required
AND example_id = '{{ example_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists examples under a Supervisor Agent.

```sql
SELECT
name,
example_id,
guidelines,
question
FROM databricks_workspace.supervisoragents.examples
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' -- required
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

Creates an example for a Supervisor Agent.

```sql
INSERT INTO databricks_workspace.supervisoragents.examples (
question,
guidelines,
example_id,
name,
supervisor_agent_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ question }}' /* required */,
'{{ guidelines }}' /* required */,
'{{ example_id }}',
'{{ name }}',
'{{ supervisor_agent_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
example_id,
guidelines,
question
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: examples
  props:
    - name: supervisor_agent_id
      value: "{{ supervisor_agent_id }}"
      description: Required parameter for the examples resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the examples resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the examples resource.
    - name: question
      value: "{{ question }}"
      description: |
        The example question.
    - name: guidelines
      value:
        - "{{ guidelines }}"
      description: |
        Guidelines for answering the question.
    - name: example_id
      value: "{{ example_id }}"
      description: |
        The universally unique identifier (UUID) of the example.
    - name: name
      value: "{{ name }}"
      description: |
        Full resource name: supervisor-agents/{supervisor_agent_id}/examples/{example_id}
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

Updates an example in a Supervisor Agent.

```sql
UPDATE databricks_workspace.supervisoragents.examples
SET 
question = '{{ question }}',
guidelines = '{{ guidelines }}',
example_id = '{{ example_id }}',
name = '{{ name }}'
WHERE 
supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND example_id = '{{ example_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND question = '{{ question }}' --required
AND guidelines = '{{ guidelines }}' --required
RETURNING
name,
example_id,
guidelines,
question;
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

Deletes an example from a Supervisor Agent.

```sql
DELETE FROM databricks_workspace.supervisoragents.examples
WHERE supervisor_agent_id = '{{ supervisor_agent_id }}' --required
AND example_id = '{{ example_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
