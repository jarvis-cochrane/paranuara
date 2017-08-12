# Paranuara

# Introduction

This project is a possible solution to the Paranuara coding challenge at
https://github.com/joaosgreccia/hivery-backend-challenge.

This solution is optimised for development time and has some rough edges!

## Installation

1. Create a virtualenv environment with Python 3.6

    `python -m venv env`

2. Enable the virtual environment

    `source env/bin/activate`

3. Install dependencies

    `pip install -r requirements.txt`

4. Create database

    `python manage.py migrate`

5. Create admin user for web admin interface

    `python manage.py createsuperuser`

## Run test cases

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Run test cases

    `python manage.py test`

## Import sample data

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Import companies

    `python manage.py import_companies resources/companies.json`

3. Import clean foodstuff data

    `python manage.py import_foodstuffs resources/foodstuffs.json`

4. Import person data

    `python manage.py import_people resources/people.json`

## Run web server and access REST end points

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Start the web server

    `python manage.py runserver`

Access admin pages by navigating to http://localhost:8000/admin

Access the REST API by navigating to http://localhost:8000/api

### Rest API

The REST API is not *quite* self documenting. The following urls are supported:

    /companies                                          list all companies
    /companies/{company_index}                          get company details & list employees
    /people                                             list all people
    /people/{person_index}                              get person details & favourite foods
    /people/{person_index}/friends                      list friends of person
    /people/{person_index_1}/friends/{person_index_2}   get details of person 1 and person 2,
                                                        and any mutual friends who are alive and
                                                        have brown eyes.

    
