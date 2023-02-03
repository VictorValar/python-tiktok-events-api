# install: requirements.txt
# 	pip install -r requirements.txt

build: setup.py
	python setup.py sdist bdist_wheel

dist:
	twine upload dist/*
