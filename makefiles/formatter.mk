.PHONY: lint
lint:
	pflake8 app tests
	mypy app tests

.PHONY: format
format:
	black --exclude .venv app tests
	autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables app tests
	isort --profile=black app tests
