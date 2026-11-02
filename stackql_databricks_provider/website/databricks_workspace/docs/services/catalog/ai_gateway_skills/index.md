---
title: ai_gateway_skills
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_skills
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_skills</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_skills" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_skills" /></td></tr>
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
    "description": "Resource name of the skill. Format: ``skills/&#123;catalog&#125;.&#123;schema&#125;.&#123;skill&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``skill_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the skill."
  },
  {
    "name": "bundle_name",
    "type": "string",
    "description": "Name from the most recently successfully finalized SKILL.md. It may differ from the final component of the Skill resource name. Unset until FinalizeSkill succeeds."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided comment for the skill. Free-text, user-editable via UpdateSkill (listed in its ``update_mask``). DISTINCT from ``description``, which is the server-parsed, OUTPUT_ONLY SKILL.md frontmatter value: ``comment`` is the customer's own annotation and is preserved across bundle re-uploads. When ``comment`` is in the update mask, omitting it clears the field, while an explicitly empty string is retained."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the skill was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description from the most recently successfully finalized SKILL.md. Unset until FinalizeSkill succeeds."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the skill."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "finalize_time",
    "type": "string (date-time)",
    "description": "Time of the most recent successful FinalizeSkill. Unset until one succeeds."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time of the most recent Skill metadata mutation. Uploading bundle files alone does not change this value."
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
    "description": "Resource name of the skill. Format: ``skills/&#123;catalog&#125;.&#123;schema&#125;.&#123;skill&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``skill_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the skill."
  },
  {
    "name": "bundle_name",
    "type": "string",
    "description": "Name from the most recently successfully finalized SKILL.md. It may differ from the final component of the Skill resource name. Unset until FinalizeSkill succeeds."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided comment for the skill. Free-text, user-editable via UpdateSkill (listed in its ``update_mask``). DISTINCT from ``description``, which is the server-parsed, OUTPUT_ONLY SKILL.md frontmatter value: ``comment`` is the customer's own annotation and is preserved across bundle re-uploads. When ``comment`` is in the update mask, omitting it clears the field, while an explicitly empty string is retained."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the skill was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Description from the most recently successfully finalized SKILL.md. Unset until FinalizeSkill succeeds."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the skill."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "finalize_time",
    "type": "string (date-time)",
    "description": "Time of the most recent successful FinalizeSkill. Unset until one succeeds."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time of the most recent Skill metadata mutation. Uploading bundle files alone does not change this value."
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
    <td>Returns the skill identified by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists skills in a Unity Catalog schema. Provide ``parent`` as ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Results</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-skill_id"><code>skill_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a skill in a Unity Catalog schema and provisions its managed bundle storage. Specify its name</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Updates a skill. Only fields named in ``update_mask`` are changed; currently only ``comment`` is</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the skill identified by its resource name and makes its managed bundle path unavailable.</td>
</tr>
<tr>
    <td><a href="#finalize"><CopyableCode code="finalize" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Finalizes a skill after its bundle files are uploaded or changed through the Files API. Call it again</td>
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
    <td>The `full_name` segment of the `name` resource name (`skills/&#123;full_name&#125;`). Full resource name of the skill. Format: ``skills/&#123;catalog&#125;.&#123;schema&#125;.&#123;skill&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-skill_id">
    <td><CopyableCode code="skill_id" /></td>
    <td><code>string</code></td>
    <td>Name for the skill, e.g. "basic-math". The server normalizes this identifier to lowercase. It is independent of the bundle name read from SKILL.md.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update; validated against ``skill``. REQUIRED, matching the sibling Update RPCs. ``comment`` is the only mutable field.</td>
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
    <td>Maximum number of skills to return. Defaults to 200 when unset or 0; the maximum is 200. Use ``page_token`` to retrieve additional pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from a previous request.</td>
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

Returns the skill identified by its resource name.

```sql
SELECT
name,
metastore_id,
bundle_name,
comment,
create_time,
created_by,
description,
effective_owner,
etag,
finalize_time,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_skills
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists skills in a Unity Catalog schema. Provide ``parent`` as ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Results

```sql
SELECT
name,
metastore_id,
bundle_name,
comment,
create_time,
created_by,
description,
effective_owner,
etag,
finalize_time,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_skills
WHERE parent = '{{ parent }}' -- required
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

Creates a skill in a Unity Catalog schema and provisions its managed bundle storage. Specify its name

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_skills (
bundle_name,
comment,
create_time,
created_by,
description,
effective_owner,
etag,
finalize_time,
metastore_id,
name,
update_time,
updated_by,
parent,
skill_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ bundle_name }}',
'{{ comment }}',
'{{ create_time }}',
'{{ created_by }}',
'{{ description }}',
'{{ effective_owner }}',
'{{ etag }}',
'{{ finalize_time }}',
'{{ metastore_id }}',
'{{ name }}',
'{{ update_time }}',
'{{ updated_by }}',
'{{ parent }}',
'{{ skill_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
metastore_id,
bundle_name,
comment,
create_time,
created_by,
description,
effective_owner,
etag,
finalize_time,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_skills
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_skills resource.
    - name: skill_id
      value: "{{ skill_id }}"
      description: Required parameter for the ai_gateway_skills resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_skills resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the ai_gateway_skills resource.
    - name: bundle_name
      value: "{{ bundle_name }}"
      description: |
        Name from the most recently successfully finalized SKILL.md. It may differ from the final component of the Skill resource name. Unset until FinalizeSkill succeeds.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided comment for the skill. Free-text, user-editable via UpdateSkill (listed in its \`\`update_mask\`\`). DISTINCT from \`\`description\`\`, which is the server-parsed, OUTPUT_ONLY SKILL.md frontmatter value: \`\`comment\`\` is the customer's own annotation and is preserved across bundle re-uploads. When \`\`comment\`\` is in the update mask, omitting it clears the field, while an explicitly empty string is retained.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time the skill was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        Creator identity.
    - name: description
      value: "{{ description }}"
      description: |
        Description from the most recently successfully finalized SKILL.md. Unset until FinalizeSkill succeeds.
    - name: effective_owner
      value: "{{ effective_owner }}"
      description: |
        Owner of the skill.
    - name: etag
      value: "{{ etag }}"
      description: |
        Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's \`\`etag\`\` field. In REST responses, this value is a base64 string; URL-encode it when setting the \`\`etag\`\` query parameter.
    - name: finalize_time
      value: "{{ finalize_time }}"
      description: |
        Time of the most recent successful FinalizeSkill. Unset until one succeeds.
    - name: metastore_id
      value: "{{ metastore_id }}"
      description: |
        Metastore hosting the skill.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name of the skill. Format: \`\`skills/{catalog}.{schema}.{skill}\`\`. Each \`\`{...}\`\` component is capped at 255 characters individually. Server-derived on Create from \`\`parent\`\` + \`\`skill_id\`\`; required and immutable on Update/Get/Delete.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time of the most recent Skill metadata mutation. Uploading bundle files alone does not change this value.
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

Updates a skill. Only fields named in ``update_mask`` are changed; currently only ``comment`` is

```sql
UPDATE databricks_workspace.catalog.ai_gateway_skills
SET 
bundle_name = '{{ bundle_name }}',
comment = '{{ comment }}',
create_time = '{{ create_time }}',
created_by = '{{ created_by }}',
description = '{{ description }}',
effective_owner = '{{ effective_owner }}',
etag = '{{ etag }}',
finalize_time = '{{ finalize_time }}',
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
bundle_name,
comment,
create_time,
created_by,
description,
effective_owner,
etag,
finalize_time,
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

Deletes the skill identified by its resource name and makes its managed bundle path unavailable.

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_skills
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="finalize"
    values={[
        { label: 'finalize', value: 'finalize' }
    ]}
>
<TabItem value="finalize">

Finalizes a skill after its bundle files are uploaded or changed through the Files API. Call it again

```sql
EXEC databricks_workspace.catalog.ai_gateway_skills.finalize 
@full_name='{{ full_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
