#!/usr/Scripts/Python
# -*- coding: utf-8 -*-
#数据库升级脚本
from migrate .versioning import api
from config import SQLALCHEMY_DATABASE_URL
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO)
print"Current database version:" + str(api.db_version(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO))
