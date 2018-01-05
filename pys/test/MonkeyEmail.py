# !/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

Write_Python_version = '3.4.3'
from platform import python_version
import re, os, time, datetime, subprocess
import random

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

# 文本信息
m1=u'长的黑，是因为帅炸了，炸了以后，焦了，就黑了。'
m2=u'不要逼我出手，我疯起来连自己都打。'
m3=u'你会喜欢我吗？不会我教你啊。'
m4=u'对方已被太阳热死，无法接收你的消息。'
m5=u'你的智商和你的胸一样幼稚。'
m6=u'我就不信，你能顺着网线爬过来打我。'
message_user_list=[m1,m2,m3,m4,m5,m6]
message_user = random.choice(message_user_list)
# 附件本地路径
msg_file_url = r'C:\Users\lifeix\Desktop\test.txt'
crash_info=u'我就是来打你脸的，打你的脸我不疼。'
message='=.='+message_user+'=.=\n\n'+crash_info

#格式化收件人
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#发送邮件
def send_mail(message, msg_file_url):
    # 输入邮件地址, 口令和POP3服务器地址:
    # email = input('Email: ')
    from_addr = ''
    print('发件人：%s'%from_addr)
    # password = input('Password: ')
    password = ''

    # 收件服务器
    # pop3_server = input('POP3 server: ')
    pop3_server = 'imap.exmail.qq.com'
    # smtp发件服务器
    smtp_server = 'smtp.exmail.qq.com'

    # 收件人信息,必须传入list
    to_addr = ['']
    for to_add in to_addr:
        print('收件人：%s'%to_add)

    # 邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Monkey 测试 <%s>' % from_addr)  # 发件人信息

    # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可，+连接。
    ## 收件人信息
    #多人收件固定信息
    # msg['To'] = \
    # _format_addr('公子 <%s>'%to_addr[0])+','+\
    # _format_addr('盗帅 <%s>'%to_addr[1])+','+\
    # _format_addr('才子 <%s>'%to_addr[2])
    #单人写死
    # msg['To'] = \
    #     _format_addr('公子 <%s>' % to_addr[0])

    #不限人数信息
    def msg_to(to_add):
        msg_to_info = ['公子', '盗帅', '才子', '君子']#初始化
        # import random
        len_add = len(to_add)
        total_add=[]#格式化邮件列表
        for add in to_add:
            to_info = random.choice(msg_to_info)
            msg_to_info.remove(to_info)#删除选中的
            m_add='%s<%s>'%(to_info,add)
            f_m_add=_format_addr(m_add)
            total_add.append(f_m_add)
            total_add.append(",")
            #print(m_add)
        msg_to_info = ['公子', '盗帅', '才子', '君子']  # 重置
        total_add.pop()#删除最后一个，
        # print('total_add',total_add)
        total_add_info=''
        for add_info in total_add:
            total_add_info+=add_info
        # print('total_add_info',total_add_info)
        return total_add_info

    msg['To']=msg_to(to_addr)
    msg['Subject'] = Header('来自 Crash 的问候……', 'utf-8').encode()  # 标题

    # 邮件正文是MIMEText:
    msg.attach(MIMEText(message, 'plain', 'utf-8'))
    ## 添加附件就是加上一个MIMEBase，从本地读取一个图片:

    # 取出路径的目录名和文件名
    #import os
    tuple_path_file = os.path.split(msg_file_url)
    file = tuple_path_file[1]  # 目录名
    # print(file)
    with open(msg_file_url, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'txt', filename=file)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=file)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    server = smtplib.SMTP(smtp_server, 25)  # 服务器
    # server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password)  # 登陆发件人
    server.sendmail(from_addr, to_addr, msg.as_string())  # 发送try
    server.quit()

# 输出等于号函数
def line(num):
    print('=' * num)

