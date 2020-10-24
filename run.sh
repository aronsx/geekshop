#!/bin/bash
# add path to your project and python env
me=`basename "$0"`
python_env='/home/aronsx/Projects/geekshop/venv/bin/python'
project='/home/aronsx/Projects/geekshop/geekshop'
ip_addr='0.0.0.0'
port='8000'
name='django_run'
file_path='.local/bin/'

if [ $me != $name ]; then
	if [ -f $HOME/$file_path$name ]; then
		echo "You may start django server with command $name"
	else
		echo "Add script to $HOME/$file_path to start django server with $name? [y/n]"
		read answer
		if [ $answer = 'y' ] || [ $answer = 'Y' ]; then
			mkdir -p $HOME/$file_path
			cp $me $HOME/$file_path$name
		fi
	fi
fi

$python_env $project/manage.py runserver $ip_addr:$port
