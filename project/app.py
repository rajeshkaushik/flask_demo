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

from polls.v1.views import QuestionListApi, QuestionApi
from polls.v1.restplus_views import UsersApi

api.add_resource(QuestionListApi, '/questions')
api.add_resource(QuestionApi, '/questions/<int:id>')

api.add_resource(UsersApi, '/users')
