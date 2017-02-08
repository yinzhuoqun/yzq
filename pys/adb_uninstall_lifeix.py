#!/usr/bin/env python3
#coding:utf-8
'''
author:yinzhuoqun
python version:3.4.2
'''
import os,re
from time import sleep
def dlist():
	DevicesInfo=os.popen('adb devices')
	DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
	DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
	return DevicesList

if os.name=='nt':
	os.system('color 02')	
	
print('author:yinzhuoqun\n')

deviceslist=dlist()
if len(deviceslist)!=0:
	
	#print('you have devices:%s'%len(deviceslist))
	
	packageNameList=['com.l99.bed','com.lifeix.headline','com.l99.lotto']
	#packagename=input('输入1或直接按Enter卸载床上，输入2卸载体育头条，输入3卸载大赢家，其他请输入包名：')
	packagename=input('输入1或直接按Enter卸载床上，输入2卸载体育头条，输入3卸载大赢家，其他请输入包名：')
	packagename=packagename.strip()#去掉首尾空格
		
	if len(packagename)==0 or packagename=='1':
		packagename='com.l99.bed'
	elif packagename=='2':
		packagename='com.lifeix.headline'
	elif packagename=='3':
		packagename='com.l99.lotto'
	
	
	#set packagename设置包名后可一键卸载
	#packagename='com.l99.bed'	
	#packagename='com.lifeix.headline'	#体育头条
	#packagename='com.yzq.meid'	#printMeid
	#packagename='com.l99.lotto'	#大赢家
	#packagename='com.lecture.media'	#百家讲坛
	#packagename='com.qzone'	#qq空间
	
	
	print('uninstall packagename: %s'%packagename)
	if len(deviceslist)==1:
		#print('uninstalling packagename: %s'%packagename)
		device=deviceslist[0]
		print('devicename:',device)
		uninstall='adb -s %s uninstall %s'%(device,packagename)
		os.system(uninstall)
	elif len(deviceslist)!=1:
		db_devices={}
		number=1
		for device in deviceslist:
			db_devices[number]=device
			number+=1
		print('dict_devices:',db_devices)
		run=input('please choose device number from dict_devices:')
		while len(re.findall(r'\D',run))!=0:
			run=input('please choose device number from dict_devices:')
		if 	len(run)==0 or int(run)>len(db_devices):
			print('(You choice all devices)')
			#print('uninstalling packagename: %s'%packagename)
			for device in deviceslist:
				print('devicename:',device)
				uninstall='adb -s %s uninstall %s'%(device,packagename)
				os.system(uninstall)
		elif int(run)<=len(db_devices):
			device=db_devices[int(run)]
			print('uninstall packagename: %s'%packagename)
			print('devicename:',device)
			uninstall='adb -s %s uninstall %s'%(device,packagename)
			os.system(uninstall)
	sleep(3)
else:
	if os.name=='nt':
		os.system('color 0C')
	print('error: device not found')
	sleep(3)