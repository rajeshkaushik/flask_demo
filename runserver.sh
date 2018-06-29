#!/bin/bash
cd /appl/flask_demo/project
export DATABASE_URL='mssql+pyodbc://SA:2tr0ngpassw0rd!@172.20.16.19:1433/flask_demo'
nohup gunicorn -b 0.0.0.0:8000 run:app > ../logs/gunicorn.log
