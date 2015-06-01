#coding:utf-8
#‪python C:\Users\lifeix\Desktop\adb_install.py
#‪python C:\Users\Haier\Desktop\adb_install.py
'''
author:yinzhuoqun
python version:3.4.2
version:v1.0
createtime:2015/6/1 23:45
'''
import os,re
from time import sleep
times=times1=1
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
def line():
	print('=======================================')	
while 1:
	deviceslist=dlist()
	if len(deviceslist)!=0:
		line()
		print('Your installation Number:%s'%times)
		times=times+1
		print("Please input apk path and press ENTER:")
		apkpath=input()
		apkpath=apkpath.strip()
		deviceslist=dlist()
		print('You have devices:%s'%len(deviceslist))
		if len(deviceslist)==0:
			continue
		for device in deviceslist:
			print('devicename:',device)
			install='adb -s %s install -r %s' %(device,apkpath)
			ins=os.system(install)	
		while apkpath=='' or ins!=0:
			print("Please input apk path and press ENTER:")
			apkpath=input()
			apkpath=apkpath.strip()
			deviceslist=dlist()
			print('You have devices:%s'%len(deviceslist))
			if len(deviceslist)==0:
				break
			for device in deviceslist:
				print('devicename:',device)
				install='adb -s %s install -r %s' %(device,apkpath)
				ins=os.system(install)
	else:
		line()
		print('Error: device not found,Please connection your device.[%s]'%times1)
		times1=times1+1;w=3
		while w>0:
			print('%s s'%w)
			w=w-1;sleep(1)