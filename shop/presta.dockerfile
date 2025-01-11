FROM prestashop/prestashop:1.7.8

COPY ./shop/certs/* /etc/ssl
COPY ./config/default-ssl.conf /etc/apache2/sites-available
COPY ./shop/src /var/www/html

RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 755 /var/www/html

RUN a2enmod ssl
RUN a2ensite default-ssl