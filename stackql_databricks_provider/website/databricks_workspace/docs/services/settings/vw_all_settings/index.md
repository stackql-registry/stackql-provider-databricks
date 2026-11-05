---
title: vw_all_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_all_settings
  - settings
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

Creates, updates, deletes, gets or lists a <code>vw_all_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="vw_all_settings" /></td></tr>
<tr><td><b>Type</b></td><td>View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.settings.vw_all_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name the settings belong to.</td>
</tr>
<tr>
    <td><CopyableCode code="key" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The name of the workspace setting (only non-null values are included).</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><CopyableCode code="string" /></td>
    <td>The value of the workspace setting (only non-null values are included).</td>
</tr>
</tbody>
</table>

## Required Parameters

The following parameters are required by this view:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="deployment_name" /></td>
    <td><CopyableCode code="string" /></td>
    <td>Workspace deployment name used to scope the query.</td>
</tr>
</tbody>
</table>

## `SELECT` Examples

```sql
SELECT
  deployment_name,
  key,
  value
FROM databricks_workspace.settings.vw_all_settings
WHERE deployment_name = '{{ deployment_name }}';
```

## SQL Definition

<Tabs
defaultValue="Sqlite3"
values={[
{ label: 'Sqlite3', value: 'Sqlite3' },
{ label: 'Postgres', value: 'Postgres' }
]}
>
<TabItem value="Sqlite3">

```sql
SELECT
  c.deployment_name,
  je.key,
  je.value
FROM databricks_workspace.settings.workspace_config c,
  json_each(json_object(
    'enableWebTerminal', c.enableWebTerminal,
    'enableTokensConfig', c.enableTokensConfig,
    'maxTokenLifetimeDays', c.maxTokenLifetimeDays,
    'enableWorkspaceFilesystem', c.enableWorkspaceFilesystem,
    'enableExportNotebook', c.enableExportNotebook,
    'enableNotebookTableClipboard', c.enableNotebookTableClipboard,
    'enableResultsDownloading', c.enableResultsDownloading,
    'enableDcs', c.enableDcs,
    'enableGp3', c.enableGp3,
    'mlflowRunArtifactDownloadEnabled', c.mlflowRunArtifactDownloadEnabled,
    'enableUploadDataUis', c.enableUploadDataUis,
    'storeInteractiveNotebookResultsInCustomerAccount', c.storeInteractiveNotebookResultsInCustomerAccount,
    'enableDeprecatedGlobalInitScripts', c.enableDeprecatedGlobalInitScripts,
    'rStudioUserDefaultHomeBase', c.rStudioUserDefaultHomeBase,
    'enforceUserIsolation', c.enforceUserIsolation,
    'enableProjectsAllowList', c.enableProjectsAllowList,
    'projectsAllowListPermissions', c.projectsAllowListPermissions,
    'projectsAllowList', c.projectsAllowList,
    'reposIpynbResultsExportPermissions', c.reposIpynbResultsExportPermissions,
    'enableDbfsFileBrowser', c.enableDbfsFileBrowser,
    'enableDatabricksAutologgingAdminConf', c.enableDatabricksAutologgingAdminConf,
    'mlflowModelServingEndpointCreationEnabled', c.mlflowModelServingEndpointCreationEnabled,
    'enableVerboseAuditLogs', c.enableVerboseAuditLogs,
    'enableFileStoreEndpoint', c.enableFileStoreEndpoint,
    'loginLogo', c.loginLogo,
    'productName', c.productName,
    'homePageLogo', c.homePageLogo,
    'homePageLogoWidth', c.homePageLogoWidth,
    'homePageWelcomeMessage', c.homePageWelcomeMessage,
    'sidebarLogoText', c.sidebarLogoText,
    'sidebarLogoActive', c.sidebarLogoActive,
    'sidebarLogoInactive', c.sidebarLogoInactive,
    'customReferences', c.customReferences,
    'loginLogoWidth', c.loginLogoWidth,
    'enforceWorkspaceViewAcls', c.enforceWorkspaceViewAcls,
    'enforceClusterViewAcls', c.enforceClusterViewAcls,
    'enableJobViewAcls', c.enableJobViewAcls,
    'enableHlsRuntime', c.enableHlsRuntime,
    'enableEnforceImdsV2', c.enableEnforceImdsV2,
    'enableJobsEmailsV2', c.enableJobsEmailsV2,
    'enableProjectTypeInWorkspace', c.enableProjectTypeInWorkspace,
    'mlflowModelRegistryEmailNotificationsEnabled', c.mlflowModelRegistryEmailNotificationsEnabled,
    'jobsListBackendPaginationEnabled', c.jobsListBackendPaginationEnabled,
    'jobsListBackendPaginationOptOut', c.jobsListBackendPaginationOptOut
  )) je
WHERE c.keys = 'enableWebTerminal,enableTokensConfig,maxTokenLifetimeDays,enableWorkspaceFilesystem,enableExportNotebook,enableNotebookTableClipboard,enableResultsDownloading,enableDcs,enableGp3,mlflowRunArtifactDownloadEnabled,enableUploadDataUis,storeInteractiveNotebookResultsInCustomerAccount,enableDeprecatedGlobalInitScripts,rStudioUserDefaultHomeBase,enforceUserIsolation,enableProjectsAllowList,projectsAllowListPermissions,projectsAllowList,reposIpynbResultsExportPermissions,enableDbfsFileBrowser,enableDatabricksAutologgingAdminConf,mlflowModelServingEndpointCreationEnabled,enableVerboseAuditLogs,enableFileStoreEndpoint,loginLogo,productName,homePageLogo,homePageLogoWidth,homePageWelcomeMessage,sidebarLogoText,sidebarLogoActive,sidebarLogoInactive,customReferences,loginLogoWidth,enforceWorkspaceViewAcls,enforceClusterViewAcls,enableJobViewAcls,enableHlsRuntime,enableEnforceImdsV2,enableJobsEmailsV2,enableProjectTypeInWorkspace,mlflowModelRegistryEmailNotificationsEnabled,jobsListBackendPaginationEnabled,jobsListBackendPaginationOptOut'
  AND je.value IS NOT NULL
```

