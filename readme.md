# Installation

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

# Test Cases

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Run test cases

    `python manage.py test`

# Import test data

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Import companies

    `python manage.py import_companies resources/companies.json`

3. Import clean foodstuff data

    `python manage.py import_foodstuffs resources/foodstuffs.json`

4. Import person data

    `python manage.py import_people resources/people.json`

# Run web server and access REST end points

1. Enable the virtual environment (if required)

    `source env/bin/activate`

2. Start the web server

    `python manage.py runserver`

Access admin pages by navigating to [http://localhost:8000/admin]

Access the REST API by navigating to [http://localhost:8000/api]

    
