test:
	pytest -rP

# install: requirements.txt
# 	pip install -r requirements.txt

clean:
	rm -rf build dist *.egg-info

build: setup.py
	python setup.py sdist bdist_wheel

