FROM prestashop/prestashop:1.7.8

RUN echo "<IfModule mod_ssl.c>\n\t<VirtualHost _default_:443>\n\t\tServerAdmin webmaster@localhost\n\t\tDocumentRoot /var/www/html\n\n\t\tErrorLog \${APACHE_LOG_DIR}/error.log\n\t\tCustomLog \${APACHE_LOG_DIR}/access.log combined\n\n\t\tSSLEngine on\n\t\tSSLCertificateFile /etc/ssl/localhost.crt\n\t\tSSLCertificateKeyFile /etc/ssl/localhost.key\n\t\t<FilesMatch \"\\.(cgi|shtml|phtml|php)\$\">\n\t\t\tSSLOptions +StdEnvVars\n\t\t</FilesMatch>\n\t\t<Directory /usr/lib/cgi-bin>\n\t\t\tSSLOptions +StdEnvVars\n\t\t</Directory>\n\t\t<Directory /var/www/html>\n\t\t\tAllowOverride All\n\t\t</Directory>\n\t</VirtualHost>\n</IfModule>" > /etc/apache2/sites-available/default-ssl.conf
RUN a2enmod ssl
RUN a2ensite default-ssl
