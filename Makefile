.PHONY: black flake test types install interrogate \
		build buildcheck buildplus buildcheckplus getpackageinfo \
		github pypi testpypi \
		clean cleanall style check pipinstalltest \
		streamlit_demo streamlit_run \
		this thispy thatpy


PACKAGE_NAME := "genespeak"
TESTPYPI_DOWNLOAD_URL := "https://test.pypi.org/simple/"
PYPIPINSTALL := "python -m pip install -U --index-url"
PIPINSTALL_PYPITEST := "$(PYPIPINSTALL) $(TESTPYPI_DOWNLOAD_URL)"
PKG_INFO := "import pkginfo; dev = pkginfo.Develop('.'); print((dev.$${FIELD}))"
STREAMLIT_DEMO_APP := "./apps/demo/streamlit_app/app.py"
STREAMLIT_PORT := 12321


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

buildplus: build getpackageinfo

buildcheckplus: buildcheck getpackageinfo

getpackageinfo:
	$(eval PKG_NAME := $(shell FIELD="name" && python -c $(PKG_INFO);))
	@echo PKG_NAME is: [$(PKG_NAME)]
	$(eval PKG_VERSION := $(shell FIELD="version" && python -c $(PKG_INFO);))
	@echo PKG_VERSION is: [$(PKG_VERSION)]

github: buildplus
	# creating a github release: https://cli.github.com/manual/gh_release_create
	gh release create v$(PKG_VERSION)

githubplus: buildplus
	# creating a github release: https://cli.github.com/manual/gh_release_create
	gh release create v$(PKG_VERSION) ./dist/$(PKG_NAME)-$(PKG_VERSION)*.*

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

streamlit_demo:
	# Note: To run the following command the port 8051 needs to be available.
	#       If somehow, a previously running streamlit session did not exit
	#		properly, you need to manually and forcibly stop it.
	#       Stop an already running streamlit server:
	#
	#       sudo fuser -k 8051/tcp
	streamlit run $(STREAMLIT_DEMO_APP) --server.port=8051 &

streamlit_run:
	# Note: To run the following command the port 8051 needs to be available.
	#       If somehow, a previously running streamlit session did not exit
	#		properly, you need to manually and forcibly stop it.
	#       Stop an already running streamlit server:
	#
	#       sudo fuser -k $(STREAMLIT_PORT)/tcp
	streamlit run $(STREAMLIT_DEMO_APP) --server.port=$(STREAMLIT_PORT) &

this:
	# example: make this VERSION="0.0.3"
	@if [ $(VERSION) ]; then echo This is $(PACKAGE_NAME)==$(VERSION); else echo This is $(PACKAGE_NAME); fi;

thispy:
	#  example: https://lists.gnu.org/archive/html/help-make/2015-03/msg00011.html
	@FIELD="name" && python -c $(PKG_INFO);
	@FIELD="version" && python -c $(PKG_INFO);
	$(eval FIELD := "name")
	@echo FIELD is: [$(FIELD)]

thatpy: thispy
	@echo FIELD is: [$(FIELD)]
