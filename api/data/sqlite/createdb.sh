#!/bin/bash
# sudo chmod +x createdb.sh
# ./createdb.sh

DBFILE=data.db    
if [ -f "$FILE" ]; then
   rm $DBFILE
fi

sqlite3 $DBFILE < schema.sql
sqlite3 $DBFILE < populate.sql
mv $DBFILE ..
