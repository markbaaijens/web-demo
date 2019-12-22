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

# TODO Create DB from app: https://www.w3schools.com/python/python_mysql_create_db.asp

mysql -h localhost -u debian-sys-maint -p < schema.sql
mysql -h localhost -u debian-sys-maint -p < populate.sql

