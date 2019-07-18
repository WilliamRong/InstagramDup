# -*- encoding=UTF-8 -*-

"""
视图文件
"""
from InstagramDup import app
from flask import render_template
from models import Image,User
from sqlalchemy import text
@app.route('/')
def index():
    images=Image.query.order_by(text('id desc')).limit(10).all()#选10张图片传进模板
    return render_template('index.html',images=images)#渲染模板index.html