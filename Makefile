SHELL := /bin/bash
.PHONY: all clean dist docs install pep8 publish run-pre-commit run-tox setup-pre-commit test test_examples test_only help coverage-report

detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: all install run-pre-commit test test_examples coverage-report

test_examples:
	@echo '###############  Chdir to example directory  ###############'

	@echo '###############  Calling from outer folder  ###############'

watch:
	ls **/**.py | entr py.test -m "not integration" -s -vvv -l --tb=long --maxfail=1 tests/

test_only:
	py.test -m "not integration" -v --cov-config .coveragerc --cov=playlist -l --tb=short --maxfail=1 tests/
	coverage xml

test_integration:
	py.test -m integration -v --cov-config .coveragerc --cov=playlist --cov-append -l --tb=short --maxfail=1 tests/
	coverage xml

coverage-report:
	coverage report --fail-under=100

test: pep8 test_only

install:
	pip install --upgrade pip
	pip install -r requirements_dev.txt
	make setup-pre-commit

setup-pre-commit:
	pre-commit install
	pre-commit install-hooks

run-pre-commit:
	rm -rf .tox/
	rm -rf build/
	pre-commit run --files $$(find -E '.*\.\(py\|yaml\|yml\|md\)') -v

pep8:
	# Flake8 ignores
	#   F841 (local variable assigned but never used, useful for debugging on exception)
	#   W504 (line break after binary operator, I prefer to put `and|or` at the end)
	#   F403 (star import `from foo import *` often used in __init__ files)
	# flake8 playlist --ignore=F403,W504,W503,F841,E401,F401,E402 --exclude=playlist/vendor
	flake8 playlist --exclude=playlist/vendor*

dist: clean
	@python setup.py sdist bdist_wheel

publish:
	make run-tox
	@twine upload dist/*

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

docs:
	rm -rf legacy_docs/_build
	@cd legacy_docs;make html

run-tox:
	tox --recreate
	rm -rf .tox
