#!/usr/bin/Python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy      #此处flask_sqlalchemy不能用flask.ext.sqlalchemy代替，后者这种写法已被废弃


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views,models