.PHONY: build
build:
	docker-compose build smithworks_cli

.PHONY: shell
shell:
	docker-compose run --rm smithworks_cli /bin/bash

.PHONY: test
test:
	docker-compose run --rm smithworks_cli poetry run pytest

.PHONY: lint
lint:
	docker-compose run --rm smithworks_cli bash -c "poetry run black smithworks_cli/ && poetry run flake8 smithworks_cli/ && poetry run mypy smithworks_cli/"

.PHONY: wheel
wheel:
	docker-compose run --rm smithworks_cli poetry build -f wheel