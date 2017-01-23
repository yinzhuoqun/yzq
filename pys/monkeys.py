#coding:utf-8
#‪python C:\Users\lifeix\Desktop\monkeys.py
#‪python C:\Users\Haier\Desktop\monkeys.py
'''
author:yinzhuoqun
python version:3.4.2
'''
import os,time,re
from time import sleep
times=times1=1
#下句是设置临时python34的环境变量语句
#import os;setpath=r'set path=%path%;c:\Python34';os.system(setpath)
def times():
	print('Not found device,Please connect your device and restart the Script.')
	w=3
	while w>0:
		print('%s s'%w)
		w=w-1;time.sleep(1)
def notice():
	print("Make sure your device is connected,Please input apk path and press ENTER:")
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
def installapk():
	deviceslist=dlist()
	if len(deviceslist)!=0:
		print("Make sure your device is connected,Please input apk path and press ENTER:")
		apkpath=input()
		apkpath=apkpath.strip()
		deviceslist=dlist()
		print('You have devices:%s'%len(deviceslist))
		for device in deviceslist:
			print('devicename:',device)
			install='adb -s %s install -r %s' %(device,apkpath)
			ins=os.system(install)	
		while apkpath=='' or ins!=0:
			print("Make sure your device is connected,Please input apk path and press ENTER:")
			apkpath=input()
			apkpath=apkpath.strip()
			deviceslist=dlist()
			print('You have devices:%s'%len(deviceslist))
			for device in deviceslist:
				print('devicename:',device)
				install='adb -s %s install -r %s' %(device,apkpath)
				ins=os.system(install)
		return apkpath
	else:
		times()
apkpath=installapk()
deviceslist=dlist()
if len(deviceslist)!=0:
	#包名
	pwd=os.getcwd()
	txt='>'+pwd+r'\testpa.txt'
	aapt='aapt dump badging %s %s' %(apkpath,txt)
	os.system(aapt)
	pa=open("testpa.txt",encoding='UTF-8')
	str=pa.read()
	package1=re.search(r"(name='(.+?)' versionCode=')",str,re.S)
	a=package1.group(2)
	b=a.strip()
	print("package name:",b)
	pa.close()
	os.remove("testpa.txt")
	#事件
	print("Please input monekey evnet count(number) and press ENTER:")
	evnet=input()
	while evnet=='' or re.findall('[^0-9]',evnet):
		print("Please input monekey evnet count(number) and press ENTER:")
		evnet=input()
	#展现形式
	list2=['y','n','Y','N']
	print("Do you need to save a .txt file? please input y/n and press ENTER.")
	outputstyle=input()
	while outputstyle not in list2:
		print("Do you need to save a .txt file? please input y/n and press ENTER.")
		outputstyle=input()
	#定义monkey
	def monkeyt(device,b,evnet,txt):
		monkey='adb -s %s shell monkey -p %s -s 250 --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 50 -v -v -v %s %s' %(device,b,evnet,txt)
		os.system(monkey)
		print(filename+' save in',pwd)
	def monkeyc(device,b,evnet):
		monkey='adb -s %s shell monkey -p %s -s 250 --throttle 50 -v -v -v %s' %(device,b,evnet)
		os.system(monkey)
	#运行monkey
	if outputstyle=='y' or outputstyle=='Y':
		for device in deviceslist:
			print('devicename:',device)
			#t=time.strftime("%Y%m%d%H%M%S")
			t=time.strftime("%m%d%H%M%S")
			filename=b+'_mklog'+t+'.txt'
			txt='>>'+pwd+r'\\'+filename
			monkeyt(device,b,evnet,txt)
	else:
		for device in deviceslist:
			print('devicename:',device)
			monkeyc(device,b,evnet)
else:
	times()