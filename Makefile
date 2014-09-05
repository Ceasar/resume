
ENV=env

index.html: $(ENV) data/* templates/* static/stylesheets
	. $(ENV)/bin/activate; python build.py
 
$(ENV): requirements.txt
	virtualenv $(ENV)
	. $(ENV)/bin/activate; pip install --requirement requirements.txt

deploy:
	git checkout gh-pages
	git rebase master
	rm index.html
	make index.html
	git add index.html
	git commit --amend --no-edit
	git push origin gh-pages -f
	git checkout master

static/stylesheets: static/sass
	compass compile static
