import os

class Config(object):
    SQLITE_FILE_NAME = 'data/data.db'
    LOG_FILE_NAME = 'logs/app.log'
    LOG_MAX_SIZE = 10240000
    LOG_BACKUP_COUNT = 10

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'debian-sys-maint'
    MYSQL_PASSWORD = 'OX2VZ4XPu8tVWHYx'
    MYSQL_DATABASE = 'data'
    
