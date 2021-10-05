#!/bin/sh
git pull origin master
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py custom_email_check_permission
python3 manage.py custom_translator_permission
python3 manage.py loaddata mvp/fixtures/groups.json
python3 manage.py set_user_permission
python3 manage.py collectstatic
sudo systemctl restart apache2