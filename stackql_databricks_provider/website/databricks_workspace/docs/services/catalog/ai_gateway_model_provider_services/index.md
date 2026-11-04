---
title: ai_gateway_model_provider_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_gateway_model_provider_services
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

Creates, updates, deletes, gets or lists an <code>ai_gateway_model_provider_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ai_gateway_model_provider_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.catalog.ai_gateway_model_provider_services" /></td></tr>
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
    "description": "Resource name of the provider service. Format: ``model-provider-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_provider_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_provider_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the provider service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Provider authentication, exposed models, request-forwarding controls, rate limits, and payload logging. Required on Create. On Update, it is required only when ``config`` or one of its subpaths appears in ``update_mask``.",
    "children": [
      {
        "name": "allow_all_targets",
        "type": "boolean",
        "description": "When true, allows models from the provider's built-in model catalog in addition to explicit ``targets``. When false, only models listed in ``targets`` are routable. Defaults to false. CUSTOM providers have no built-in model catalog and must leave this false and list their models in ``targets``."
      },
      {
        "name": "amazon_bedrock",
        "type": "object",
        "description": "Amazon Bedrock provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Amazon Bedrock region and authentication configuration.",
            "children": [
              {
                "name": "aws_access_key",
                "type": "object",
                "description": "AWS access-key-pair authentication. Set ``access_key_id`` and ``secret_access_key.plaintext``. Mutually exclusive with ``service_credential``."
              },
              {
                "name": "region",
                "type": "string",
                "description": "AWS region where the Bedrock endpoint is hosted (e.g., ``us-east-1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Bedrock requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``aws_access_key``. The credential is referenced by name; its value is not carried here. Only supported on AWS-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "anthropic",
        "type": "object",
        "description": "Anthropic provider configuration. Exactly one of ``direct`` or ``relayed`` must be set on<br />    Create; the two are mutually exclusive.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct authentication with an API key supplied in ``direct.api_key.plaintext``. Required unless ``relayed`` is set.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Anthropic API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              }
            ]
          },
          {
            "name": "relayed",
            "type": "object",
            "description": "Relayed authentication. Each inference request supplies the caller's OAuth token, which is forwarded to Anthropic. No Anthropic credential is stored. Mutually exclusive with ``direct``."
          }
        ]
      },
      {
        "name": "azure_openai",
        "type": "object",
        "description": "Azure OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Azure OpenAI endpoint and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Azure OpenAI API key. Supply the value in ``api_key.plaintext``. Mutually exclusive with Entra ID and Unity Catalog service credential authentication."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Full Azure OpenAI endpoint base URL, e.g. ``https://myresource.openai.azure.com``. Required on Create."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID service-principal authentication. Set ``tenant_id``, ``client_id``, and ``client_secret.plaintext``. Mutually exclusive with ``api_key`` and ``service_credential``."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Azure OpenAI requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. Only supported on Azure-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "bedrock_mantle",
        "type": "object",
        "description": "Amazon Bedrock provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Amazon Bedrock region and authentication configuration.",
            "children": [
              {
                "name": "aws_access_key",
                "type": "object",
                "description": "AWS access-key-pair authentication. Set ``access_key_id`` and ``secret_access_key.plaintext``. Mutually exclusive with ``service_credential``."
              },
              {
                "name": "region",
                "type": "string",
                "description": "AWS region where the Bedrock endpoint is hosted (e.g., ``us-east-1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Bedrock requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``aws_access_key``. The credential is referenced by name; its value is not carried here. Only supported on AWS-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "custom",
        "type": "object",
        "description": "Custom OpenAI-compatible provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Endpoint and authentication configuration for the custom provider.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Bearer token forwarded in the ``Authorization`` header. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Endpoint URL of the OpenAI-compatible service (e.g., ``https://api.example.com/v1``). Required on Create."
              },
              {
                "name": "header_auth",
                "type": "object",
                "description": "Header-based API-key auth: the secret is forwarded on outbound requests under a caller-chosen HTTP header rather than as an ``Authorization`` bearer token. Set this instead of ``api_key`` for header auth."
              }
            ]
          }
        ]
      },
      {
        "name": "forward_headers",
        "type": "boolean",
        "description": "Whether to forward incoming HTTP headers to the upstream provider. Defaults to false and is configured for the entire provider service, not per request. Upstream authentication is configured separately in the provider-specific configuration."
      },
      {
        "name": "forward_query_parameters",
        "type": "boolean",
        "description": "Whether to forward incoming query parameters to the upstream provider. Defaults to false and is configured for the entire provider service, not per request."
      },
      {
        "name": "forward_unmanaged_paths",
        "type": "boolean",
        "description": "Whether to proxy paths that AI Gateway does not recognize as configured provider-native API types. Defaults to false. When true, these paths are forwarded unchanged to the upstream provider. When false, only recognized API paths are served. Enabling this broadens the upstream API surface exposed through the provider service. AI Gateway cannot evaluate Service Policies on opaque unmanaged requests, so unmanaged requests are rejected whenever Service Policies are attached to this securable."
      },
      {
        "name": "gemini_enterprise",
        "type": "object",
        "description": "Gemini Enterprise provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Gemini Enterprise project, region, and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Google Gemini Enterprise API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "project_id",
                "type": "string",
                "description": "GCP project ID hosting the Gemini Enterprise endpoint. Required on Create."
              },
              {
                "name": "region",
                "type": "string",
                "description": "GCP region of the Gemini Enterprise endpoint (e.g., ``us-central1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Gemini Enterprise requests. On Create, supply ``service_credential.name`` as ``credentials/&#123;name&#125;``; required when using service-credential authentication and mutually exclusive with ``api_key``. The credential is referenced by name; its value is not carried here. On read, the resolved ``id`` and ``is_deleted`` are also populated. Supported only on GCP-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "inference_table",
        "type": "object",
        "description": "Payload logging configuration for requests sent directly to this provider service. Requests routed through a model service are captured by that model service's inference table instead.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent Unity Catalog schema where the inference table is created, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required when configuring an inference table. After the inference table is created, this field cannot be changed."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced inference table has been deleted. The configuration remains visible so you can identify the broken dependency. Payload logging cannot continue until the table is restored or the configuration is updated."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix used to form the inference table's registered name. AI Gateway appends ``_payload``; for example, ``table_name_prefix = \"orders\"`` creates ``orders_payload``. If unset, the prefix defaults to the service name. Read ``table`` from the response for the resulting resource name. After the inference table is created, this field cannot be changed."
          }
        ]
      },
      {
        "name": "microsoft_foundry",
        "type": "object",
        "description": "Microsoft Foundry provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Microsoft Foundry endpoint and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Microsoft Foundry API key. Supply the value in ``api_key.plaintext``. Mutually exclusive with Entra ID and Unity Catalog service credential authentication."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Microsoft Foundry endpoint URL. Required on Create."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID service-principal authentication. Set ``tenant_id``, ``client_id``, and ``client_secret.plaintext``. Mutually exclusive with ``api_key`` and ``service_credential``."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Microsoft Foundry requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. Only supported on Azure-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "openai",
        "type": "object",
        "description": "OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "OpenAI configuration with an API key supplied in the request.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "OpenAI API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Optional custom base URL. Defaults to ``https://api.openai.com/v1``. Use for OpenAI-API-compatible third-party endpoints or in-network proxies."
              },
              {
                "name": "organization",
                "type": "string",
                "description": "Optional OpenAI organization ID. When set, the platform forwards it as the ``OpenAI-Organization`` header."
              }
            ]
          }
        ]
      },
      {
        "name": "pricing",
        "type": "object",
        "description": "Pricing configuration for this provider service. An explicitly empty configuration is retained on Create and Update and applies no adjustment.",
        "children": [
          {
            "name": "default_discount_basis_points",
            "type": "integer",
            "description": "Provider-wide adjustment to external-model spend estimates in basis points: 2000 = 20% off; -2000 = a 20% markup. Negative values have no lower bound beyond the int32 range. Values cannot exceed 10000 (100% off). An omitted value or zero leaves the estimate unchanged."
          }
        ]
      },
      {
        "name": "provider_type",
        "type": "string",
        "description": "External model provider. Required on Create and immutable thereafter. Set the matching provider-specific configuration, such as ``openai``, ``azure_openai``, or ``amazon_bedrock``. (EXTERNAL_MODEL_PROVIDER_TYPE_AMAZON_BEDROCK, EXTERNAL_MODEL_PROVIDER_TYPE_ANTHROPIC, EXTERNAL_MODEL_PROVIDER_TYPE_AZURE_OPENAI, EXTERNAL_MODEL_PROVIDER_TYPE_BEDROCK_MANTLE, EXTERNAL_MODEL_PROVIDER_TYPE_CUSTOM, EXTERNAL_MODEL_PROVIDER_TYPE_GEMINI_ENTERPRISE, EXTERNAL_MODEL_PROVIDER_TYPE_MICROSOFT_FOUNDRY, EXTERNAL_MODEL_PROVIDER_TYPE_OPENAI)"
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits for requests sent directly to this provider service. Requests routed through a model service use that model service's rate limits instead.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope of the rate limit. Depending on this value, the limit applies to a principal, the service as a whole, or each user by default. (RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required when ``key`` applies to a user, group, or service principal; otherwise it must be unset."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Maximum requests allowed in one renewal period. Leave unset for no request limit. Set to ``0`` to deny all requests."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Maximum tokens allowed in one renewal period. Leave unset for no token limit. Set to ``0`` to deny all requests."
          }
        ]
      },
      {
        "name": "targets",
        "type": "array",
        "description": "Models and provider-native API types exposed by this provider service. Each entry must include at least one ``native_api_types`` value. When ``allow_all_targets`` is false, at least one entry is required and model service destinations can reference only listed models. When ``allow_all_targets`` is true, models from the provider's built-in model catalog are also routable. CUSTOM providers must explicitly list their models here and cannot enable ``allow_all_targets``.",
        "children": [
          {
            "name": "model",
            "type": "string",
            "description": "Provider-side model identifier, such as ``gpt-5`` or ``claude-opus-4-7``. This identifies a model at the upstream provider; it is not a Unity Catalog model resource."
          },
          {
            "name": "endpoint_route",
            "type": "string",
            "description": "Relative path appended to a custom provider's ``base_url`` for this model, such as ``serve/openai/chat``. Nonempty values are only supported for custom model provider service targets; other provider types reject them. Model service destinations do not support this field. Do not include URI templates, queries, or fragments. When empty, ``base_url`` is used unchanged."
          },
          {
            "name": "native_api_types",
            "type": "array",
            "description": "Provider-native API types supported by this model, such as ``openai/v1/chat/completions``. A model provider service target requires at least one value. A model service destination may omit the list to use the matching provider service target's types when available. AI Gateway uses the selected types for translation. At most 64 entries of 256 characters each are allowed."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the provider service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the model provider service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the provider service was last modified."
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
    "description": "Resource name of the provider service. Format: ``model-provider-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_provider_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually. Server-derived on Create from ``parent`` + ``model_provider_service_id``; required and immutable on Update/Get/Delete."
  },
  {
    "name": "metastore_id",
    "type": "string",
    "description": "Metastore hosting the provider service."
  },
  {
    "name": "comment",
    "type": "string",
    "description": "User-provided description."
  },
  {
    "name": "config",
    "type": "object",
    "description": "Provider authentication, exposed models, request-forwarding controls, rate limits, and payload logging. Required on Create. On Update, it is required only when ``config`` or one of its subpaths appears in ``update_mask``.",
    "children": [
      {
        "name": "allow_all_targets",
        "type": "boolean",
        "description": "When true, allows models from the provider's built-in model catalog in addition to explicit ``targets``. When false, only models listed in ``targets`` are routable. Defaults to false. CUSTOM providers have no built-in model catalog and must leave this false and list their models in ``targets``."
      },
      {
        "name": "amazon_bedrock",
        "type": "object",
        "description": "Amazon Bedrock provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Amazon Bedrock region and authentication configuration.",
            "children": [
              {
                "name": "aws_access_key",
                "type": "object",
                "description": "AWS access-key-pair authentication. Set ``access_key_id`` and ``secret_access_key.plaintext``. Mutually exclusive with ``service_credential``."
              },
              {
                "name": "region",
                "type": "string",
                "description": "AWS region where the Bedrock endpoint is hosted (e.g., ``us-east-1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Bedrock requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``aws_access_key``. The credential is referenced by name; its value is not carried here. Only supported on AWS-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "anthropic",
        "type": "object",
        "description": "Anthropic provider configuration. Exactly one of ``direct`` or ``relayed`` must be set on<br />    Create; the two are mutually exclusive.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Direct authentication with an API key supplied in ``direct.api_key.plaintext``. Required unless ``relayed`` is set.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Anthropic API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              }
            ]
          },
          {
            "name": "relayed",
            "type": "object",
            "description": "Relayed authentication. Each inference request supplies the caller's OAuth token, which is forwarded to Anthropic. No Anthropic credential is stored. Mutually exclusive with ``direct``."
          }
        ]
      },
      {
        "name": "azure_openai",
        "type": "object",
        "description": "Azure OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Azure OpenAI endpoint and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Azure OpenAI API key. Supply the value in ``api_key.plaintext``. Mutually exclusive with Entra ID and Unity Catalog service credential authentication."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Full Azure OpenAI endpoint base URL, e.g. ``https://myresource.openai.azure.com``. Required on Create."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID service-principal authentication. Set ``tenant_id``, ``client_id``, and ``client_secret.plaintext``. Mutually exclusive with ``api_key`` and ``service_credential``."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Azure OpenAI requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. Only supported on Azure-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "bedrock_mantle",
        "type": "object",
        "description": "Amazon Bedrock provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Amazon Bedrock region and authentication configuration.",
            "children": [
              {
                "name": "aws_access_key",
                "type": "object",
                "description": "AWS access-key-pair authentication. Set ``access_key_id`` and ``secret_access_key.plaintext``. Mutually exclusive with ``service_credential``."
              },
              {
                "name": "region",
                "type": "string",
                "description": "AWS region where the Bedrock endpoint is hosted (e.g., ``us-east-1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Bedrock requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``aws_access_key``. The credential is referenced by name; its value is not carried here. Only supported on AWS-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "custom",
        "type": "object",
        "description": "Custom OpenAI-compatible provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Endpoint and authentication configuration for the custom provider.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Bearer token forwarded in the ``Authorization`` header. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Endpoint URL of the OpenAI-compatible service (e.g., ``https://api.example.com/v1``). Required on Create."
              },
              {
                "name": "header_auth",
                "type": "object",
                "description": "Header-based API-key auth: the secret is forwarded on outbound requests under a caller-chosen HTTP header rather than as an ``Authorization`` bearer token. Set this instead of ``api_key`` for header auth."
              }
            ]
          }
        ]
      },
      {
        "name": "forward_headers",
        "type": "boolean",
        "description": "Whether to forward incoming HTTP headers to the upstream provider. Defaults to false and is configured for the entire provider service, not per request. Upstream authentication is configured separately in the provider-specific configuration."
      },
      {
        "name": "forward_query_parameters",
        "type": "boolean",
        "description": "Whether to forward incoming query parameters to the upstream provider. Defaults to false and is configured for the entire provider service, not per request."
      },
      {
        "name": "forward_unmanaged_paths",
        "type": "boolean",
        "description": "Whether to proxy paths that AI Gateway does not recognize as configured provider-native API types. Defaults to false. When true, these paths are forwarded unchanged to the upstream provider. When false, only recognized API paths are served. Enabling this broadens the upstream API surface exposed through the provider service. AI Gateway cannot evaluate Service Policies on opaque unmanaged requests, so unmanaged requests are rejected whenever Service Policies are attached to this securable."
      },
      {
        "name": "gemini_enterprise",
        "type": "object",
        "description": "Gemini Enterprise provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Gemini Enterprise project, region, and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Google Gemini Enterprise API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "project_id",
                "type": "string",
                "description": "GCP project ID hosting the Gemini Enterprise endpoint. Required on Create."
              },
              {
                "name": "region",
                "type": "string",
                "description": "GCP region of the Gemini Enterprise endpoint (e.g., ``us-central1``). Required on Create."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Gemini Enterprise requests. On Create, supply ``service_credential.name`` as ``credentials/&#123;name&#125;``; required when using service-credential authentication and mutually exclusive with ``api_key``. The credential is referenced by name; its value is not carried here. On read, the resolved ``id`` and ``is_deleted`` are also populated. Supported only on GCP-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "inference_table",
        "type": "object",
        "description": "Payload logging configuration for requests sent directly to this provider service. Requests routed through a model service are captured by that model service's inference table instead.",
        "children": [
          {
            "name": "parent",
            "type": "string",
            "description": "Parent Unity Catalog schema where the inference table is created, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required when configuring an inference table. After the inference table is created, this field cannot be changed."
          },
          {
            "name": "is_deleted",
            "type": "boolean",
            "description": "Whether the referenced inference table has been deleted. The configuration remains visible so you can identify the broken dependency. Payload logging cannot continue until the table is restored or the configuration is updated."
          },
          {
            "name": "table",
            "type": "string",
            "description": "Resolved UC table for payload logs. Format: ``tables/&#123;catalog&#125;.&#123;schema&#125;.&#123;table&#125;``."
          },
          {
            "name": "table_name_prefix",
            "type": "string",
            "description": "Prefix used to form the inference table's registered name. AI Gateway appends ``_payload``; for example, ``table_name_prefix = \"orders\"`` creates ``orders_payload``. If unset, the prefix defaults to the service name. Read ``table`` from the response for the resulting resource name. After the inference table is created, this field cannot be changed."
          }
        ]
      },
      {
        "name": "microsoft_foundry",
        "type": "object",
        "description": "Microsoft Foundry provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "Microsoft Foundry endpoint and authentication configuration.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "Microsoft Foundry API key. Supply the value in ``api_key.plaintext``. Mutually exclusive with Entra ID and Unity Catalog service credential authentication."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Microsoft Foundry endpoint URL. Required on Create."
              },
              {
                "name": "entra_service_principal",
                "type": "object",
                "description": "Entra ID service-principal authentication. Set ``tenant_id``, ``client_id``, and ``client_secret.plaintext``. Mutually exclusive with ``api_key`` and ``service_credential``."
              },
              {
                "name": "service_credential",
                "type": "object",
                "description": "Reference to a Unity Catalog service credential authorizing Microsoft Foundry requests. On Create, supply ``service_credential.name`` in the form ``credentials/&#123;name&#125;``. Required on Create when using service-credential authentication; mutually exclusive with ``api_key`` and ``entra_service_principal``. The credential is referenced by name; its value is not carried here. Only supported on Azure-hosted workspaces."
              }
            ]
          }
        ]
      },
      {
        "name": "openai",
        "type": "object",
        "description": "OpenAI provider configuration.",
        "children": [
          {
            "name": "direct",
            "type": "object",
            "description": "OpenAI configuration with an API key supplied in the request.",
            "children": [
              {
                "name": "api_key",
                "type": "object",
                "description": "OpenAI API key. Required when creating the service. Supply the value in ``api_key.plaintext``."
              },
              {
                "name": "base_url",
                "type": "string",
                "description": "Optional custom base URL. Defaults to ``https://api.openai.com/v1``. Use for OpenAI-API-compatible third-party endpoints or in-network proxies."
              },
              {
                "name": "organization",
                "type": "string",
                "description": "Optional OpenAI organization ID. When set, the platform forwards it as the ``OpenAI-Organization`` header."
              }
            ]
          }
        ]
      },
      {
        "name": "pricing",
        "type": "object",
        "description": "Pricing configuration for this provider service. An explicitly empty configuration is retained on Create and Update and applies no adjustment.",
        "children": [
          {
            "name": "default_discount_basis_points",
            "type": "integer",
            "description": "Provider-wide adjustment to external-model spend estimates in basis points: 2000 = 20% off; -2000 = a 20% markup. Negative values have no lower bound beyond the int32 range. Values cannot exceed 10000 (100% off). An omitted value or zero leaves the estimate unchanged."
          }
        ]
      },
      {
        "name": "provider_type",
        "type": "string",
        "description": "External model provider. Required on Create and immutable thereafter. Set the matching provider-specific configuration, such as ``openai``, ``azure_openai``, or ``amazon_bedrock``. (EXTERNAL_MODEL_PROVIDER_TYPE_AMAZON_BEDROCK, EXTERNAL_MODEL_PROVIDER_TYPE_ANTHROPIC, EXTERNAL_MODEL_PROVIDER_TYPE_AZURE_OPENAI, EXTERNAL_MODEL_PROVIDER_TYPE_BEDROCK_MANTLE, EXTERNAL_MODEL_PROVIDER_TYPE_CUSTOM, EXTERNAL_MODEL_PROVIDER_TYPE_GEMINI_ENTERPRISE, EXTERNAL_MODEL_PROVIDER_TYPE_MICROSOFT_FOUNDRY, EXTERNAL_MODEL_PROVIDER_TYPE_OPENAI)"
      },
      {
        "name": "rate_limits",
        "type": "array",
        "description": "Rate limits for requests sent directly to this provider service. Requests routed through a model service use that model service's rate limits instead.",
        "children": [
          {
            "name": "key",
            "type": "string",
            "description": "Scope of the rate limit. Depending on this value, the limit applies to a principal, the service as a whole, or each user by default. (RATE_LIMIT_KEY_SERVICE, RATE_LIMIT_KEY_SERVICE_PRINCIPAL, RATE_LIMIT_KEY_USER, RATE_LIMIT_KEY_USER_DEFAULT, RATE_LIMIT_KEY_USER_GROUP)"
          },
          {
            "name": "renewal_period",
            "type": "string",
            "description": "Renewal period. (RATE_LIMIT_RENEWAL_PERIOD_HOUR, RATE_LIMIT_RENEWAL_PERIOD_MINUTE)"
          },
          {
            "name": "principal",
            "type": "string",
            "description": "Principal this limit applies to: user email, group name, or service principal application ID. Required when ``key`` applies to a user, group, or service principal; otherwise it must be unset."
          },
          {
            "name": "requests",
            "type": "integer",
            "description": "Maximum requests allowed in one renewal period. Leave unset for no request limit. Set to ``0`` to deny all requests."
          },
          {
            "name": "tokens",
            "type": "integer",
            "description": "Maximum tokens allowed in one renewal period. Leave unset for no token limit. Set to ``0`` to deny all requests."
          }
        ]
      },
      {
        "name": "targets",
        "type": "array",
        "description": "Models and provider-native API types exposed by this provider service. Each entry must include at least one ``native_api_types`` value. When ``allow_all_targets`` is false, at least one entry is required and model service destinations can reference only listed models. When ``allow_all_targets`` is true, models from the provider's built-in model catalog are also routable. CUSTOM providers must explicitly list their models here and cannot enable ``allow_all_targets``.",
        "children": [
          {
            "name": "model",
            "type": "string",
            "description": "Provider-side model identifier, such as ``gpt-5`` or ``claude-opus-4-7``. This identifies a model at the upstream provider; it is not a Unity Catalog model resource."
          },
          {
            "name": "endpoint_route",
            "type": "string",
            "description": "Relative path appended to a custom provider's ``base_url`` for this model, such as ``serve/openai/chat``. Nonempty values are only supported for custom model provider service targets; other provider types reject them. Model service destinations do not support this field. Do not include URI templates, queries, or fragments. When empty, ``base_url`` is used unchanged."
          },
          {
            "name": "native_api_types",
            "type": "array",
            "description": "Provider-native API types supported by this model, such as ``openai/v1/chat/completions``. A model provider service target requires at least one value. A model service destination may omit the list to use the matching provider service target's types when available. AI Gateway uses the selected types for translation. At most 64 entries of 256 characters each are allowed."
          }
        ]
      }
    ]
  },
  {
    "name": "create_time",
    "type": "string (date-time)",
    "description": "Time the provider service was created."
  },
  {
    "name": "created_by",
    "type": "string",
    "description": "Creator identity."
  },
  {
    "name": "effective_owner",
    "type": "string",
    "description": "Owner of the model provider service."
  },
  {
    "name": "etag",
    "type": "string",
    "description": "Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's ``etag`` field. In REST responses, this value is a base64 string; URL-encode it when setting the ``etag`` query parameter."
  },
  {
    "name": "update_time",
    "type": "string (date-time)",
    "description": "Time the provider service was last modified."
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
    <td>Returns the model provider service identified by its resource name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-page_size"><code>page_size</code></a>, <a href="#parameter-page_token"><code>page_token</code></a>, <a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-view"><code>view</code></a></td>
    <td>Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-parent"><code>parent</code></a>, <a href="#parameter-model_provider_service_id"><code>model_provider_service_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td></td>
    <td>Creates a model provider service in a Unity Catalog schema. A model provider service stores</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-update_mask"><code>update_mask</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Updates a model provider service. Only the fields named in ``update_mask`` are changed; the resource</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-full_name"><code>full_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-workspace_domain"><code>workspace_domain</code></a></td>
    <td><a href="#parameter-etag"><code>etag</code></a></td>
    <td>Deletes the model provider service identified by its resource name. Optionally supply an ``etag`` to</td>
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
<tr id="parameter-full_name">
    <td><CopyableCode code="full_name" /></td>
    <td><code>string</code></td>
    <td>The `full_name` segment of the `name` resource name (`model-provider-services/&#123;full_name&#125;`). Resource name of the model provider service. Format: ``model-provider-services/&#123;catalog&#125;.&#123;schema&#125;.&#123;model_provider_service&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-model_provider_service_id">
    <td><CopyableCode code="model_provider_service_id" /></td>
    <td><code>string</code></td>
    <td>Name for the model provider service, e.g. "openai_prod".</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Name of the parent schema. Format: ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-update_mask">
    <td><CopyableCode code="update_mask" /></td>
    <td><code>object</code></td>
    <td>Fields to update. Use ``config`` to replace the entire configuration. The replacement must include every required field; any optional field you omit is cleared. To preserve sibling fields, use one or more granular paths: ``comment``; ``config.provider`` to replace the active provider-specific value (for example, ``config.openai``; the mask path remains ``config.provider``); ``config.allow_all_targets``, ``config.targets``, ``config.forward_headers``, ``config.forward_query_parameters``, ``config.forward_unmanaged_paths``, ``config.rate_limits``, ``config.pricing.default_discount_basis_points``, or ``config.inference_table``. For a pricing update, an explicitly empty ``pricing`` object clears the discount but retains the object; omitting ``pricing`` clears it. ``config.pricing`` is not a supported mask path. The provider type is immutable. A ``config`` or ``config.provider`` replacement that carries no authentication material preserves the existing authentication binding; input-only plaintext does not need to be read back and re-sent.</td>
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
    <td>Maximum number of provider services to return. Defaults to 200 when unset or 0; the maximum is 1000 for ``view = BASIC`` and 200 for ``view = FULL``. Use ``page_token`` to retrieve additional pages.</td>
</tr>
<tr id="parameter-page_token">
    <td><CopyableCode code="page_token" /></td>
    <td><code>string</code></td>
    <td>Opaque pagination token from the previous response.</td>
</tr>
<tr id="parameter-parent">
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent schema to list within, in the form ``schemas/&#123;catalog&#125;.&#123;schema&#125;``. Required. Each ``&#123;...&#125;`` component is capped at 255 characters individually.</td>
</tr>
<tr id="parameter-view">
    <td><CopyableCode code="view" /></td>
    <td><code>string</code></td>
    <td>Fields to return for each service. ``FULL`` includes resolved service-credential and inference-table details and rate-limit principal names. ``BASIC`` omits those details and principal names from rate limits. Defaults to ``BASIC`` when unset.</td>
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

Returns the model provider service identified by its resource name.

```sql
SELECT
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_provider_services
WHERE full_name = '{{ full_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the model provider services in a Unity Catalog schema. Provide ``parent`` as

```sql
SELECT
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
update_time,
updated_by
FROM databricks_workspace.catalog.ai_gateway_model_provider_services
WHERE deployment_name = '{{ deployment_name }}' -- required
AND workspace_domain = '{{ workspace_domain }}' -- required
AND page_size = '{{ page_size }}'
AND page_token = '{{ page_token }}'
AND parent = '{{ parent }}'
AND view = '{{ view }}'
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

Creates a model provider service in a Unity Catalog schema. A model provider service stores

```sql
INSERT INTO databricks_workspace.catalog.ai_gateway_model_provider_services (
comment,
config,
create_time,
created_by,
effective_owner,
etag,
metastore_id,
name,
update_time,
updated_by,
parent,
model_provider_service_id,
deployment_name,
workspace_domain
)
SELECT 
'{{ comment }}',
'{{ config }}',
'{{ create_time }}',
'{{ created_by }}',
'{{ effective_owner }}',
'{{ etag }}',
'{{ metastore_id }}',
'{{ name }}',
'{{ update_time }}',
'{{ updated_by }}',
'{{ parent }}',
'{{ model_provider_service_id }}',
'{{ deployment_name }}',
'{{ workspace_domain }}'
RETURNING
name,
metastore_id,
comment,
config,
create_time,
created_by,
effective_owner,
etag,
update_time,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: ai_gateway_model_provider_services
  props:
    - name: parent
      value: "{{ parent }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: model_provider_service_id
      value: "{{ model_provider_service_id }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: workspace_domain
      value: "{{ workspace_domain }}"
      description: Required parameter for the ai_gateway_model_provider_services resource.
    - name: comment
      value: "{{ comment }}"
      description: |
        User-provided description.
    - name: config
      description: |
        Provider authentication, exposed models, request-forwarding controls, rate limits, and payload logging. Required on Create. On Update, it is required only when \`\`config\`\` or one of its subpaths appears in \`\`update_mask\`\`.
      value:
        allow_all_targets: {{ allow_all_targets }}
        amazon_bedrock:
          direct:
            aws_access_key:
              access_key_id: "{{ access_key_id }}"
              secret_access_key:
                plaintext: "{{ plaintext }}"
                secret_reference: "{{ secret_reference }}"
            region: "{{ region }}"
            service_credential:
              name: "{{ name }}"
        anthropic:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
          relayed: "{{ relayed }}"
        azure_openai:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
            base_url: "{{ base_url }}"
            entra_service_principal:
              client_id: "{{ client_id }}"
              client_secret:
                plaintext: "{{ plaintext }}"
                secret_reference: "{{ secret_reference }}"
              tenant_id: "{{ tenant_id }}"
            service_credential:
              name: "{{ name }}"
        bedrock_mantle:
          direct:
            aws_access_key:
              access_key_id: "{{ access_key_id }}"
              secret_access_key:
                plaintext: "{{ plaintext }}"
                secret_reference: "{{ secret_reference }}"
            region: "{{ region }}"
            service_credential:
              name: "{{ name }}"
        custom:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
            base_url: "{{ base_url }}"
            header_auth:
              api_key_name: "{{ api_key_name }}"
              api_key_value:
                plaintext: "{{ plaintext }}"
                secret_reference: "{{ secret_reference }}"
        forward_headers: {{ forward_headers }}
        forward_query_parameters: {{ forward_query_parameters }}
        forward_unmanaged_paths: {{ forward_unmanaged_paths }}
        gemini_enterprise:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
            project_id: "{{ project_id }}"
            region: "{{ region }}"
            service_credential:
              name: "{{ name }}"
        inference_table:
          parent: "{{ parent }}"
          is_deleted: {{ is_deleted }}
          table: "{{ table }}"
          table_name_prefix: "{{ table_name_prefix }}"
        microsoft_foundry:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
            base_url: "{{ base_url }}"
            entra_service_principal:
              client_id: "{{ client_id }}"
              client_secret:
                plaintext: "{{ plaintext }}"
                secret_reference: "{{ secret_reference }}"
              tenant_id: "{{ tenant_id }}"
            service_credential:
              name: "{{ name }}"
        openai:
          direct:
            api_key:
              plaintext: "{{ plaintext }}"
              secret_reference:
                name: "{{ name }}"
            base_url: "{{ base_url }}"
            organization: "{{ organization }}"
        pricing:
          default_discount_basis_points: {{ default_discount_basis_points }}
        provider_type: "{{ provider_type }}"
        rate_limits:
          - key: "{{ key }}"
            renewal_period: "{{ renewal_period }}"
            principal: "{{ principal }}"
            requests: {{ requests }}
            tokens: {{ tokens }}
        targets:
          - model: "{{ model }}"
            endpoint_route: "{{ endpoint_route }}"
            native_api_types: "{{ native_api_types }}"
    - name: create_time
      value: "{{ create_time }}"
      description: |
        Time the provider service was created.
    - name: created_by
      value: "{{ created_by }}"
      description: |
        Creator identity.
    - name: effective_owner
      value: "{{ effective_owner }}"
      description: |
        Owner of the model provider service.
    - name: etag
      value: "{{ etag }}"
      description: |
        Optimistic concurrency token returned on every read. To make an Update or Delete conditional, pass the last-read value in that request's \`\`etag\`\` field. In REST responses, this value is a base64 string; URL-encode it when setting the \`\`etag\`\` query parameter.
    - name: metastore_id
      value: "{{ metastore_id }}"
      description: |
        Metastore hosting the provider service.
    - name: name
      value: "{{ name }}"
      description: |
        Resource name of the provider service. Format: \`\`model-provider-services/{catalog}.{schema}.{model_provider_service}\`\`. Each \`\`{...}\`\` component is capped at 255 characters individually. Server-derived on Create from \`\`parent\`\` + \`\`model_provider_service_id\`\`; required and immutable on Update/Get/Delete.
    - name: update_time
      value: "{{ update_time }}"
      description: |
        Time the provider service was last modified.
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

Updates a model provider service. Only the fields named in ``update_mask`` are changed; the resource

```sql
UPDATE databricks_workspace.catalog.ai_gateway_model_provider_services
SET 
comment = '{{ comment }}',
config = '{{ config }}',
create_time = '{{ create_time }}',
created_by = '{{ created_by }}',
effective_owner = '{{ effective_owner }}',
etag = '{{ etag }}',
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
comment,
config,
create_time,
created_by,
effective_owner,
etag,
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

Deletes the model provider service identified by its resource name. Optionally supply an ``etag`` to

```sql
DELETE FROM databricks_workspace.catalog.ai_gateway_model_provider_services
WHERE full_name = '{{ full_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND workspace_domain = '{{ workspace_domain }}' --required
AND etag = '{{ etag }}'
;
```
</TabItem>
</Tabs>
