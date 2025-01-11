FROM prestashop/prestashop:1.7.8

COPY ./certs/* /etc/ssl
COPY ../config/default-ssl.conf /etc/apache2/sites-available

RUN a2enmod ssl
RUN a2ensite default-ssl
