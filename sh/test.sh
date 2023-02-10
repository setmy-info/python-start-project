#!/bin/sh

CUR_DIR=$(pwd)
. ./.venv/bin/activate
python -m unittest discover -s ./ -p *_test.py
cd ${CUR_DIR}

exit 0
