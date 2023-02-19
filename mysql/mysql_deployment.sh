#!/bin/bash

#firstly created the mysql based container with own appointed env datas
docker build -t my-mysql-image .

#creation of a new bridge network to be connected by mysql and python-api app contaieners
docker network create api-network


#the main mysql service and client system must be stopped in order to make the default port 3306 free
service mysql stop

#secondly created the mysql container with own created mysql-image
docker run -ti -p 3306:3306 --name mysql-container --network api-network -v mysql_data:/var/lib/mysql my-mysql-image bash

docker exec -it mysql-container bash -c "apt-get update && apt-get install mysql-client"

# creation of table
#docker exec -it mysql-container /bin/bash -c "mysql -u root -pPassword <./table.sql "

