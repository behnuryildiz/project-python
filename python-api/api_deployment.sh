#!/bin/bash

docker build -t my-python-app .

docker run -dp 5000:5000 --name my-app-container --network api-network my-python-app

docker ps -a
