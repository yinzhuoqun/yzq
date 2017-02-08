#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'
__version__ = 'v1.1.20161118'


import os, json


json_filename = 'http_server_path.txt' #变量保存文件
port_oray = '9000' #本人花生壳端口


def info_input():
    """
    输入数据并序列化
    """
    start_path = input(u'请输入开启 http 下载服务器的目录:\n').strip()
    while os.path.exists(start_path) == False and len(start_path) != 0:
        start_path = input(u'您输入的目录不存在,请输入开启 http 下载服务器的目录:\n').strip()
        
    if len(start_path) == 0:
        start_path = os.getcwd()
    
    input_str = '请输入 http 服务绑定的端口号（花生壳：%s）：\n' % port_oray
    port = input(input_str).strip()
    while port.isdigit() == False and len(port) != 0:
        port = input(input_str).strip()
    
    if len(port) == 0:
        port = port_oray #本人花生壳端口
        
    with open(json_filename,'w+') as f:
        start_path_d = {'start_path':start_path}
        start_path_d['port'] = port
        json.dump(start_path_d,f) # 载入文件
        
    return start_path_d
    

def json_load():
    """
    载入序列化的数据或重新输入数据
    """
    if os.path.exists(json_filename) == False:
        start_path_d = info_input()
    else:
        re_input = input(u'start httpserver, 需要重新输入信息吗(Y/N)？\n').strip()
        if re_input == 'N' or re_input == 'n' or len(re_input) == 0:
            
            with open(json_filename,'r') as f:
                start_path_d = json.load(f)
                start_path = start_path_d['start_path'] # 导出变量值
                port = start_path_d['port'] # 导出变量值
              
        else:
            
            if os.path.exists(json_filename) == True:           
                os.remove(json_filename)               
                start_path_d = info_input()
        
    return start_path_d

 
def httpserver_start(kw):
    """
    开启 http 服务
    """
    print(kw)
    
    if 'start_path' in kw.keys():
        try:
            path = kw['start_path']
        except Exception as e:
            print(e)
            path = os.getcwd()
        print('目录：%s' % path)
    
    if 'port' in kw.keys():
        try:
            port = kw['port']
        except Exception as e:
            print(e)
            port = '9000' # 本人花生壳端口
    # port = '9000' # 本人花生壳端口
      
    os.chdir(path)
    try:
        os.system('python -m http.server %s' % port) # 3.x
    except Exception as e:
        os.system('python -m SimpleHTTPServer %s' % port) # 2.x
            
     
if __name__ == '__main__':
    
     httpserver_start(json_load())