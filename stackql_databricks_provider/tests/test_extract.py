"""Tests for stackql_databricks_provider.extract module."""

import json

import pytest
from databricks.sdk.service import (
    agentbricks,
    agentkit,
    billing,
    catalog,
    compute,
    domains,
    iam,
    networking,
    provisioning,
    sandbox,
    settings,
)

from stackql_databricks_provider.extract import (
    _parse_resource_name_template,
    get_data_classes,
    get_enums,
    get_operation_details,
    get_operations,
    get_resources,
    get_schema_from_data_class,
    get_schema_from_enum,
)


# ---------------------------------------------------------------------------
# get_resources
# ---------------------------------------------------------------------------

class TestGetResources:
    def test_returns_list_of_tuples(self):
        resources = get_resources(agentbricks)
        assert isinstance(resources, list)
        for item in resources:
            assert isinstance(item, tuple)
            assert len(item) == 2

    def test_finds_agentbricks_api(self):
        resources = get_resources(agentbricks)
        class_names = [c for c, _ in resources]
        assert "AgentBricksAPI" in class_names

    def test_snake_case_conversion(self):
        resources = get_resources(agentbricks)
        result = dict(resources)
        assert result["AgentBricksAPI"] == "agent_bricks"

    def test_multiple_resources(self):
        resources = get_resources(catalog)
        assert len(resources) > 10  # catalog has many API classes

    def test_sorted_by_class_name(self):
        resources = get_resources(catalog)
        class_names = [c for c, _ in resources]
        assert class_names == sorted(class_names)

    def test_excludes_non_api_classes(self):
        resources = get_resources(agentbricks)
        class_names = [c for c, _ in resources]
        # Dataclasses like CustomLlm should not appear
        assert "CustomLlm" not in class_names
        assert "Dataset" not in class_names


# ---------------------------------------------------------------------------
# get_operations
# ---------------------------------------------------------------------------

