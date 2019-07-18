# -*- encoding=UTF-8 -*-
"""
脚本文件
"""
from InstagramDup import app,db
from sqlalchemy import  or_,and_
from flask_script import Manager
from InstagramDup.models import User,Image,Comment
import  random
manager=Manager(app)

def get_image_url():
    return  'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

@manager.command
def init_database():
    db.drop_all()#先删掉所有的表
    db.create_all()#把所有的表串接

    #插入
    for i in range(0,100):#添加100个用户
        db.session.add(User('User'+str(i+1),'a'+str(i)))
        for j in range(0,3):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,4):
                db.session.add(Comment('This is a comment'+ str(k),1+i*4+j,i+1))
    db.session.commit()#与git一样,事务需要提交

    #修改
    for i in range(50,100,2):
        user=User.query.get(i)
        user.username='[New1]'+user.username
    for i in range(51,100,2):
        User.query.filter_by(id=51).update({'username':'[New2]'})#常用的更新方法
    db.session.commit()#修改需要提交，查询不需要

    #删除
    for i in range(50,100,2):
        comment=Comment.query.get(i+1)
        db.session.delete(comment)
    db.session.commit()#删除需要提交，查询不需要
    #查询
    #print 1,User.query.all()#调用了__repr__()
    #print 2,User.query.get(3)
    #print 3,User.query.filter_by(id=5).first()
    #print 4,User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    #print 5,User.query.filter(User.username.endswith('0')).limit(3).all()
    #print 6,User.query.filter(or_(User.id==88,User.id==99)).all()#去掉all()会打印sql语句
    #print 7,User.query.filter(and_(User.id>88,User.id<94)).first_or_404()
    #print 8,User.query.filter(and_(User.id>88,User.id<94)).all()
    #print 9,User.query.paginate(page=1,per_page=10).items#分页显示
    #user=User.query.get(1)
    #print 10,user.images#一对多查询

    #image=Image.query.get(1)
    #print 11,image.user


if __name__=='__main__':
    manager.run()