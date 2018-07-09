import os

from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config


app = Flask(__name__)
config_name = os.getenv('APP_SETTINGS', 'development')
app.config.from_object(app_config[config_name])

db = SQLAlchemy()
db.init_app(app)
api = Api(app)

from polls import poll_ns

api.add_namespace(poll_ns)
