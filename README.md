# flask_demo
Sample flask project with docker and gunicorn

# Environment variables
These are the environement variables that are required for the app to function correctly. Add these to a `.env` file:

    DB_USER=<user>
    DB_PASS=<password>
    DB_HOST=mssqldev
    DB_PORT=1433
    DB_NAME=flask_demo

    APP_HOST=0.0.0.0
    APP_PORT=8000

    MSSQL_SA_PASSWORD=<password>

# Deploying with docker

1. Create network

        docker network create mynet

2. Create and run application

        docker build -t flask_demo:1 .
        docker run --net mynet --name flask_demo --env-file .env -d -p 8000:8000 flask_demo:1

3. Create and run MS SQL Server

        docker build -t mssql -f Dockerfile-MSSQL .
        docker run --net mynet --name mssql --env-file .env -d -p 1433:1433 mssql

    If the image runs, use the following commands to create the database:

        docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P <password>
        > create database flask_demo
        > go


# Code quality

Running Flake 8:

    flake8

Run tests

    pytest

Generating Code coverage

    coverage run -m pytest
    coverage report