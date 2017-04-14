#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

Write_Python_version = '3.4.3'
from platform import python_version
import time, re, os, sys
import subprocess, threading


# 判断python版本
def versionStatus():
    writelist = re.split('\D', Write_Python_version)  # print(writelist)
    Write_version = writelist[0]  # print(Write_version)
    Currentlist = re.split('\D', python_version())  # print(Currentlist)
    Current_version = Currentlist[0]  # print(Current_version)
    if Current_version != Write_version:
        print(u'author:yinzhuoqun\n\nPython 版本不兼容!')
        time.sleep(3)
        return 0
    else:
        return 1


# 获取设备列表函数
def deivicesFunc():
    devicesInfo = os.popen('adb devices')
    devicesInfo = devicesInfo.read();  # print(DevicesInfo)
    devicesList = re.findall(r'(.*?)\tdevice\b', devicesInfo)
    return devicesList


# 输出等于号函数
def line(num):
    print('=' * num)


# 导出包名、启动activity 函数
def dumpPA(path):
    aapt = 1
    try:
        PAInfo = subprocess.check_output('aapt dump badging %s' % path).decode('gbk', 'ignore')
    except Exception as e:

        where_adb = subprocess.check_output('where adb').decode('gbk', 'ignore');  # print(where_adb)
        where_aapt = subprocess.check_output('where aapt').decode('gbk', 'ignore');  # print(where_aapt)

        adb_env_list = re.findall('adb.exe', where_adb);  # print(adb_env_list)
        aapt_env_list = re.findall('aapt.exe', where_aapt);  # print(aapt_env_list)

        if len(adb_env_list) == 0:
            print('错误：请添加 adb.exe 的环境变量')
        if len(aapt_env_list) == 0:
            print('错误：请添加 aapt.exe 的环境变量')
        else:
            print('错误：无效的apk文件')

        aapt = 0
        return 0

    if aapt == 1:
        PList = re.findall(r"name='(.+?)' versionCode='", PAInfo);  # print('Plist',PList)
        Alist = re.findall(r"launchable-activity: name='(.+?)'  label='", PAInfo);  # print('Alist',Alist)
        if len(PList) != 0:
            if len(Alist) != 0:
                PAList = PList + Alist;  # print(PAList)
                return PAList
            else:
                print('警告：导出启动的 Activity 失败')
                return PList;  # print(PList)

        else:
            print('警告：导出包名、启动的 Activity 失败')
            return 0


# 判断字符是否能转为数字
def isInt(text):
    if len(text) != 0:
        try:
            ifInt = int(text)
        # print(ifInt,type(ifInt))

        except Exception as e:
            ifInt = False
        # print(ifInt,", isn't int")
        finally:
            return ifInt
    else:
        # 返回空
        return text


# 在一定的长度内选择序号
def chooseNumber(lenth, number):
    if isInt(number) != False:
        if int(number) <= lenth:
            return int(number)
        else:
            return "all"
    else:
        return 'all'


# 判断目录是否含有空格和中文
def existSpaceAndChinese(str):
    space = re.findall(r'(\s)', str)  # 匹配空格
    tuplePathFile = os.path.split(str)
    # path = tuplePathFile[0];#print(path);#目录
    file = tuplePathFile[1];  # print(file);#文件名称
    fileChinese = re.findall(r'[\u0391-\uFFE5]', file)  # #匹配双字节字符（汉字+全角符号）

    if len(space) != 0 and len(fileChinese) != 0:
        print('错误：路径同时含有全角字符和空格')
        return True
    else:
        return False


# 判断路径是否含有两个冒号
def existTwoColon(str):
    colon = re.findall(r'"', str)
    if len(colon) != 2:
        # print(colon)
        return False
    else:
        return True


# 判断名称是否含有全角符号
def existFileChinese(str):
    # 取出路径的目录名和文件名
    tuplePathFile = os.path.split(str)
    path = tuplePathFile[0];  # print(path);#目录
    file = tuplePathFile[1];  # print(file);#文件名称
    fileChinese = re.findall(r'[\u0391-\uFFE5]', file);  # print(fileChinese);#匹配双字节字符（汉字+全角符号）
    if len(fileChinese) != 0:
        print('警告：文件名称含有全角字符')
        return True

    else:
        return False


# 把中文文件名修改成英文
def chineseNameToEnglishname(path):
    # 取出路径的目录名和文件名
    tuple_path_file = os.path.split(path)
    file = tuple_path_file[1]  # 文件名称
    ###分离文件名与扩展名
    tuple_filename_filepro = os.path.splitext(file);  # print(tuple_filename_filepro)
    filename = tuple_filename_filepro[0];  # print(filename)
    # 把中文文件名修改成英文
    if tuple_filename_filepro[1] == '.apk':
        t = time.strftime("%H%M%S")  # 当前时间
        tempname = 'tempPackage%s.apk' % t
        os.chdir(tuple_path_file[0])  # 不更改路径就找不到包
        os.rename(tuple_path_file[1], tempname)
        new_path = os.path.join(tuple_path_file[0], tempname)
        # print('newpath',new_path)
        return new_path, file

    else:
        print('提示：修改文件名称为纯英文字符失败')
        return False


# 把英文名的文件修改成指定的文件名
def englishNameToChinesename(path, chinesename):
    # 取出路径的目录名和文件名
    tuple_path_file = os.path.split(path)
    file = tuple_path_file[1]  # 目录名
    ###分离文件名与扩展名
    tuple_filename_filepro = os.path.splitext(file)
    # 连接目录与旧文件名
    tempname = chinesename
    os.chdir(tuple_path_file[0])
    os.rename(tuple_path_file[1], tempname)
    new_path = os.path.join(tuple_path_file[0], tempname)


