# Makefile for the StackQL Databricks provider workflow.
#
# Run from this directory (stackql_databricks_provider/) in a POSIX shell
# (Linux, macOS, or WSL on Windows). See AGENTS.md at the repo root for the
# full workflow description.
#
#   make upstream-pull   pull the latest upstream Databricks SDK changes
#   make all             end-to-end: specs -> inventories -> providers -> tests -> docs

SHELL := /bin/bash
ROOT_DIR := $(abspath $(dir $(abspath $(lastword $(MAKEFILE_LIST))))/..)
PROVIDER_DIR := $(ROOT_DIR)/stackql_databricks_provider
SOURCE_PROJECT ?= https://github.com/stackql-registry/stackql-provider-databricks

# Prefer the repo venv when present, otherwise fall back to python3 on PATH.
PYTHON ?= $(shell test -x $(ROOT_DIR)/.venv/bin/python && echo $(ROOT_DIR)/.venv/bin/python || echo python3)

STACKQL_BIN ?= $(PROVIDER_DIR)/stackql

# Hosts, auth and pagination are mastered in provider-config/*.json (the only
# place the Databricks hosts are written; see AGENTS.md "Multi-cloud hosts").
# provider-utils takes them as JSON strings, so they are read here.
CONFIG_DIR := $(PROVIDER_DIR)/provider-config
ACCOUNT_SERVERS := $(shell cat $(CONFIG_DIR)/account_servers.json)
WORKSPACE_SERVERS := $(shell cat $(CONFIG_DIR)/workspace_servers.json)
PROVIDER_CONFIG := $(shell cat $(CONFIG_DIR)/provider_config.json)
SERVICE_CONFIG := $(shell cat $(CONFIG_DIR)/service_config.json)

.PHONY: help deps upstream-pull specs inventory unit-test provider-account provider-workspace \
        transforms merge-views providers test-meta stackql smoke smoke-read-only smoke-live docs docs-build all clean

help:
	@echo "StackQL Databricks provider workflow"
	@echo ""
	@echo "  make deps              install python (editable) and npm dependencies"
	@echo "  make upstream-pull     fetch and merge upstream databricks-sdk-py main"
	@echo "  make specs             generate OpenAPI specs from the SDK"
	@echo "  make inventory         regenerate CSV operation inventories"
	@echo "  make unit-test         run the python unit test suite"
	@echo "  make providers         generate both providers + transforms + views"
	@echo "  make test-meta         run meta-route tests against both providers"
	@echo "  make stackql           download the stackql binary (POSIX)"
	@echo "  make smoke             live smoke tests (resource queries, self-cleaning lifecycles, views) against the local provider"
	@echo "  make smoke-read-only   the same without the create/delete lifecycles"
	@echo "  make smoke-live        smoke tests against the latest published providers"
	@echo "                         (CLOUD=aws|azure|gcp reads .env.<cloud>, see .env.<cloud>.example; ENV_FILE=... and SMOKE_ARGS=... override)"
	@echo "  make docs              generate docusaurus doc sources for both providers"
	@echo "  make docs-build        build both docusaurus microsites"
	@echo "  make all               end-to-end: everything above except upstream-pull"
	@echo "  make clean             remove generated provider output and doc builds"

deps:
	cd $(ROOT_DIR) && $(PYTHON) -m pip install -e ".[dev]"
	cd $(PROVIDER_DIR) && npm install

upstream-pull:
	cd $(ROOT_DIR) && git fetch upstream && git merge upstream/main
	@echo ""
	@echo "Upstream merged. Review new service modules with:"
	@echo "  git diff HEAD~1 --name-status -- databricks/sdk/service/ | grep '^A'"
	@echo "and register any new modules/classes in stackql_databricks_provider/registry.py"
	@echo "(see 'How to Update' in stackql_databricks_provider/README.md)."

specs:
	cd $(ROOT_DIR) && $(PYTHON) -m stackql_databricks_provider.generate

inventory:
	cd $(ROOT_DIR) && $(PYTHON) -m stackql_databricks_provider.inventory_gen --refresh-response-objects
	cd $(ROOT_DIR) && $(PYTHON) -m stackql_databricks_provider.inventory_gen --populate-object-keys
	cd $(ROOT_DIR) && $(PYTHON) -m stackql_databricks_provider.inventory_gen

unit-test:
	cd $(ROOT_DIR) && $(PYTHON) -m pytest stackql_databricks_provider/tests/ -q

provider-account:
	cd $(PROVIDER_DIR) && npm run generate-provider -- \
	  --provider-name databricks_account \
	  --input-dir openapi_generated/account \
	  --output-dir stackql-provider/src/databricks_account \
	  --config-path inventory/account/all_services.csv \
	  --servers '$(ACCOUNT_SERVERS)' \
	  --provider-config '$(PROVIDER_CONFIG)' \
	  --service-config '$(SERVICE_CONFIG)' \
	  --naive-req-body-translate \
	  --overwrite

provider-workspace:
	cd $(PROVIDER_DIR) && npm run generate-provider -- \
	  --provider-name databricks_workspace \
	  --input-dir openapi_generated/workspace \
	  --output-dir stackql-provider/src/databricks_workspace \
	  --config-path inventory/workspace/all_services.csv \
	  --servers '$(WORKSPACE_SERVERS)' \
	  --provider-config '$(PROVIDER_CONFIG)' \
	  --service-config '$(SERVICE_CONFIG)' \
	  --naive-req-body-translate \
	  --overwrite

