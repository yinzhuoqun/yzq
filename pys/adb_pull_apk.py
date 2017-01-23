#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('Author:yinzhuoqun\n')

Write_Python_version = '3.4.3'
from platform import python_version
from time import sleep
import re,os,time

def version_status():
	writelist = re.split('\D', Write_Python_version)  # print(writelist)
	Write_version = writelist[0]  # print(Write_version)
	Currentlist = re.split('\D', python_version())  # print(Currentlist)
	Current_version = Currentlist[0]  # print(Current_version)
	if Current_version != Write_version:
		print(u'Python 版本不兼容!')
		sleep(3)
		return 0
	else:
		return 1
		
def stop_run():
	stop_run=input('请按ENTER键停止运行...\n')
	if len(stop_run)>=0:
		pass
		
def dlist():
	DevicesInfo=os.popen('adb devices')
	DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
	DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
	return DevicesList
	
def englishname_to_chinesename(path,chinesename):
	#取出路径的目录名和文件名
	tuple_path_file=os.path.split(path)
	file=tuple_path_file[1]#目录名
	###分离文件名与扩展名
	tuple_filename_filepro=os.path.splitext(file)
	#连接目录与旧文件名
	tempname=chinesename
	os.chdir(tuple_path_file[0])
	os.rename(tuple_path_file[1],tempname)
	new_path=os.path.join(tuple_path_file[0],tempname)
	
if os.name=='nt':	
	os.system('color 02')

run = version_status()
if run==1:
	packageName=''
	packageNameTemp='com.l99.bed' #设置后不会弹出输入包名输入框
	#packageNameTemp='com.lecture.media' #设置后不会弹出输入包名输入框
	#packageNameTemp='com.netease.gameforums' #设置后不会弹出输入包名输入框
	#packageNameTemp='com.netease.newsreader.activity' #设置后不会弹出输入包名输入框
	#packageNameTemp='com.tencent.mm' #设置后不会弹出输入包名输入框
	#packageNameTemp='com.yzq.meid' #设置后不会弹出输入包名输入框

	deviceslist=dlist()
	
	if len(deviceslist)==1:
			
		while len(packageName)==0:
			print('(直接按下 Enter 键选择导出 %s)'%packageNameTemp)
			packageName=input('请输入需要导出apk的包名：')
			if len(packageName)==0:
				packageName=packageNameTemp
				
		print('正在尝试导出：%s'%packageName)	
		pm_path_command='adb shell pm path %s'%packageName			
		apkPath=os.popen(pm_path_command).read();#print(apkPath,type(apkPath))
		apkPathlist=re.findall(r'package:(.+?.apk)',apkPath);#print(apkPathlist)
		if len(apkPathlist)!=0:
			#文件手机存的路径
			apkPathValue=apkPathlist[0];#print(apkPathValue)
			deskTopPath=os.path.join(os.path.expanduser("~"),"Desktop")	#保存至桌面
			adb_push_command='adb pull %s %s'%(apkPathValue,deskTopPath)
			os.system(adb_push_command)
			tuple_path_file=os.path.split(apkPathValue)
			apk_name=tuple_path_file[1]
			apk_path=os.path.join(deskTopPath,apk_name)
			t = time.strftime("%m-%d_%H-%M-%S")
			apkNewName=packageName+'_'+t+'.apk'
			englishname_to_chinesename(apk_path,apkNewName)
			apk_pc_path=os.path.join(deskTopPath,apkNewName)
			if os.path.exists(apk_pc_path)==True:
				print('文件保存的路径是：%s\n'%apk_pc_path)
		else:
			print('警告：未发现此包名的apk')
	elif len(deviceslist)>1:
		while len(packageName)==0:
			print('(直接按下 Enter 键选择导出 %s)'%packageNameTemp)
			packageName=input('请输入需要导出apk的包名：')
			if len(packageName)==0:
				packageName=packageNameTemp
				
		db_devices={};number=1
		for device in deviceslist:
			db_devices[number]=device
			number+=1
		print(u'设备对应的序号表：',db_devices)
		
		deviceNumber=input(u'请从设备序号表中选择需要安装设备的序号：')
		device=db_devices[int(deviceNumber)]
		
		print('正在尝试导出：%s'%packageName)	
		pm_path_command='adb -s %s shell pm path %s'%(device,packageName)
			
		apkPath=os.popen(pm_path_command).read();#print(apkPath,type(apkPath))
		apkPathlist=re.findall(r'package:(.+?.apk)',apkPath);#print(apkPathlist)
		if len(apkPathlist)!=0:
			#文件手机存的路径
			apkPathValue=apkPathlist[0];#print(apkPathValue)
			deskTopPath=os.path.join(os.path.expanduser("~"),"Desktop")	#保存至桌面
			adb_push_command='adb -s %s pull %s %s'%(device,apkPathValue,deskTopPath)
			os.system(adb_push_command)
			tuple_path_file=os.path.split(apkPathValue)
			apk_name=tuple_path_file[1]
			apk_path=os.path.join(deskTopPath,apk_name)
			t = time.strftime("%m-%d_%H-%M-%S")
			apkNewName=packageName+'_'+t+'.apk'
			englishname_to_chinesename(apk_path,apkNewName)
			apk_pc_path=os.path.join(deskTopPath,apkNewName)
			if os.path.exists(apk_pc_path)==True:
				print('文件保存的路径是：%s\n'%apk_pc_path)
		else:
			print('警告：未发现此包名的apk')
	
	
	else:
		print('错误：未发现设备')
	stop_run()