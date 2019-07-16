#-*- encoding=utf-8 -*-

def log(func):
    def wrapper(*args,**kwargs):
        print 'before calling',func.__name__
        func(*args,**kwargs)
        print'after calling',func.__name__
        return wrapper
@log
def hello(name):
    print "hello",name

if __name__=='__main__':
    hello('nowc')