#-*- encoding=UTF-8 -*-

from flask import Flask,render_template,request,make_response

app=Flask(__name__)
app.jinja_env.line_statement_prefix= '#'
@app.route('/index/')
@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<uid>',methods=['Get','Post'])
def profile(uid):
    colors =('red','green','black')
    infos = {'i':'abc','j':'def'}
    return render_template('profile.html',uid=uid,colors=colors,infos=infos)

@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res=request.args.get('key','defaultkey')+'<br>'
    res=res+request.url+'++'+request.path+'<br>'
    for property in dir(request):
        res=res+str(property)+'|==|'+str(eval('request.'+property))+'<br>'
    response=make_response(res)
    response.set_cookie('nwid',key)
    response.status ='404'
    response.headers['myface']='hello my face~'
    return response


if __name__ =='__main__':
    app.run(debug=True)