# -*- encoding=UTF-8 -*-

"""
模型文件
"""
from InstagramDup import db
from datetime import  datetime
import random

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content=db.Column(db.String(1024))
    image_id=db.Column(db.Integer,db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status=db.Column(db.Integer,default=0)#0正常 1被删除
    user=db.relationship('User')#与user表关联

    def __init__(self, content, image_id,user_id):
        self.content = content
        self.image_id=image_id
        self.user_id = user_id


    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url=db.Column(db.String(512))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    created_date=db.Column(db.DateTime)
    comments=db.relationship('Comment')


    def __init__(self,url,user_id):
        self.url=url
        self.user_id=user_id
        self.created_date=datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)

class User(db.Model):
    #__tablename__='user'#可以命名，需要更改其他语句中的表名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(80),unique=True)
    password=db.Column(db.String(32))
    head_url=db.Column(db.String(256))
    images=db.relationship('Image',backref='user',lazy='dynamic')#这样image就能查到user了


    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.head_url='http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'
        #牛客网上随机抓图作为头像

    def __repr__(self):
        return '<User %d %s>'%(self.id,self.username)