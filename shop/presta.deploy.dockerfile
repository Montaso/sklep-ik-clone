FROM prestashop/prestashop:1.7.8

COPY ./shop/dbdump/dump.sql /usr/dump.sql
COPY ./shop/presta-entrypoint.sh /usr/entrypoint.sh

COPY ./shop/certs/* /etc/ssl
COPY ./config/default-ssl.conf /etc/apache2/sites-available
COPY ./shop/src /var/www/html

RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html \
    && a2enmod ssl \
    && a2ensite default-ssl
