from app.config import SQLALCHEMY_URI_KEY_NAME

from flask_sqlalchemy import SQLAlchemy


def setup_db(app, uri):
    app.config[SQLALCHEMY_URI_KEY_NAME] = uri
    return SQLAlchemy(app)
