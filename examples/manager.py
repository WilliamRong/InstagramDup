#-*- encoding=UTF-8 -*-
from flask_script import  Manager
from flaskTest import app

manager=Manager(app)

@manager.command
def hello(name):
    print 'hello',name

@manager.command
def initialize_database():
   'initialze database'
    print 'database ..'
if __name__=='__main__':
    manager.run()