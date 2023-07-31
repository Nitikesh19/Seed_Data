#!/bin/bash
set -x #echo on
rm db.sqlite3
rm -rf ./core/migrations/*.py
touch ./core/migrations/__init__.py
python ./manage.py makemigrations
if [ $? -ne 0 ]; then
  exit 1
fi
python ./manage.py migrate