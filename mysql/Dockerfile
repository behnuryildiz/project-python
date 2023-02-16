# Use the official MySQL 8.0 image as the base image
FROM mysql:8.0

# Set the root password
ENV MYSQL_ROOT_PASSWORD="Password" 
ENV MYSQL_USER="user"
ENV MYSQL_USER_PASSWORD="Password"

# Copy the custom SQL file to the container
COPY table.sql /docker-entrypoint-initdb.d/