</TabItem>
<TabItem value="Postgres">

```sql
SELECT
  c.deployment_name,
  je.key,
  je.value
FROM databricks_workspace.settings.workspace_config c,
  jsonb_each_text(jsonb_build_object(
    'enableWebTerminal', c.enableWebTerminal,
    'enableTokensConfig', c.enableTokensConfig,
    'maxTokenLifetimeDays', c.maxTokenLifetimeDays,
    'enableWorkspaceFilesystem', c.enableWorkspaceFilesystem,
    'enableExportNotebook', c.enableExportNotebook,
    'enableNotebookTableClipboard', c.enableNotebookTableClipboard,
    'enableResultsDownloading', c.enableResultsDownloading,
    'enableDcs', c.enableDcs,
    'enableGp3', c.enableGp3,
    'mlflowRunArtifactDownloadEnabled', c.mlflowRunArtifactDownloadEnabled,
    'enableUploadDataUis', c.enableUploadDataUis,
    'storeInteractiveNotebookResultsInCustomerAccount', c.storeInteractiveNotebookResultsInCustomerAccount,
    'enableDeprecatedGlobalInitScripts', c.enableDeprecatedGlobalInitScripts,
    'rStudioUserDefaultHomeBase', c.rStudioUserDefaultHomeBase,
    'enforceUserIsolation', c.enforceUserIsolation,
    'enableProjectsAllowList', c.enableProjectsAllowList,
    'projectsAllowListPermissions', c.projectsAllowListPermissions,
    'projectsAllowList', c.projectsAllowList,
    'reposIpynbResultsExportPermissions', c.reposIpynbResultsExportPermissions,
    'enableDbfsFileBrowser', c.enableDbfsFileBrowser,
    'enableDatabricksAutologgingAdminConf', c.enableDatabricksAutologgingAdminConf,
    'mlflowModelServingEndpointCreationEnabled', c.mlflowModelServingEndpointCreationEnabled,
    'enableVerboseAuditLogs', c.enableVerboseAuditLogs,
    'enableFileStoreEndpoint', c.enableFileStoreEndpoint,
    'loginLogo', c.loginLogo,
    'productName', c.productName,
    'homePageLogo', c.homePageLogo,
    'homePageLogoWidth', c.homePageLogoWidth,
    'homePageWelcomeMessage', c.homePageWelcomeMessage,
    'sidebarLogoText', c.sidebarLogoText,
    'sidebarLogoActive', c.sidebarLogoActive,
    'sidebarLogoInactive', c.sidebarLogoInactive,
    'customReferences', c.customReferences,
    'loginLogoWidth', c.loginLogoWidth,
    'enforceWorkspaceViewAcls', c.enforceWorkspaceViewAcls,
    'enforceClusterViewAcls', c.enforceClusterViewAcls,
    'enableJobViewAcls', c.enableJobViewAcls,
    'enableHlsRuntime', c.enableHlsRuntime,
    'enableEnforceImdsV2', c.enableEnforceImdsV2,
    'enableJobsEmailsV2', c.enableJobsEmailsV2,
    'enableProjectTypeInWorkspace', c.enableProjectTypeInWorkspace,
    'mlflowModelRegistryEmailNotificationsEnabled', c.mlflowModelRegistryEmailNotificationsEnabled,
    'jobsListBackendPaginationEnabled', c.jobsListBackendPaginationEnabled,
    'jobsListBackendPaginationOptOut', c.jobsListBackendPaginationOptOut
  )) je
WHERE c.keys = 'enableWebTerminal,enableTokensConfig,maxTokenLifetimeDays,enableWorkspaceFilesystem,enableExportNotebook,enableNotebookTableClipboard,enableResultsDownloading,enableDcs,enableGp3,mlflowRunArtifactDownloadEnabled,enableUploadDataUis,storeInteractiveNotebookResultsInCustomerAccount,enableDeprecatedGlobalInitScripts,rStudioUserDefaultHomeBase,enforceUserIsolation,enableProjectsAllowList,projectsAllowListPermissions,projectsAllowList,reposIpynbResultsExportPermissions,enableDbfsFileBrowser,enableDatabricksAutologgingAdminConf,mlflowModelServingEndpointCreationEnabled,enableVerboseAuditLogs,enableFileStoreEndpoint,loginLogo,productName,homePageLogo,homePageLogoWidth,homePageWelcomeMessage,sidebarLogoText,sidebarLogoActive,sidebarLogoInactive,customReferences,loginLogoWidth,enforceWorkspaceViewAcls,enforceClusterViewAcls,enableJobViewAcls,enableHlsRuntime,enableEnforceImdsV2,enableJobsEmailsV2,enableProjectTypeInWorkspace,mlflowModelRegistryEmailNotificationsEnabled,jobsListBackendPaginationEnabled,jobsListBackendPaginationOptOut'
  AND je.value IS NOT NULL
```

</TabItem>
</Tabs>
