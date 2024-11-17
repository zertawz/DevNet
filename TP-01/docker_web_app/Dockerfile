FROM php:7-apache
# Installer des logiciel à l'aide d'apt-get
RUN apt-get update && apt-get install -y libpng-dev curl libcurl4-openssl-dev
# Ajoute l'extension pdo_mysql avec les outils docker
RUN docker-php-ext-install pdo_mysql gd
# Activer le module rewrite dans apache
RUN a2enmod rewrite
RUN service apache2 restart
# Donner un nom au serveur
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
# Pour intégrer le dossier de votre site web directement dans l'image
COPY index.php /var/www/html