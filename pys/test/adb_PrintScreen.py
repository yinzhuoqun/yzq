#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'
__version__ = 'v1.1.20170306'

from platform import python_version  # 导入当前运行的python版本号
import re, os, time, json
import threading

import win32con
import win32clipboard as clipboard


def get_clipboard_text():
    """
    获取剪切板的数据
    """
    clipboard.OpenClipboard()
    clipboard_text = clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    clipboard.CloseClipboard()

    return clipboard_text


def set_clipboard_text(istr):
    """
    设置剪切板的数据
    """
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, istr)
    clipboard.CloseClipboard()


try:
    from PIL import Image

    pil_status = "pil_true"


except Exception as e:
    pil_status = "pil_false"
    print(e)


def out_eq():
    out_eq_count = 40
    print('=' * out_eq_count)


def version_status():
    Write_Python_version = '3.4.3'  # 编写脚本的python版本
    writelist = re.split('\D', Write_Python_version)  # print(writelist)
    Write_version = writelist[0]  # print(Write_version)
    Currentlist = re.split('\D', python_version())  # print(Currentlist)
    Current_version = Currentlist[0]  # print(Current_version)
    if Current_version != Write_version:
        print(u'Python 版本不兼容!')
        return 0
    else:
        return 1


# version=version_status()

def adb_devices():
    devices_info = os.popen('adb devices')
    devices_info = devices_info.read();  # print(devices_info)
    devices = re.findall(r'(.*?)\tdevice\b', devices_info)
    return devices


def find_unlock_apk(device, packagename):
    # 查找解锁屏幕的app是否存在
    apk_path_command = 'adb -s %s shell pm path %s' % (device, packagename)
    apk_path = os.popen(apk_path_command).read()
    apk_path_list = re.findall(r'package:(.+?.apk)', apk_path)
    if len(apk_path_list) != 0:
        return True
    else:
        return False


def stop_run():
    stop_run = input('请按ENTER键继续截图...\n')
    if len(stop_run) >= 0:
        pass


def find_no_int(str):
    no_int = re.findall(r'\D+', str)  # 判断str含有非数字的字符
    # print(no_int)
    if len(no_int) != 0:
        return True  # 找到非数字字符
    else:
        False  # 未找到非数字字符


# 截图到手机
def get_screen(deviceslist, sdcard_path):
    for device in deviceslist:
        screen_command = 'adb -s %s shell /system/bin/screencap -p %s' % (device, sdcard_path)
        print(screen_command)
        os.system(screen_command)


# 缩略图
def thumbnail(img):
    size = (480, 854)  # x,y
    img_n = os.path.splitext(img)[0] + ".png"
    try:
        img_s = Image.open(img)
        img_s.thumbnail(size)
        img_s.save(img_n, "PNG")

        return img_s

    except IOError:
        print("cannot create thumbnail for", img)

        return None


# 从手机复制到电脑
def screen_to_pc(deviceslist, pwd):
    picTimes = 1  # 初始化图片序号
    for device in deviceslist:
        # t=time.strftime("%m-%d_%H-%M-%S")	#格式化时间
        t = time.strftime("%Y%m%d%H%M%S")
        filename = '%s_%s.png' % (t, picTimes)
        pc_path = os.path.join(pwd, filename)
        pull_command = 'adb -s %s pull %s %s' % (device, sdcard_path, pc_path)
        try:
            os.system(pull_command)
        except Exception as e:
            print(e)
        else:
            if os.path.exists(pc_path) == True:
                print(pc_path)
                if pil_status == "pil_true":
                    thumbnail(pc_path)
                url_path = r"%s/%s/%s" % (django_upload_url, app_version, filename)
                set_clipboard_text(url_path)
                print(url_path)
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 图片保存至电脑桌面
                desktop_file = os.path.join(desktop_path, "url_path.txt")
                # with open(desktop_file,"a+") as f:
                with open(desktop_file, "w") as f:
                    f.seek(0, 0)
                    s_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(url_path)
            picTimes += 1  # 叠加图片序号防止重名


def pic_save_path_dump(pic_save_path):
    ##序列化PicSavaPath
    if os.path.exists('PicSavaPathTemp.txt') == False:
        with open('PicSavaPathTemp.txt', 'w') as PicSavaPathFile:
            dPicSavaFile = []
            dPicSavaFile.append(pic_save_path)
            json.dump(dPicSavaFile, PicSavaPathFile)
            # print('dump')


