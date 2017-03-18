#!/usr/bin/env python3

# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from flask import Flask
import os
# from flask import url_for
# from flask import abort
# from flask import redirect
# from flask import render_template
from flask import make_response

###访问静态文件脚本
#安装库 pip install flask
#脚本 和 static 同目录
#static 目录下放静态文件


app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

    
# @app.route('/apk')   
# def apk():
    # path = r'I:\yzq\MyPythonTest\static\app'
    # base_dir = os.path.dirname(__file__)
    #resp = make_response(open(os.path.join(base_dir, "apk")).read())
    # resp = make_response(open(path).read())
    #resp.headers["Content-type"]="application/json;charset=UTF-8"
    # return resp
    
  

if __name__ == '__main__':
    app.debug = True  # 调试模式，修改文件会重新启动
    # app.run(host='0.0.0.0',port =9000,debug=True) # 0.0.0.0 监听所有公网 IP
    app.run(host='0.0.0.0', port=8000)  # 0.0.0.0 监听所有公网 IP

