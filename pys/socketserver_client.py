# coding:utf-8

import os
import json
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 实例化一个TCP 的 socket对象
sock.connect(("127.0.0.1", 8000))  # 进行连接
sock.send("hello I am your client".encode())  # 向服务端打招呼

responseHander = sock.recv(128).decode()  # 接收文件的头部
print('server hander dict : %s' % responseHander)

responseHander = json.loads(responseHander)
file_receive_name = responseHander['name']
file_name = os.path.splitext(file_receive_name)[0]
file_attr = os.path.splitext(file_receive_name)[1]
print(file_name, file_attr)


# sock.send(requestHeader)

if responseHander == "no file to send":
    pass
else:
    requestHeader = {
        "method": "get",
        "name": responseHander["name"]
    }
    requestHeader = json.dumps(requestHeader)

    sock.send(requestHeader.encode())  # 发送请求的头部
    # if responseHander[u"method"] == u"get":

    time_now_strf = time.strftime('%Y%m%d%H%M%S')
    file_local_name = file_name + '_' + time_now_strf + file_attr
    print(file_local_name)
    f = open(file_local_name, "ab+")
    # 假使我们每次只接受512
    file_size = responseHander[u"size"]
    down_num = file_size / 512.0
    if int(down_num) == down_num:
        pass
    else:
        down_num = int(down_num) + 1
    for i in range(down_num):
        print(i)
        data = sock.recv(512).decode()  # 接收文件的正文，并且转存
        print(data + "+++")
        f.write(data)
    f.close()
    # recvContent = sock.recv(512)
    # print(recvContent+"0000")

sock.close()

# 1、因为文件不存在导致逻辑错误
# json 模块在有字符串转换为字典或者回转的过程当中，对一部分编码是不支持的。utf-8 + 无BOM
# Windows
