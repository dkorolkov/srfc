#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cd srfc
./manage.py makemigrations
./manage.py migrate
./manage.py load_data usermenu/data/initdata.yaml