transforms:
	cd $(PROVIDER_DIR) && $(PYTHON) add_response_transforms.py

merge-views:
	cd $(PROVIDER_DIR) && $(PYTHON) merge_views.py

# Full provider build: generation for both scopes, then the post-gen steps.
# merge-views must run last so views land in the final specs.
providers: provider-account provider-workspace transforms merge-views

test-meta:
	cd $(PROVIDER_DIR) && npm run start-server -- --registry $(PROVIDER_DIR)/stackql-provider
	cd $(PROVIDER_DIR) && npm run test-meta-routes -- databricks_account --verbose
	cd $(PROVIDER_DIR) && npm run test-meta-routes -- databricks_workspace --verbose
	cd $(PROVIDER_DIR) && npm run stop-server

stackql:
	@if [ ! -f "$(STACKQL_BIN)" ]; then \
	  OS=$$(uname -s | tr '[:upper:]' '[:lower:]'); \
	  ARCH=$$(uname -m); \
	  if [ "$$ARCH" = "x86_64" ]; then ARCH=amd64; fi; \
	  if [ "$$ARCH" = "aarch64" ] || [ "$$ARCH" = "arm64" ]; then ARCH=arm64; fi; \
	  echo "Downloading stackql ($$OS $$ARCH)..."; \
	  curl -sL -o $(PROVIDER_DIR)/stackql.zip "https://releases.stackql.io/stackql/latest/stackql_$${OS}_$${ARCH}.zip"; \
	  cd $(PROVIDER_DIR) && unzip -o stackql.zip && rm stackql.zip && chmod +x stackql; \
	fi
	@$(STACKQL_BIN) --version

# Live smoke tests (authenticated; resource queries, self-cleaning lifecycles,
# views). Credentials come from an env file (gitignored; copy the matching
# .env.<cloud>.example): .env by default, .env.$(CLOUD) when CLOUD=aws|azure|gcp
# is given, or any file via ENV_FILE=... The cloud itself comes from CLOUD or
# DATABRICKS_CLOUD (aws is the provider default). Extra harness flags go in
# SMOKE_ARGS, e.g.
#   make smoke CLOUD=azure
#   make smoke SMOKE_ARGS="--skip-views --scope account"
CLOUD ?=
ENV_FILE ?= $(if $(CLOUD),$(PROVIDER_DIR)/.env.$(CLOUD),$(PROVIDER_DIR)/.env)
SMOKE_ARGS ?=
smoke_cloud = $(if $(CLOUD),--cloud $(CLOUD),)

smoke: stackql
	cd $(PROVIDER_DIR) && $(PYTHON) smoke_tests/smoke.py --stackql-bin $(STACKQL_BIN) --env-file $(ENV_FILE) $(smoke_cloud) $(SMOKE_ARGS)

smoke-read-only: stackql
	cd $(PROVIDER_DIR) && $(PYTHON) smoke_tests/smoke.py --stackql-bin $(STACKQL_BIN) --env-file $(ENV_FILE) $(smoke_cloud) --read-only $(SMOKE_ARGS)

smoke-live: stackql
	cd $(PROVIDER_DIR) && $(PYTHON) smoke_tests/smoke.py --live --stackql-bin $(STACKQL_BIN) --env-file $(ENV_FILE) $(smoke_cloud) $(SMOKE_ARGS)

docs:
	cd $(PROVIDER_DIR) && npm run generate-docs -- \
	  --provider-name databricks_account \
	  --provider-dir ./stackql-provider/src/databricks_account/v00.00.00000 \
	  --output-dir ./website/databricks_account \
	  --provider-data-dir ./docgen/provider-data/databricks_account \
	  --source-project $(SOURCE_PROJECT)
	cd $(PROVIDER_DIR) && npm run generate-docs -- \
	  --provider-name databricks_workspace \
	  --provider-dir ./stackql-provider/src/databricks_workspace/v00.00.00000 \
	  --output-dir ./website/databricks_workspace \
	  --provider-data-dir ./docgen/provider-data/databricks_workspace \
	  --source-project $(SOURCE_PROJECT)
	cd $(PROVIDER_DIR) && $(PYTHON) add_doc_examples.py --doc-dir website

docs-build:
	cd $(PROVIDER_DIR)/website/databricks_account && npm install --no-audit --no-fund && npm run build
	cd $(PROVIDER_DIR)/website/databricks_workspace && npm install --no-audit --no-fund && npm run build

all: specs inventory unit-test providers test-meta smoke docs docs-build
	@echo ""
	@echo "End-to-end provider build complete."

clean:
	rm -rf $(PROVIDER_DIR)/stackql-provider/src/databricks_account $(PROVIDER_DIR)/stackql-provider/src/databricks_workspace
	rm -rf $(PROVIDER_DIR)/website/databricks_account/build $(PROVIDER_DIR)/website/databricks_workspace/build
	rm -rf $(PROVIDER_DIR)/.stackql-smoke $(PROVIDER_DIR)/.stackql-smoke-live
