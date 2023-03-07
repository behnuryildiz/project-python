#!/bin/bash

#firstly created the mysql based container with own appointed env datas
#docker build -t my-mysql-image .

#creation of a new bridge network to be connected by mysql and python-api app contaieners
docker network create api-network

#stop the local running mysql-server
service mysql stop


#the main mysql service and client system must be stopped in order to make the default port 3306 free
#service mysql stop
sleep 5
#secondly created the mysql container with own created mysql-image
docker run -di -p 3306:3306 --name mysql-container --network api-network -v mysql_data:/var/lib/mysql mysql:5.6 bash 


docker exec -id mysql-container bash -c "service mysql start"

sleep 15

docker cp ./init.sql mysql-container:/docker-entrypoint-initdb.d/

docker exec -it mysql-container bash -c 'mysql -u root< /docker-entrypoint-initdb.d/init.sql'

#/etc/init.d/mysql start && 
