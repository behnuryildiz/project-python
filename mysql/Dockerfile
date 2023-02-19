# Use the official MySQL 8.0 image as the base image
FROM mysql:latest

WORKDIR /docker-entrypoint-initdb.d/

# Copy the custom mySQL file to the container
COPY ./init.sql .

# Set the root password
ENV MYSQL_ROOT_PASSWORD="Password" 
#ENV MYSQL_USER="user"
#ENV MYSQL_USER_PASSWORD="Password"

EXPOSE 3306

CMD ["mysql", "./init.sql"]