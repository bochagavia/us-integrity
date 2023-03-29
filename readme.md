# US Integrity - Leagues APP

## Requirements
* Python3.10
* sqlite3

## Steps to run the app

Create a virtualenv and install requirements
```
pip install -r requirements.txt
```

Run Migrations
```
python manage.py migrate
```

Create Super User
```
python manage.py createsuperuser
```

Seed the Database
```
python manage.py loaddata leagues/fixtures.json
```

Run Server
```
python manage.py runserver
```

Go to ```http://localhost:800``` to see the list of leagues with their teams.

The admin is available at ```http://localhost:800/admin```

## Tests
```
python manage.py test
```