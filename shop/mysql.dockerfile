FROM mysql:9

COPY ./shop/dbdump/dump.sql /docker-entrypoint-initdb.d/