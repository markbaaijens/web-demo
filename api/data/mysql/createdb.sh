#!/bin/bash
# sudo chmod +x createdb.sh
# ./createdb.sh

# (check)
# mysql -h localhost -u <user_name> -p
# Password: <password>
# show databases;
# use data;
# describe Books;
# show index from Books;
# use information_schema;
# select * from CHECK_CONSTRAINTS;
# exit

# TODO Create DB from app: https://www.w3schools.com/python/python_mysql_create_db.asp

user_name="debian-sys-maint"
password="OX2VZ4XPu8tVWHYx"

mysql -h localhost -u $user_name -p$password < schema.sql
mysql -h localhost -u $user_name -p$password < populate.sql
