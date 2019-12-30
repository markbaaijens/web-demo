# web-demo
Demo for web-app, 3-tier. The rest-api written in flask/python. The API has several data-models
to choose from, including flatfile, sqlite, mysql, etc.

## Requirements
OS:
- python3
- sqlite3 (apt install sqlite3)

Python packages
- pip install -r requirements.txt

## Choose the desired data-model
- comment or uncomment in api/logic.py the desired model

## Create sqlite-database (optional)
- $ cd api/data/sqlite
- $ chmod +x createdb.sh
- $ ./createdb.sh
- (database 'data.db' is created in api/data)

## Create sqlite-database (optional)
- (setup a mysql-server with a admin-user)
- $ cd api/data/mysql
- (modify createdb.sh: replace server, user_name and password)
- $ chmod +x createdb.sh
- $ ./createdb.sh
- (database 'data' is created on the mysql-server)

## Run application
Start API
- cd api
- python controller.py
=> localhost:5000

Start webserver:
- cd web/flask
- python controller.py
=> (browser) localhost:5001

## Documentation
- General https://github.com/markbaaijens/web-demo/wiki
- Todo's https://github.com/markbaaijens/web-demo/wiki/Todo
- Roadmap https://github.com/markbaaijens/web-demo/wiki/Roadmap
