black:
	black --target-version py38 genespeak tests setup.py

flake:
	flake8 genespeak tests setup.py

test:
	pytest tests

types:
	python -m genespeak tests

install:
	python -m pip install -e ".[dev]"
	pre-commit install

interrogate:
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 tests
	interrogate -vv --ignore-nested-functions --ignore-semiprivate --ignore-private --ignore-magic --ignore-module --ignore-init-method --fail-under 100 genespeak

build: clean
	python setup.py sdist
	python setup.py bdist_wheel --universal

pypi: build
	# python setup.py sdist
	# python setup.py bdist_wheel --universal
	twine upload dist/*

testpypi: build
	# source: https://packaging.python.org/en/latest/guides/using-testpypi/#using-testpypi-with-twine
	twine upload --repository testpypi dist/*

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache

style: clean black flake interrogate clean

check: clean black flake interrogate test clean
