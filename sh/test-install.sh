#!/bin/sh

CUR_DIR=$(pwd)

python3 -m venv ./.venv2
. ./.venv2/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

cd ${CUR_DIR}

exit 0
