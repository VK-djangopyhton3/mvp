# MVP for Translator
_Backend_ python code
The objective of this assignment is to develop an Translator system for Organization. A typical workflow for Organization .

## Clone the project
###Clone the project from Github:

    Project Root Directory: `/var/www` Or any
    
    git clone remote url

## Create Environment file

    Go to the settings folder then create settings.ini or .env file

    Note : Like see the example.ini file in project root folder, same veriable copy and paste in settings.ini file on settings folder then update env varible .

## Virtual Environment Setup
###Create Virtualenv Folder

    virtualenv --python=python3.9 Project_dir/.venv


###Activate Environment:

    source pro# mvp
###Backend python code

## Clone the project
Clone the project from Github:

    Project Root Directory: `/var/www`
    
    git clone remote url

## Create Environment file

    Go to the settings folder then create settings.ini or .env file

    Note : Like see the example.ini file in project root folder, same veriable copy and paste in settings.ini file on settings folder then update env varible .

## Virtual Environment Setup
###Create Virtualenv Folder

    virtualenv --python=python3.9 Project_dir/.venv


###Activate Environment:

    source project_venv/bin/activate

## Install dependencies:

    pip install -r requirements.txt


## Apply database migrations
    
    python3 manage.py makemigrations 
    python3 manage.py migrate


## Run Management Commands & Load base data
###Commands & Load fixtures::

    python3 manage.py custom_email_check_permission
    python3 manage.py custom_translator_permission
    python3 manage.py loaddata mvp/fixtures/groups.json
    python3 manage.py set_user_permission


## Create super user
    
    python3 manage.py createsuperuser


# Manual Project Setup with AWS
    
### Install web server
    sudo apt-get install apache2 apache2-dev
    Follow above process then.

### Install python dependencies
    sudo apt-get install python3.9-dev #or another python version

## Setup conf file for apache

     <VirtualHost *:80>
        ServerName ip or domain
    
        Alias /static /var/www/project_dir/staticfiles
    
        <Directory /var/www/project_dir/staticfiles>
            Require all granted
        </Directory>
        <Directory /var/www/project_dir/>
            <Files wsgi.py>
                Require all granted
            </Files>
        </Directory>
    
        WSGIPassAuthorization On
        WSGIDaemonProcess project_name python-home=/var/www/project_dir/.venv python-path=/var/www/mvp
        WSGIProcessGroup project_name
        WSGIScriptAlias / /var/www/project_dir//wsgi.py
        LoadModule wsgi_module "/var/www/project_dir/.venv/lib/python3.9/site-packages/mod_wsgi/server/mod_wsgi-py39.cpython-39-x86_64-linux-gnu.so"
    
    </VirtualHost>

    Then deactivate current activated conf and activate our conf then run

    sudo service apache2 restart
