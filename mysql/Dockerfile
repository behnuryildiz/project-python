# Use the official MySQL image as the base image
FROM mysql:5.6

WORKDIR /docker-entrypoint-initdb.d/

# Copy the custom mySQL file to the container
COPY ./init.sql /docker-entrypoint-initdb.d/

# Set the root password
ENV MYSQL_ROOT_PASSWORD="Password" 
ENV MYSQL_USER="root"
ENV MYSQL_USER_PASSWORD="Password"

EXPOSE 3306


#CMD /etc/init.d/mysql start && mysql -u root -p${MYSQL_ROOT_PASSWORD} < /docker-entrypoint-initdb.d/init.sql
