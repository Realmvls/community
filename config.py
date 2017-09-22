#!/usr/bin/Python
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'you_will_never_guess'

OPENID_PROVIDERS = [
    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://me.yahoo.com'},
    {'name':'AOL','url':'https://openid.aol.com/<username>'},
    {'name':'Flickr','url':'https://www.flickr.com/<username>'},
    {'name':'MyOpenID','url':'https://www.myopenid.com'}
]

