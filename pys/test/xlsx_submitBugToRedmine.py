#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'
__email__ = "zhuoqun527@qq.com"
__version__ = 'v1.6.0'


# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)


import time, os, json

try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
except Exception as e:
    print(e)

try:
    import xlrd
except Exception as e:
    print(e)

'''
try:
    import wx
    # from wx import xrc
except Exception as e:
    print(e)
''' 
    

# 获取表格 bug 信息，第一个 sheet 
def get_xlsx_info(path):
    if os.path.exists(path) == True:
        try:
            data = xlrd.open_workbook(path)  # 打开Excel文件读取数据
        except Exception as e:    
            print('警告：文件打开失败')
            
        else:
            table = data.sheets()[0]  # 通过索引顺序获取sheet[0123]
            nrows = table.nrows # 获取行数
            ncols = table.ncols # 获取列数
            title_t = {}
            for ncol in range(0,ncols):
                row_content = table.row(0)[ncol].value
                title_t[ncol] = row_content
            # print(title_t)
            for (key,value) in title_t.items():
                if value.find('title') > -1 or value.find('标题') > -1:
                    title_index = key
                if value.find('content')> -1 or value.find('内容') > -1 or value.find('描述') > -1 or value.find('重现步骤') > -1:
                    content_index = key
                if value.find('version')> -1 or value.find('版本') > -1:
                    version_index = key
                if value.find('user') > -1 or value.find('指派') > -1:
                    user_index = key
            logging.info('nrows:%s'%nrows)
            bugs_list = []
            bug_info_list = []
            for bug_num in range(1,nrows):
                bug_title = str(table.row(bug_num)[title_index].value)
                bug_content = str(table.row(bug_num)[content_index].value)           
                if len(str(bug_content)) == 0:
                    bug_content = bug_title
                bug_version = str(table.row(bug_num)[version_index].value)
                appoint_user = str(table.row(bug_num)[user_index].value)
                logging.info(bug_content)
                logging.info(bug_version)
                logging.info(appoint_user)
                if len(bug_title) != 0: 
                    bug_info_list.append(bug_title)
                    bug_info_list.append(bug_content)
                    bug_info_list.append(bug_version)
                    bug_info_list.append(appoint_user)
                    bugs_list.append(bug_info_list)
                bug_info_list = []
            logging.info(bugs_list)
            # print(bugs_list)
            
            return bugs_list
           
    else:
        print('警告：文件不存在')

        
