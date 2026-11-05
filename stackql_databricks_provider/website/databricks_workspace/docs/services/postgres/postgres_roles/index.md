---
title: postgres_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_roles
  - postgres
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

Creates, updates, deletes, gets or lists a <code>postgres_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="postgres_roles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.postgres.postgres_roles" /></td></tr>
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
    "description": "Output only. The full resource path of the role. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
  },
  {
    "name": "role_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The Branch where this Role exists. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the role configuration, including identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "Controls how the Postgres role authenticates when a client opens a database connection. Supported values: - LAKEBASE_OAUTH_V1: the role authenticates by presenting a Databricks OAuth access token derived from the backing managed identity (the Databricks user, service principal, or group named by the role's ``postgres_role``). No static password exists for roles using this method. - PG_PASSWORD_SCRAM_SHA_256: the role authenticates with a Postgres password verified server-side using the SCRAM-SHA-256 mechanism. Lakebase generates a password for the role. - NO_LOGIN: the role cannot open a Postgres session at all. Useful for roles that exist only to own objects or to aggregate privileges that are then granted to other, loginable roles. If auth_method is left unspecified, a meaningful authentication method is derived from the identity_type: - For the managed identities, OAUTH is used. - For the regular postgres roles, authentication based on postgres passwords is used. NOTE: for the Databricks identity type GROUP, LAKEBASE_OAUTH_V1 is the default auth method (group can login as well). (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of role. When specifying a managed-identity, the chosen role_id must be a valid: - application ID for SERVICE_PRINCIPAL - user email for USER - group name for GROUP (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Role. If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 3. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the role, including its identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of the role. (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role."
      },
      {
        "name": "role_id",
        "type": "string",
        "description": "Part of the resource name."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "name",
    "type": "string",
    "description": "Output only. The full resource path of the role. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;"
  },
  {
    "name": "role_id",
    "type": "string",
    "description": "The part of the name, chosen by the user when the resource was created."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": ""
  },
  {
    "name": "parent",
    "type": "string",
    "description": "The Branch where this Role exists. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;"
  },
  {
    "name": "spec",
    "type": "object",
    "description": "The spec contains the role configuration, including identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "Controls how the Postgres role authenticates when a client opens a database connection. Supported values: - LAKEBASE_OAUTH_V1: the role authenticates by presenting a Databricks OAuth access token derived from the backing managed identity (the Databricks user, service principal, or group named by the role's ``postgres_role``). No static password exists for roles using this method. - PG_PASSWORD_SCRAM_SHA_256: the role authenticates with a Postgres password verified server-side using the SCRAM-SHA-256 mechanism. Lakebase generates a password for the role. - NO_LOGIN: the role cannot open a Postgres session at all. Useful for roles that exist only to own objects or to aggregate privileges that are then granted to other, loginable roles. If auth_method is left unspecified, a meaningful authentication method is derived from the identity_type: - For the managed identities, OAUTH is used. - For the regular postgres roles, authentication based on postgres passwords is used. NOTE: for the Databricks identity type GROUP, LAKEBASE_OAUTH_V1 is the default auth method (group can login as well). (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of role. When specifying a managed-identity, the chosen role_id must be a valid: - application ID for SERVICE_PRINCIPAL - user email for USER - group name for GROUP (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role. This expects a valid Postgres identifier as specified in the link below. https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS Required when creating the Role. If you wish to create a Postgres Role backed by a managed Databricks identity, then postgres_role must be one of the following: 1. user email for IdentityType.USER 2. app ID for IdentityType.SERVICE_PRINCIPAL 3. group name for IdentityType.GROUP"
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "Current status of the role, including its identity type, authentication method, and role attributes.",
    "children": [
      {
        "name": "attributes",
        "type": "object",
        "description": "Attributes that can be granted to a Postgres role. We are only implementing a subset for now,<br />    see xref: https://www.postgresql.org/docs/16/sql-createrole.html The values follow Postgres<br />    keyword naming e.g. CREATEDB, BYPASSRLS, etc. which is why they don't include typical<br />    underscores between words.",
        "children": [
          {
            "name": "bypassrls",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createdb",
            "type": "boolean",
            "description": ""
          },
          {
            "name": "createrole",
            "type": "boolean",
            "description": ""
          }
        ]
      },
      {
        "name": "auth_method",
        "type": "string",
        "description": "How the role is authenticated when connecting to Postgres. (LAKEBASE_OAUTH_V1, NO_LOGIN, PG_PASSWORD_SCRAM_SHA_256)"
      },
      {
        "name": "identity_type",
        "type": "string",
        "description": "The type of the role. (GROUP, SERVICE_PRINCIPAL, USER)"
      },
      {
        "name": "membership_roles",
        "type": "array",
        "description": "An enum value for a standard role that this role is a member of."
      },
      {
        "name": "postgres_role",
        "type": "string",
        "description": "The name of the Postgres role."
      },
      {
        "name": "role_id",
        "type": "string",
        "description": "Part of the resource name."
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": ""
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
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-role_id"><code>role_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information about the specified Postgres role, including its authentication method and</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Returns a paginated list of Postgres roles in the branch.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-replace_existing"><code>replace_existing</code></a>, <a href="#parameter-role_id"><code>role_id</code></a></td>
    <td>Creates a new Postgres role in the branch.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-role_id"><code>role_id</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Update a role for a branch.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-role_id"><code>role_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-reassign_owned_to"><code>reassign_owned_to</code></a></td>
    <td>Deletes the specified Postgres role.</td>
</tr>
<tr>
    <td><a href="#reveal_password"><CopyableCode code="reveal_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-project_id"><code>project_id</code></a>, <a href="#parameter-branch_id"><code>branch_id</code></a>, <a href="#parameter-role_id"><code>role_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Reveals the current password for a password-authenticated Postgres role.</td>
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
<tr id="parameter-branch_id">
    <td><CopyableCode code="branch_id" /></td>
    <td><code>string</code></td>
    <td>The `branch_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;`). The full resource path of the role whose password should be revealed. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace deployment name: the host prefix of the workspace URL (dbc-abcd0123-a1bc on AWS, adb-1234567890123456.7 on Azure, 1234567890123456.7 on GCP). Set DATABRICKS_DEPLOYMENT_NAME to default it for the session. (default: dbc-abcd0123-a1bc, x-stackQL-envVar: DATABRICKS_DEPLOYMENT_NAME)</td>
</tr>
<tr id="parameter-project_id">
    <td><CopyableCode code="project_id" /></td>
    <td><code>string</code></td>
    <td>The `project_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;`). The full resource path of the role whose password should be revealed. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;</td>
</tr>
<tr id="parameter-role_id">
    <td><CopyableCode code="role_id" /></td>
    <td><code>string</code></td>
    <td>The `role_id` segment of the `name` resource name (`projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;`). The full resource path of the role whose password should be revealed. Format: projects/&#123;project_id&#125;/branches/&#123;branch_id&#125;/roles/&#123;role_id&#125;</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The list of fields to update.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned. Cannot be negative.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Page token from a previous response. If not provided, returns the first page.</td>
</tr>
<tr id="parameter-reassign_owned_to">
    <td><CopyableCode code="reassign_owned_to" /></td>
    <td><code>string</code></td>
    <td>Reassign objects. If this is set, all objects owned by the role are reassigned to the role specified in this parameter. NOTE: setting this requires spinning up a compute to succeed, since it involves running SQL queries.</td>
</tr>
<tr id="parameter-replace_existing">
    <td><CopyableCode code="replace_existing" /></td>
    <td><code>boolean</code></td>
    <td>If true, update the role if it already exists instead of returning an error. When the role already exists, the provided ``role`` spec fully replaces the existing one: ``membership_roles`` is overwritten, not merged. Leaving ``membership_roles`` empty clears all of the role's existing memberships, including ``DATABRICKS_SUPERUSER``. Always send the complete desired list of memberships when using this field.</td>
</tr>
<tr id="parameter-role_id">
    <td><CopyableCode code="role_id" /></td>
    <td><code>string</code></td>
    <td>The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.</td>
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

Retrieves information about the specified Postgres role, including its authentication method and

```sql
SELECT
name,
role_id,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
AND role_id = '{{ role_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns a paginated list of Postgres roles in the branch.

```sql
SELECT
name,
role_id,
create_time,
parent,
spec,
status,
update_time
FROM databricks_workspace.postgres.postgres_roles
WHERE project_id = '{{ project_id }}' -- required
AND branch_id = '{{ branch_id }}' -- required
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

Creates a new Postgres role in the branch.

```sql
INSERT INTO databricks_workspace.postgres.postgres_roles (
create_time,
name,
parent,
role_id,
spec,
status,
update_time,
project_id,
branch_id,
deployment_name,
workspace_domain,
replace_existing,
role_id
)
SELECT 
'{{ create_time }}',
'{{ name }}',
'{{ parent }}',
'{{ role_id }}',
'{{ spec }}',
'{{ status }}',
'{{ update_time }}',
'{{ project_id }}',
'{{ branch_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}',
'{{ replace_existing }}',
'{{ role_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: postgres_roles
  props:
    - name: project_id
      value: "{{ project_id }}"
      description: Required parameter for the postgres_roles resource.
    - name: branch_id
      value: "{{ branch_id }}"
      description: Required parameter for the postgres_roles resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the postgres_roles resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the postgres_roles resource.
    - name: create_time
      value: "{{ create_time }}"
    - name: name
      value: "{{ name }}"
      description: |
        Output only. The full resource path of the role. Format: projects/{project_id}/branches/{branch_id}/roles/{role_id}
    - name: parent
      value: "{{ parent }}"
      description: |
        The Branch where this Role exists. Format: projects/{project_id}/branches/{branch_id}
    - name: role_id
      value: "{{ role_id }}"
      description: |
        The part of the name, chosen by the user when the resource was created.
    - name: spec
      description: |
        The spec contains the role configuration, including identity type, authentication method, and role attributes.
      value:
        attributes:
          bypassrls: {{ bypassrls }}
          createdb: {{ createdb }}
          createrole: {{ createrole }}
        auth_method: "{{ auth_method }}"
        identity_type: "{{ identity_type }}"
        membership_roles:
          - "{{ membership_roles }}"
        postgres_role: "{{ postgres_role }}"
    - name: status
      description: |
        Current status of the role, including its identity type, authentication method, and role attributes.
      value:
        attributes:
          bypassrls: {{ bypassrls }}
          createdb: {{ createdb }}
          createrole: {{ createrole }}
        auth_method: "{{ auth_method }}"
        identity_type: "{{ identity_type }}"
        membership_roles:
          - "{{ membership_roles }}"
        postgres_role: "{{ postgres_role }}"
        role_id: "{{ role_id }}"
    - name: update_time
      value: "{{ update_time }}"
    - name: replace_existing
      value: {{ replace_existing }}
      description: If true, update the role if it already exists instead of returning an error. When the role already exists, the provided \`\`role\`\` spec fully replaces the existing one: \`\`membership_roles\`\` is overwritten, not merged. Leaving \`\`membership_roles\`\` empty clears all of the role's existing memberships, including \`\`DATABRICKS_SUPERUSER\`\`. Always send the complete desired list of memberships when using this field.
      description: If true, update the role if it already exists instead of returning an error. When the role already exists, the provided \`\`role\`\` spec fully replaces the existing one: \`\`membership_roles\`\` is overwritten, not merged. Leaving \`\`membership_roles\`\` empty clears all of the role's existing memberships, including \`\`DATABRICKS_SUPERUSER\`\`. Always send the complete desired list of memberships when using this field.
    - name: role_id
      value: "{{ role_id }}"
      description: The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.
      description: The ID to use for the Role, which will become the final component of the role's resource name. This ID becomes the role in Postgres. This value should be 4-63 characters, and valid characters are lowercase letters, numbers, and hyphens, as defined by RFC 1123. If role_id is not specified in the request, it is generated automatically.
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

Update a role for a branch.

```sql
UPDATE databricks_workspace.postgres.postgres_roles
SET 
create_time = '{{ create_time }}',
name = '{{ name }}',
parent = '{{ parent }}',
role_id = '{{ role_id }}',
spec = '{{ spec }}',
status = '{{ status }}',
update_time = '{{ update_time }}'
WHERE 
project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND role_id = '{{ role_id }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required;
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

Deletes the specified Postgres role.

```sql
DELETE FROM databricks_workspace.postgres.postgres_roles
WHERE project_id = '{{ project_id }}' --required
AND branch_id = '{{ branch_id }}' --required
AND role_id = '{{ role_id }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND reassign_owned_to = '{{ reassign_owned_to }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reveal_password"
    values={[
        { label: 'reveal_password', value: 'reveal_password' }
    ]}
>
<TabItem value="reveal_password">

Reveals the current password for a password-authenticated Postgres role.

```sql
EXEC databricks_workspace.postgres.postgres_roles.reveal_password 
@project_id='{{ project_id }}' --required, 
@branch_id='{{ branch_id }}' --required, 
@role_id='{{ role_id }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@workspace_domain='{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
