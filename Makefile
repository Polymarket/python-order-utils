.PHONY: help init test fmt lint

help: ## Show available Make targets
	@echo "Available targets:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' Makefile | \
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

init: ## Install project dependencies
	pip install -r requirements.txt

test: ## Run tests
	pytest -s

fmt: ## Format code with black
	black ./

lint: ## Run basic lint checks
	python -m compileall py_order_utils
