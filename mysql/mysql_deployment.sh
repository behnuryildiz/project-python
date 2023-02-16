#!/bin/bash

#firstly created the mysql based container with own appointed env datas
docker build -t my-mysql-image .

#creation of a new bridge network to be connected by mysql and python-api app contaieners
docker network create api-network

#the main mysql service and client system must be stopped in order to make the default port 3306 free
sudo service mysql stop

#secondly created the mysql container with own created mysql-image
docker run -dp 3306:3306 --name mysql-container --network api-network -v mysql_data:/var/lib/mysql my-mysql-image
sleep 3

# creation of table
docker exec -it mysql-container /bin/bash -c "mysql -u root -p <docker-entrypoint-initdb.d/table.sql "
docker exec -it mysql-container /bin/bash -c "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password'; "
docker exec -it mysql-container /bin/bash -c "FLUSH PRIVILEGES; "
#after creating of my-mysql-container we'll be able to execute this container with that following command line:
#docker exec -it mysql-container bash

