# Intro

This is the source code for the Cover Tutoring system which you can find on https://tutoring.svcover.nl.

# Usage

# Install
As requirements you'll need:
- Python
- Virtual Environments

First, set up your virtual environment in `.env`. Then, install the python requirements.

```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt

```


Next, you need to setup a few django-related things
```bash
cd web

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata languages.yaml
python manage.py loaddata subjects.yaml

# You'll only need this one when you're on the server:
python manage.py collectstatic --no-input
```
As soon as you did that, you should be ready to go! Give it a test by spinning up the development server :)

```bash
python manage.py runserver
```

Now you can preview the site on http://localhost:8000/

When you're done, wrap up by pressing Ctrl+C and:

```bash
deactivate
```

## Sending mails

You can trigger the mail digest by:

```bash
python manage.py sendmaildigest
```

But watch out! If you do this on production you'll spam everyone who has new messages.

# Testing

If you want to write unit tests make sure you make it easy for yourself and first read this tutorial:

https://docs.djangoproject.com/en/2.0/topics/testing/overview/

# Organisation

The website is built using [Django 1.11.6](https://www.djangoproject.com).

The main code can be found in `tutoring/`.

So far there are the following apps:

## CoverAccounts
This app handles everything related to users and their cover accounts:
- model
- Authentication forms & logistics
- Profile setting

## messages
This app handles everything concerning messages between users

## maildigest
This app adds `sendmaildigest` as command and handles everything concerned with sending the weekly mail digest.

## tutors
This app handles tutors, tutoring requests, tutoring subjects and languages. And everything concerned with it (models, views, controllers).
