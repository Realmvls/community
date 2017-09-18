#!/usr/bin/Python
# -*- coding: utf-8 -*-
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


from app import views