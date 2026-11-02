---
title: app_spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - app_spaces
  - apps
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

Creates, updates, deletes, gets or lists an <code>app_spaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_spaces" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.app_spaces" /></td></tr>
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
    "description": "The unique identifier of the app space."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "assume_group_id",
    "type": "string",
    "description": "The group whose permissions users assume via Role Authorization for apps in this space. When set, user tokens assume the role of this group instead of doing regular obo token downscoping. Set only at space creation."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The effective usage policy ID used by apps in the space."
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": "The service principal client ID for the app space."
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": "The service principal ID for the app space."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy ID for managing cost at the space level."
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": "The service principal name for the app space."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The creation time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app space."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app space."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app space. Resources configured at the space level are available to all apps in the space.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "app",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_USE)"
          }
        ]
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "postgres",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": ""
          },
          {
            "name": "database",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
          }
        ]
      },
      {
        "name": "serving_endpoint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, MODEL_SERVICE, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          },
          {
            "name": "securable_kind",
            "type": "string",
            "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The status of the app space.",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The state of the app space. (SPACE_ACTIVE, SPACE_CREATING, SPACE_DELETED, SPACE_DELETING, SPACE_ERROR, SPACE_UPDATING)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The update time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app space."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": "OAuth scopes for apps in the space."
  }
]} />
</TabItem>
<TabItem value="list">

