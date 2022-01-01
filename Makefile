.PHONY: black flake test types install interrogate build buildcheck pypi testpypi clean cleanall style check pipinstall this

PACKAGE_NAME := "genespeak"
TESTPYPI_DOWNLOAD_URL := "https://test.pypi.org/simple/"

black:
	black --target-version py38 $(PACKAGE_NAME) tests setup.py

flake:
	flake8 $(PACKAGE_NAME) tests setup.py

test:
	pytest tests

types:
	python -m $(PACKAGE_NAME) tests

install:
	python -m pip install -e ".[dev]"
	pre-commit install

interrogate:
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 tests
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 $(PACKAGE_NAME)

build: clean
	python setup.py sdist
	python setup.py bdist_wheel \
		# --universal

buildcheck: build
	twine check dist/*

pypi: build
	twine upload dist/*

testpypi: build
	# source: https://packaging.python.org/en/latest/guides/using-testpypi/#using-testpypi-with-twine
	twine upload --repository testpypi dist/*

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache

cleanall: clean
	rm -rf build/* dist/* $(PACKAGE_NAME).egg-info/*

style: clean black flake interrogate clean

check: clean black flake interrogate test clean

pipinstalltest:
	python -m pip install -U --index-url $(TESTPYPI_DOWNLOAD_URL) $(PACKAGE_NAME)

this:
	# example: make this VERSION="0.0.3"
	@echo $(PACKAGE_NAME)==$(VERSION)
