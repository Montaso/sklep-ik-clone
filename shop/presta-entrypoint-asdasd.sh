#!/bin/bash

echo "running entrypoint..."

echo "loading db dump..."
mysql -hadmin-mysql_db -uroot -pstudent BE_193237 < /usr/dump.sql
echo "loaded db dump"

echo "starting apache2 server..."
exec apache2-foreground
