#!/bin/bash
# sudo chmod +x createdb.sh
# ./createdb.sh

# TODO Create DB from app: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/

# (check)
# sqlite3 data.db
# .schemas
# .tables
# .exit 

DBFILE=data.db    
if [ -f "$FILE" ]; then
   rm $DBFILE
fi

sqlite3 $DBFILE < schema.sql
sqlite3 $DBFILE < populate.sql
mv $DBFILE ..
