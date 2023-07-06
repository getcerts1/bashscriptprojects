#!/bin/bash

apt update

apt install apache2 -y

apt install mysql-server -y

mysql_secure_installation 

apt install php libapache2-mod-php php-mysql -y

service apache2 restart

