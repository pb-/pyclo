lint:
	pipenv run flake8 pyclo
.PHONY: lint

test:
	pipenv run pytest
.PHONY: test

install:
	pipenv install --dev
.PHONY: install

dist:
	rm -f dist/*
	pipenv run python setup.py sdist bdist_wheel
.PHONY: dist

upload:
	pipenv run twine upload dist/*
.PHONY: upload
