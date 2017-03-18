#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('Author:yinzhuoqun') 

from platform import python_version	#导入当前运行的python版本号
import re,os,time

def out_eq():
	out_eq_count=40
	print('='*out_eq_count)

def version_status():
	Write_Python_version='3.4.3' #编写脚本的python版本
	writelist=re.split('\D',Write_Python_version)#print(writelist)
	Write_version=writelist[0]#print(Write_version)
	Currentlist=re.split('\D',python_version())#print(Currentlist)
	Current_version=Currentlist[0]#print(Current_version)
	if Current_version!=Write_version:
		print(u'Python 版本不兼容!')
		return 0
	else:
		return 1
		
def dlist():
	DevicesInfo=os.popen('adb devices')
	DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
	DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
	return DevicesList
	
def stop_run():
	stop_run=input('请按ENTER键再次运行...\n')
	if len(stop_run)>=0:
		pass
		
phone_ip='192.168.68.146' #adbWireless 显示的ip
phone_ip='192.168.66.89' #adbWireless 显示的ip
phone_ip='192.168.68.56' #adbWireless 显示的ip
#phone_ip='172.16.251.3' #adbWireless 显示的ip

input_list=['L','D','l','d','G','g','']

if os.name=='nt':
	os.system('color 02')

connectTimes=1
while 1:
	connect_command='adb connect %s'%phone_ip
	disconnect_command='adb disconnect %s'%phone_ip

	print('\n当前选择的 设备IP 是: %s'%phone_ip)
	connetHint='请选择运行的指令 (连接/断开设备：Enter，更换设备：设备IP ):\n'
	choice_command=input(connetHint)

	if choice_command=='' and connectTimes%2==1:
		print('连接设备...')
		os.system(connect_command)
	elif choice_command=='' and connectTimes%2==0:
		print('断开设备...')
		os.system(disconnect_command)
	elif len(choice_command)!=0:
		phone_ip=choice_command		
		while len(phone_ip)==0:
			phone_ip=input("请输入 设备IP：")
			
		'''
		ping_result=os.popen('ping %s'%phone_ip);
		readPIng=ping_result.read();#print(readPIng)
		percent0=re.findall('(丢失 = 4 (100% 丢失))',readPIng);print(percent0)
		if len(percent0)==0:
			os.system(connect_command)
		else:
			print('警告：请检查是否在同一局域网')
			print(readPIng)
		'''
		connect_command='adb connect %s'%phone_ip
		os.system(connect_command)
		
	connectTimes+=1
	#stop_run()
	