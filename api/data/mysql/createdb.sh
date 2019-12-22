#!/bin/bash
# sudo chmod +x createdb.sh
# ./createdb.sh

# TODO Create DB from app: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

mysql -h localhost -u debian-sys-maint < schema.sql
# OX2VZ4XPu8tVWHYx

# TODO sqlite3 $DBFILE < populate.sql

