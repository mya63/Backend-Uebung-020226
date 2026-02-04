# Django Backend - Auth & Protected Endpoint

Kleines Django-REST-Backend mit:
-User Registration
-Token-Login
-Geschütztem API-Endpoint

## Setup
```bash
python -m venv venv
source venv/Scripts/activate # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver