#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'




try:
    from selenium import webdriver

    install_selenium = True
except Exception as e:
    import os, re, subprocess
    # os.system('pip install selenium')
    #------防止pip未加入环境变量--|--不能用try去捕获os.system命令失败的异常 
    where_python = subprocess.check_output('where python').decode('gbk', 'ignore');
    # where_python：数据类型 str 
    python_env_list = re.findall('python.exe', where_python)
    if len(python_env_list) == 0:
        print('错误：请添加 python.exe 的环境变量')
    else:
        path_file = os.path.split(where_python)
        python_path = path_file[0]  # 取出 python 路径
        pip_path = os.path.join(python_path,'Scripts') # 拼接 python3 pip的路径
        if os.path.exists(pip_path) == True:
            os.chdir(pip_path)
            os.system('pip install selenium')
            install_selenium = True
        else:
            print('错误：请添加 pip.exe 的环境变量')
            install_selenium = False

            
if install_selenium != False:

    from selenium import webdriver
    import time, datetime
    import sched
    import sys, random
    
    import logging
    # logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.WARNING)       
    # 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
    
    
    #简单加密解密
    def eAd(enORde,str):
        import base64
        if enORde == 'en':
            #加码
            b_ende = str.encode(encoding="utf-8")
            b_result = base64.b64encode(b_ende)
            # print(b_result)
            return b_result
        else:
            #解码
            result = base64.b64decode(str)
            b_result = result.decode()
            # print(b_result)
            # base64.b64decode(str).decode()
            return b_result
    
    # webdriver
    def qiandao():
        try:
            driver = webdriver.Firefox()
            # driver = webdriver.Chrome()
        except Exception as e:
            print(e, '提示：可能需要安装火狐浏览器，也可能火狐浏览器版本过高，建议安装 41.02(http://pan.baidu.com/s/1jIHIBJ4)')
        else:
            driver.maximize_window() #浏览器最大化
            driver.get("http://123.206.92.65/web/login.php")# 打开网址
            print('标题：', driver.title) # 获取网页标题
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="u"]').send_keys(eAd('de',qq))  # 已注册QQ号
            driver.find_element_by_xpath('//*[@id="p"]').send_keys(eAd('de',pw))  # 密码
            driver.find_element_by_class_name('button_blue').click() # 登陆
            time.sleep(1)
            for times in range(2):
                driver.find_element_by_class_name('ae_b').click() # 点击签到
                alert = driver.switch_to_alert()
                time.sleep(2)
                print('页面：', alert.text) #获取页面警告提示
                alert.accept() # 接受网页警告提示
            time.sleep(3)  # AttributeError: 'time.struct_time' object has no attribute 'time.sleep'
            driver.quit() # 退出浏览器
    
    
    # 倒计时
    def count_down(wait_time):
        while wait_time >= 0:
            h = int(wait_time / 3600);  # print(h)
            sUp_h = wait_time - 3600 * h
            m = int(sUp_h / 60);  # print(m)
            sUp_m = sUp_h - 60 * m
            s = sUp_m;  # print(s)
            sys.stdout.write('%02d:%02d:%02d\r' % (h, m, s))
            sys.stdout.flush()
            time.sleep(1)
            wait_time = wait_time - 1    
        print() # 消除 sys.stdout.write 对覆盖输出的影响
 
    qd_status = False #定义初始签到状态
    qq = 'NTkyMDA2MzM5'        
    pw = 'MTIzNDU2'
    
    times = 0
    # def qd_start():
    while True:

        schedule = sched.scheduler(time.time, time.sleep)  # 生成调度器
        # 生成调度器,第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
        
        # time = time.localtime(time.time())
        # time.struct_time(tm_year=2016, tm_mon=9, tm_mday=5, tm_hour=17, tm_min=48, tm_sec = 30, tm_wday = 0, tm_yday = 249, tm_isdst = 0)
        
        cuurent_date = time.localtime(time.time()) # 获取当前时间
        tm_mon = cuurent_date.tm_mon;logging.info('tm_mon:%s'%tm_mon)
        tm_day = cuurent_date.tm_mday;logging.info('tm_day:%s'%tm_day)
        tm_min = cuurent_date.tm_min;logging.info('tm_min:%s'%tm_min)
        tm_sec = cuurent_date.tm_min;logging.info('tm_sec:%s'%tm_sec)
                     
        random_min = random.randint(3,35);logging.info('random_min:%s'%random_min) # 随机选择签到分钟数
        # random_min = 10 # mock min
        qd_startime_random = datetime.datetime(2016, tm_mon, tm_day, 20, random_min, 0)
                       
        qd_startime_default = datetime.datetime(2016, tm_mon, tm_day, 20, 1, 0)  # 获取当日默认签到开始时间
        qd_endtime = datetime.datetime(2016, tm_mon, tm_day, 20, 45, 0) # 获取当日签到结束时间
                        
        cuurent_time = datetime.datetime.now() # 获取当前时间       
          
        # print(qd_startime_default > cuurent_time)    
        if qd_startime_default < cuurent_time < qd_endtime: #当前时间在签到时间内就开始签到
            qd_startime = qd_startime_default
            
        elif cuurent_time < qd_startime_default :#当前时间小于默认签到时间就随机选一个分钟数
            if time != 0 :
                qd_startime = qd_startime_random
                # print('选择下次签到时间：\n%s'%qd_startime)
                
                
            else:
                
                qd_startime =  qd_startime_default
                # print('选择下次签到时间：\n%s'%qd_startime)
                    
        else:
            qd_startime = qd_startime_default
            # print('选择下次签到时间：\n%s'%qd_startime)
         
            
        qd_startime = qd_startime_random;logging.info(qd_startime)
        
        if cuurent_time < qd_startime :#or qd_status == True:
            print('O(∩_∩)O~还没到签到时间哦~O(∩_∩)O')
            # cuurent_time = datetime.datetime.now() # 更新当前时间
            # wait_time = (qd_startime - cuurent_time).seconds; # 距离下次签到时间的秒数
            # logging.info('wait_time_seconds:%s'%wait_time)
            # count_down(wait_time) # 调用倒计时函数
            
        
        elif qd_startime <= cuurent_time < qd_endtime :
            print('正在签到...\n')
            schedule.enter(0, 0, qiandao, ())
            # enter用来安排某事件的发生时间，从现在起第n秒开始启动  
            # schedule.enter(4, 0, func, ("test1", time.time()))
            # 第一个参数是一个整数或者float，代表多少 秒 后执行这个action任务
            # 第二个参数priority是优先级，0代表优先级最高，1次之，2次次之
            # 第三个参数就是你要执行的任务，可以简单的理解成你要执行的函数的函数名
            # 第四个参数是你要传入的这个定时执行的action为函数名的函数的参数，最好是用"()"括号来包起来，包起来肯定是不会出错的。--
            # --其次，当你只传入一个参数时，用括号包起来后，一定要记住再打上一个逗号。
            
            # schedule.run() # 持续运行，直到计划时间队列变成空为止
            
            # 签到完成后需要继续等下一天的签到时间
            # qd_startime += datetime.timedelta(1) #更新下次开始签到时间
            
            # cuurent_time = datetime.datetime.now() # 更新当前时间
            # wait_time = (qd_startime - cuurent_time).seconds; # 距离下次签到时间的秒数
            # logging.info('wait_time_seconds:%s'%wait_time)
            # count_down(wait_time) # 调用倒计时函数
          
            # qd_endtime += datetime.timedelta(1) #更新下次结束签到时间
            # qd_startime_default += datetime.timedelta(1) 
            # qd_startime_random += datetime.timedelta(1)
            
            
            
            qd_status = True #更新签到状态
        elif cuurent_time > qd_endtime or qd_status == True:
            print('%>_<% 已超过今天的 签到时间啦 %>_<%')               

            # wait_time_formatH = qd_startime - cuurent_time; # 距离下次的小时数
            # logging.info('wait_time_days:%s'%wait_time_formatH)
            
            # cuurent_time = datetime.datetime.now() # 更新当前时间
            # wait_time = (qd_startime - cuurent_time).seconds; # 距离下次签到时间的秒数
            # logging.info('wait_time_seconds:%s'%wait_time)
            # count_down(wait_time) # 调用倒计时函数

            # end_time_formatH = qd_endtime - cuurent_time;
            # logging.info('end_time_days:%s'%end_time_formatH)
            # end_time = (qd_endtime - cuurent_time).seconds;
            # logging.info('end_time_seconds:%s'%end_time)

            # print('type wait_time',type(wait_time))
            
            # print('选择下次签到时间：\n%s'%qd_startime)
            
        if qd_status == True:
           
            print('^_^ 今天已经签到过啦 ^_^')
            print('距离下次签到时间:')
            # cuurent_time = datetime.datetime.now() # 更新当前时间
            # wait_time = (qd_startime - cuurent_time).seconds; # 距离下次签到时间的秒数
            # logging.info('wait_time_seconds:%s'%wait_time)
            # count_down(wait_time) # 调用倒计时函数
            
            qd_endtime += datetime.timedelta(1) #更新下次结束签到时间
            qd_startime_default += datetime.timedelta(1) 
            qd_startime_random += datetime.timedelta(1)
            
            
            
         # wait_time = 3 # mock data
        cuurent_time = datetime.datetime.now() # 更新当前时间
        wait_time = (qd_startime - cuurent_time).seconds; # 距离下次签到时间的秒数
        logging.info('wait_time_seconds:%s'%wait_time)
        count_down(wait_time) # 调用倒计时函数
        
        times += 1
        qd_status = False #更新签到状态
            