def version_status():
    writelist = re.split('\D', Write_Python_version)  # print(writelist)
    Write_version = writelist[0]  # print(Write_version)
    Currentlist = re.split('\D', python_version())  # print(Currentlist)
    Current_version = Currentlist[0]  # print(Current_version)
    if Current_version != Write_version:
        print(u'错误：Python 版本不兼容，建议使用 v3.4.X')
        time.sleep(3)
        return 0
    else:
        return 1


# 获取设备列表函数
def dlist():
    DevicesInfo = os.popen('adb devices')
    DevicesInfo = DevicesInfo.read();  # print(DevicesInfo)
    DevicesList = re.findall(r'(.*?)\tdevice\b', DevicesInfo)
    return DevicesList


# 输出未发现设备计时函数
def nodevice_error(times1):
    if os.name == 'nt':
        os.system('color 0C')  # 红色文字

    import sys
    for i in range(3):
        time.sleep(1)
        # if language==u'chinese':
        if times1 <= 60:
            sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%ss]\r' % times1)
            sys.stdout.flush()
        else:
            a = int(times1 / 60);  # print('a',a)
            b = times1 % 60;  # print('b',b)
            sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%smin%ss]\r' % (a, b))
            sys.stdout.flush()
        times1 += 1
        return times1


# 导出包名
def dump_pa(path):
    aapt = 1
    try:
        PaInfo = subprocess.check_output('aapt dump badging %s' % path).decode('gbk', 'ignore')

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
            if os.path.exists(path) == True:
                print('错误：无效的 apk 文件')
            else:
                print('错误：路径不存在')

        aapt = 0
        return 0

    if aapt == 1:
        PList = re.findall(r"name='(.+?)' versionCode='", PaInfo);  # print(PList)
        Alist = re.findall(r"launchable-activity: name='(.+?)'  label='", PaInfo);  # print(Alist)
        if len(PList) != 0 and len(Alist) != 0:
            # print("package name:",PList[0])
            # print("startActivity name:",Alist[0])
            PaList = PList + Alist;  # print(PaList)
            return PaList
        else:
            print('警告：导出包名、启动activity失败')
            return False


# 把中文文件名修改成英文
def chinesename_to_englishname(path):
    # 取出路径的目录名和文件名
    tuple_path_file = os.path.split(path)
    file = tuple_path_file[1]  # 目录名
    # 分离文件名与扩展名
    tuple_filename_filepro = os.path.splitext(file)
    filename = tuple_filename_filepro[0]
    filepro = tuple_filename_filepro[1]
    # print(filename)	#文件名称
    # print(filepro) #扩展名
    # 把中文文件名修改成英文
    if tuple_filename_filepro[1] == '.apk':
        t = time.strftime("%H%M%S")  # 当前时间
        tempname = 'tempPackage%s.apk' % t
        os.chdir(tuple_path_file[0])
        os.rename(tuple_path_file[1], tempname)
        new_path = os.path.join(tuple_path_file[0], tempname)
    # print('newpath',new_path)
    return new_path, file


# 把英文名的文件修改成指定的文件名
def englishname_to_chinesename(path, chinesename):
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


# 定义monkey
def monkeyt(device, packagename, evnet):
    # t=time.strftime("%m%d%H%M%S")
    t = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = packagename + '_log' + t + '.txt'
    # pwd=os.getcwd()#日志保存至工作路径
    pwd = os.path.join(os.path.expanduser("~"), "Desktop")  # 日志保存至桌面
    log_path = os.path.join(pwd, filename)  # 日志路径
    txt = '> ' + log_path  # 全局拿日志路径

    throttleTime = 50 # 事件间隔时间 毫秒（ms）
    seed = random.randint(100,500)#随进seed值
    monkey = 'adb -s %s shell monkey -p %s -s %s --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle %s -v %s %s' % (
        device, packagename, seed, throttleTime, evnet, txt)
    # print(monkey)

    monkeyStartTime = datetime.datetime.now();  # print(monkeyStartTime)
    # monkeyUsedTime=throttleTime/2000*int(evnet);print(monkeyUsedTime)
    monkeyUsedTime = 0.016 * int(evnet)  # 计算--throttle为50时，7组平均数
    monkeyEndTime = monkeyStartTime + datetime.timedelta(seconds=monkeyUsedTime);  # print(monkeyEndTime)
    print('=.= 预计 %s 执行完毕 =.=' % monkeyEndTime.strftime("%H:%M:%S"))

    starttime = datetime.datetime.now()
    os.system(monkey)

    # monkeyEndNotice()	#弹出monkey已结束的窗口提示

    lasttime = datetime.datetime.now()
    taketime = (lasttime - starttime).seconds
    print('用时:', taketime, 's')

    print('日志:', filename, '\n位于:', pwd)
    crashPull(log_path, packagename)  # 导出crash


