---
title: knowledge_assistants
hide_title: false
hide_table_of_contents: false
keywords:
  - knowledge_assistants
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

Creates, updates, deletes, gets or lists a <code>knowledge_assistants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="knowledge_assistants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.knowledgeassistants.knowledge_assistants" /></td></tr>
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
    "description": "Deprecated: use knowledge_assistant_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the Knowledge Assistant. Format: knowledge-assistants/&#123;knowledge_assistant_id&#125;"
  },
  {
    "name": "experiment_id",
    "type": "string",
    "description": "The MLflow experiment ID."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the Knowledge Assistant, unique at workspace level. Required when creating a Knowledge Assistant. When updating a Knowledge Assistant, optional unless included in update_mask."
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the knowledge assistant agent endpoint."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Creation timestamp."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The creator of the Knowledge Assistant."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this agent can do (user-facing). Required when creating a Knowledge Assistant. When updating a Knowledge Assistant, optional unless included in update_mask."
  },
  {
    "name": "error_info",
    "type": "string",
    "description": "Error details when the Knowledge Assistant is in FAILED state."
  },
  {
    "name": "instructions",
    "type": "string",
    "description": "Additional global instructions on how the agent should generate answers. Optional on create and update. When updating a Knowledge Assistant, include this field in update_mask to modify it."
  },
  {
    "name": "state",
    "type": "string",
    "description": "State of the Knowledge Assistant. Not returned in List responses. (ACTIVE, CREATING, FAILED)"
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "Deprecated: use knowledge_assistant_id instead."
  },
  {
    "name": "name",
    "type": "string",
    "description": "The resource name of the Knowledge Assistant. Format: knowledge-assistants/&#123;knowledge_assistant_id&#125;"
  },
  {
    "name": "experiment_id",
    "type": "string",
    "description": "The MLflow experiment ID."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "The display name of the Knowledge Assistant, unique at workspace level. Required when creating a Knowledge Assistant. When updating a Knowledge Assistant, optional unless included in update_mask."
  },
  {
    "name": "endpoint_name",
    "type": "string",
    "description": "The name of the knowledge assistant agent endpoint."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Creation timestamp."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The creator of the Knowledge Assistant."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description of what this agent can do (user-facing). Required when creating a Knowledge Assistant. When updating a Knowledge Assistant, optional unless included in update_mask."
  },
  {
    "name": "error_info",
    "type": "string",
    "description": "Error details when the Knowledge Assistant is in FAILED state."
  },
  {
    "name": "instructions",
    "type": "string",
    "description": "Additional global instructions on how the agent should generate answers. Optional on create and update. When updating a Knowledge Assistant, include this field in update_mask to modify it."
  },
  {
    "name": "state",
    "type": "string",
    "description": "State of the Knowledge Assistant. Not returned in List responses. (ACTIVE, CREATING, FAILED)"
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
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets a Knowledge Assistant.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>List Knowledge Assistants</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-knowledge_assistant"><code>knowledge_assistant</code></a></td>
    <td></td>
    <td>Creates a Knowledge Assistant.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-knowledge_assistant"><code>knowledge_assistant</code></a></td>
    <td></td>
    <td>Updates a Knowledge Assistant.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-knowledge_assistant_id"><code>knowledge_assistant_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes a Knowledge Assistant.</td>
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
    <td>The `knowledge_assistant_id` segment of the `name` resource name (`knowledge-assistants/&#123;knowledge_assistant_id&#125;`). The resource name of the knowledge assistant to be deleted. Format: knowledge-assistants/&#123;knowledge_assistant_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Comma-delimited list of fields to update on the Knowledge Assistant. Allowed values: ``display_name``, ``description``, ``instructions``. Examples: - ``display_name`` - ``description,instructions``</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of knowledge assistants to return. If unspecified, at most 100 knowledge assistants will be returned. The maximum value is 100; values above 100 will be coerced to 100.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>A page token, received from a previous ``ListKnowledgeAssistants`` call. Provide this to retrieve the subsequent page. If unspecified, the first page will be returned.</td>
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

Gets a Knowledge Assistant.

```sql
SELECT
id,
name,
experiment_id,
display_name,
endpoint_name,
create_time,
creator,
description,
error_info,
instructions,
state
FROM databricks_workspace.knowledgeassistants.knowledge_assistants
WHERE knowledge_assistant_id = '{{ knowledge_assistant_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Knowledge Assistants

```sql
SELECT
id,
name,
experiment_id,
display_name,
endpoint_name,
create_time,
creator,
description,
error_info,
instructions,
state
FROM databricks_workspace.knowledgeassistants.knowledge_assistants
WHERE deployment_name = '{{ deployment_name }}' -- required
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

Creates a Knowledge Assistant.

```sql
INSERT INTO databricks_workspace.knowledgeassistants.knowledge_assistants (
knowledge_assistant,
deployment_name,
workspace_domain
)
SELECT 
'{{ knowledge_assistant }}' /* required */,
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
id,
name,
experiment_id,
display_name,
endpoint_name,
create_time,
creator,
description,
error_info,
instructions,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: knowledge_assistants
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the knowledge_assistants resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the knowledge_assistants resource.
    - name: knowledge_assistant
      description: |
        The Knowledge Assistant to create.
      value:
        display_name: "{{ display_name }}"
        description: "{{ description }}"
        create_time: "{{ create_time }}"
        creator: "{{ creator }}"
        endpoint_name: "{{ endpoint_name }}"
        error_info: "{{ error_info }}"
        experiment_id: "{{ experiment_id }}"
        id: "{{ id }}"
        instructions: "{{ instructions }}"
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

Updates a Knowledge Assistant.

```sql
UPDATE databricks_workspace.knowledgeassistants.knowledge_assistants
SET 
knowledge_assistant = '{{ knowledge_assistant }}'
WHERE 
knowledge_assistant_id = '{{ knowledge_assistant_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND knowledge_assistant = '{{ knowledge_assistant }}' --required
RETURNING
id,
name,
experiment_id,
display_name,
endpoint_name,
create_time,
creator,
description,
error_info,
instructions,
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

Deletes a Knowledge Assistant.

```sql
DELETE FROM databricks_workspace.knowledgeassistants.knowledge_assistants
WHERE knowledge_assistant_id = '{{ knowledge_assistant_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
