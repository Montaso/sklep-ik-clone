#!/bin/bash

echo "running entrypoint..."

DB_USER="root"
DB_PASS="student"
DB_NAME="BE_193237"
DB_HOST="admin-mysql_db"

DUMP_FILE="/usr/dump.sql"
if [ ! -f "$DUMP_FILE" ]; then
    echo "Error: Dump file $DUMP_FILE not found."
    exit 1
fi

echo "running query..."

RESULT=$(mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASS" -D "$DB_NAME" -se \
"SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = '$DB_NAME' AND TABLE_NAME = 'ps_shop_url';")

echo "SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_SCHEMA = '$DB_NAME' AND TABLE_NAME = 'ps_shop_url'; returned: $RESULT"

if [ "$RESULT" == "ps_shop_url" ]; then
    echo "Table ps_shop_url exists in the database $DB_NAME."
    echo "Skipping datbase seed..."
else
    echo "loading db dump..."
    mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" < "$DUMP_FILE"
    echo "loaded db dump"
fi

echo "starting apache2 server..."
exec apache2-foreground
