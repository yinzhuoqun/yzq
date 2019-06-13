#!/usr/bin/env python3
#coding:utf-8
import os,re
from time import sleep

#导出设备列表
def dlist():
    DevicesInfo=os.popen('adb devices')
    DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
    DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
    return DevicesList

# 启动APP
def startAPP(device, packageName, startActivityName):
    startAPP = 'adb -s %s shell am start -n %s/%s' % (device, packageName, startActivityName)
    os.system(startAPP)
    
deviceslist=dlist()
if len(deviceslist)!=0:
    if os.name=='nt':
        os.system('color 02')#只在windows可用

    #packagename=input('please input packagename and press ENTER:\n');packagename=packagename.strip()
    # packagename='com.lexiangquan.supertao'	#set packagename设置包名后可一键卸载
    # packagename='com.qmsh.hbq'	#set packagename设置包名后可一键卸载
    packagename='com.sandianji.sdjandroid'	#set packagename设置包名后可一键卸载

    print('you have devices:%s'%len(deviceslist))
    print('clearing packagename: %s'%packagename)
    if len(deviceslist)==1:
        #print('clearing packagename: %s'%packagename)
        device=deviceslist[0]
        print('devicename:',device)
        clear='adb -s %s shell pm clear %s'%(device,packagename)
        os.system(clear)
    elif len(deviceslist)!=1:
        db_devices={}
        number=1
        for device in deviceslist:
            db_devices[number]=device
            number+=1
        print('dict_devices:',db_devices)
        device_num=input('Please choose device number from dict_devices:')
        if 	len(device_num)==0 or device_num>str(len(db_devices)):
            print('(You choice all devices)')
            #print('clearing packagename: %s'%packagename)
            for device in deviceslist:
                print('devicename:',device)
                clear='adb -s %s shell pm clear %s'%(device,packagename)
                os.system(clear)
        elif device_num<=str(len(db_devices)):
            device=db_devices[int(device_num)]
            #print('clearing packagename: %s'%packagename)
            print('devicename:',device)
            clear='adb -s %s shell pm clear %s'%(device,packagename)
            os.system(clear)
    #清除后打开app
    for device in deviceslist: #批量
        if packagename == 'com.l99.bed':
            startActivityName = 'com.l99.WelcomActivity'
            startAPP(device, packagename, startActivityName)
    
    sleep(3)
else:
    if os.name=='nt':
        os.system('color 0C')
    print('error: device not found')
    sleep(3)