import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_restful import Resource, Api
from boot import make_celery

app = Flask(__name__)

app.config.update(
DEBUG=True,
SECRET_KEY = 'cechceyFleshayffilethDulRysAfed0',
SQLALCHEMY_DATABASE_URI = "postgresql://radius:z5beMSt57r7h@192.168.100.58/radius",
SQLALCHEMY_TRACK_MODIFICATIONS = True,
CELERY_BROKER_URL = 'redis://192.168.100.58:6379/0',
CELERY_BACKEND = 'redis://192.168.100.58:6379/0'
)

#app.config.from_object('src.settings')
#app.config.from_envvar('AP_SETTINGS')

db = SQLAlchemy(app)
admin = Admin(app, name='accesspoint', template_mode='bootstrap3')
celery = make_celery(app)
api = Api(app)

import urls, models, views, modelviews
from tasks import add_together
