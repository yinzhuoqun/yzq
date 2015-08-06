#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Write_Python_version='3.4.3'
from platform import python_version
import re,os
def out_eq():
	out_eq_count=40
	print('='*out_eq_count)
def version_status():
	writelist=re.split('\D',Write_Python_version)#print(writelist)
	Write_version=writelist[0]#print(Write_version)
	Currentlist=re.split('\D',python_version())#print(Currentlist)
	Current_version=Currentlist[0]#print(Current_version)
	if Current_version!=Write_version:
		print(u'Python 版本不兼容!')
		#out_eq()
		return 0
	else:
		#print(u'Python 版本兼容。')
		#out_eq()
		return 1
#out_eq()
#print('Current Python version',python_version())
#print('Write Python version',Write_Python_version)
print('Author:yinzhuoqun') 
#out_eq()
version=version_status()
#设置提示语言
language_db={1:'chinese',2:'english'}
language=language_db[1]
if version==1:
	from time import sleep
	times=times1=1
	#获取设备列表函数
	def dlist():
		pwd=os.getcwd()
		devicestxt='>'+pwd+r'\testde.txt'
		adbd='adb devices %s' %devicestxt
		deviceslist=[];list=[];listoff=[]
		os.system(adbd)
		f=open("testde.txt")
		for line in f:
			liner=re.search(r'device\b',line)
			if liner==None:
				pass
			else:
				list.append(line.strip())
		f.close()
		os.remove("testde.txt")
		for i in range(len(list)):
			yzq=list[i].split('\t')
			device=yzq[0]
			deviceslist.append(device)
		return deviceslist
	#输出等于号函数
	def line(num):
		print('='*num)
	#输出未发现设备超时函数
	def nodevice_error():
		if language==u'chinese':
			print(u'错误：没发现设备，请连接你的设备。[%s]'%times1)
		else:
			print('Error: not found device,Please connection your device.[%s]'%times1)
		times1=times1+1;w=3
		while w>0:
			print('%s s'%w)
			w=w-1;sleep(1)
	#输入函数
	def input_timeout(run):
		if language==u'chinese':
			run['data']=input(u'请从设备序号表中选择需要安装设备的序号：')
		else:
			run['data']=input('Please input device number from dict_devices:')
		#return run
	def color():
		import random
		try:
			colorlist=['02','03','04','05','06','08','09','0A','0B','0C','0D','0E']
			color=random.choice(colorlist);#print(color)
			color='02'
			command='color '+color
			os.system(command)
		except Exception as e:
			print('Error:change to color font color failure!')
	while 1:
		deviceslist=dlist()
		if len(deviceslist)!=0:
			color()
			print('')
			#line(40)
			if language==u'chinese':
				print(u'你的安装次数：第%s次'%times)
			else:
				print('Your are install times:%s'%times)
			times=times+1
			apkpath='Ture';ins=1
			while apkpath==None or ins!=0:
				if language==u'chinese':
					print(u'请输入apk的路径并按下ENTER键：')
				else:
					print("Please input apk path and press ENTER:")
				apkpath=input()
				while os.path.exists(apkpath)==False:
					if language==u'chinese':
						print(u'请输入apk的路径并按下ENTER键：')
					else:
						print("Please input apk path and press ENTER:")
					apkpath=input()
				apkpath=apkpath.strip()
				deviceslist=dlist()
				if len(deviceslist)==1:
					if language==u'chinese':
						print(u'你有设备：%s台'%len(deviceslist))
					else:
						print('You have devices:%s'%len(deviceslist))
					device=deviceslist[0]
					if language==u'chinese':
						print(u'设备名称：',device)
					else:
						print('devicename:',device)
					install='adb -s %s install -r %s' %(device,apkpath)
					ins=os.system(install)
				elif len(deviceslist)>=2:
					if language==u'chinese':
						print(u'你有设备：%s台'%len(deviceslist))
					else:
						print('You have devices:%s'%len(deviceslist))
					#print('Deviceslist',deviceslist)
					db_devices={}
					number=1
					for device in deviceslist:
						db_devices[number]=device
						number+=1
					if language==u'chinese':
						print(u'设备对应的序号表：',db_devices)
					else:
						print('dict_devices:',db_devices)
					#设置超时 True OR False和超时时间
					timeout_set=False
					timeout_value=3					
					if timeout_set==True:
						if language==u'chinese':
							print(u'（%s秒钟后自动安装全部设备。）'%timeout_value)
						else:
							print('(Auto choice all after %s seconds.)'%timeout_value)
					#超时自动选择
					if timeout_set==True:
						import threading
						run={'data':'a'}
						t=threading.Thread(target=input_timeout,args=(run,))						
						t.start()
						print('\n')
						#print('(Auto choice all)\n')
						t.join(timeout_value)	#等待时间
						run=run['data']						
					else:
						if language==u'chinese':
							run=input(u'请从设备序号表中选择需要安装设备的序号：')
						else:
							run=input('Please input device number from dict_devices:')
					if 	len(run)==0 or run>str(len(db_devices)):
						if language==u'chinese':
							print(u'（你选择了安装全部设备）')
						else:
							print('(You choice all devices)')
						for device in deviceslist:						
							if language==u'chinese':
								print(u'设备名称：',device)
							else:
								print('devicename:',device)
							install='adb -s %s install -r %s' %(device,apkpath)
							ins=os.system(install)
							#print('ins1',ins)
					elif run<=str(len(db_devices)):
						device=db_devices[int(run)]
						if language==u'chinese':
							print(u'设备名称：',device)
						else:
							print('devicename:',device)
						install='adb -s %s install -r %s' %(device,apkpath)
						ins=os.system(install)
						#print('ins0',ins)
				else:
					break
		else:
			os.system('color 0C')
			import sys
			for i in range(3):
				sleep(1)
				if language==u'chinese':
					if times1<=60:
						sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%ss]\r'%times1)
						sys.stdout.flush()
					else:
						a=int(times1/60);#print('a',a)
						b=times1%60;#print('b',b)
						sys.stdout.write(u'错误：没发现设备，请连接你的设备。[%smin%ss]\r'%(a,b))
						sys.stdout.flush()
				else:
					if times1<=60:
						sys.stdout.write('Error: not found device,Please connection your device.[%ss]\r'%times1)
						sys.stdout.flush
					else:
						a=int(times1/60);#print('a',a)
						b=times1%60;#print('b',b)
						sys.stdout.write('Error: not found device,Please connection your device.[%smin%ss]\r'%(a,b))
						sys.stdout.flush()
				times1+=1
else:
	from time import sleep
	sleep(3)