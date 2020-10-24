#!/bin/bash
# add path to your env and project
python_env='/home/aronsx/Projects/geekshop/venv/bin/python'
project='/home/aronsx/Projects/geekshop/geekshop'
ip_addr='0.0.0.0'
port='8000'

$python_env $project/manage.py runserver $ip_addr:$port
