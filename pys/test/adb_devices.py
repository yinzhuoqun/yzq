#!/usr/bin/env python3
#coding:utf-8
import os,re
from time import sleep
def dlist1():
	pwd=os.getcwd()
	devicestxt='>'+pwd+r'\testde.txt'
	adbd='adb devices %s' %devicestxt
	deviceslist=[]
	list=[]
	listoff=[]
	os.system(adbd)
	#f=open("testde.txt")
	with open("testde.txt") as f:
		for line in f:
			liner=re.search(r'device\b',line)
			if liner==None:
				pass
				#listoff.append(line.strip())
			else:
				list.append(line.strip())
		#f.close()
	while os.path.exists(pwd+r'\testde.txt')==True:
		os.remove("testde.txt")
	for i in range(len(list)):
		yzq=list[i].split('\t')
		device=yzq[0]
		deviceslist.append(device)
	return deviceslist

def dlist():
	DevicesInfo=os.popen('adb devices')
	DevicesInfo=DevicesInfo.read();#print(DevicesInfo)
	DevicesList=re.findall(r'(.*?)\tdevice\b',DevicesInfo)
	return DevicesList
if os.name=='nt':	
	os.system('color 02')#只在windows可用
n=1;t=0
if t==0:
	while 1:
		deviceslist=dlist()
		print('deviceslist=%s'%deviceslist,'lenth=%s'%len(deviceslist),'times=%s'%n)
		n+=1
		sleep(3)
else:
	for x in range(10):	
		deviceslist=dlist()
		print('deviceslist=%s'%deviceslist,'lenth=%s'%len(deviceslist),'times=%s'%n)
		n+=1
		sleep(3)