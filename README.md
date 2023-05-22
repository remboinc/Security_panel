# Bank security console
A site with pass data, which shows the number of active passes, data for each pass, and who entered the vault. The program marks visits as suspicious if the person has spent more than an hour in the vault.
## How to start
Clone the project:
```
git clone https://github.com/remboinc/Security_panel.git
```
## Environment
Create a virtual environment on directory project:
```
python3.11 -m venv env
```
Start virtual environment:
```
.env/bin/activate
```
## Requirements
Before start to deploy install requirements:
```
pip install -r requirements.txt
```
## Environment variables
You need to create an .env file. Example:
```
DB_ENGINE=django.db.backends.example
DB_HOST=example.com
DB_PORT=5432
DB_NAME=example
DB_USER=admin
DB_PASSWORD=example


APP_SECRET_KEY=example
DEBUG=true
ALLOWED_HOSTS=0.0.0.0,localhost
```
## Run
To run the script, enter the command:
```
python manage.py runserver 0.0.0.0:8000
```

## Project Goals
This code was written for educational purposes as part of an online course for web developers at dvmn.org.