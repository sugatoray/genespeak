.PHONY: black flake test types install interrogate build buildcheck pypi testpypi clean cleanall style check pipinstalltest this

PACKAGE_NAME := "genespeak"
TESTPYPI_DOWNLOAD_URL := "https://test.pypi.org/simple/"
PYPIPINSTALL := "python -m pip install -U --index-url"
PIPINSTALL_PYPITEST := "$(PYPIPINSTALL) $(TESTPYPI_DOWNLOAD_URL)"

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

buildcheck: cleanall build
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
	@if [ $(VERSION) ]; then $(PIPINSTALL_PYPITEST) $(PACKAGE_NAME)==$(VERSION); else $(PIPINSTALL_PYPITEST) $(PACKAGE_NAME); fi;

this:
	# example: make this VERSION="0.0.3"
	@if [ $(VERSION) ]; then echo This is $(PACKAGE_NAME)==$(VERSION); else echo This is $(PACKAGE_NAME); fi;