<SchemaTable fields={[
  {
    "name": "id",
    "type": "string",
    "description": "The unique identifier of the app space."
  },
  {
    "name": "name",
    "type": "string",
    "description": ""
  },
  {
    "name": "assume_group_id",
    "type": "string",
    "description": "The group whose permissions users assume via Role Authorization for apps in this space. When set, user tokens assume the role of this group instead of doing regular obo token downscoping. Set only at space creation."
  },
  {
    "name": "effective_usage_policy_id",
    "type": "string",
    "description": "The effective usage policy ID used by apps in the space."
  },
  {
    "name": "service_principal_client_id",
    "type": "string",
    "description": "The service principal client ID for the app space."
  },
  {
    "name": "service_principal_id",
    "type": "integer",
    "description": "The service principal ID for the app space."
  },
  {
    "name": "usage_policy_id",
    "type": "string",
    "description": "The usage policy ID for managing cost at the space level."
  },
  {
    "name": "service_principal_name",
    "type": "string",
    "description": "The service principal name for the app space."
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "The creation time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "creator",
    "type": "string",
    "description": "The email of the user that created the app space."
  },
  {
    "name": "description",
    "type": "string",
    "description": "The description of the app space."
  },
  {
    "name": "effective_user_api_scopes",
    "type": "array",
    "description": "The effective api scopes granted to the user access token."
  },
  {
    "name": "resources",
    "type": "array",
    "description": "Resources for the app space. Resources configured at the space level are available to all apps in the space.",
    "children": [
      {
        "name": "name",
        "type": "string",
        "description": ""
      },
      {
        "name": "app",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_USE)"
          }
        ]
      },
      {
        "name": "database",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "instance_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "database_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "description",
        "type": "string",
        "description": "Description of the App Resource."
      },
      {
        "name": "experiment",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "experiment_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_READ)"
          }
        ]
      },
      {
        "name": "genie_space",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "space_id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_EDIT, CAN_MANAGE, CAN_RUN, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "job",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permissions to grant on the Job. Supported permissions are: \"CAN_MANAGE\", \"IS_OWNER\", \"CAN_MANAGE_RUN\", \"CAN_VIEW\". (CAN_MANAGE, CAN_MANAGE_RUN, CAN_VIEW, IS_OWNER)"
          }
        ]
      },
      {
        "name": "postgres",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "branch",
            "type": "string",
            "description": ""
          },
          {
            "name": "database",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CAN_CONNECT_AND_CREATE)"
          }
        ]
      },
      {
        "name": "secret",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "scope",
            "type": "string",
            "description": ""
          },
          {
            "name": "key",
            "type": "string",
            "description": "Key of the secret to grant permission on."
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the secret scope. For secrets, only one permission is allowed. Permission must be one of: \"READ\", \"WRITE\", \"MANAGE\". (MANAGE, READ, WRITE)"
          }
        ]
      },
      {
        "name": "serving_endpoint",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "name",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the serving endpoint. Supported permissions are: \"CAN_MANAGE\", \"CAN_QUERY\", \"CAN_VIEW\". (CAN_MANAGE, CAN_QUERY, CAN_VIEW)"
          }
        ]
      },
      {
        "name": "sql_warehouse",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "id",
            "type": "string",
            "description": ""
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Permission to grant on the SQL warehouse. Supported permissions are: \"CAN_MANAGE\", \"CAN_USE\", \"IS_OWNER\". (CAN_MANAGE, CAN_USE, IS_OWNER)"
          }
        ]
      },
      {
        "name": "uc_securable",
        "type": "object",
        "description": "",
        "children": [
          {
            "name": "securable_full_name",
            "type": "string",
            "description": ""
          },
          {
            "name": "securable_type",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (CONNECTION, FUNCTION, MODEL_SERVICE, TABLE, VOLUME)"
          },
          {
            "name": "permission",
            "type": "string",
            "description": "Create a collection of name/value pairs.<br /><br />Example enumeration:<br /><br />&gt;&gt;&gt; class Color(Enum):<br />...     RED = 1<br />...     BLUE = 2<br />...     GREEN = 3<br /><br />Access them by:<br /><br />- attribute access:<br /><br />  &gt;&gt;&gt; Color.RED<br />  &lt;Color.RED: 1&gt;<br /><br />- value lookup:<br /><br />  &gt;&gt;&gt; Color(1)<br />  &lt;Color.RED: 1&gt;<br /><br />- name lookup:<br /><br />  &gt;&gt;&gt; Color['RED']<br />  &lt;Color.RED: 1&gt;<br /><br />Enumerations can be iterated over, and know how many members they have:<br /><br />&gt;&gt;&gt; len(Color)<br />3<br /><br />&gt;&gt;&gt; list(Color)<br />[&lt;Color.RED: 1&gt;, &lt;Color.BLUE: 2&gt;, &lt;Color.GREEN: 3&gt;]<br /><br />Methods can be added to enumerations, and members can have their own<br />attributes -- see the documentation for details. (EXECUTE, MODIFY, READ_VOLUME, SELECT, USE_CONNECTION, WRITE_VOLUME)"
          },
          {
            "name": "securable_kind",
            "type": "string",
            "description": "The securable kind from Unity Catalog. See https://docs.databricks.com/api/workspace/tables/get#securable_kind_manifest-securable_kind."
          }
        ]
      }
    ]
  },
  {
    "name": "status",
    "type": "object",
    "description": "The status of the app space.",
    "children": [
      {
        "name": "message",
        "type": "string",
        "description": ""
      },
      {
        "name": "state",
        "type": "string",
        "description": "The state of the app space. (SPACE_ACTIVE, SPACE_CREATING, SPACE_DELETED, SPACE_DELETING, SPACE_ERROR, SPACE_UPDATING)"
      }
    ]
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "The update time of the app space. Formatted timestamp in ISO 6801."
  },
  {
    "name": "updater",
    "type": "string",
    "description": "The email of the user that last updated the app space."
  },
  {
    "name": "user_api_scopes",
    "type": "array",
    "description": "OAuth scopes for apps in the space."
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
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Retrieves information for the app space with the supplied name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a></td>
    <td>Lists all app spaces in the workspace.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates a new app space.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Updates an app space. The update process is asynchronous and the status of the update can be checked</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Deletes an app space.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the app space.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>The field mask must be a single string, with multiple fields separated by commas (no spaces). The field path is relative to the resource object, using a dot (``.``) to navigate sub-fields (e.g., ``author.given_name``). Specification of elements in sequence or map fields is not allowed, as only the entire collection field can be specified. Field names must exactly match the resource field names. A field mask of ``*`` indicates full replacement. It’s recommended to always explicitly list the fields being updated and avoid using ``*`` wildcards, as it can lead to unintended results if the API changes in the future.</td>
</tr>
<tr id="parameter-workspace_domain">
    <td><CopyableCode code="workspace_domain" /></td>
    <td><code>string</code></td>
    <td>The Databricks workspace domain suffix for the cloud. Selected by DATABRICKS_CLOUD (aws, azure or gcp; default aws). (default: cloud.databricks.com, x-stackQL-envVarSelector: &#123;"envVar":"DATABRICKS_CLOUD","default":"aws","values":&#123;"aws":"cloud.databricks.com","azure":"azuredatabricks.net","gcp":"gcp.databricks.com"&#125;&#125;)</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>Upper bound for items returned.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Pagination token to go to the next page of app spaces. Requests first page if absent.</td>
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

Retrieves information for the app space with the supplied name.

```sql
SELECT
id,
name,
assume_group_id,
effective_usage_policy_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
create_time,
creator,
description,
effective_user_api_scopes,
resources,
status,
update_time,
updater,
user_api_scopes
FROM databricks_workspace.apps.app_spaces
WHERE name = '{{ name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all app spaces in the workspace.

```sql
SELECT
id,
name,
assume_group_id,
effective_usage_policy_id,
service_principal_client_id,
service_principal_id,
usage_policy_id,
service_principal_name,
create_time,
creator,
description,
effective_user_api_scopes,
resources,
status,
update_time,
updater,
user_api_scopes
FROM databricks_workspace.apps.app_spaces
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

Creates a new app space.

```sql
INSERT INTO databricks_workspace.apps.app_spaces (
name,
assume_group_id,
create_time,
creator,
description,
effective_usage_policy_id,
effective_user_api_scopes,
id,
resources,
service_principal_client_id,
service_principal_id,
service_principal_name,
status,
update_time,
updater,
usage_policy_id,
user_api_scopes,
deployment_name,
workspace_domain
)
SELECT 
'{{ name }}' /* required */,
'{{ assume_group_id }}',
'{{ create_time }}',
'{{ creator }}',
'{{ description }}',
'{{ effective_usage_policy_id }}',
'{{ effective_user_api_scopes }}',
'{{ id }}',
'{{ resources }}',
'{{ service_principal_client_id }}',
{{ service_principal_id }},
'{{ service_principal_name }}',
'{{ status }}',
'{{ update_time }}',
'{{ updater }}',
'{{ usage_policy_id }}',
'{{ user_api_scopes }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_spaces
  props:
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the app_spaces resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the app_spaces resource.
    - name: name
      value: "{{ name }}"
    - name: assume_group_id
      value: "{{ assume_group_id }}"
      description: |
        The group whose permissions users assume via Role Authorization for apps in this space. When set, user tokens assume the role of this group instead of doing regular obo token downscoping. Set only at space creation.
    - name: create_time
      value: "{{ create_time }}"
      description: |
        The creation time of the app space. Formatted timestamp in ISO 6801.
    - name: creator
      value: "{{ creator }}"
      description: |
        The email of the user that created the app space.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the app space.
    - name: effective_usage_policy_id
      value: "{{ effective_usage_policy_id }}"
      description: |
        The effective usage policy ID used by apps in the space.
    - name: effective_user_api_scopes
      value:
        - "{{ effective_user_api_scopes }}"
      description: |
        The effective api scopes granted to the user access token.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier of the app space.
    - name: resources
      description: |
        Resources for the app space. Resources configured at the space level are available to all apps in the space.
      value:
        - name: "{{ name }}"
          app:
            name: "{{ name }}"
            permission: "{{ permission }}"
          database:
            instance_name: "{{ instance_name }}"
            database_name: "{{ database_name }}"
            permission: "{{ permission }}"
          description: "{{ description }}"
          experiment:
            experiment_id: "{{ experiment_id }}"
            permission: "{{ permission }}"
          genie_space:
            name: "{{ name }}"
            space_id: "{{ space_id }}"
            permission: "{{ permission }}"
          job:
            id: "{{ id }}"
            permission: "{{ permission }}"
          postgres:
            branch: "{{ branch }}"
            database: "{{ database }}"
            permission: "{{ permission }}"
          secret:
            scope: "{{ scope }}"
            key: "{{ key }}"
            permission: "{{ permission }}"
          serving_endpoint:
            name: "{{ name }}"
            permission: "{{ permission }}"
          sql_warehouse:
            id: "{{ id }}"
            permission: "{{ permission }}"
          uc_securable:
            securable_full_name: "{{ securable_full_name }}"
            securable_type: "{{ securable_type }}"
            permission: "{{ permission }}"
            securable_kind: "{{ securable_kind }}"
    - name: service_principal_client_id
      value: "{{ service_principal_client_id }}"
      description: |
        The service principal client ID for the app space.
    - name: service_principal_id
      value: {{ service_principal_id }}
      description: |
        The service principal ID for the app space.
    - name: service_principal_name
      value: "{{ service_principal_name }}"
      description: |
        The service principal name for the app space.
    - name: status
      description: |
        The status of the app space.
      value:
        message: "{{ message }}"
        state: "{{ state }}"
    - name: update_time
      value: "{{ update_time }}"
      description: |
        The update time of the app space. Formatted timestamp in ISO 6801.
    - name: updater
      value: "{{ updater }}"
      description: |
        The email of the user that last updated the app space.
    - name: usage_policy_id
      value: "{{ usage_policy_id }}"
      description: |
        The usage policy ID for managing cost at the space level.
    - name: user_api_scopes
      value:
        - "{{ user_api_scopes }}"
      description: |
        OAuth scopes for apps in the space.
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

Updates an app space. The update process is asynchronous and the status of the update can be checked

```sql
UPDATE databricks_workspace.apps.app_spaces
SET 
name = '{{ name }}',
assume_group_id = '{{ assume_group_id }}',
create_time = '{{ create_time }}',
creator = '{{ creator }}',
description = '{{ description }}',
effective_usage_policy_id = '{{ effective_usage_policy_id }}',
effective_user_api_scopes = '{{ effective_user_api_scopes }}',
id = '{{ id }}',
resources = '{{ resources }}',
service_principal_client_id = '{{ service_principal_client_id }}',
service_principal_id = {{ service_principal_id }},
service_principal_name = '{{ service_principal_name }}',
status = '{{ status }}',
update_time = '{{ update_time }}',
updater = '{{ updater }}',
usage_policy_id = '{{ usage_policy_id }}',
user_api_scopes = '{{ user_api_scopes }}'
WHERE 
name = '{{ name }}' --required
AND update_mask = '{{ update_mask }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND name = '{{ name }}' --required;
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

Deletes an app space.

```sql
DELETE FROM databricks_workspace.apps.app_spaces
WHERE name = '{{ name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
;
```
</TabItem>
</Tabs>
