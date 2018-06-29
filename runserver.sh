#!/bin/bash
cd /appl/flask_demo/project
export DATABASE_URL='mssql+pyodbc://SA:2tr0ngpassw0rd!@172.20.11.76:1433/flask_demo?driver=ODBC+Driver+17+for+SQL+Server'
nohup gunicorn -b 0.0.0.0:8000 run:app > ../logs/gunicorn.log
