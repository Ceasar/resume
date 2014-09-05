
ENV=env

index.html: $(ENV) data/* templates/*
	. $(ENV)/bin/activate; python build.py
 
$(ENV): requirements.txt
	virtualenv $(ENV)
	. $(ENV)/bin/activate; pip install --requirement requirements.txt
