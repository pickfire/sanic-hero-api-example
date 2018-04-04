Python, Sanic, Peewee Rest API Example
======================================

Build Restful CRUD API for a simple application using Python, Sanic and Peewee.

Requirements
------------
- python 3 > 3.5.x

Setup
-----

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    export DATABASE_URL=mysql+pool://user:pass@localhost/heroes
    sudo python app.py

Explore Rest APIs
-----------------
The app defines following CRUD APIs.

    GET /heroes

You can test them using postman or any other rest client.

Learn more
----------
Check out @sean3z blog post - <https://medium.com/p/1867308352d8>
