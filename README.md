# MVP
_Backend_ python code

## Clone the project
###Clone the project from Github:

    Project Root Directory: `/var/www`
    
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
