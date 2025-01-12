FROM prestashop/prestashop:1.7.8

COPY ./shop/certs/* /etc/ssl
COPY ./config/default-ssl.conf /etc/apache2/sites-available
COPY ./shop/src /var/www/html

RUN chown -R www-data:www-data /var/www/html \
    && chmod -R 755 /var/www/html \
    && a2enmod ssl \
    && a2ensite default-ssl
