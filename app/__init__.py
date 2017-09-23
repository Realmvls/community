#!flask/Scripts/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy      #此处flask_sqlalchemy不能用flask.ext.sqlalchemy代替，后者这种写法已被废弃
import os


app = Flask(__name__)
app.config.from_object('config')
#先定义SQLALCHEMY_DATABASE_URL
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app.db')
db = SQLAlchemy(app)

from app import views,models