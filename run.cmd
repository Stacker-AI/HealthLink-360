@echo off

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

start cmd /k "cd frontend && ng serve"
