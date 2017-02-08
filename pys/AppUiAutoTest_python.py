#!/usr/bin/env python3
#coding:utf-8
#from selenium import webdriver #selenium 
from appium import webdriver #appium 
import unittest
import os,re,time,random
import urllib.request

import logging
logging.basicConfig(level=logging.INFO)#有debug，info，warning，error等几个级别

#获取测试设备
def dlist():
	DevicesInfo=os.popen('adb devices')
	DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
	DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
	return DevicesList
deviceslist=dlist()
if len(deviceslist)!=0:
	device=deviceslist[0];print('getDeviceName:',device)	#自动选择第一台设备
	#device='4f25e81b';print('setDeviceName:',device	#手动设备名称	
else:
	print('error: device not found')
	
#清除指定包名的数据
packagename='com.l99.bed'
def adb_clear(device,packagename):
	clear='adb -s %s shell pm clear %s'%(device,packagename)
	try:
		print('Tips: clear the package data ...')
		os.system(clear)
	except Exception as e:
		print('error: clear the package data failed')
adb_clear(device,packagename)	

#StartActivity='com.l99.ui.login.Login'
StartActivity='com.l99.WelcomActivity'
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = device#'4f25e81b'#'4.4.2'
#desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk') # 指定安装包，未指定时运行已安装的包
desired_caps['appPackage'] = 'com.l99.bed'
desired_caps['appActivity'] = StartActivity
time.sleep(5)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

# 获取手机屏幕分辨率
def get_window_size():
	try:
		width=driver.get_window_size()['width']
		height=driver.get_window_size()['height']
		print('Window size: %s*%s'%(height,width))
		return height,width
	except IOError:
		print('error: get window size failed')
window_size_list=get_window_size()
if len(window_size_list)!=0:
	height=window_size_list[0]
	width=window_size_list[1]
	#print(type(height))
		
# 截图
img_save_path=r'I:/91UserData/ScreenCapture/work_summary' #img保存路径用左斜杠/
def get_screen():	
	time_sign=time.strftime("%Y-%m-%d_%H-%M-%S")	
	fileName=time_sign+".png"
	filePath=os.path.join(img_save_path,fileName)
	driver.get_screenshot_as_file(filePath)
	
#滑动 duration为ms
def my_swipe(x1,y1,x2,y2,times=1):
	for x in range(times):
		driver.swipe(start_x=x1,start_y=y1,end_x=x2,end_y=y2,duration=1000)
		
#id定位点击方法
def id_click(id_name):
	'''
	element=driver.find_element_by_id(id_name)
	element.click()
	time.sleep(2)
	return element
	'''
	times=1	#循环次数初始化
	timeout=10	#超时x秒
	elementList=driver.find_elements_by_id(id_name)
	while len(elementList)==0:
		elementList=driver.find_elements_by_id(id_name)	
		if times==timeout:
			print('error：not found %s'%id_name)
			break
		times+=1
		time.sleep(1)
		
	if len(elementList)!=0:
		element=elementList[0]
		element.click()
		return element
		
	else:
		print('error: no found %s'%id_name)

#从相同的id中随机选择一个
def ids_click_one(id_name):
	elementList=driver.find_elements_by_id(id_name)
	element=random.choice(elementList)
	element.click()
	time.sleep(2)
	return element
#text定位点击方法
def text_click(name):
	driver.find_element(by=By.PARTIAL_LINK_TEXT, value=name).click()
	time.sleep(2)

#uiautomator定位点击方法
def uiautomator_find_element(str):
	driver.find_element_by_android_uiautomator(str)
def uiautomator_find_elements():
	driver.find_elements_by_android_uiautomator('.elements()[1].cells()[2]')
	
#从api获取验证码
def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html
def get_SMS_Message(phoneNumber):
	url=r'http://guojia.api.l99.com/cgi-bin/vericode.py?mobilePhone=%s&appid=CS'%phoneNumber
	page = urllib.request.urlopen(url)
	msg = page.read().decode('utf-8')
	verCodeList=re.findall(r'\d\d\d\d\d\d',msg)
	if len(verCodeList)!=0:		
		return verCodeList[0]
	else:
		print('error：get SMS Message failed')

##登陆
id_login_btn='com.l99.bed:id/lead_btn'#登陆btn
id_login_name='com.l99.bed:id/username_login'#输入账号
id_login_pw='com.l99.bed:id/password_login'#输入密码
##注册
id_register='com.l99.bed:id/register_in_login'#注册
id_register_btn='com.l99.bed:id/register__btn'#注册btn
#验证手机号码
id_register_phonenumber='com.l99.bed:id/layout_edit_text'
#id_register_phonenumber='com.l99.bed:id/phone_register_num'
#id_register_pw='com.l99.bed:id/phone_register_password'
#id_register_confirm_pw='com.l99.bed:id/confirm_phone_register_password'
id_set_id_next='com.l99.bed:id/next' #手机号码下一步
##输入验证码
id_input_center_ver='com.l99.bed:id/text_center_ver'#输入验证码
id_center_ver_next='com.l99.bed:id/next'#验证码下一步
#设置密码
id_password='com.l99.bed:id/text_center_ver'
id_set_password_next='com.l99.bed:id/next'