def monkeyc(device, packagename, evnet):
	
    monkey = 'adb -s %s shell monkey -p %s -s 250 --throttle 50 -v -v -v %s' % (device, packagename, evnet)
    # print(monkey)
    # starttime=datetime.datetime.now()
    os.system(monkey)


# monkeyEndNotice()	#弹出monkey已结束的窗口提示

# lasttime=datetime.datetime.now()
# taketime=(lasttime-starttime).seconds
# print('Time used:',taketime,'s')

# 查看包名的APK包是否已安装
def exsitPackageName(devicename, packagename):
    if devicename in dlist():
        pm_path_command = 'adb -s %s shell pm path %s' % (devicename, packagename)
        apkPath = os.popen(pm_path_command).read();  # print(apkPath,type(apkPath))
        apkPathlist = re.findall(r'package:(.+?.apk)', apkPath);  # print(apkPathlist)
        return len(apkPathlist)
    else:
        # print('错误：选择的设备[%s]未连接1'%device)
        return 0


# 判断字符是否能转为数字
def isInt(text):
    try:
        ifInt = int(text)
    # print(ifInt,type(ifInt))

    except Exception as e:
        ifInt = False
    # print(ifInt,", isn't int")
    finally:
        return ifInt


# 导出crash
def crashPull(mk_log_path, diy_name):
    import codecs
    # mk_fo = open(mk_log_path)
    # str = mk_fo.read()
    # mk_log_path=r'C:\Users\lifeix\Desktop\com.l99.lotto_log2016-06-29_14-44-00.txt'
    mk_fo = codecs.open(mk_log_path, 'r', encoding='utf-8')
    str = mk_fo.read()
    mk_fo.close()
    # print('str:',str)
    # 匹配crash
    reg = re.compile(r"CRASH", re.S)
    crash_list = reg.findall(str)
    # print('crash_count=',len(crash_list))
    # 匹配crash_log
    # reg=re.compile(r"// CRASH.+?Native Method\)",re.S)#贪婪模式

    reg_log = re.compile(r"(// CRASH.*?\r\r\n//) \r", re.S)  # 贪婪模式
    # reg_log = re.compile(r'// CRASH.*?// \n', re.S)  # 非贪婪模式:*? 转义字符：\
    crash_log_list = reg_log.findall(str)
    # print('crash_log_count=',len(crash_log_list))
    # 输出crash log
    def crash_write(str):
        # pwd=os.getcwd()#保存至工作路径
        pwd = os.path.join(os.path.expanduser("~"), "Desktop")  # 保存至桌面
        t = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = '%s_crash_log%s.txt' % (diy_name, t)
        crash_path = pwd + '\\' + filename
        # print(crash_path)
        crash_fo = open(crash_path, 'ab')
        str = str.encode()
        crash_fo.write(str)
        crash_fo.close()
        return crash_path, pwd, filename

    if len(crash_list) != 0:
        if len(crash_log_list) > 0:  # 防止匹配为空时报file_info未定义
            times = 1  # 初始化导出次数
            for str_crash in crash_log_list:
                print('第%s个 crash：' % times)
                print(str_crash, len(str_crash))
                crash_write(str_crash)  # 导出bug
                file_info = crash_write('\n\n\n')
                times += 1
                line(40)
            if os.path.exists(file_info[0]) == True:
                print('crash 日志:%s' % file_info[2])#文件名
                print('crash 位于:%s' % file_info[1])#目录
                with open(file_info[0],'r') as f:
                    crash_info = f.read()
                # msg_file_url=file_info[0]#附件为crash log 部分
                msg_file_url=mk_log_path #附件为整个log

        allow_error = len(crash_list) - len(crash_log_list)
        # print('allow_error:',allow_error)
        print('提示：共有%s个 crash，还有%s个 crash 未导出' % (len(crash_list), allow_error))
        message = '=.=' + message_user + '=.=\n\n' + crash_info
        send_mail(message,msg_file_url)#发送邮件

    else:

            # 没有crash时删除日志
            delete_log = input('未发现 crash，删除日志按 ENTER，保留日志输入任意字符：')
            if len(delete_log) == 0:
                while os.path.exists(mk_log_path) == True:
                    os.remove(mk_log_path)
                    if os.path.exists(mk_log_path) == False:
                        print('提示：日志已删除')
            else:
                pass

