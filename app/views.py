#!/usr/bin/Python
# -*- coding: utf-8 -*-
from app import app

@app.route('/')
def index():
    return"hello,world"

# @app.route('/article/<id>')          #url传参还没成功，标记一下
# def article(id):
#     return u'您请求的参数id为：%s' % id
