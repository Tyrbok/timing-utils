PACKAGE_NAME = timing_utils
PYPI_REPO = pypi
TESTPYPI_REPO = testpypi

.PHONY: help
help: 
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z\/_-]+:.*?## / {sub("\\\\n",sprintf("\n%22c"," "), $$2);printf " \033[36m%-20s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:
	uv pip install -e .[dev]

test:
	pytest

tox:
	tox

lint:
	ruff check .

build:
	rm -rf dist/
	python -m build

publish: build
	twine upload --repository $(PYPI_REPO) dist/*

test-publish: build
	twine upload --repository $(TESTPYPI_REPO) dist/*

clean:
	rm -rf dist/ *.egg-info/ .pytest_cache/ .tox/ .coverage htmlcov/

uninstall:
	pip uninstall -y $(PACKAGE_NAME)