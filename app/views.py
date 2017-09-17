#!/usr/bin/Python
# -*- coding: utf-8 -*-
from app import app

@app.route('/')
@app.route('/')
def index():
    return"hello,world"