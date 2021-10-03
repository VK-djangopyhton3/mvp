#!/bin/sh
git pull origin master
pip3 install -r requirements.txt
source /var/www/mvp/.venv/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
sudo systemctl restart apache2