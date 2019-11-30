#!/bin/bash
source ~/.bashrc
mkvirtualenv --python=/usr/bin/python36 django-press
workon django-press
python manage.py runserver &
