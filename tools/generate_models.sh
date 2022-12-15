#!/bin/bash

# if [ ! -e fhir-parser ]; then
# 	git submodule update --init --recursive
# fi

TOOLS_DIR=$(dirname "$0")
cd $TOOLS_DIR
#source fhir-parser/.venv/bin/activate

cp ../fhirbug/Fhir/base/settings.py fhir-parser/settings.py
cd fhir-parser
./generate.py $1
cd ..
