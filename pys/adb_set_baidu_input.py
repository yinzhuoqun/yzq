#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Write_Python_version='3.4.3'
from platform import python_version
from time import sleep
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
		return 0
	else:
		return 1
os.system('color 02')
print('Author:yinzhuoqun\n')
version=version_status()
path_input=r'I:\yzq\apk\baiduinput_AndroidPhone_1000e.apk'#百度输入法包的路径
path_input=r'‪I:\yzq\apk\com.tencent.qqpinyin_5.3.0.apk'#QQ输入法包的路径

pwd=os.getcwd()
file_tmp=pwd+r'/'+'tmp_ime_list.txt'
command_list_ime='adb shell ime list -s > '+file_tmp	###
#input='com.baidu.input/.ImeService'
input='com.tencent.qqpinyin/.QQPYInputMethodService'
#input='com.google.android.inputmethod.pinyin/.PinyinIME'
#input='com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME'
command_set_ime='adb shell ime set %s'%input	###
if version==1:
	def dlist():
		pwd=os.getcwd()
		devicestxt='>'+pwd+r'\devices_tmp.txt'
		adbd='adb devices %s' %devicestxt
		deviceslist=[];list=[];listoff=[]
		os.system(adbd)
		f=open("devices_tmp.txt")
		for line in f:
			liner=re.search(r'device\b',line)
			if liner==None:
				pass
			else:
				list.append(line.strip())
		f.close()
		try:
			os.remove("devices_tmp.txt")
		except Exception as e:
			print('Error:devices_tmp.txt delete failure,Please delete manually.the file path at %s'%pwd)
		for i in range(len(list)):
			yzq=list[i].split('\t')
			device=yzq[0]
			deviceslist.append(device)
		return deviceslist
	deviceslist=dlist()
	if len(deviceslist)==1:
		os.system(command_list_ime)
		f=open('tmp_ime_list.txt')
		list_ime=[]
		for line in f:
			#liner=re.search(r'baidu',line);#print(liner)
			liner=re.search(r'qqpinyin',line);#print(liner)
			if liner==None:
				pass
			else:
				list_ime.append(line);#print(list_ime)
		f.close()
		os.remove("tmp_ime_list.txt")
		if len(list_ime)!=0:
			os.system(command_set_ime)
			sleep(3)
		else:
			os.system('adb install %s'%path_input)
			os.system(command_set_ime)
			sleep(3)
	elif len(deviceslist)==0:
		print('Error:not found device\n错误：没有发现设备')
		sleep(3)
	else:
		print('Error:more than one device and emulator\n错误：设备不止一台')
		sleep(3)