#!/flask/Scripts/Python
# -*- coding: utf-8 -*-
#数据库迁移脚本
import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URL
from config import SQLALCHEMY_MIGRATE_REPO
migration = SQLALCHEMY_MIGRATE_REPO + '\\version\\%03d_migration.py' % (api.db_version(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO) + 1)
tmp_module = imp.new_module('old_model')
old_model = api.create_model(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO)
exec old_model in tmp_module.__dict__
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO,tmp_module.meta,db.metadata)
open('migration',"wb").write(script)            #open后面两个参数都要加引号
api.upgrade(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO)
print 'New migration saved as' + migration
print 'Current database version:' + str(api.db_version(SQLALCHEMY_DATABASE_URL,SQLALCHEMY_MIGRATE_REPO))