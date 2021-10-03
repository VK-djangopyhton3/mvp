#!/bin/sh
git pull origin master
source /var/www/mvp/.venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo systemctl restart apache2