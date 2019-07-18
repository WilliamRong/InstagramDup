# -*- encoding=UTF-8 -*-

"""
导出文件
"""
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
app=Flask(__name__)#创建app
app.config.from_pyfile('app.conf')#从app.conf中初始化设置
db=SQLAlchemy(app)#可以操作数据库了
from InstagramDup import views,models