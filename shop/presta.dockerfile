FROM prestashop/prestashop:1.7.8

COPY ./shop/certs/* /etc/ssl
COPY ./config/default-ssl.conf /etc/apache2/sites-available

RUN rm -rf /var/www/html
COPY --chown=www-data:www-data --chmod=755 ./shop/src/ /var/www/html

RUN a2enmod ssl && a2ensite default-ssl
