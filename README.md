# web-demo
Demo for web-app; 3-tier; rest-api written in flask/python

REQUIREMENTS
OS:
- python3
- sqlite3 (apt install sqlite3)

Python packages
- pip install -r requirements.txt

Start API
- cd api
- python controller.py
Access: localhost:5000

Start webserver:
- cd web/flask
- python controller.py
Access: localhost:5001

TODO 
- logging
- authentication/authorisation (token)
- data validating (RequestParser)
- database persistence SQLAlchemy/SQLite
- testing
  - python test-framework (unittest/api)
- frontend
  - angular
