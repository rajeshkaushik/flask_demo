from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from polls.v1.views import QuestionListApi, QuestionApi

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    api = Api(app)

    api.add_resource(QuestionListApi, '/questions')
    api.add_resource(QuestionApi, '/questions/<int:id>')

    return app
