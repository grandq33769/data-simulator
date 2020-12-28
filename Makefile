PKG_LIST := src
name ?= $(shell echo `git remote show -n origin | grep Fetch | cut -d/ -f4- | cut -d. -f1`)
.DEFAULT_GOAL := help

.PHONY: init flake8 pylint lint test clean dev commit run simple-clean pre-commit-clean prod dev pre-commit help

init: simple-clean ## Init python base
	pipenv --python 3.7

prod: init ## Init production environment
	pipenv install

dev: init ## Init development environment
	pipenv install --dev --skip-lock

pre-commit: dev ## Init development environment with pre-commit
	pipenv run pre-commit install
	pipenv run pre-commit install -t commit-msg

commit: ## Commitizen commit
	pipenv run cz commit

commit-retry: ## Commitizen commit retry
	pipenv run cz commit --retry

bump: ## Commitizen bump
	pipenv run cz bump --yes

changelog: ## Commitizen changelog
	pipenv run cz changelog

freeze: ## Freeze the packages to .txt
	pipenv lock -r > requirements.txt
	pipenv lock --dev -r > requirements-dev.txt

lint: pylint flake8 ## Lint bundle

flake8: ## Lint .py using flake8
	pipenv run flake8 --max-line-length=120

pylint: ## Lint .py using pylint
	# No Need to ignore "tests", it is a bug
	# Reference: https://github.com/PyCQA/pylint/issues/2686
	for pkg in $(PKG_LIST) ; do \
        echo $$pkg && pipenv run pylint $$pkg; \
    done

reformat: black isort ## Reformat bundle

black: ## Format the .py
	pipenv run black **/*.py

isort: ## Sort import .py import order
	pipenv run isort **/*.py

test: ## Pytest
	for pkg in $(PKG_LIST) ; do \
		pipenv run pytest --cov=$$pkg --cov-report term-missing -rsx; \
	done

ci-bundle: reformat lint test ## CI bundle tasks

docker-build: ## Docker Image build
	docker build -t $(name) .

docker-deploy: ## Docker Image deploy
	docker $(name):$(tag)
	docker push $(name):$(tag)

simple-clean: ## Clean cache
	find . -type f -name '*.py[co]' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf .mypy_cache
	rm -rf .hypothesis
	rm -rf .pytest_cache
	rm -rf .tox
	rm -f report.xml
	rm -f coverage.xml

pre-commit-clean: ## Clean pre-commit setting
	pipenv run pre-commit uninstall
	pipenv run pre-commit clean

clean: ## Clean all cache and pre-commit setting
	make simple-clean
	make pre-commit-clean

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' \
	| column -t  -s ' '