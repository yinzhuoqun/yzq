#!/usr/bin/env python3
# coding:utf-8
# from selenium import webdriver #selenium
___author___ = 'yinzhuoqun'
___version___ = '1.0'
___appVersion__ = '4.7.8'

from appium import webdriver  # appium
import unittest, HTMLTestRunner
import os, re, time, datetime
# import random
# import urllib.request

import logging
logging.basicConfig(level=logging.INFO)  # 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别


# 登陆
id_login_btn = 'com.l99.bed:id/lead_btn'  # 登陆btn
id_login_name = 'com.l99.bed:id/username_login'  # 输入账号
id_login_pw = 'com.l99.bed:id/password_login'  # 输入密码
# 注册
id_register = 'com.l99.bed:id/register_in_login'  # 注册
id_register_btn = 'com.l99.bed:id/register__btn'  # 注册btn
# 验证手机号码
id_register_phonenumber = 'com.l99.bed:id/layout_edit_text'
# id_register_phonenumber='com.l99.bed:id/phone_register_num'
# id_register_pw='com.l99.bed:id/phone_register_password'
# id_register_confirm_pw='com.l99.bed:id/confirm_phone_register_password'
id_set_id_next = 'com.l99.bed:id/next'  # 手机号码下一步
# 输入验证码
id_input_center_ver = 'com.l99.bed:id/text_center_ver'  # 输入验证码
id_center_ver_next = 'com.l99.bed:id/next'  # 验证码下一步
# 设置密码
id_password = 'com.l99.bed:id/text_center_ver'
id_set_password_next = 'com.l99.bed:id/next'

# 填写个人资料
id_register_avatar = 'com.l99.bed:id/register_avatar'  # 头像
id_take_photo = 'com.l99.bed:id/take_photo'  # 拍摄照片
id_select_album = 'com.l99.bed:id/select_album'  # 相册选择
id_avatar_cancel = 'com.l99.bed:id/cancel'  # 选择照片取消按钮
id_avatar_internet = 'com.l99.bed:id/select_internet_avaters'  # 网络选取头像
id_avatar = 'com.l99.bed:id/internet_avater'  # 选择网络头像

id_register_name = 'com.l99.bed:id/nick_name_ew'  # 昵称

id_register_man = 'com.l99.bed:id/male'  # sex man
id_register_female = 'com.l99.bed:id/female'  # sex female
id_sex_ok = 'com.l99.bed:id/confirm'  # 性别确定按钮

id_register_birthday = 'com.l99.bed:id/register_birthday_edit'  # birthday
id_birthdat_ok = 'android:id/button1'  # 生日确定按钮
id_birthdat_cancel = 'android:id/button2'  # 生日取消按钮
id_info_next = 'com.l99.bed:id/avatar_next'  # 立即注册

# 导航栏id
id_nice = 'com.l99.bed:id/nice_layout'  # 发现
id_category = 'com.l99.bed:id/category_layout'  # 社区
id_rank = 'com.l99.bed:id/rank_layout'  # 排行
id_msg = 'com.l99.bed:id/msg_layout'  # 消息
id_personal = 'com.l99.bed:id/personal_layout'  # 我

# 我页面
id_personal_hearder = 'com.l99.bed:id/headerlayout'  # 个人信息栏

# 自己的主页
id_personal_avatar = 'com.l99.bed:id/avatar'  # 头像


# 每日登陆奖励
id_get_award = 'com.l99.bed:id/get_award'  # 领取奖励
id_become_vip = 'com.l99.bed:id/become_vip'  # 开通vip

'''
# 百度外卖
es=driver.find_element_by_xpath("//android.view.View[@index='4']")
es.click()
get_screen()

es=driver.find_element_by_xpath("//android.view.View[@index='0']")
es.click()
get_screen()

es=driver.find_element_by_xpath("//android.view.View[@index='1']")
es.click()
get_screen()

es=driver.find_element_by_xpath("//android.view.View[@index='2']")
es.click()
get_screen()

es=driver.find_element_by_xpath("//android.view.View[@index='3']")
es.click()
get_screen()
'''

# 指定启动的包名和启动的activity
packageName = 'com.l99.bed'
# packageName = 'com.baidu.lbs.waimai'
# StartActivity='com.l99.ui.login.Login'
StartActivity = 'com.l99.WelcomActivity'
# StartActivity = 'com.baidu.lbs.waimai.SplashActivity'

img_save_path = r'I:/91UserData/ScreenCapture/work_summary'  # windows img保存路径用左斜杠/
desktop = os.path.join(os.path.expanduser("~"), "Desktop")  # 桌面
logging.info(desktop)
if os.path.exists(img_save_path) == False:
    os.chdir(desktop)
    mydir = 'AppUiAutoTestPic'
    img_save_path_new = os.path.join(desktop,mydir)
    if os.path.exists(img_save_path_new) != True:
        os.mkdir(mydir)
    img_save_path = img_save_path_new
    logging.info(img_save_path)

# 包的路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def dlist():
    # 获取测试设备列表函数
    DevicesInfo = os.popen('adb devices')
    DevicesInfo = DevicesInfo.read();  # print(DevicesInfo)
    DevicesList = re.findall(r'(.*?)\tdevice\b', DevicesInfo)

    if len(DevicesList) != 0:
        device = DevicesList[-1];  # 自动选择最后一台连接的设备
        # device = '4f25e81b';print('setDeviceName:',device）	#三星note2 手动设备名称
        # device = '1d04f6f'  # 米3黑
        print('getDeviceName:', device)

    else:
        device = False
        print('error: device not found')

    return device


