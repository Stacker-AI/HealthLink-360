@echo off

python3 -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser

python manage.py graph_models api -o api_model.png