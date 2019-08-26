### Setup

Use `Python 3` for back-end.

All the requirements are described in `requirements.txt`. 

Initial requirements include:

- [Django](https://docs.djangoproject.com/en/2.2/) as the base framework


The application uses SQLite for the database by default.

Migrate the database before the first run:

    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser

Load initial data for projects:

    python manage.py loaddata apps/main/fixtures/initial.json

### Running the application

    python manage.py runserver

The application should be visible at `127.0.0.1:8000` after that.

In our initial data we have created 2 users user1 and user2, password for both is "test"

now you can check that user1 (which belongs to group1) has access to view1 only, and user2 has access to view2 only