class TestGetOperations:
    def test_returns_list_of_strings(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert isinstance(ops, list)
        for op in ops:
            assert isinstance(op, str)

    def test_finds_crud_operations(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert "create_custom_llm" in ops
        assert "get_custom_llm" in ops
        assert "delete_custom_llm" in ops
        assert "update_custom_llm" in ops

    def test_excludes_private_methods(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        for op in ops:
            assert not op.startswith("_")

    def test_sorted(self):
        ops = get_operations(agentbricks, "AgentBricksAPI")
        assert ops == sorted(ops)

    def test_missing_class_returns_empty(self):
        ops = get_operations(agentbricks, "NonExistentAPI")
        assert ops == []


# ---------------------------------------------------------------------------
# get_operation_details
# ---------------------------------------------------------------------------

class TestGetOperationDetails:
    def test_returns_path_dict(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        assert isinstance(details, dict)
        assert len(details) == 1

    def test_get_operation_structure(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        assert path in details
        assert "get" in details[path]
        op = details[path]["get"]
        assert op["operationId"] == "agent_bricks_get_custom_llm"
        assert "parameters" in op
        assert op["parameters"][0]["name"] == "id"
        assert op["parameters"][0]["in"] == "path"

    def test_post_has_request_body(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "create_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms"
        assert path in details
        op = details[path]["post"]
        assert "requestBody" in op
        schema = op["requestBody"]["content"]["application/json"]["schema"]
        assert "name" in schema["properties"]
        assert "instructions" in schema["properties"]

    def test_required_body_params(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "create_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms"
        schema = details[path]["post"]["requestBody"]["content"]["application/json"]["schema"]
        assert "name" in schema["required"]
        assert "instructions" in schema["required"]

    def test_return_type_ref(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        response = details[path]["get"]["responses"]["200"]
        assert "$ref" in response["content"]["application/json"]["schema"]

    def test_void_return_no_content(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "delete_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        response = details[path]["delete"]["responses"]["200"]
        assert "content" not in response

    def test_tags_present(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        tags = details[path]["get"]["tags"]
        assert "agentbricks" in tags

    def test_error_response_present(self):
        details = get_operation_details(
            agentbricks, "AgentBricksAPI", "get_custom_llm",
            service_name="agentbricks", resource_snake_name="agent_bricks"
        )
        path = "/api/2.0/custom-llms/{id}"
        assert "default" in details[path]["get"]["responses"]

    def test_raises_on_missing_class(self):
        with pytest.raises(ValueError, match="not found"):
            get_operation_details(agentbricks, "FakeAPI", "get")

    def test_raises_on_missing_method(self):
        with pytest.raises(ValueError, match="not found"):
            get_operation_details(agentbricks, "AgentBricksAPI", "fake_method")


# ---------------------------------------------------------------------------
# get_data_classes
# ---------------------------------------------------------------------------

class TestGetDataClasses:
    def test_returns_list_of_types(self):
        dcs = get_data_classes(agentbricks)
        assert isinstance(dcs, list)
        for dc in dcs:
            assert isinstance(dc, type)

    def test_finds_expected_classes(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert "CustomLlm" in names
        assert "Dataset" in names
        assert "Table" in names

    def test_excludes_non_dataclasses(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert "AgentBricksAPI" not in names  # API class, not dataclass
        assert "State" not in names  # Enum, not dataclass

    def test_sorted_by_name(self):
        dcs = get_data_classes(agentbricks)
        names = [dc.__name__ for dc in dcs]
        assert names == sorted(names)


# ---------------------------------------------------------------------------
# get_enums
# ---------------------------------------------------------------------------

class TestGetEnums:
    def test_returns_list_of_enum_types(self):
        enums = get_enums(agentbricks)
        assert isinstance(enums, list)
        from enum import Enum
        for e in enums:
            assert issubclass(e, Enum)

    def test_finds_state_enum(self):
        enums = get_enums(agentbricks)
        names = [e.__name__ for e in enums]
        assert "State" in names


# ---------------------------------------------------------------------------
# get_schema_from_data_class
# ---------------------------------------------------------------------------

class TestGetSchemaFromDataClass:
    def test_returns_dict_with_class_name_key(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        assert "CustomLlm" in schema

    def test_schema_has_type_object(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        assert schema["CustomLlm"]["type"] == "object"

    def test_properties_present(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        props = schema["CustomLlm"]["properties"]
        assert "name" in props
        assert "instructions" in props
        assert "id" in props

    def test_required_fields(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        required = schema["CustomLlm"]["required"]
        assert "name" in required
        assert "instructions" in required
        # Optional fields should not be required
        assert "id" not in required
        assert "creation_time" not in required

    def test_resolves_list_type(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        datasets_prop = schema["CustomLlm"]["properties"]["datasets"]
        assert datasets_prop["type"] == "array"
        assert "$ref" in datasets_prop["items"]

    def test_resolves_enum_type(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        state_prop = schema["CustomLlm"]["properties"]["optimization_state"]
        assert "$ref" in state_prop

    def test_field_descriptions(self):
        dcs = get_data_classes(agentbricks)
        custom_llm = next(dc for dc in dcs if dc.__name__ == "CustomLlm")
        schema = get_schema_from_data_class(agentbricks, custom_llm)
        props = schema["CustomLlm"]["properties"]
        assert "description" in props["instructions"]

    def test_raises_on_non_dataclass(self):
        from enum import Enum
        class NotADataclass(Enum):
            A = "a"
        with pytest.raises(TypeError):
            get_schema_from_data_class(agentbricks, NotADataclass)


# ---------------------------------------------------------------------------
# get_schema_from_enum
# ---------------------------------------------------------------------------

class TestGetSchemaFromEnum:
    def test_returns_string_enum_schema(self):
        enums = get_enums(agentbricks)
        state = next(e for e in enums if e.__name__ == "State")
        schema = get_schema_from_enum(state)
        assert "State" in schema
        assert schema["State"]["type"] == "string"
        assert "x-enum" in schema["State"]

    def test_enum_values(self):
        enums = get_enums(agentbricks)
        state = next(e for e in enums if e.__name__ == "State")
        schema = get_schema_from_enum(state)
        values = schema["State"]["x-enum"]
        assert "CANCELLED" in values
        assert "COMPLETED" in values
        assert "RUNNING" in values


# ---------------------------------------------------------------------------
# Cross-service tests (validate on larger services)
# ---------------------------------------------------------------------------

class TestCrossService:
    def test_compute_has_many_resources(self):
        resources = get_resources(compute)
        assert len(resources) >= 5

    def test_iam_account_api_operations(self):
        ops = get_operations(iam, "AccountGroupsAPI")
        assert len(ops) > 0

    def test_catalog_dataclasses(self):
        dcs = get_data_classes(catalog)
        assert len(dcs) > 50

    def test_billing_operation_details(self):
        ops = get_operations(billing, "BillableUsageAPI")
        assert len(ops) > 0
        details = get_operation_details(
            billing, "BillableUsageAPI", ops[0],
            service_name="billing", resource_snake_name="billable_usage"
        )
        assert len(details) > 0


# ---------------------------------------------------------------------------
# Response media type detection
# ---------------------------------------------------------------------------

class TestResponseMediaType:
    def test_billing_download_is_text_plain(self):
        """BillableUsageAPI.download sets Accept: text/plain."""
        details = get_operation_details(
            billing, "BillableUsageAPI", "download",
            service_name="billing", resource_snake_name="billable_usage",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                resp_200 = operation["responses"]["200"]
                assert "text/plain" in resp_200["content"], (
                    "BillableUsageAPI.download should have text/plain response"
                )
                assert "application/json" not in resp_200["content"]

    def test_billing_download_text_plain_schema_has_contents_property(self):
        """text/plain response should use object with contents property."""
        details = get_operation_details(
            billing, "BillableUsageAPI", "download",
            service_name="billing", resource_snake_name="billable_usage",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                schema = operation["responses"]["200"]["content"]["text/plain"]["schema"]
                assert schema["type"] == "object"
                assert "contents" in schema["properties"]
                assert schema["properties"]["contents"]["type"] == "string"

    def test_json_endpoint_still_uses_application_json(self):
        """Normal JSON endpoints should still use application/json."""
        details = get_operation_details(
            billing, "BudgetPolicyAPI", "create",
            service_name="billing", resource_snake_name="budget_policy",
        )
        for path, methods in details.items():
            for verb, operation in methods.items():
                resp_200 = operation["responses"]["200"]
                assert "application/json" in resp_200["content"]


# ---------------------------------------------------------------------------
# Object field expansion in request bodies
# ---------------------------------------------------------------------------

class TestObjectFieldExpansion:
    def test_credentials_create_aws_credentials_is_ref(self):
        """aws_credentials param should be a $ref, not type: string."""
        details = get_operation_details(
            provisioning, "CredentialsAPI", "create",
            service_name="provisioning", resource_snake_name="credentials",
        )
        path = "/api/2.0/accounts/{account_id}/credentials"
        schema = details[path]["post"]["requestBody"]["content"]["application/json"]["schema"]
        aws_creds = schema["properties"]["aws_credentials"]
        assert "$ref" in aws_creds, (
            f"aws_credentials should be a $ref but got: {aws_creds}"
        )
        assert aws_creds["$ref"] == "#/components/schemas/CreateCredentialAwsCredentials"

    def test_encryption_keys_create_has_object_refs(self):
        """Encryption key creation params like aws_key_info should be $ref."""
        details = get_operation_details(
            provisioning, "EncryptionKeysAPI", "create",
            service_name="provisioning", resource_snake_name="encryption_keys",
        )
        for path, methods in details.items():
            schema = methods["post"]["requestBody"]["content"]["application/json"]["schema"]
            aws_key = schema["properties"].get("aws_key_info")
            if aws_key:
                assert "$ref" in aws_key, (
                    f"aws_key_info should be a $ref but got: {aws_key}"
                )

    def test_string_params_stay_string(self):
        """Simple string params like credentials_name should remain type: string."""
        details = get_operation_details(
            provisioning, "CredentialsAPI", "create",
            service_name="provisioning", resource_snake_name="credentials",
        )
        path = "/api/2.0/accounts/{account_id}/credentials"
        schema = details[path]["post"]["requestBody"]["content"]["application/json"]["schema"]
        cred_name = schema["properties"]["credentials_name"]
        assert cred_name.get("type") == "string"
        assert "$ref" not in cred_name


# ---------------------------------------------------------------------------
# Resource-name style paths (/api/2.0/{name} with name="domains/{domain_id}")
# ---------------------------------------------------------------------------


class TestResourceNameTemplates:
    def test_parse_format_cue(self):
        assert _parse_resource_name_template(
            "Full resource name of the domain to delete. Format: ``domains/{domain_id}``"
        ) == "domains/{domain_id}"

    def test_parse_in_the_form_cue(self):
        assert _parse_resource_name_template(
            "Resource name of the sandbox to start, in the form ``sandboxes/{sandbox_id}``."
        ) == "sandboxes/{sandbox_id}"

    def test_parse_multi_segment(self):
        desc = ("Resource name in the form "
                "``memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}``.")
        assert _parse_resource_name_template(desc) == (
            "memory-stores/{managed_memory_store_id}/entries/{managed_memory_entry_id}"
        )

    def test_parse_singleton_requires_format_cue(self):
        assert _parse_resource_name_template(
            "The resource name of this singleton resource. Format: default-workspace-base-environment"
        ) == "default-workspace-base-environment"
        # Prose after "in the form" with no placeholder is not a template.
        assert _parse_resource_name_template("Supplied in the form of a JSON string") is None

    def test_parse_example_value_is_not_a_template(self):
        assert _parse_resource_name_template(
            "Sandbox resource name, for example ``sandboxes/my-sandbox``."
        ) is None

    def test_parse_empty(self):
        assert _parse_resource_name_template("") is None
        assert _parse_resource_name_template("The name of the operation resource.") is None

    def test_parse_three_level_name_is_one_full_name_segment(self):
        assert _parse_resource_name_template(
            "Full resource name of the skill. Format: ``skills/{catalog}.{schema}.{skill}``. Each "
            "``{...}`` component is capped at 255 characters individually."
        ) == "skills/{full_name}"
        assert _parse_resource_name_template(
            'The Full resource name of the synced table, of the format '
            '"synced_tables/{catalog}.{schema}.{table}", where (catalog, schema, table) are the UC entity names.'
        ) == "synced_tables/{full_name}"


class TestResourceNameExpansion:
    def test_domains_expand_name(self):
        details = get_operation_details(
            domains, "DomainsAPI", "get_domain", service_name="domains", resource_snake_name="domains"
        )
        assert list(details) == ["/api/2.0/domains/{domain_id}"]
        params = details["/api/2.0/domains/{domain_id}"]["get"]["parameters"]
        path_params = [p for p in params if p["in"] == "path"]
        assert [p["name"] for p in path_params] == ["domain_id"]
        assert path_params[0]["required"] is True
        assert path_params[0]["schema"] == {"type": "string"}
        assert "domains/{domain_id}" in path_params[0]["description"]
        # the consumed ``name`` parameter is not re-emitted as a query param
        assert not any(p["name"] == "name" for p in params)

    def test_sibling_fallback_for_undocumented_name(self):
        # SandboxAPI.get_sandbox documents no format; start_sandbox documents
        # ``sandboxes/{sandbox_id}`` for the same noun.
        details = get_operation_details(
            sandbox, "SandboxAPI", "get_sandbox", service_name="sandbox", resource_snake_name="sandbox"
        )
        assert list(details) == ["/api/2.0/sandboxes/{sandbox_id}"]

    def test_parent_in_nested_path(self):
        details = get_operation_details(
            sandbox, "SandboxAPI", "list_commands", service_name="sandbox", resource_snake_name="sandbox"
        )
        assert list(details) == ["/api/2.0/sandbox-exec/sandboxes/{sandbox_id}/commands"]

    def test_non_name_param_with_documented_template(self):
        details = get_operation_details(
            agentkit, "AgentKitAPI", "extract_memories",
            service_name="agentkit", resource_snake_name="agent_kit",
        )
        path = "/api/2.0/agents/session-stores/{session_store_id}/sessions/{session_id}/extractions"
        assert list(details) == [path]
        names = [p["name"] for p in details[path]["post"]["parameters"] if p["in"] == "path"]
        assert names == ["session_store_id", "session_id"]

    def test_curated_template(self):
        # networking.EndpointsAPI.get_endpoint documents nothing for ``name``;
        # resource_name_templates.json supplies the template.
        details = get_operation_details(
            networking, "EndpointsAPI", "get_endpoint",
            service_name="networking", resource_snake_name="endpoints",
        )
        assert list(details) == ["/api/networking/v1/accounts/{account_id}/endpoints/{endpoint_id}"]

    def test_lro_operation_name_is_not_inferred_from_siblings(self):
        details = get_operation_details(
            networking, "PrivateNetworkGatewaysAPI", "get_private_network_gateway_operation",
            service_name="networking", resource_snake_name="private_network_gateways",
        )
        assert list(details) == ["/api/networking/v1/{name}"]

    def test_distinct_resources_no_longer_collide(self):
        paths = set()
        for op in ("get_memory_store", "get_session_store", "get_session", "get_memory"):
            details = get_operation_details(
                agentkit, "AgentKitAPI", op, service_name="agentkit", resource_snake_name="agent_kit"
            )
            paths.update(details)
        assert len(paths) == 4


# ---------------------------------------------------------------------------
# Request bodies spread from a dataclass (body = <param>.as_dict())
# ---------------------------------------------------------------------------


def _body_schema(details, path, verb):
    return details[path][verb]["requestBody"]["content"]["application/json"]["schema"]


class TestSpreadRequestBody:
    def test_dataclass_fields_are_the_body(self):
        # create_network_connectivity_configuration(network_connectivity_config: Create...)
        # sends network_connectivity_config.as_dict() as the body: {"name", "region"}.
        details = get_operation_details(
            settings, "NetworkConnectivityAPI", "create_network_connectivity_configuration",
            service_name="settings", resource_snake_name="network_connectivity",
        )
        schema = _body_schema(details, "/api/2.0/accounts/{account_id}/network-connectivity-configs", "post")
        assert "network_connectivity_config" not in schema["properties"]
        assert set(schema["properties"]) >= {"name", "region"}
        assert set(schema.get("required", [])) >= {"name", "region"}

    def test_private_endpoint_rule_body(self):
        details = get_operation_details(
            settings, "NetworkConnectivityAPI", "create_private_endpoint_rule",
            service_name="settings", resource_snake_name="private_endpoint_rules",
        )
        path = "/api/2.0/accounts/{account_id}/network-connectivity-configs/{network_connectivity_config_id}/private-endpoint-rules"
        schema = _body_schema(details, path, "post")
        assert "private_endpoint_rule" not in schema["properties"]
        assert {"resource_id", "group_id"} <= set(schema["properties"])

    def test_spread_body_keeps_other_body_params(self):
        # update_private_endpoint_rule spreads the rule and takes update_mask as a query param
        details = get_operation_details(
            settings, "NetworkConnectivityAPI", "update_private_endpoint_rule",
            service_name="settings", resource_snake_name="private_endpoint_rules",
        )
        (path,) = details
        op = details[path]["patch"]
        assert "private_endpoint_rule" not in op["requestBody"]["content"]["application/json"]["schema"]["properties"]
        assert any(p["name"] == "update_mask" and p["in"] == "query" for p in op["parameters"])

    def test_explicit_body_keys_unchanged(self):
        # ClustersAPI.create assigns body["spark_version"] = ... field by field: no spread
        details = get_operation_details(
            compute, "ClustersAPI", "create", service_name="compute", resource_snake_name="clusters"
        )
        schema = _body_schema(details, "/api/2.1/clusters/create", "post")
        assert "spark_version" in schema["properties"]

    def test_new_service_create_is_spread(self):
        details = get_operation_details(
            domains, "DomainsAPI", "create_domain", service_name="domains", resource_snake_name="domains"
        )
        schema = _body_schema(details, "/api/2.0/domains", "post")
        assert "domain" not in schema["properties"]
        assert {"name", "tag_key"} <= set(schema["properties"])