# 启动APP
def startAPP(device, packageName, startActivityName):
    my_command = 'adb -s %s shell am start -n %s/%s' % (device, packageName, startActivityName)

    # os.system(startAPP)    

    sub_process = subprocess.Popen(my_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(sub_process.stdout.read().decode())


# adb -s device install -r path
def adbInstall(device, apkPath, packageName="", startActivityName=""):
    my_command = 'adb -s %s install -r %s' % (device, apkPath)

    # os.system(my_command)

    sub_process = subprocess.Popen(my_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # sub_process = subprocess.Popen(my_command, tdout=None, stderr=None)

    # print(sub_process.stderr.read().decode())
    # print(sub_process.stdout.read().decode())

    while sub_process.poll() is None:
        err = sub_process.stderr.read(1).decode()
        sys.stdout.write(err)

        # out = sub_process.stdout.read(1).decode()
        # sys.stdout.write(out)

        sys.stdout.flush()

        # out = sub_process.stdout.read(1).decode()
        # if out == '' and sub_process.poll() != None:
        # break
        # if out != '':
        # sys.stdout.write(out)
        # sys.stdout.flush()

    install_out = sub_process.stdout.read().decode()
    print(install_out)

    if "Success" in install_out:
        if packageName != "" and startActivityName != "":
            startAPP(device, packageName, startActivityName)
        return True
    else:
        return False

        ##########################


version = versionStatus()

if version == 1:

    # print('author:yinzhuoqun')
    print('《adb install》\n Author Email : zhuoqun527@qq.com')
    reApkPath = ''
    disconnectTime = 1
    while 1:

        if len(deivicesFunc()) != 0:
            if os.name == 'nt':
                os.system('color 02')

            disconnectTime = 1
            apkPath = ''
            dumpContent = 0
            apkCount = 1

            while apkCount == 0 or dumpContent == 0 or existSpaceAndChinese(apkPath) == True:
                apkPath = input('\n请拖入apk文件并按下ENTER键：');  # print(len(apkPath))

                if len(reApkPath) != 0 and len(apkPath) == 0:
                    print('=.=你触发一个特技：即将安装上次的包=.=')
                    apkPath = reApkPath
                    print(apkPath)

                apkPath = apkPath.strip();  # print(len(apkPath))	#去掉首尾空格
                apkCount = len(re.findall('(.apk)', apkPath))

                # 没有空格时判断路径是否存在
                if existTwoColon(apkPath) == False:
                    if os.path.exists(apkPath) == False:
                        # print(123)
                        continue
                # 判断是否是apk文件
                if len(apkPath) != 0 and apkCount != 0:
                    dumpContent = dumpPA(apkPath);  # print(type(dumpContent))

            if dumpContent != 0:
                reApkPath = apkPath;  # print(reApkPath)
                packageName = dumpContent[0];  # print(packageName)
                if len(dumpContent) > 1:
                    startActivityName = dumpContent[1];  # print(startActivityName)

            # 防止输入中文报Failure [INSTALL_FAILED_INVALID_URI]
            resultExistChinese = existFileChinese(apkPath)
            if resultExistChinese == True:
                newPathAndOldNameList = chineseNameToEnglishname(apkPath)
                if newPathAndOldNameList != False:
                    apkPath = newPathAndOldNameList[0]  # 新路径
                    oldName = newPathAndOldNameList[1]  # 旧名称

            devicesList = deivicesFunc()
            if len(devicesList) >= 1:

                if len(devicesList) == 1:

                    device = devicesList[0];
                    print('设备名称：%s' % device)
                    adbInstall(device, apkPath, packageName, startActivityName)

                else:
                    print(u'你有设备：%s台' % len(devicesList))

                    db_devices = {}
                    number = 1
                    for device in devicesList:
                        db_devices[number] = device
                        number += 1

                    print(u'设备对应的序号表：', db_devices)

                    number = input('请从设备序号表中选择需要安装的设备序号：')

                    while isInt(number) == False:
                        number = input('请从设备序号表中选择需要安装的设备序号：')

                    if len(number) == 0 or int(number) > len(db_devices):
                        print('=.=你触发一个特技：即将安装到全部设备=.=')

                        # for device in devicesList:
                        # print(u'设备名称：%s' % device)
                        # adbInstall(device, apkPath)
                        # print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 当前时间
                        # if len(dumpContent) > 1:
                        # startAPP(device, packageName, startActivityName)

                        install_threads = []
                        for device in devicesList:
                            apk_install = threading.Thread(target=adbInstall,
                                                           args=(device, apkPath, packageName, startActivityName),
                                                           name=device)
                            install_threads.append(apk_install)
                        for t in install_threads:
                            # print('主线程 %s' % threading.current_thread().getName())
                            print('设备名称：%s' % t.getName())
                            # t.setDaemon(True)
                            t.start()
                            # t.join()


                    elif int(number) <= len(db_devices):
                        device = db_devices[int(number)]
                        print(u'设备名称：%s' % device)
                        adbInstall(device, apkPath, packageName, startActivityName)
                        print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 当前时间
                        # if len(dumpContent) > 1:
                        # startAPP(device, packageName, startActivityName)

                # 从改变的英文路径还原回中文路径
                if resultExistChinese == True and newPathAndOldNameList != False:
                    englishNameToChinesename(apkPath, oldName)

        else:
            if os.name == 'nt':
                os.system('color 0C')
            import sys

            for i in range(3):
                time.sleep(1)
                if disconnectTime <= 60:
                    sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%ss]\r' % disconnectTime)
                    sys.stdout.flush()
                else:
                    a = int(disconnectTime / 60);  # print('a',a)
                    b = disconnectTime % 60;  # print('b',b)
                    sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%smin%ss]\r' % (a, b))
                    sys.stdout.flush()

                disconnectTime += 1
