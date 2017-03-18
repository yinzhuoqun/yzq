#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Write_Python_version = '3.4.3'
from platform import python_version
import re


import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def submitBug(url,username,password,bug_list,appoint_user,appoint_version):
    try:
        driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(10) # seconds
    except Exception as e:
        print(e)
        try:
            driver = webdriver.Chrome()
            # driver.implicitly_wait(10) # seconds
        except Exception as e:
            print(e, '提示：可能需要安装火狐浏览器，也可能火狐浏览器版本过高，建议安装 41.02(http://pan.baidu.com/s/1jIHIBJ4)')
    else:
        driver.maximize_window() #浏览器最大化
        driver.get(url)# 打开网址
        print('标题：', driver.title) # 获取网页标题
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="account"]/ul/li/a').click()  # 点击登录
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)  # 账号
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)  # 密码
        driver.find_element_by_name('login').click() # 登陆
        time.sleep(1)  
        
        for var in bug_list:
            str_min_pos = var.find('Short')
            str_max_pos = var.find('Long')
            if str_max_pos != -1 and str_min_pos != -1 :
                bug_title = '【monkey】' + var[str_min_pos:str_max_pos-3]               
            else:
                bug_title = '【monkey】Auto submit'
           
            # bug_info = '【monkey】Auto submit'
            
            driver.refresh() # 必须要到在 新建问题元素前                       
            time.sleep(1)           
            driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[7]/a').click() # 点击新建问题 
            
            # bug_info1 = var
            # bug_info1 = var[0:600]           
            # driver.find_element_by_xpath('//*[@id="issue_description"]').send_keys(bug_info1)  #新建问题_内容 
            
            # bug_info2 = var[500:999]
            # driver.find_element_by_xpath('//*[@id="issue_description"]').send_keys(bug_info2)
            
            info_list = var.split('\n')
            print(info_list)
            for info in info_list:
                info_to = driver.find_element_by_xpath('//*[@id="issue_description"]') # 新建问题_内容                 
                info_to.send_keys(info)
                time.sleep(1)
            
            
            # select = Select(driver.find_element_by_id('issue_assigned_to_id')) # 选择指派人下拉框
            # select.select_by_visible_text(appoint_user)                                   
            # select = Select(driver.find_element_by_id('issue_fixed_version_id')) # 选择目标版本下拉框
            # select.select_by_visible_text(appoint_version)
                                 
            # driver.find_element_by_xpath('//*[@id="issue_subject"]').send_keys(bug_title) # 新建问题_标题 
            
           
            
            
            # info_list = var.split('\n')
            # print(info_list)
            # for info in info_list:
            
                # info_to = driver.find_element_by_xpath('//*[@id="issue_description"]') # 新建问题_内容              
                # time.sleep(1)
                # info_to.send_keys(info.encode('utf-8')) 
                   
            # select = Select(driver.find_element_by_id('issue_assigned_to_id')) # 选择指派人下拉框
            # select.select_by_visible_text(appoint_user)
       
                                
            # select = Select(driver.find_element_by_id('issue_fixed_version_id')) # 选择目标版本下拉框
            # select.select_by_visible_text(appoint_version)
                     
            # driver.find_element_by_xpath('//*[@id="issue-form"]/input[1]').click() # 提交 
            # time.sleep(2)           
            # print('标题：', driver.title) 

            

        # driver.quit() # 退出浏览器




def out_eq():
    out_eq_count = 40
    print('=' * out_eq_count)


def version_status():
    writelist = re.split('\D', Write_Python_version)  # print(writelist)
    Write_version = writelist[0]  # print(Write_version)
    Currentlist = re.split('\D', python_version())  # print(Currentlist)
    Current_version = Currentlist[0]  # print(Current_version)
    if Current_version != Write_version:
        print(u'Python 版本不兼容!')
        out_eq()
        return 0
    else:
        # print('uPython 版本兼容.')
        out_eq()
        return 1


