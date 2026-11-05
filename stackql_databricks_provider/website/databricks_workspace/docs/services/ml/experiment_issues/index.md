---
title: experiment_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_issues
  - ml
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

Creates, updates, deletes, gets or lists an <code>experiment_issues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="experiment_issues" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.ml.experiment_issues" /></td></tr>
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
    "description": "experiments/&#123;experiment&#125;/issues/&#123;issue&#125;"
  },
  {
    "name": "issue_id",
    "type": "string",
    "description": "The last segment of ``name``. Issue assessments on traces reference the Issue by this ID."
  },
  {
    "name": "source_id",
    "type": "string",
    "description": "Set once at create. For ADHOC_RUN and SCHEDULED_RUN, the ID of the issue detection run in the same experiment that created the Issue. Absent for MANUAL."
  },
  {
    "name": "categories",
    "type": "array",
    "description": "At most 10 values of at most 64 UTF-8 bytes each, unique case-insensitively. Leading and trailing whitespace is trimmed."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "When the Issue was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "The email of the user whose request created the Issue. source_type tells whether issue detection created it."
  },
  {
    "name": "description",
    "type": "string",
    "description": "Markdown, at most 32 KiB."
  },
  {
    "name": "last_seen_time",
    "type": "string (date-time)",
    "description": "The request time of the latest trace the Issue affects. Required, and can't be cleared, unless source_type is MANUAL. A MANUAL Issue without one returns its create_time."
  },
  {
    "name": "last_updated_by",
    "type": "string",
    "description": "The email of the user whose request last updated the Issue."
  },
  {
    "name": "metadata",
    "type": "object",
    "description": "Additional details about the Issue, such as how issue detection observed it. Not a stable contract: keys and values can change without notice, so clients must tolerate unknown and missing keys. At most 20 entries, with keys of at most 64 UTF-8 bytes."
  },
  {
    "name": "severity",
    "type": "string",
    "description": "Cannot be cleared: an Issue without a severity would match no severity filter. (HIGH, LOW, MEDIUM)"
  },
  {
    "name": "source_type",
    "type": "string",
    "description": "Set once at create. Defaults to MANUAL. (ADHOC_RUN, MANUAL, SCHEDULED_RUN, SINGLE_TRACE_ANALYSIS)"
  },
  {
    "name": "status",
    "type": "string",
    "description": "Defaults to PENDING on create, and can't be cleared. (PENDING, REJECTED, RESOLVED)"
  },
  {
    "name": "tags",
    "type": "object",
    "description": "Caller-owned; the server never writes system values here. At most 10 entries. Keys match ^[A-Za-z0-9_.:/-]+$ and are at most 128 UTF-8 bytes; values are at most 256 UTF-8 bytes."
  },
  {
    "name": "title",
    "type": "string",
    "description": "Non-empty, at most 250 UTF-8 bytes."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "When the Issue was last updated."
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
    <td><a href="#parameter-experiment"><code>experiment</code></a>, <a href="#parameter-issue"><code>issue</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Gets an issue.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-experiment"><code>experiment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-title"><code>title</code></a>, <a href="#parameter-severity"><code>severity</code></a></td>
    <td><a href="#parameter-issue_id"><code>issue_id</code></a></td>
    <td>Creates an issue in an experiment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-experiment"><code>experiment</code></a>, <a href="#parameter-issue"><code>issue</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Updates the fields of an issue named in ``update_mask``.</td>
</tr>
<tr>
    <td><a href="#search"><CopyableCode code="search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-experiment"><code>experiment</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Searches the issues in an experiment, filtered and sorted.</td>
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
<tr id="parameter-experiment">
    <td><CopyableCode code="experiment" /></td>
    <td><code>string</code></td>
    <td>The `experiment` segment of the `parent` resource name (`experiments/&#123;experiment&#125;`). experiments/&#123;experiment&#125;</td>
</tr>
<tr id="parameter-issue">
    <td><CopyableCode code="issue" /></td>
    <td><code>object</code></td>
    <td>``issue.name`` identifies the target.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Accepts title, description, status, severity, categories, tags, last_seen_time, and metadata.&lt;key&gt;. A path with an empty value clears the field, except that title, status, and severity can't be cleared, and last_seen_time can be cleared only when source_type is MANUAL. categories and tags are replaced whole. metadata is updated per key: a metadata.&lt;key&gt; path sets that key from issue.metadata, or removes it when issue.metadata lacks it, and leaves the other keys alone. A bare metadata path is rejected.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-issue_id">
    <td><CopyableCode code="issue_id" /></td>
    <td><code>string</code></td>
    <td>Optional client-chosen ID: iss- followed by 32 lowercase hex digits. A retry with the same ID fails with ALREADY_EXISTS rather than making a duplicate. The server generates one if unset.</td>
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

Gets an issue.

```sql
SELECT
name,
issue_id,
source_id,
categories,
create_time,
created_by,
description,
last_seen_time,
last_updated_by,
metadata,
severity,
source_type,
status,
tags,
title,
update_time
FROM databricks_workspace.ml.experiment_issues
WHERE experiment = '{{ experiment }}' -- required
AND issue = '{{ issue }}' -- required
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

Creates an issue in an experiment.

```sql
INSERT INTO databricks_workspace.ml.experiment_issues (
title,
severity,
categories,
create_time,
created_by,
description,
issue_id,
last_seen_time,
last_updated_by,
metadata,
name,
source_id,
source_type,
status,
tags,
update_time,
experiment,
deployment_name,
workspace_domain,
issue_id
)
SELECT 
'{{ title }}' /* required */,
'{{ severity }}' /* required */,
'{{ categories }}',
'{{ create_time }}',
'{{ created_by }}',
'{{ description }}',
'{{ issue_id }}',
'{{ last_seen_time }}',
'{{ last_updated_by }}',
'{{ metadata }}',
'{{ name }}',
'{{ source_id }}',
'{{ source_type }}',
'{{ status }}',
'{{ tags }}',
'{{ update_time }}',
'{{ experiment }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ issue_id }}'
RETURNING
name,
issue_id,
source_id,
categories,
create_time,
created_by,
description,
last_seen_time,
last_updated_by,
metadata,
severity,
source_type,
status,
tags,
title,
update_time
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: experiment_issues
  props:
    - name: experiment
      value: "{{ experiment }}"
      description: Required parameter for the experiment_issues resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the experiment_issues resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the experiment_issues resource.
    - name: title
      value: "{{ title }}"
      description: |
        Non-empty, at most 250 UTF-8 bytes.
    - name: severity
      value: "{{ severity }}"
      description: |
        Cannot be cleared: an Issue without a severity would match no severity filter.
    - name: categories
      value:
        - "{{ categories }}"
      description: |
        At most 10 values of at most 64 UTF-8 bytes each, unique case-insensitively. Leading and trailing whitespace is trimmed.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        When the Issue was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        The email of the user whose request created the Issue. source_type tells whether issue detection created it.
    - name: description
      value: "{{ description }}"
      description: |
        Markdown, at most 32 KiB.
    - name: issue_id
      value: "{{ issue_id }}"
      description: |
        The last segment of \`\`name\`\`. Issue assessments on traces reference the Issue by this ID.
    - name: last_seen_time
      value: "{{ last_seen_time }}"
      description: |
        The request time of the latest trace the Issue affects. Required, and can't be cleared, unless source_type is MANUAL. A MANUAL Issue without one returns its create_time.
    - name: last_updated_by
      value: "{{ last_updated_by }}"
      description: |
        The email of the user whose request last updated the Issue.
    - name: metadata
      value: "{{ metadata }}"
      description: |
        Additional details about the Issue, such as how issue detection observed it. Not a stable contract: keys and values can change without notice, so clients must tolerate unknown and missing keys. At most 20 entries, with keys of at most 64 UTF-8 bytes.
    - name: name
      value: "{{ name }}"
      description: |
        experiments/{experiment}/issues/{issue}
    - name: source_id
      value: "{{ source_id }}"
      description: |
        Set once at create. For ADHOC_RUN and SCHEDULED_RUN, the ID of the issue detection run in the same experiment that created the Issue. Absent for MANUAL.
    - name: source_type
      value: "{{ source_type }}"
      description: |
        Set once at create. Defaults to MANUAL.
    - name: status
      value: "{{ status }}"
      description: |
        Defaults to PENDING on create, and can't be cleared.
    - name: tags
      value: "{{ tags }}"
      description: |
        Caller-owned; the server never writes system values here. At most 10 entries. Keys match ^[A-Za-z0-9_.:/-]+$ and are at most 128 UTF-8 bytes; values are at most 256 UTF-8 bytes.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        When the Issue was last updated.
    - name: issue_id
      value: "{{ issue_id }}"
      description: Optional client-chosen ID: iss- followed by 32 lowercase hex digits. A retry with the same ID fails with ALREADY_EXISTS rather than making a duplicate. The server generates one if unset.
      description: Optional client-chosen ID: iss- followed by 32 lowercase hex digits. A retry with the same ID fails with ALREADY_EXISTS rather than making a duplicate. The server generates one if unset.
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

Updates the fields of an issue named in ``update_mask``.

```sql
UPDATE databricks_workspace.ml.experiment_issues
SET 
-- No updatable properties
WHERE 
experiment = '{{ experiment }}' --required
AND issue = '{{ issue }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
RETURNING
name,
issue_id,
source_id,
categories,
create_time,
created_by,
description,
last_seen_time,
last_updated_by,
metadata,
severity,
source_type,
status,
tags,
title,
update_time;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="search"
    values={[
        { label: 'search', value: 'search' }
    ]}
>
<TabItem value="search">

Searches the issues in an experiment, filtered and sorted.

```sql
EXEC databricks_workspace.ml.experiment_issues.search 
@experiment='{{ experiment }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required 
@@json=
'{
"categories": "{{ categories }}", 
"page_size": {{ page_size }}, 
"page_token": "{{ page_token }}", 
"query": "{{ query }}", 
"severities": "{{ severities }}", 
"sort_key": "{{ sort_key }}", 
"sort_order": "{{ sort_order }}", 
"statuses": "{{ statuses }}", 
"tag_filters": "{{ tag_filters }}", 
"view": "{{ view }}"
}'
;
```
</TabItem>
</Tabs>
