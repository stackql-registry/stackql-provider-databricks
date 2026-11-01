---
title: knowledge_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_sources
  - knowledgeassistants
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

Creates, updates, deletes, gets or lists a <code>knowledge_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_sources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.knowledgeassistants.knowledge_sources" /></td></tr>
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
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: knowledge-assistants/&#123;knowledge_assistant_id&#125;/knowledge-sources/&#123;knowledge_source_id&#125;"
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display name of the knowledge source. Required when creating a Knowledge Source. When updating a Knowledge Source, optional unless included in update_mask."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when this knowledge source was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the knowledge source. Required when creating a Knowledge Source. When updating a Knowledge Source, optional unless included in update_mask."
  },
  {
    "name": "file_table",
    "type": "object",
    "description": "FileTableSpec specifies a file table source configuration.",
    "children": [
      {
        "name": "table_name",
        "type": "string",
        "description": "Full UC name of the table, in the format of &#123;CATALOG&#125;.&#123;SCHEMA&#125;.&#123;TABLE_NAME&#125;."
      },
      {
        "name": "file_col",
        "type": "string",
        "description": "The name of the column containing BINARY file content to be indexed."
      }
    ]
  },
  {
    "name": "files",
    "type": "object",
    "description": "FilesSpec specifies a files source configuration.",
    "children": [
      {
        "name": "path",
        "type": "string",
        "description": "A UC volume path that includes a list of files."
      }
    ]
  },
  {
    "name": "index",
    "type": "object",
    "description": "IndexSpec specifies a vector search index source configuration.",
    "children": [
      {
        "name": "index_name",
        "type": "string",
        "description": "Full UC name of the vector search index, in the format of &#123;CATALOG&#125;.&#123;SCHEMA&#125;.&#123;INDEX_NAME&#125;."
      },
      {
        "name": "text_col",
        "type": "string",
        "description": "The column that includes the document text for retrieval."
      },
      {
        "name": "doc_uri_col",
        "type": "string",
        "description": "The column that specifies a link or reference to where the information came from."
      }
    ]
  },
  {
    "name": "knowledge_cutoff_time",
    "type": "string (date-time)",
    "description": "Timestamp representing the cutoff before which content in this knowledge source is being ingested."
  },
  {
    "name": "source_type",
    "type": "string",
    "description": "The type of the source: \"index\", \"files\", or \"file_table\". Required when creating a Knowledge Source. When updating a Knowledge Source, this field is ignored."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FAILED_UPDATE, UPDATED, UPDATING)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": ""
  },
  {
    "name": "name",
    "type": "string",
    "description": "Full resource name: knowledge-assistants/&#123;knowledge_assistant_id&#125;/knowledge-sources/&#123;knowledge_source_id&#125;"
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Human-readable display name of the knowledge source. Required when creating a Knowledge Source. When updating a Knowledge Source, optional unless included in update_mask."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Timestamp when this knowledge source was created."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of the knowledge source. Required when creating a Knowledge Source. When updating a Knowledge Source, optional unless included in update_mask."
  },
  {
    "name": "file_table",
    "type": "object",
    "description": "FileTableSpec specifies a file table source configuration.",
    "children": [
      {
        "name": "table_name",
        "type": "string",
        "description": "Full UC name of the table, in the format of &#123;CATALOG&#125;.&#123;SCHEMA&#125;.&#123;TABLE_NAME&#125;."
      },
      {
        "name": "file_col",
        "type": "string",
        "description": "The name of the column containing BINARY file content to be indexed."
      }
    ]
  },
  {
    "name": "files",
    "type": "object",
    "description": "FilesSpec specifies a files source configuration.",
    "children": [
      {
        "name": "path",
        "type": "string",
        "description": "A UC volume path that includes a list of files."
      }
    ]
  },
  {
    "name": "index",
    "type": "object",
    "description": "IndexSpec specifies a vector search index source configuration.",
    "children": [
      {
        "name": "index_name",
        "type": "string",
        "description": "Full UC name of the vector search index, in the format of &#123;CATALOG&#125;.&#123;SCHEMA&#125;.&#123;INDEX_NAME&#125;."
      },
      {
        "name": "text_col",
        "type": "string",
        "description": "The column that includes the document text for retrieval."
      },
      {
        "name": "doc_uri_col",
        "type": "string",
        "description": "The column that specifies a link or reference to where the information came from."
      }
    ]
  },
  {
    "name": "knowledge_cutoff_time",
    "type": "string (date-time)",
    "description": "Timestamp representing the cutoff before which content in this knowledge source is being ingested."
  },
  {
    "name": "source_type",
    "type": "string",
    "description": "The type of the source: \"index\", \"files\", or \"file_table\". Required when creating a Knowledge Source. When updating a Knowledge Source, this field is ignored."
  },
  {
    "name": "state",
    "type": "string",
    "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (FAILED_UPDATE, UPDATED, UPDATING)"
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
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-knowledge_source_id"><code>knowledge_source_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a Knowledge Source.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists Knowledge Sources under a Knowledge Assistant.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-knowledge_source"><code>knowledge_source</code></a></td>
    <td></td>
    <td>Creates a Knowledge Source under a Knowledge Assistant.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-knowledge_source_id"><code>knowledge_source_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-knowledge_source"><code>knowledge_source</code></a></td>
    <td></td>
    <td>Updates a Knowledge Source.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-knowledge_source_id"><code>knowledge_source_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a Knowledge Source.</td>
</tr>
<tr>
    <td><a href="#sync"><CopyableCode code="sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Sync all non-index Knowledge Sources for a Knowledge Assistant (index sources do not require sync)</td>
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
<tr id="parameter-knowledge_assistant_id">
    <td><CopyableCode code="knowledge_assistant_id" /></td>
    <td><code>string</code></td>
    <td>The `knowledge_assistant_id` segment of the `name` resource name (`knowledge-assistants/&#123;knowledge_assistant_id&#125;`). The resource name of the Knowledge Assistant. Format: knowledge-assistants/&#123;knowledge_assistant_id&#125;</td>
</tr>
<tr id="parameter-knowledge_source_id">
    <td><CopyableCode code="knowledge_source_id" /></td>
    <td><code>string</code></td>
    <td>The `knowledge_source_id` segment of the `name` resource name (`knowledge-assistants/&#123;knowledge_assistant_id&#125;/knowledge-sources/&#123;knowledge_source_id&#125;`). The resource name of the Knowledge Source to delete. Format: knowledge-assistants/&#123;knowledge_assistant_id&#125;/knowledge-sources/&#123;knowledge_source_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Comma-delimited list of fields to update on the Knowledge Source. Allowed values: ``display_name``, ``description``. Examples: - ``display_name`` - ``display_name,description``</td>
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

Gets a Knowledge Source.

```sql
SELECT
id,
name,
display_name,
create_time,
description,
file_table,
files,
index,
knowledge_cutoff_time,
source_type,
state
FROM databricks_workspace.knowledgeassistants.knowledge_sources
WHERE knowledge_assistant_id = '{{ knowledge_assistant_id }}' -- required
AND knowledge_source_id = '{{ knowledge_source_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists Knowledge Sources under a Knowledge Assistant.

```sql
SELECT
id,
name,
display_name,
create_time,
description,
file_table,
files,
index,
knowledge_cutoff_time,
source_type,
state
FROM databricks_workspace.knowledgeassistants.knowledge_sources
WHERE knowledge_assistant_id = '{{ knowledge_assistant_id }}' -- required
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

Creates a Knowledge Source under a Knowledge Assistant.

```sql
INSERT INTO databricks_workspace.knowledgeassistants.knowledge_sources (
knowledge_source,
knowledge_assistant_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ knowledge_source }}' /* required */,
'{{ knowledge_assistant_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
id,
name,
display_name,
create_time,
description,
file_table,
files,
index,
knowledge_cutoff_time,
source_type,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: knowledge_sources
  props:
    - name: knowledge_assistant_id
      value: "{{ knowledge_assistant_id }}"
      description: Required parameter for the knowledge_sources resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the knowledge_sources resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the knowledge_sources resource.
    - name: knowledge_source
      description: |
        KnowledgeSource represents a source of knowledge for the KnowledgeAssistant. Used in
        create/update requests and returned in Get/List responses. Note: REQUIRED annotations below
        represent create-time requirements. For updates, required fields are determined by the update
        mask.
      value:
        display_name: "{{ display_name }}"
        description: "{{ description }}"
        source_type: "{{ source_type }}"
        create_time: "{{ create_time }}"
        file_table:
          table_name: "{{ table_name }}"
          file_col: "{{ file_col }}"
        files:
          path: "{{ path }}"
        id: "{{ id }}"
        index:
          index_name: "{{ index_name }}"
          text_col: "{{ text_col }}"
          doc_uri_col: "{{ doc_uri_col }}"
        knowledge_cutoff_time: "{{ knowledge_cutoff_time }}"
        name: "{{ name }}"
        state: "{{ state }}"
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

Updates a Knowledge Source.

```sql
UPDATE databricks_workspace.knowledgeassistants.knowledge_sources
SET 
knowledge_source = '{{ knowledge_source }}'
WHERE 
knowledge_assistant_id = '{{ knowledge_assistant_id }}' --required
AND knowledge_source_id = '{{ knowledge_source_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND knowledge_source = '{{ knowledge_source }}' --required
RETURNING
id,
name,
display_name,
create_time,
description,
file_table,
files,
index,
knowledge_cutoff_time,
source_type,
state;
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

Deletes a Knowledge Source.

```sql
DELETE FROM databricks_workspace.knowledgeassistants.knowledge_sources
WHERE knowledge_assistant_id = '{{ knowledge_assistant_id }}' --required
AND knowledge_source_id = '{{ knowledge_source_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="sync"
    values={[
        { label: 'sync', value: 'sync' }
    ]}
>
<TabItem value="sync">

Sync all non-index Knowledge Sources for a Knowledge Assistant (index sources do not require sync)

```sql
EXEC databricks_workspace.knowledgeassistants.knowledge_sources.sync 
@knowledge_assistant_id='{{ knowledge_assistant_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