# 查找数字，可以直接int，然后用except来确定是否是数字
def find_int(str):
    find_int = re.findall(r'\D+', str)  # \D找除数字之外的
    if len(find_int) != 0:
        return True  # 找到非数字字符
    else:
        return False  # 未找到非数字字符


# 查找.apk扩展名的文件
def find_apk(path):
    apk_count = len(re.findall('(.apk)', path))
    if apk_count != 0:
        return True
    else:
        return False


# adb命令只有 文件名称为中文时不能安装，有空格也能安装
# python 只有目录没有空格， 才能修改中文的文件名
def pathStatus(str):
    # space = re.findall(r'(\s)', str)#匹配空格
    tuplePathFile = os.path.split(str)
    # path = tuplePathFile[0];#print(path);#目录
    file = tuplePathFile[1];  # print(file);#文件名称
    fileChinese = re.findall(r'[\u0391-\uFFE5]', file)
    fileSpace = re.findall(r'(\s)', file)  # 匹配空格

    dir = tuplePathFile[0]
    dirChinese = re.findall(r'[\u0391-\uFFE5]', dir)  # 匹配空格
    dirSpace = re.findall(r'(\s)', dir)  # 匹配空格

    if len(fileChinese) != 0:
        fc = 1000
    else:
        fc = 2000

    if len(fileSpace) != 0:
        fs = 100
    else:
        fs = 200

    if len(dirChinese) != 0:
        dc = 10
    else:
        dc = 20

    if len(dirSpace) != 0:
        ds = 1
    else:
        ds = 2

    pathStatusCode = fc + fs + dc + ds;
    print('pathStatusCode:%s' % pathStatusCode)
    return pathStatusCode


# 匹配目录是否含有空格
def existDirSpaceAndFileChinese(str):
    tuplePathFile = os.path.split(str)
    file = tuplePathFile[1];  # print('file',file);#文件名称
    fileChinese = re.findall(r'[\u0391-\uFFE5]', file)

    dir = tuplePathFile[0];  # print('dir',dir)#目录
    dirSpace = re.findall(r'(\s)', dir)  # 匹配空格
    if len(dirSpace) != 0 and len(fileChinese) != 0:
        return True
    else:
        return False


# 弹出monkey运行完的提示
def monkeyEndNotice():
    import tkinter.messagebox as messagebox
    messagebox.showinfo('MonkeyTest', 'Monkey finished')