device = dlist()  # 获取设备列表


def adb_clear(device, package):
    # 清除指定包名的数据函数
    clear = 'adb -s %s shell pm clear %s' % (device, package)
    try:
        print('clear the package data ...')
        os.system(clear)
    except Exception as e:
        print('error: clear the package data failed')


adb_clear(device, packageName)  # 清除数据命令


class app(unittest.TestCase):

    def setUp(self):
        #初始化工作

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = device

        # desired_caps['app'] = PATH(r'C:\Users\yzq\Desktop\chuangshang_anzhi.4.7.8.build139.release.bedigest1.apk')
        # desired_caps['app'] = app
        # 指定安装包，未指定时运行已安装的包
        desired_caps['appPackage'] = packageName
        desired_caps['appActivity'] = StartActivity
        # desired_caps['automationName']='Selendroid'#Android 2.3到4.3
        desired_caps['unicodeKeyboard'] = 'true'  # Android 可以支持输入 Unicode 字符
        desired_caps['resetKeyboard'] = 'true'  # 关闭 Appium 的 Unicode 键盘
        #desired_caps['newCommandTimeout'] = '999' #命令超时时间
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 服务监听

    def tearDown(self):
        #退出清理工作

        #time.sleep(60)
        #self.driver.close_app()
        self.driver.quit()
        logging.info('teardown')

    # 获取手机屏幕分辨率函数
    def get_window_size(self):
        try:
            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            print('Window size: %s*%s' % (height, width))
            return height, width
        except IOError:
            print('error: get window size failed')
            return False

        window_size_list = get_window_size(self)  # 获取手机屏幕分辨率
        if window_size_list != False:
            height = window_size_list[0];  # print(type(height))
            width = window_size_list[1]

    # 截图
    def get_screen(self):
        time_sign = time.strftime("%Y-%m-%d_%H-%M-%S")
        fileName = time_sign + ".png"
        filePath = os.path.join(img_save_path, fileName)
        self.driver.get_screenshot_as_file(filePath)
        if os.path.exists(filePath) == True:
            print('get screen success')
        else:
            print('get screen failed')

    # 滑动 duration为ms
    def my_swipe(self, x1, y1, x2, y2, times=1):
        for x in range(times):
            self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y2, duration=1000)

    def test_login(self):
        # 具体的测试用例，一定要以test开头

        self.get_window_size()
        #self.driver.implicitly_wait(7)  # 隐式等待
        time.sleep(10)
        button_register = self.driver.find_element_by_name(u"注册")
        button_register.click()
        self.get_screen()
        button_back = self.driver.find_element_by_xpath("//android.widget.TextView[@index='0']")  # back
        button_back.click()
        self.get_screen()
        button_login = self.driver.find_element_by_name(u"登录")
        button_login.click()
        self.get_screen()

        edit_id = self.driver.find_element_by_name(u"床号/手机号")
        # edit_id = self.driver.find_element_by_xpath("//android.widget.EditText/index[2]")

        edit_id.click()
        self.get_screen()
        edit_id.send_keys(9418482)  # 账号
        self.get_screen()

        # edit_password_list=self.driver.find_elements_by_id('com.l99.bed:id/layout_edit_text');#print(len(edit_password_list))
        # edit_password_id=edit_password_list[1] # 选择密码输入框

        edit_password_id = self.driver.find_element_by_xpath("//android.widget.EditText[@NAF='true']")
        # driver.find_elements_by_xpath("//android.widget.ImageView[@NAF='true'][@index=1]")
        edit_password_id.click()
        edit_password_id.send_keys(123456789)  # 密码


        # a="//android.widget.EditText[@index='1']"
        # a="/android.widget.FrameLayout[@index='4']"
        # edit_password = self.driver.find_element_by_xpath(a)  # 点击密码输入区
        # edit_password.click()
        # edit_password.send_keys(123456789)

        self.get_screen()

        button_into1 = self.driver.find_elements_by_name(u"登录")
        button_into = button_into1[1]
        # button_into = self.driver.find_element_by_id("com.l99.bed:id/next")

        button_into.click()
        self.get_screen()

        time.sleep(3)
        #self.driver.quit() # 此处不应有 driver.quit
        #test_loginout()


    def test_loginout(self):
        self.driver.implicitly_wait(7)  # 隐式等待
        for x in range(3):
            os.system('adb shell input tap 50 50')

        button_my = self.driver.find_element_by_id(u"com.l99.bed:id/tv_me")
        for x in range(1):
            button_my.click()

        button_set = self.driver.find_element_by_id('com.l99.bed:id/iv_iv_top_option')
        for x in range(1):
            button_set.click()

        for x in range(3):
            os.system('adb shell input tap 50 50')

        button_loginout = self.driver.find_element_by_id('com.l99.bed:id/id_settings_exit')
        button_loginout.click()

        button_confirm_loginout = self.driver.find_element_by_id('com.l99.bed:id/confirm')
        button_confirm_loginout.click()

if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(app('test_login'))
    # timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
    # reportPath = r'C:\Users\lifeix\Desktop'
    # filename = 'TestReport%s.html' % timestr
    # filepath = os.path.join(reportPath, filename)
    # if os.path.exists(reportPath) == False:
    #     filepath = os.path.join(desktop, filename)
    # fp = open(filepath, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'TestReport',
    #     description=u'TestReport'
    # )
    # runner.run(suite)
    # fp.close()
    # if os.path.exists('TestReport%s.html' % timestr) == True:
    #     print('TestReport save to %s' % filename)
