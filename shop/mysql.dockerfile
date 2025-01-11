FROM mysql:9

COPY ./dbdump/dump.sql /docker-entrypoint-initdb.d/