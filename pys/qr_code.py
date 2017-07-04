#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

Write_Python_version = '3.4.3'
from platform import python_version
import re, time


# 输入==号间隔线
def out_eq():
    out_eq_count = 17
    print('=' * out_eq_count)


# 判断python版本
def version_status():
    writelist = re.split('\D', Write_Python_version)  # print(writelist)
    Write_version = writelist[0]  # print(Write_version)
    Currentlist = re.split('\D', python_version())  # print(Currentlist)
    Current_version = Currentlist[0]  # print(Current_version)
    if Current_version != Write_version:
        print(u'Python 版本不兼容!')
        time.sleep(3)
        return 0
    else:
        return 1


run = version_status()
if run == 1:
    import os, time
    import qrcode

    if os.name == 'nt':
        os.system('color 02')
    print('Author:yinzhuoqun\n')
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1
    )

    data = ''
    while len(data) == 0:
        data = input('请输入需要转换成二维码的内容：\n')
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    # set图片输出路径方式
    ImgOutputPath = 1
    if ImgOutputPath == 1:
        pwd = os.path.join(os.path.expanduser("~"), "Desktop")  # 保存至桌面
    elif ImgOutputPath == 2:
        pwd = input('请输入二维码保存的路径：\n')
        while os.path.exists(pwd) == False:
            pwd = input('请输入二维码保存的路径：\n')
            # pwd='C:/Users/lifeix/Desktop'  #手动输入路径，windows用 /左斜杠
    elif ImgOutputPath == 3:
        pwd = os.getcwd()  # 保存至当前运行路径

    os.chdir(pwd)
    t = time.strftime("%Y%m%d%H%M%S")
    ImgName = "YourWant_qrcode%s.png" % t
    ImgPath = os.path.join(pwd, ImgName)
    img.save(ImgName)  # print(ImgPath)
    if os.path.exists(ImgPath) == True:
        print('文件保存的路径是：%s，文件名称是：%s' % (pwd, ImgName))
    time.sleep(5)
