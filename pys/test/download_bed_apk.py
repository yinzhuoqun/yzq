#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Write_Python_version = '3.4.3'
from platform import python_version
from time import sleep
import re,random

#比较版本号
def char_comp(char1,char2):
	char1list=re.split('\D',char1);#print(char1list)
	char2list=re.split('\D',char2);#print(char2list)
	int2=int(char2list[0])*100+int(char2list[1])*10+int(char2list[2]);#print('int2=',int2,type(int2))	
	if len(char1list)==1:
		int1=int(char1list[0])*100;#print('int1=',int1,type(int1))
	elif len(char1list)==2:
		int1=int(char1list[0])*100+int(char1list[1])*10;#print('int1=',int1,type(int1))
	elif len(char1list)==3:
		int1=int(char1list[0])*100+int(char1list[1])*10+int(char1list[2]);#print('int1=',int1,type(int1))
	elif len(char1list)>3:
		int1=int(char1list[0])*100+int(char1list[1])*10+int(char1list[2]);#print('int1=',int1,type(int1))
	#print('int1=%s,int2=%s'%(int1,int2))
	if int1<int2:
		return 0
	else:
		return 1

#判断字符是否能转为数字
def isInt(text):
	try:
		ifInt=int(text)
		#print(ifInt,type(ifInt))
		ifInt=True
	except Exception as e:
		ifInt=False
		#print(ifInt,", isn't int")
	finally:
		return ifInt	
		
