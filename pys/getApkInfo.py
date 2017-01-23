#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='yinzhuoqun'

import os,re,time,zipfile
from xml.dom.minidom import parse
import xml.dom.minidom

AXMLPrinter2Path=r'C:\Users\lifeix\Desktop\AXMLPrinter2.jar'#AXMLPrinter2.jar解析引擎路径

if os.name=='nt':
	os.system('color 02')
print('author: yinzhuoqun\n')
######################
#渠道名称
channelNameList=['001','002','003','004','005','006','007','008','360',
'anzhi','baidu','eoe','huawei','jifeng','jinli','kupai','l99','lianxiang',
'meizhu','mumayi','nduo','oppo','ppzhushou','uc','wandoujia','xiaomi',
'yingyongbao','yingyonghui','pp']

#,
#print(channelNameList,len(channelNameList))#输入渠道名称和渠道总数
######################
ApkPath = input('请输入APK的路径:\n')
apk_count=len(re.findall('(.apk)',ApkPath))	#防止输入非apk文件
while os.path.exists(ApkPath)==False or apk_count==0:
	ApkPath = input('请输入APK的路径:\n')
	apk_count=len(re.findall('(.apk)',ApkPath))	#防止输入非apk文件	


def channelInfo(ApkPath):
	if os.path.exists(ApkPath)==True:
		zipfile.ZipFile(ApkPath).extract("AndroidManifest.xml") #从apk中解压出xml文件
		xmlNameStatus=False
		for channel in channelNameList:
			#channel=re.compile(channel)
			getChannelNameList=re.findall(channel,ApkPath)
			if len(getChannelNameList)!=0:
				print(getChannelNameList)
				xmlName=getChannelNameList[0]+'.xml';print(xmlName)
				xmlNameStatus=True
			
				

		if xmlNameStatus==True:
			os.system('java -jar %s AndroidManifest.xml > %s'%(AXMLPrinter2Path,xmlName))#用AMLPirnter2解析xml文件
			while os.path.exists('AndroidManifest.xml')==True: 
				os.remove('AndroidManifest.xml')#删除解压出来的AndroidManifest.xml
				


			'''
			DOMTree = parse("getAndroidManfest.xml")#打开解析的xml文件
			collection = DOMTree.documentElement #得到文档的元素
			print(collection.nodeName)
			print(collection.nodeValue)
			print(collection.nodeType)
			books = collection.getElementsByTagName("meta-data")
			print(books)
			for book in books:
				print(book.nodeName);#print(book.childNodes[0].nodeValue)
				print(book.nodeValue)
				print(book.nodeType)
			'''

			
			with open(xmlName) as f:
				str=f.read()
				
				packageList=re.findall('package="(.+)"',str)
				if len(packageList)!=0:
					print('包  名:',packageList[0])
				else:
					print('! 提示：未发现包名')
				file=f.name;#print(file)
				tuple_filename_filepro=os.path.splitext(file)
				filename=tuple_filename_filepro[0]
				channelList=re.findall(filename,str)
				if len(channelList)!=0:
					channelName=channelList[0]
					print('渠道号:',channelName)
				else:
					print('! 提示：未发现渠道号')
					channelName='notFound'
				
				versionList=re.findall('android:versionName="(.+)"',str)
				if len(versionList)!=0:
					print('版本号:',versionList[0])
				else:
					print('! 提示：未发现版本号')
				
			if channelName in ApkPath:
				print('! 提示：APK 包渠道号正确')
			else:
				print('! 提示：APK 包渠道号错误')
		else:		
			print('! 提示：APK 包名称未指定渠道号')
			print('渠道号名称格式：\n',channelNameList)
		
	else:
		print('! 提示:文件路径不存在')

	
channelInfo(ApkPath)		
stop_run = input('请按 ENTER 键停止运行...\n')
