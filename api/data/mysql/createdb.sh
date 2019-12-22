#!/bin/bash
# sudo chmod +x createdb.sh
# ./createdb.sh

# (check)
# mysql -h localhost -u debian-sys-maint -p
# Password: OX2VZ4XPu8tVWHYx
# show databases;
# describe Books;
# show index from Books;
# use information_schema;
# select * from CHECK_CONSTRAINTS;
# exit

# TODO Create DB from app: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

mysql -h localhost -u debian-sys-maint -p < schema.sql
 
# TODO sqlite3 $DBFILE < populate.sql