##填写个人资料
id_register_avatar='com.l99.bed:id/register_avatar' #头像
id_take_photo='com.l99.bed:id/take_photo'#拍摄照片
id_select_album='com.l99.bed:id/select_album'#相册选择
id_avatar_cancel='com.l99.bed:id/cancel'#选择照片取消按钮
id_avatar_internet='com.l99.bed:id/select_internet_avaters'#网络选取头像
id_avatar='com.l99.bed:id/internet_avater'#选择网络头像

id_register_name='com.l99.bed:id/nick_name_ew'#昵称  

id_register_man='com.l99.bed:id/male'#sex man
id_register_female='com.l99.bed:id/female'#sex female
id_sex_ok='com.l99.bed:id/confirm'#性别确定按钮

id_register_birthday='com.l99.bed:id/register_birthday_edit'#birthday
id_birthdat_ok='android:id/button1'#生日确定按钮
id_birthdat_cancel='android:id/button2'#生日取消按钮
id_info_next='com.l99.bed:id/avatar_next'#立即注册

#导航栏id
id_nice='com.l99.bed:id/nice_layout' #发现
id_category='com.l99.bed:id/category_layout' #社区
id_rank='com.l99.bed:id/rank_layout' #排行
id_msg='com.l99.bed:id/msg_layout' #消息
id_personal='com.l99.bed:id/personal_layout' #我

#我页面
id_personal_hearder='com.l99.bed:id/headerlayout'#个人信息栏

#自己的主页
id_personal_avatar='com.l99.bed:id/avatar'#头像


#每日登陆奖励
id_get_award='com.l99.bed:id/get_award'#领取奖励
id_become_vip='com.l99.bed:id/become_vip'#开通vip


###################################################

#引导页滑动
try:
	#my_swipe(216,1280,864,1280,3)	#1080p  
	x1=width/5;y1=int(height/3*2);x2=width-width/5;y2=int(height/3*2)
	my_swipe(x1,y1,x2,y2,3)	#Auto 竖屏
except Exception as e:
	print('error: guide-login-page swipe failed!')


#验证手机号码
id_click(id_register_btn)
phonePosition=id_click(id_register_phonenumber)
phoneNumber='14533331195'
phonePosition.send_keys(phoneNumber)
get_screen()
id_click(id_set_id_next)

#填写验证码
verCode=get_SMS_Message(phoneNumber)
verCodePosition=id_click(id_input_center_ver)
verCodePosition.send_keys(verCode)
get_screen()
id_click(id_center_ver_next)

#设置密码
passwordPositon=id_click(id_password)
password='q1234567'
passwordPositon.send_keys(password)
get_screen()
id_click(id_set_password_next)

###填写个人资料
#头像
id_click(id_register_avatar)#点击上传头像


#id_click(id_avatar_internet)#点击从网络头像
#ids_click_one(id_avatar)#随机选择一张头像
#id_click(id_avatar)#选择第一张头像
id_click(id_take_photo)
id_click('com.android.camera:id/v6_shutter_button_internal') #小米3拍照
id_click('com.android.camera:id/v6_btn_done')#确定
id_click('com.l99.bed:id/save')#保存
#昵称
#name='13147758520'
name=random.randint(111111,999999)
namePositon=id_click(id_register_name) 
namePositon.send_keys(name)

#driver.hide_keyboard()	#收起键盘
#性别
id_register_sex_list=[id_register_man,id_register_female]	#性别列表
id_click(random.choice(id_register_sex_list))	#随机选择性别
#id_click(id_register_female)
id_click(id_sex_ok)	#性别确定按钮
#选择生日
id_click(id_register_birthday)
try:
	'''
	#1080p
	for x in range(random.randint(1,3)):
		my_swipe(330,800,300,height-300,1)
	for x in range(random.randint(1,3)):
		my_swipe(600,800,600,height-300,1)
	for x in range(random.randint(1,3)):
		my_swipe(800,800,800,height-300,1)

	#720p
	for x in range(random.randint(1,3)):
		my_swipe(150,570,150,940,1)
	for x in range(random.randint(1,3)):
		my_swipe(350,570,380,1000,1)
	for x in range(random.randint(1,3)):
		my_swipe(520,580,520,950,1)
	'''
	#Auto
	for x in range(random.randint(1,3)):
		my_swipe(width/3,height/5*2,width/3,height-300,1)
	for x in range(random.randint(1,3)):
		my_swipe(width/3*2,height/5*2,width/3*2,height-300,1)
	for x in range(random.randint(1,3)):
		my_swipe(width-100,height/5*2,width/3*2,height-300,1)
except Exception as e:
	print('error: birthday swipe failed!')
id_click(id_birthdat_ok)#生日确定按钮
#立即注册
get_screen()
id_click(id_info_next)
get_screen()

#time.sleep(2)#等待2s
id_click(id_get_award)#领取奖励
id_click(id_personal)#切换到我
id_click(id_personal)#切换到我
get_screen()
id_click(id_personal_hearder)#点击我的信息
#time.sleep(2)
get_screen()
for x in range(3):
	id_click(id_personal_avatar)#点击我的头像
	get_screen()


