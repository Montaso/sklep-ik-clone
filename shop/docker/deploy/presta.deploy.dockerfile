FROM prestashop/prestashop:1.7.8

COPY ./shop/dbdump/dump.sql /usr/dump.sql
COPY ./shop/certs/* /etc/ssl

COPY ./config/default-ssl.conf /etc/apache2/sites-available
COPY ./config/presta-deploy-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh && rm -rf /var/www/html

COPY --chown=www-data:www-data --chmod=755 ./shop/src/ /var/www/html
COPY --chown=www-data:www-data --chmod=755 ./config/parameters.deploy.php /var/www/html/app/config/parameters.php

RUN a2enmod ssl && a2ensite default-ssl