# webdriver
def submitBug(url,username,password,bug_list):
    if len(bug_list) != 0:
        sleep_time = 0.5
        driver_status = True
        try:
            driver = webdriver.Firefox()
            # driver = webdriver.Ie()
            # driver = webdriver.Chrome()
            # driver.implicitly_wait(10) # seconds
        except Exception as e:
            print('嗨，你怎么没安装火狐浏览器呢？你看，报错了：%s'%e)   
            try:           
                driver = webdriver.Chrome()
                # driver = webdriver.Firefox()
                # driver.implicitly_wait(10) # seconds
            except Exception as e:
                print('哎呀，你没救了，打开火狐和谷歌浏览都失败了!\n你可以下载火狐浏览器 41.02(http://pan.baidu.com/s/1jIHIBJ4)\nChrome 浏览器需要添加驱动（http://pan.baidu.com/s/1i5gACWd）到环境变量')
                driver_status = False
                time.sleep(3)
        if driver_status == True:
            driver.maximize_window() #浏览器最大化
            driver.get(url)# 打开网址
            print('标题：', driver.title) # 获取网页标题
            time.sleep(sleep_time)
            driver.find_element_by_xpath('//*[@id="account"]/ul/li/a').click()  # 点击登录
            time.sleep(sleep_time)
            driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)  # 账号
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)  # 密码
            driver.find_element_by_name('login').click() # 登陆
            time.sleep(sleep_time)  
                
            driver.refresh() # 必须要到在 新建问题元素前                       
            time.sleep(sleep_time)
          
            for bug_info in bug_list:
                driver.find_element_by_xpath('//*[@id="main-menu"]/ul/li[7]/a').click() # 点击新建问题 
                bug_title = bug_info[0]
                bug_content = bug_info[1]
                appoint_version = bug_info[2]
                appoint_user = bug_info[3]
                logging.info(bug_title)
                logging.info(appoint_version)
                logging.info(appoint_user)
                
                time.sleep(sleep_time)
                driver.find_element_by_xpath('//*[@id="issue_subject"]').send_keys(bug_title) # 新建问题_标题 
                             
                info_to = driver.find_element_by_xpath('//*[@id="issue_description"]') # 新建问题_内容
                if bug_content.startswith(("http:", "https:")) and bug_content.endswith((".png", ".jpg")):
                    # 添加单张图片地址
                    bug_content = "![](%s)" % bug_content
                else:
                    bug_content = "## %s" % bug_content
                info_to.send_keys(bug_content) 
                time.sleep(sleep_time)
                        
                select = Select(driver.find_element_by_id('issue_assigned_to_id')) # 选择指派人下拉框
                select.select_by_visible_text(appoint_user)
                                     
                select = Select(driver.find_element_by_id('issue_fixed_version_id')) # 选择目标版本下拉框
                # print(select.first_selected_option)
                # print(select.options)
                # print(select.all_selected_options)
                # print(select.deselect_by_visible_text)
                select.select_by_visible_text(appoint_version)
                     
                driver.find_element_by_xpath('//*[@id="issue-form"]/input[1]').click() # 提交 
                time.sleep(sleep_time)           
                print('标题：', driver.title)
                driver.refresh()
                
            driver.quit() # 退出浏览器
    
    else:
        print('提示：bug 列表为空哦')
        time.sleep(3)
        

def input_info():

    xlsx_path = input('请输入 bug 信息表的路径：\n')
    while os.path.exists(xlsx_path) == False or xlsx_path.endswith(('.xlsx','.xls')) == False:
        xlsx_path = input('请输入 bug 信息表的路径：\n')
    
    url_module = input('请输入 Redmime 模块的地址：\n')
    while url_module.startswith('http://') == False:
        url_module = input('请输入 Redmime 模块的地址：\n')
    
    username = input('请输入 Redmime 用户名：\n')
    password = input('请输入 Redmime 密码：\n')
    
    with open('submit_bug_json.txt','w+') as f:
        user_info = {'path': xlsx_path}
        user_info['url'] = url_module
        user_info['username'] = username
        user_info['password'] = password
               
        json.dump(user_info, f) # 载入文件
        
    return user_info

        
# 序列化输入数据
def json_load():
      
    if os.path.exists('submit_bug_json.txt') == False:
        user_info = input_info()
              
    else:
        with open('submit_bug_json.txt','r') as f:
            user_info = json.load(f)
            print("Redmime 用户名称：%s" % user_info["username"])
            print("Redmime 登陆密码：%s" % user_info["password"])
            print("Redmime 模块地址：%s" % user_info["url"])
            print("Bug 信息表的路径：%s" % user_info["path"])
            
        re_input = input('需要重新输入信息吗(Y/N)？\n')
        if re_input == 'N' or re_input == 'n' or len(re_input) == 0:
            
            with open('submit_bug_json.txt','r') as f:
                user_info = json.load(f)
              
        else:
            
            if os.path.exists('submit_bug_json.txt') == True:           
                os.remove('submit_bug_json.txt')
                
                user_info = input_info()
                       
    logging.info(user_info)
  
    return user_info
    
        
if __name__ == '__main__': 

    if os.name == 'nt':
        os.system('color 02')
    print('author: yinzhuoqun\n')
    
    user_info = json_load()
    xlsx_path = user_info['path'] 
    url_module = user_info['url']
    username = user_info['username'] 
    password = user_info['password']
    bug_list = get_xlsx_info(xlsx_path)
    
    submitBug(url_module,username,password,bug_list)
    
    
