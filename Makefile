setup:
	python3 -m pip install -r requirements-dev.txt

build:
	python3 -m build

release:
	python3 -m twine upload dist/*

.PHONY: setup build release
