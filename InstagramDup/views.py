# -*- encoding=UTF-8 -*-

"""
视图文件
"""
from InstagramDup import app
from flask import render_template,redirect
from models import Image,User
from sqlalchemy import text
@app.route('/')
def index():
    images=Image.query.order_by(text('id asc')).limit(10).all()#选10张图片传进模板
    return render_template('index.html',images=images)#渲染模板index.html

@app.route('/image/<int:image_id>/')
def image(image_id):
    image=Image.query.get(image_id)
    if image==None:
        return redirect('/')
    return render_template('pageDetail.html',image=image)

@app.route('/profile/<int:user_id>/')
def profile(user_id):
    user=User.query.get(user_id)
    if user==None:
        return redirect('/')
    return render_template('profile.html',user=user)