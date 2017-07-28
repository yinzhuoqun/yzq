#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'


#需要安装 pip install pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# from pyftpdlib.handlers import ThrottledDTPHandler #下载速度限制

from pyftpdlib.servers import ThreadedFTPServer #多线程
# from pyftpdlib.servers import MultiprocessFTPServer #多进程,3.x貌似去掉了

import socket, os

def main(user,password,ftppath=".",port=21):
    #新建一个用户组
    authorizer = DummyAuthorizer()
    
    #将用户名，密码，用户访问指定目录，权限 添加到里面，当目录用"."表示.py文件当前所在的目录
    authorizer.add_user(user, password, ftppath, perm="elr") #elr只读,perm="elradfmw",windows 路径用 /
    # authorizer.add_user(user, password, ftppath, perm="elradfmw") #全部权限elradfmw
    
    #这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
    authorizer.add_anonymous(ftppath) #windows 路径用 /
    
    #下载速度限制
    # dtp_handler = ThrottledDTPHandler
    # dtp_handler.read_limit = 30720  # 30 Kb/sec (30 * 1024)
    # dtp_handler.write_limit = 30720  # 30 Kb/sec (30 * 1024)
       
    #头部
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "pyftpdlib based ftpd ready."
    
    #ssl 认证
    handler.tls_control_required = True
    handler.tls_data_required = True
    
    #开启服务器
    ip = socket.gethostbyname(socket.gethostname()) # 获取本机ip地址
    # server = FTPServer((ip, 21), handler) #ip、端口、协议
    
    server = ThreadedFTPServer((ip, port), handler) # 多线程
    # server = MultiprocessFTPServer((ip, 21), handler) #多进程，多进程,3.x貌似去掉了
    
    #连接数
    server.max_cons = 48 #ip连接总数
    server.max_cons_per_ip = 3 #每个ip连接总数  
    
    server.serve_forever() #一直打开
    
if __name__ ==  "__main__": 
    user = "root"
    password= "root123456"
    ftppath = "I:/yzq/work/apktest" # windows 路径用 / ，路径不能有下划线，目录用"."表示.py文件当前所在的目录
    # ftppath = os.getcwd() # windows 路径用 / ，路径不能有下划线，目录用"."表示.py文件当前所在的目录
    # ftppath = "."
    
    ftppath= 'I:/yzq'
    main(user,password,ftppath)