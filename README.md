# web-demo
Demo for web-app; 3-tier; rest-api written in flask/python

REQUIREMENTS
pip install flask
pip install requests

TODO 
- logging
- authentication/authorisation (token)
- data validating (RequestParser)
- database persistence SQLAlchemy/SQLite
- semi-persistence by 
  - adding save-method on insert/update/delete
  - read stored file if exist
- testing
  - (curl) multiple checks per test
  - python test-framework (unittest/api)
- frontend
  - simple: flask
  - angular