def pic_save_path_load():
    ##反序列化PicSavaPath
    if os.path.exists('PicSavaPathTemp.txt') == True:
        with open('PicSavaPathTemp.txt', 'r') as rePicSavaPathFile:
            rePicSavaPathFile = open('PicSavaPathTemp.txt', 'r')
            dPicSavaPath = json.load(rePicSavaPathFile)
            pic_save_path = dPicSavaPath[0]
            # print(pic_save_path)
            return pic_save_path


if os.name == 'nt':
    os.system('color 02')
print('Author Email: zhuoqun527@qq.com\n')

sdcard_path = r'/sdcard/screenshot.png'  # 设置图片在手机中保存的位置
app_version = '6.1.0'  # 图片保存目录
django_upload_url = "http://192.168.66.55/media/upload"
# pic_save_path = r'I:\91UserData\ScreenCapture'  # 设置图片在电脑中的文件夹
pic_save_path = r'I:\yzq\MyPythonTest\yzqProgram\media\upload\%s' % app_version  # 设置图片在电脑中的文件夹

if os.path.exists(pic_save_path) == False:
    try:
        os.mkdir(pic_save_path)
    except Exception as e:
        pic_save_path = os.path.join(os.path.expanduser("~"), "Desktop")  # 图片保存至电脑桌面

'''
if os.path.exists('PicSavaPathTemp.txt') == False:
	pic_save_path=input('请输入截图保存的路径:')
	while os.path.exists(pic_save_path)==False:
		pic_save_path=input('请输入截图保存的路径:')
	pic_save_path_dump(pic_save_path)	

pic_save_path=pic_save_path_load() #初始化图片保存的路径
'''

unlockPackagename = 'io.appium.unlock'
unlockActivity = '.Unlock'
unlock_switch = False  # 解锁屏幕开关，等于 False 不运行解锁的app
times1 = 1  # 初始化未连接设备时的时间

# while 1:

deviceslist = adb_devices()
if len(deviceslist) != 0:
    if os.name == 'nt':
        os.system('color 02')

    if len(deviceslist) <= 2:

        # 截图        
        get_screen(deviceslist, sdcard_path)
        time.sleep(0.5)
        # 导出图片到pc
        if len(deviceslist) == 1:
            screen_to_pc(deviceslist, pic_save_path)

        if len(deviceslist) == 2:

            db_devices = {}
            number = 1
            for device in deviceslist:
                db_devices[number] = device
                number += 1
            print('设备序号表：', db_devices)

            device_number = input(u'请从 <设备序号表> 中选择需要截图设备的序号：')
            while find_no_int(device_number) == True:
                device_number = input(u'请从 <设备序号表> 中选择需要截图设备的序号：')

            if len(device_number) == 0:
                print(u'（你选择了截图全部设备）')
                screen_to_pc(deviceslist, pic_save_path)

            # 指定设备
            elif device_number <= str(len(db_devices)):
                # 选择设备导出图片到pc
                device = db_devices[int(device_number)]
                deviceslist = [device]
                screen_to_pc(deviceslist, pic_save_path)
            elif device_number > str(len(db_devices)):
                print(u'（你放弃了截图）')
    if len(deviceslist) >= 3:
        db_devices = {}
        number = 1
        for device in deviceslist:
            db_devices[number] = device
            number += 1
        print('设备序号表：', db_devices)

        device_number = input(u'请从 <设备序号表> 中选择需要截图设备的序号：')
        while find_no_int(device_number) == True:
            device_number = input(u'请从 <设备序号表> 中选择需要截图设备的序号：')

        if len(device_number) == 0:
            print(u'（你选择了截图全部设备）')
            # 截图
            get_screen(deviceslist, sdcard_path)
            # 导出图片到pc
            screen_to_pc(deviceslist, pic_save_path)

        elif device_number <= str(len(db_devices)):
            # 生成新的deviceslist
            device = db_devices[int(device_number)]
            deviceslist = [device]
            # 对选定的设备截图
            get_screen(deviceslist, sdcard_path)
            # 导出图片到pc
            screen_to_pc(deviceslist, pic_save_path)
        elif device_number > str(len(db_devices)):
            print(u'（你放弃了截图）')

    times1 = 1  # 重置未连接设备时的时间
    # time.sleep(10)

# stop_run()	#再次运行

else:
    if os.name == 'nt':
        os.system('color 0C')
    import sys

    for i in range(3):
        time.sleep(1)  # 间隔1s
        if times1 <= 60:
            sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%ss]\r' % times1)
            sys.stdout.flush()
        else:
            a = int(times1 / 60)  # print('a',a)
            b = times1 % 60  # print('b',b)
            sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%smin%ss]\r' % (a, b))
            sys.stdout.flush()
        times1 += 1
