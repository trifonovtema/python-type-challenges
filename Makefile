.PHONY: install format typing

install:
	poetry install

format:
	poetry run black src

typing:
	poetry run pyright src
	poetry run mypy src --exclude typed-dict