#输入=号分隔线		
def out_eq():
	out_eq_count = 17
	print('=' * out_eq_count)
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
print('Author:yinzhuoqun\n')
run = version_status()
if run == 1:
	import urllib.request
	import os, time,sys,datetime,re
	if os.name=='nt':
		os.system('color 02')
	def getHtml(url):
		page = urllib.request.urlopen(url)
		html = page.read()
		return html
	# 设置是否手动输入版本号
	#input_version = False  # 非手动输入，‘#’号是注释
	#input_version=True	#手动输入，‘#’号是注释
	version_db={1:True,0:False}
	
	input_version=version_db[1]#1 是手动输入  0是自定义

	if input_version == True:
		www = ''
		apk_min_version='4.6.11'
		char_comp_result='1'
		while len(re.findall('(\d\.\d\.\d)',www))==0 or char_comp_result==0:
		#while len(www) == 0 or www < '4.3.2':
			char_comp_result='1'
			www = input('请输入版本号：')
			if len(re.findall('(\d\.\d\.\d)',www))!=0:
				if char_comp(www,apk_min_version)==0:
					print('警告：版本号小于 %s'%apk_min_version)
					char_comp_result=0
			elif len(www)==0:
				print('警告：版本号不能为空')
			else:
				print('警告：输入的版本号不存在可下载列表')
			#if www < '4.3.2':
				#print('错误：版本号小于4.3.2！')
	else:
		# 手动设置的版本号		
		www = '4.7.1.0'
		print('版本号是：%s' % www)
	#url = r'http://192.168.2.113/bedigest/' + www + '/'
	url = r'http://192.168.2.131/bedigest/' + www + '/'
	
	try:
		urlstatus=urllib.request.urlopen(url).getcode()
	except urllib.error.HTTPError as e:
		urlstatus=e.code#;print(e.code)
		#print(e.read().decode("utf-8"))
		if e.code==403:
			print('错误：资源禁止访问')
			#sleep(3)
		elif e.code==404:
			print('错误：访问的资源不存在')
			#sleep(3)
		elif e.code==500:
			print('错误：服务器错误')
			#sleep(3)
		else:
			print('错误：s%'%e.code)
			#sleep(3)
		apkpath=None
	#except Exception as e:
		#print('错误：打开网址失败！')
		#urlstatus=0
	if urlstatus==200:	
		html = getHtml(url)  # 获取图片网站地址
		try:
			html=html.decode('UTF-8')
		except Exception as e:
			html=html.decode('gbk')	
		# print(html)
		def getImg(html):
			reg = r'href="(.*?.apk)"'
			imgre = re.compile(reg)
			imglist = re.findall(imgre, html)
			return imglist

		def getTxt(html):
			txtreg = r'href="(chuangshang.*?)\n'
			txtre = re.compile(txtreg, re.S)
			txtlist = re.findall(txtre, html)
			return txtlist
		#显示下载进度
		def download(num,block,total):
			'''回调函数 单位byte
			@num-blocknum: 已经下载的数据块
			@block-blocksize: 数据块的大小
			@total-totalsize: 远程文件的大小
			'''
			per=100.0*num*block/total
			if per>100:
				per=100
			if num*block>total:
				a=total
			else:
				a=num*block
			if total<1024*1024:
				sys.stdout.write('%.2f/%.2f(KB)  %.2f%%\r'%(a/1024,total/1024,per))
			else:
				sys.stdout.write('%.2f/%.2f(MB)  %.2f%%\r'%(a/1024/1024,total/1024/1024,per))		
			sys.stdout.flush()
		txtlist = getTxt(html);  #print('txtlist',txtlist)
		if len(txtlist) == 0:
			print('错误：匹配“chuangshang”失败，或许此版本还没有测试包！')
		else:
			listtime = [];
			listdate = []
			for x in txtlist:
				txttime = re.findall(r'\d\d-.+-\d\d\d\d.\d\d:\d\d', x);#print('txttime',txttime)
				listtime += txttime
			#print('listtime',listtime)#所有的时间信息
			#print('maxtime',max(listtime))#最近的时间信息
			###download_index = listtime.index(max(listtime))	#选择最近时间的索引
			#print('near_index',download_index)
			
			setDownLoadWay=''		#设置下载方式，随机下载多个渠道包、下载最新的安装包
			while len(setDownLoadWay)==0 or isInt(setDownLoadWay)==False:
				setDownLoadWay=input('请输入渠道包下载的数量（整数）：')
			
			if int(setDownLoadWay)>0:
				#####随机选择个数下载渠道包
				down_count=int(setDownLoadWay)	#按需要下载			
				#down_count=3	#下载数量，手动设置下载数量
				
				if down_count<=len(listtime):
					choice_txttime_list = random.sample(listtime,down_count)#随机选择的时间信息
				else:
					print('错误：渠道包下载数量超出可下载数量，选择最新的包下载...')
					####选择最近时间的索引
					choice_txttime_list=[]
					choice_txttime = max(listtime);#print(choice_txttime)
					choice_txttime_list.append(choice_txttime)
			elif int(setDownLoadWay)==0:
				####选择最近时间的索引
				choice_txttime_list=[]
				choice_txttime = max(listtime);#print(choice_txttime)
				choice_txttime_list.append(choice_txttime)
				
			print(choice_txttime_list)#输出选择的时间信息
			
			download_index_list=[]
			for choice_txttime in choice_txttime_list:
				download_index = listtime.index(choice_txttime)
				download_index_list.append(download_index)
			#print('download_index_list',download_index_list)#选择索引列表
			
			for download_index in download_index_list:
						
				###################
				want_str = txtlist[download_index]	#索引对应的字符串信息
				print('下载文件信息：\n', want_str)
				apkname = re.findall(r'(chuangshang.+?)">chuangshang', want_str);  # print('apkname',apkname)
				###################
				
				######################
				'''
				apkNameList=getImg(html);
				print('渠道包总共数量：%s'%len(apkNameList))
				#print(apkNameList)
				imgUrlList=[]
				for x in apkNameList:
					downLoadUrl=url+x
					imgUrlList.append(downLoadUrl)
					#print('渠道包下载地址:\n',downLoadUrl)
				#print(imgUrlList)#输出渠道包下载地址list	
				'''
				######################
				
				imgurl = url + apkname[0]	#最新文件的下载地址
				apkname = re.findall('(chuangshang.*?).apk', imgurl)
				filename = apkname[0]
				# 文件保存的路径
				#pwd = 'C:/Users/lifeix/Desktop'  # 注意格式 /左斜杠
				pwd=os.path.join(os.path.expanduser("~"),"Desktop")	#保存至桌面			
				os.chdir(pwd)
				print('文件下载地址:\n', imgurl)
				t=time.strftime("%m-%d_%H-%M-%S")
				downloadstatus=1	#初始化下载状态		
				starttime=datetime.datetime.now()	#下载计时开始
				
				#'''
				try:				
					urllib.request.urlretrieve(imgurl,'%s-%s.apk' % (filename, t),download)
				except Exception as e: 
					print('错误：下载失败！')
					downloadstatus=0	#下载失败时重置下载状态
				#'''
				
				lasttime=datetime.datetime.now()	#下载计时结束
				if downloadstatus!=0:
					taketime=(lasttime-starttime).seconds				
					print('\n文件下载耗时：%s秒'%taketime)#不能删掉，防止下载进度的百分比被遮盖
					down_file = pwd + '/' + '%s-%s.apk' % (filename, t)  # ;print(down_file)
					if os.path.exists(down_file) == True:
						print(u'文件保存目录：%s' % pwd)
						print(u'下载的文件名：\n%s_%s.apk' % (filename, t))
						apkpath=pwd+'\\'+filename+'-'+t+'.apk';#print(apkpath)
					out_eq()
			
	window_close_time = 0  # 窗口关闭时间
	if window_close_time != 0: 
		print('窗口 %ss 后自动关闭' % window_close_time)
		sleep(window_close_time)	
else:
	sleep(3)