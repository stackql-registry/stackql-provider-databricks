---
title: sandbox_directories
hide_title: false
hide_table_of_contents: false
keywords:
  - sandbox_directories
  - sandbox
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

Creates, updates, deletes, gets or lists a <code>sandbox_directories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sandbox_directories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.sandbox.sandbox_directories" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sandbox_id"><code>sandbox_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td></td>
    <td>Creates a directory in a sandbox, including missing parents by default.</td>
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
<tr id="parameter-sandbox_id">
    <td><CopyableCode code="sandbox_id" /></td>
    <td><code>string</code></td>
    <td>The `sandbox_id` segment of the `parent` resource name (`sandboxes/&#123;sandbox_id&#125;`).</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a directory in a sandbox, including missing parents by default.

```sql
INSERT INTO databricks_workspace.sandbox.sandbox_directories (
path,
parents,
sandbox_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ path }}' /* required */,
{{ parents }},
'{{ sandbox_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sandbox_directories
  props:
    - name: sandbox_id
      value: "{{ sandbox_id }}"
      description: Required parameter for the sandbox_directories resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the sandbox_directories resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the sandbox_directories resource.
    - name: path
      value: "{{ path }}"
      description: |
        Absolute UTF-8 path of the directory.
    - name: parents
      value: {{ parents }}
      description: |
        Defaults to true, which also succeeds when the directory already exists.
`}</CodeBlock>

</TabItem>
</Tabs>
