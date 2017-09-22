#!/usr/bin/Python
# -*- coding: utf-8 -*-
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')          #当出现视图函数改变而页面没有改变的情况时看看资源管理器里是否有多个后台运行的python.py程序，关闭即可
def index():
    user = {'nickname':'jochen'}   #fake user
    posts = [
        {'author':{'nickname':'jochen'},
         'body':'beautiful day in shanghai'},
        {'author':{'nickname':'bob'},
         'body':'flask web'},
        {'author': {'nickname': 'jam'},
         'body': 'the movie was so cool!'},
        {'author': {'nickname': 'jack'},
         'body': 'is active'},
        {'author': {'nickname': 'lisa'},
         'body': 'scrapy'}
    ]
    return render_template("index.html",title = 'Home',user = user,posts = posts)


# def index():
#     user = {'nickname':'Miguel'}   #fake user
#     return'''
# <html>
#   <head>
#     <title>Home Page</title>
#   </head>
#   <body>
#     <h5>Hello,'''+user['nickname']+'''</h5>
#   </body>
# </html>
#   '''
@app.route('/article/<id>')
def article(id):
    return u'您请求的参数id为：%s' % id

