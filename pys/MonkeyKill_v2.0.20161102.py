# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'
__version__ = 'v2.0.20161102'


import os, re, time


# get devices
def get_devices():
    DevicesInfo = os.popen('adb devices')
    DevicesInfo = DevicesInfo.read();  # print(DevicesInfo)
    DevicesList = re.findall(r'(.*?)\tdevice\b', DevicesInfo)
    return DevicesList


# 查找数字，可以直接int，然后用except来确定是否是数字
def find_int(str):
    find_int = re.findall(r'\D+', str)  # \D找除数字之外的
    if len(find_int) != 0:
        return True  # 找到非数字字符
    else:
        return False  # 未找到非数字字符	


# ps moneky id
def get_ps_monkey_ids(device):
    ps_info = os.popen('adb -s %s shell ps' % device)
    ps_info = ps_info.read();  # print(ps_info)
    ps_monkeys = re.findall(r'[shell|root].*?com.android.commands.monkey', ps_info);  # print(ps_monkeys)
    return ps_monkeys


# devices_choice
def devices_choice():
    devices = get_devices()
    devices_choice = []
    if len(devices) != 0:
        if len(devices) > 1:
            print(u'你有设备：%s 台' % len(devices))
            db_devices = {}
            number = 1
            for device in devices:
                db_devices[number] = device
                number += 1
            # print(u'设备对应的序号表:', db_devices)
            for x in db_devices.keys():
                print('%s : %s'%(x,db_devices[x]))

            ###    devices_str
            devices_str = [str(x) for x in range(1, len(devices)+1)]
            devices_str = devices_str + ['a', 'A', '']
            ###

            device_number = input(u'请选择操作设备的序号(A|a为全部):\n')
            while device_number not in devices_str:
                device_number = input(u'请选择操作设备的序号(A|a为全部):\n')

            if device_number.isdigit():
                device = db_devices[int(device_number)]
                devices_choice.append(device)
                print(u'选中的设备名称：', device)
            else:
                print('提示：你选择了全部设备')
                devices_choice = devices


        elif len(devices) <= 1:
            device = devices[0]
            devices_choice.append(device)
            print(u'当前设备：', device)
    else:
        print('提示：没有连接的安卓设备')
        time.sleep(3)

    return devices_choice


# kill monkeyprocesss    
def moneky_kill(devices):
    for device in devices:
        print('操作设备：%s' % device)
        ps_monkeys = get_ps_monkey_ids(device)  # 所有 monkey 进程组成的列表
        # print(ps_monkeys)
        if len(ps_monkeys) > 0:
            for monkey_device in ps_monkeys:
                ps_reg = re.compile(r'\s+')
                monkey_ps_ids = ps_reg.split(monkey_device)  # 列表索引 1 的位置是 进程号
                monkey_ps_id = monkey_ps_ids[1]
                print('-- Monkey 进程号:', monkey_ps_id)

                os.system('adb -s %s shell kill %s'%(device,monkey_ps_id)) # 杀进程

                ps_monkeys = get_ps_monkey_ids(device)
                if len(ps_monkeys) == 0:
                    print('-- %s 进程号已结束 ' % monkey_ps_id )
                else:
                    print('-- 有新的 Monkey 进程')

        else:
            print('--提示：未发现 Monkey 运行')

        time.sleep(3)
        
        
if __name__ == '__main__':

    if os.name == 'nt':
        os.system('color 02')
    print('《 Kill Monkey Processes 》\n Author Email : zhuoqun527@qq.com\n')

    ### debug ###
    # print(get_devices())
    # print(get_ps_monkey_ids(get_devices()[0]))
    # print(devices_choice())

    ### run ###
    # kill > moneky ps > choice device > devices
    moneky_kill(devices_choice())
