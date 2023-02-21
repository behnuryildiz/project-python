# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt 

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for MySQL connection
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Password
ENV MYSQL_HOST=mysql
ENV MYSQL_DB=customer_data

# Expose the port on which the application runs
EXPOSE 5000


# Run the command to start the application
CMD ["python", "app.py"]
