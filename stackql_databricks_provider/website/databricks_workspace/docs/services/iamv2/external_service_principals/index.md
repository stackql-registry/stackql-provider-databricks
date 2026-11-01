---
title: external_service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - external_service_principals
  - iamv2
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

Creates, updates, deletes, gets or lists an <code>external_service_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="external_service_principals" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iamv2.external_service_principals" /></td></tr>
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
    "description": "The resource name of the external service principal. The format depends on the API that returned it: - Account-scoped: accounts/&#123;account_id&#125;/external-service-principals/&#123;external_service_principal_id&#125; - Workspace-scoped: external-service-principals/&#123;external_service_principal_id&#125;"
  },
  {
    "name": "account_id",
    "type": "string",
    "description": "The parent account ID, from Databricks."
  },
  {
    "name": "application_id",
    "type": "string",
    "description": "Application ID of the service principal, from the customer's IdP."
  },
  {
    "name": "external_service_principal_id",
    "type": "string",
    "description": "The external ID of the service principal in the customer's IdP."
  },
  {
    "name": "internal_id",
    "type": "string",
    "description": "Internal servicePrincipalId of the service principal in Databricks."
  },
  {
    "name": "display_name",
    "type": "string",
    "description": "Display name of the service principal, from the customer's IdP."
  },
  {
    "name": "account_sp_status",
    "type": "string",
    "description": "The activity status of the service principal in the Databricks account. (ACTIVE, INACTIVE)"
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
    <td><a href="#parameter-external_service_principal_id"><code>external_service_principal_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves an external service principal with the given external ID from the customer's IdP. If the</td>
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
<tr id="parameter-external_service_principal_id">
    <td><CopyableCode code="external_service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The `external_service_principal_id` segment of the `name` resource name (`external-service-principals/&#123;external_service_principal_id&#125;`). Required. The resource name of the external service principal. Format: external-service-principals/&#123;external_service_principal_id&#125;</td>
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

Retrieves an external service principal with the given external ID from the customer's IdP. If the

```sql
SELECT
name,
account_id,
application_id,
external_service_principal_id,
internal_id,
display_name,
account_sp_status
FROM databricks_workspace.iamv2.external_service_principals
WHERE external_service_principal_id = '{{ external_service_principal_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
</Tabs>
