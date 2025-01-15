FROM mysql:9

COPY ./../../../shop/dbdump/dump-mysql9.sql /docker-entrypoint-initdb.d/