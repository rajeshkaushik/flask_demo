from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    api = Api(app)
    from polls import poll_ns
    api.add_namespace(poll_ns)

    db.init_app(app)
    return app
