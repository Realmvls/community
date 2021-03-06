# -*- coding: utf-8 -*-
#!flask/Scripts/python
#创建数据库的脚本
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URL
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO,api.version(SQLALCHEMY_MIGRATE_REPO))