version = version_status()
if version == 1:
    times1 = 1
    if os.name == 'nt':
        os.system('color 02')  # 绿色文字
    print('author:yinzhuoqun')

    while 1:
        deviceslist = dlist()
        if len(deviceslist) != 0:
            if os.name == 'nt':
                os.system('color 02')
            if len(deviceslist) > 1:
                print(u'你有设备：%s台' % len(deviceslist))
                db_devices = {}
                number = 1
                for device in deviceslist:
                    db_devices[number] = device
                    number += 1
                print(u'设备对应的序号表:', db_devices)

                # 生成设备数量的整数list
                deviceNumberList = []
                devicesCount = len(deviceslist)
                for Number in range(1, devicesCount + 1):
                    deviceNumberList.append(Number)
                # print(deviceNumberList,type(deviceNumberList[0]))

                deviceNumber = ''
                deviceNumberRange = False
                while deviceNumberRange == False or len(deviceNumber) == 0:
                    deviceNumber = input(u'请从设备序号表中选择 MonkeyTest 设备的序号:');  # print(type(deviceNumber))
                    if len(deviceNumber) != 0 and find_int(deviceNumber) == False:
                        if (int(deviceNumber) in deviceNumberList):
                            # print(1)
                            deviceNumberRange = True
                        else:
                            deviceNumberRange = False

                device = db_devices[int(deviceNumber)]
                print(u'设备名称：', device)
            print('')  # 防止没有设备从无到有的时候文字覆盖不完全的现象
            if len(deviceslist) == 1:
                device = deviceslist[0]
                print(u'设备名称：', device)
            packageNameORpath = '';
            pathORname = 1  # 初始化
            while len(packageNameORpath) == 0 or pathORname == 0:
                packageNameORpath = input('请输入包名或者包的路径:')

                #########################立方快捷设置
                # packageNameORpath = input('请输入包名或者包的路径，输入1选择床上，2选择体育头条，3选择大赢家:')
                # if len(packageNameORpath) == 0 or packageNameORpath == '1':
                #     packageNameORpath = 'com.l99.bed'
                # elif packageNameORpath == '2':
                #     packageNameORpath = 'com.lifeix.headline'
                # elif packageNameORpath == '3':
                #     packageNameORpath = 'com.l99.lotto'
                ########################

                # NoDevices=False#初始化NoDevices

                if device in dlist() and len(packageNameORpath) != 0:

                    packageNameORpath = packageNameORpath.strip()  # 去除输入内容的首尾空格

                    # 判断 输入的字符串是否是包名，包名是否已经安装在手机
                    packageNameCount = exsitPackageName(device, packageNameORpath)
                    if packageNameCount == 0:

                        # 查询文件是否是apk文件
                        if find_apk(packageNameORpath) == True and dump_pa(packageNameORpath) != 0:

                            # 查询输入的路径中的包名是否已经安装
                            packageNameList = dump_pa(
                                packageNameORpath);  # print('dump_pa_return:',packageNameCount)#导出包名
                            if packageNameList != 0:
                                packagename = packageNameList[0]  # 获取包名
                                packageNameCount = exsitPackageName(device, packagename)  # 查询包名的APK是否已经安装
                            # print(packageNameCount)

                            # 如果packageNameCount不等于零说明设备已安装该APK，否则没有安装
                            if packageNameList != 0 and packageNameCount != 0:

                                break

                            else:
                                if device in dlist():
                                    if packageNameList != 0:
                                        if existDirSpaceAndFileChinese(packageNameORpath) == False:
                                            myPathCode = 1212
                                            pathStatusCode = pathStatus(packageNameORpath)
                                            if pathStatusCode == myPathCode:
                                                new_path_old_name_list = chinesename_to_englishname(packageNameORpath)
                                                packageNameORpath = new_path_old_name_list[0]
                                                oldname = new_path_old_name_list[1]

                                            print('警告：检测到设备[%s]未安装 %s ,执行安装...' % (device, packagename))

                                            # 未安装时进行安装
                                            os.system('adb -s %s install %s' % (device, packageNameORpath))

                                            # 安装后才恢复原来名称，从改变的英文路径还原回中文路径
                                            if pathStatusCode == myPathCode:
                                                englishname_to_chinesename(packageNameORpath, oldname)
                                            # print('提示：已改回原文件名 %s'%oldname)

                                            # 安装完成后终止while条件
                                            break

                                        else:
                                            # 路径同时含有全角字符和空格，重新输入
                                            print('错误：同时存在目录含有空格、文件名称含有全角字符')
                                            pathORname = 0

                                    else:

                                        pathORname = 0

                                else:
                                    print('错误：选择的设备[%s]未连接' % device)

                        else:
                            # print('提示：设备[%s]未安装'%device,packageNameORpath)
                            pathORname = 0

                    else:

                        if device in dlist():
                            # print('提示：设备[%s]未安装'%device,packageNameORpath)
                            packagename = packageNameORpath
                            break

                        # pathORname=0
                        else:
                            print('错误：选择的设备[%s]未连接' % device)
                            break

                else:
                    # NoDevices=True
                    pass

            # 事件数量
            if device in dlist():  # NoDevices!=True:
                text_stop_run = '## MonkeyTest 已经执行完毕，按 ENTER 重复执行一次，输入数字更改事件的次数运行，输入非数字重新运行：\n'

                evnet = ''  # 初始化event
                setEvnet = 20000  # 默认event数量
                while len(evnet) == 0 or re.findall('[^0-9]', evnet):
                    evnet = input("请输入 MonkeyTest 事件的次数(整数)，按 ENTER 运行 %s次:" % setEvnet)
                    if len(evnet) != 0:
                        pass
                    else:
                        evnet = setEvnet
                        break
                # 日志展现形式
                text_outputstyle = '日志保存到文件请按 ENTER，输出至当前窗口请输入任意字符:'
                outputstyle = input(text_outputstyle)
                if len(outputstyle) == 0:
                    NewDevicesList = dlist()
                    if len(NewDevicesList) != 0:
                        if device in NewDevicesList:
                            packageNameCount = exsitPackageName(device, packagename)  # 查询包名的APK是否已经安装
                            if packageNameCount != 0:
                                monkeyt(device, packagename, evnet)
                                stop_run = input(text_stop_run)  # 弹出重复运行提示
                            else:
                                print('提示：设备[%s]未安装' % device, packagename)
                                continue
                        else:
                            print('错误：选择的设备[%s]未连接' % device)

                    else:
                        # 没有设备
                        pass
                else:

                    NewDevicesList = dlist()
                    if len(NewDevicesList) != 0:
                        if device in NewDevicesList:
                            packageNameCount = exsitPackageName(device, packagename)  # 查询包名的APK是否已经安装
                            if packageNameCount != 0:
                                monkeyc(device, packagename, evnet)
                                stop_run = input(text_stop_run)  # 弹出重复运行提示
                            else:
                                print('提示：设备[%s]未安装' % device, packagename)
                                continue
                        else:
                            print('错误：选择的设备[%s]未连接' % device)

                    else:
                        # 终止运行，转到无设备计时
                        pass

                # 重复运行
                while device in NewDevicesList:

                    NewDevicesList = dlist()
                    if len(NewDevicesList) != 0:
                        if device in NewDevicesList:
                            if isInt(stop_run) != False:
                                evnet = isInt(stop_run)
                            if len(stop_run) == 0 or isInt(stop_run) != False:
                                packageNameCount = exsitPackageName(device, packagename)  # 查询包名的APK是否已经安装
                                if packageNameCount != 0:
                                    if len(outputstyle) == 0:
                                        monkeyt(device, packagename, evnet)
                                    else:
                                        monkeyc(device, packagename, evnet)
                                    stop_run = input(text_stop_run)  # 弹出重复运行提示
                                else:
                                    print('提示：设备[%s]未安装' % device, packagename)
                                    break
                            else:
                                break  # 终止运行，重新开始

                        else:
                            print('错误：选择的设备[%s]未连接' % device)
                            break

                    else:
                        # 终止运行，转到无设备计时
                        break

            else:
                # 无设备时，转到无设备计时,这是在while=1层
                pass


        else:
            times1 = nodevice_error(times1)
