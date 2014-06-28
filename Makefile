.PHONY: build

ENV=env
 
$(ENV): requirements.txt
	virtualenv $(ENV)
	. $(ENV)/bin/activate; pip install --requirement requirements.txt

build: $(ENV)
	. $(ENV)/bin/activate; python build.py
