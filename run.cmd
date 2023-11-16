@echo off

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
python manage.py makemigrations
python manage.py migrate

start cmd /k "cd frontend && ng serve"
