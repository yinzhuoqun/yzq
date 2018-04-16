#!/usr/bin/env python3
# coding:utf-8
'''
author:yinzhuoqun
python version:3.4.2
'''
import os, re
from time import sleep


def dlist():
    DevicesInfo = os.popen('adb devices')
    DevicesInfo = DevicesInfo.read();  # print(DevicesInfo)
    DevicesList = re.findall(r'(.*?)\tdevice\b', DevicesInfo)
    return DevicesList


if os.name == 'nt':
    os.system('color 02')

print('author:yinzhuoqun\n')

deviceslist = dlist()
if len(deviceslist) != 0:
    package_names = {"1": {"超级淘": "com.lexiangquan.supertao"},
                     "2": {"超级淘PRO": "com.chaojitao.star"},
                     "3": {"千米红包": "com.qmsh.hbq"},
                     "4": {"微信": "com.tencent.mm"},
                     }
    input_msg = "输入"
    for key, value in package_names.items():
        input_msg += " %s 卸载 %s，" % (key, "".join([key for key, value_sub in value.items()]))
    packagename = input('{package_name_msg}其他请输入包名：'.format(package_name_msg=input_msg))
    packagename_num = packagename.strip()  # 去掉首尾空格
    if packagename_num in package_names.keys():
        packagename = "".join([value_sub for key, value_sub in package_names[packagename_num].items()])

    # 设置包名后可一键卸载
    # packagename='com.yzq.meid'	#printMeid
    # packagename='com.qzone'	#qq空间

    packagename = packagename.strip()
    if len(packagename) == 0:  # 设置默认包名
        packagename = "com.qmsh.hbq"
    print('uninstall packagename: %s' % packagename)

    if len(deviceslist) == 1:
        # print('uninstalling packagename: %s'%packagename)
        device = deviceslist[0]
        print('devicename:', device)
        uninstall = 'adb -s %s uninstall %s' % (device, packagename)
        os.system(uninstall)
    elif len(deviceslist) != 1:
        db_devices = {}
        number = 1
        for device in deviceslist:
            db_devices[number] = device
            number += 1
        print('dict_devices:', db_devices)
        run = input('please choose device number from dict_devices:')
        while len(re.findall(r'\D', run)) != 0:
            run = input('please choose device number from dict_devices:')
        if len(run) == 0 or int(run) > len(db_devices):
            print('(You choice all devices)')
            # print('uninstalling packagename: %s'%packagename)
            for device in deviceslist:
                print('devicename:', device)
                uninstall = 'adb -s %s uninstall %s' % (device, packagename)
                os.system(uninstall)
        elif int(run) <= len(db_devices):
            device = db_devices[int(run)]
            print('uninstall packagename: %s' % packagename)
            print('devicename:', device)
            uninstall = 'adb -s %s uninstall %s' % (device, packagename)
            os.system(uninstall)
    sleep(3)
else:
    if os.name == 'nt':
        os.system('color 0C')
    print('error: device not found')
    sleep(5)
