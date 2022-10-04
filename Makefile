.ONESHELL:
include .env
export 

FLASK_ENV := development
FLASK_APP := app.py

.PHONY: clean install run 

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

run:
	. venv/bin/activate; \
	export FLASK_APP=${FLASK_APP}; \
	export FLASK_ENV=${FLASK_ENV}; \
	flask run