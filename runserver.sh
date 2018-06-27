#!/bin/bash
cd /appl/flask_demo/project

nohup gunicorn -b 0.0.0.0:8000 run:app > ../logs/gunicorn.log