# out_eq()
# print('Current Python version',python_version())
# print('Write Python version',Write_Python_version)
print('Author:yinzhuoqun')
# out_eq()
run = version_status()
if run == 1:
    import os, re, time

    import codecs

    if os.name == 'nt':
        os.system('color 02')
    from time import sleep

    mk_log = input('请输入 monkey 测试 log 文件的路径名称：\n')
    while os.path.exists(mk_log) == False:
        print('错误：文件不存在！')
        mk_log = input('请输入 monkey 测试 log 的文件地址：\n')
    out_eq()

    # import sys
    # print('系统编码：%s'%sys.getdefaultencoding())#获得和设置系统默认编码

    #import chardet
    #chardet.detect(mk_log)

    # with open(mk_log,'r') as f:
    import codecs
    mk_fo = codecs.open(mk_log,'r',encoding='utf-8')
    # isinstance(mk_fo,'unicode')
    # print('type',type(mk_fo))

    str = mk_fo.read()
    mk_fo.close()
    # print('str:',str)
    # 匹配crash
    reg = re.compile(r"CRASH", re.S)
    crash_list = reg.findall(str)
    # print('crash_count=',len(crash_list))
    # 匹配crash_log
    # reg_log = re.compile(r"// CRASH.*?// \n", re.S)  # 贪婪模式
    reg_log = re.compile(r"(// CRASH.*?\r\r\n//) \r", re.S)  # 贪婪模式
    # reg_log=re.compile(r'// CRASH.*?Native Method\)',re.S)#非贪婪模式:*? 转义字符：\
    crash_log_list = reg_log.findall(str);
    # print('crash_log:',crash_log_list)


    # print('crash_log_count=',len(crash_log_list))
    ###去重####
    # for crash in crash_log_list:
    # print(crash_log_list)
    try:
        #导入 Levenshtein 比较模块
        import Levenshtein as cmp
        import_Levenshtein = True
    except Exception as e:
        print(e)
        try:
            #未安装 Levenshtein 模块时尝试安装
            os.system('pip install python-Levenshtein')
            import Levenshtein as cmp
        except Exception as e:
            print(e)
            import_Levenshtein = False
    if import_Levenshtein != False:
        for crash1 in crash_log_list:
            for crash2 in crash_log_list[crash_log_list.index(crash1)+1:]:
                # print(cmp.ratio(crash1,crash2))
                if cmp.ratio(crash1,crash2) > 0.9:
                    crash_log_list.remove(crash2)

    ###
    #print(crash_log_list)
    # 输出 crash log到 txt
    def crash_write(str):
        # pwd=os.getcwd()#保存至工作路径
        pwd = os.path.join(os.path.expanduser("~"), "Desktop")  # 保存至桌面
        t = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = 'CrashLog%s.txt' % t
        crash_path = pwd + '\\' + filename
        # print(crash_path)
        crash_fo = open(crash_path, 'ab')
        str = str.encode('utf-8')
        crash_fo.write(str)
        crash_fo.close()
        return crash_path, pwd, filename
        
    # 提交bug
    # import submitBugToRedmine
    username = 'zhuoquny'
    password = 'Zhuo2015'
    url = 'http://192.168.2.164:3000/projects/bed-for-andriod/issues' 
    bug_list = crash_log_list
    appoint_user = '尹 卓群' # 姓和名要空格
    appoint_version = '4.8.1'
    # submitBugToRedmine.submitBug(url,username,password,crash_log_list,appoint_user,appoint_version)
    submitBug(url,username,password,crash_log_list,appoint_user,appoint_version)
        
        


    if len(crash_list) != 0:
        print('提示：一共发生 %s 次 crash。' % len(crash_list))
        out_eq()
        times = 1
        if len(crash_log_list) != 0:
            for str_crash in crash_log_list:
                print('第 %s 种 crash：' % times)
                print(str_crash, len(str_crash))  # 输出到cmd
                crash_write(str_crash)  # 导出bug
                file_info = crash_write('\n\n\n')
                times += 1
                out_eq()
            if os.path.exists(file_info[0]) == True:
                print('crash 日志导出目录:%s' % file_info[1])
                print('crash 日志文件名是:%s' % file_info[2])

        allow_error = len(crash_list) - len(crash_log_list)
        # print('allow_error:',allow_error)
        # if allow_error != 0:
        #     print('提示：一共发生 %s 次 crash，还有%s个crash未导出，请自行导出。' % (len(crash_list), allow_error))
        stop_run = input('请按 ENTER 键停止运行...\n')

    else:
        print('提示：未发现 crash。')
        print('注意：脚本 5s 后自动关闭。')
        sleep(5)
