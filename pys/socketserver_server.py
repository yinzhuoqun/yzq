#coding:utf-8

import os
import json
import time
import threading
try:
    import socketserver
except Exception as e:
    import SocketServer as socketserver #as 启用别名,有利于代码的一致性


#BaseRequestHandler 是所有handel的父类
#StreamRequestHandler 是重写BaseRequestHandler从写得来的用于TCP协议的headel

class MyHandel(socketserver.BaseRequestHandler):#重写出属于我们的handel
    def setup(self):
        self.isExist = os.path.exists(path) #用os模块来判断文件是否存在
        print("%s:%s is connected"%self.client_address) #打印客户端的信息(ip port)

    def handle(self):
        clientStatus = self.request.recv(128).decode() # 接收
        print(clientStatus) #打印客户端的状态

        if self.isExist:
            #如果文件存在，就打开文件，并且向客户端发送文件头部
            self.file = open(path)
            self.request.sendall(self.__fileHeader().encode())
        else:                                                 #发送
            #如果文件不存在，我们就通知客户端文件不存在
            self.request.sendall("no file to send")

        requestHander = self.request.recv(128).decode() # 接收客户端发回的请求头 接收
        print(requestHander)
        if requestHander:
            #如果请求头有东西就发送文件正文
            self.request.sendall(self.file.read().encode()) #发送
        else:
            pass
    def finish(self):
        #关闭文件
        self.file.close()
        print("%s:%s is done" % self.client_address)

    def __fileHeader(self):
        #只是一个私有方法
        nameSplit = path.rsplit(os.path.sep, 1)
        if len(nameSplit) > 1:
            fileName = nameSplit[1]
        else:
            fileName = nameSplit[0]
        hander = {
            "method": "put",
            "name": fileName,
            "size": os.path.getsize(path),
            "data": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "code": "utf-8"
        }
        jsonData = json.dumps(hander)
        return jsonData

class MyServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass



if __name__ == '__main__':
    # path = "1.txt"  # sys.argv 表示命令行参数
    path = "1.png"  # sys.argv 表示命令行参数
    m = MyServer(("127.0.0.1",8000),MyHandel)
    th = threading.Thread(target=m.serve_forever,args=())
    th.start()