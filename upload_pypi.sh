#!/bin/bash

clear

echo "Delete old build"
rm -rf build
rm -rf dist
rm -rf *.egg-info

echo "Build package"
python3 setup.py sdist bdist_wheel

echo "Upload package"
twine upload dist/*

echo "Done"



