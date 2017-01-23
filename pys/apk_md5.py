#!/usr/bin/env python3
#coding:utf-8
import os,difflib,time,subprocess,re
#pwd=os.getcwd()
if os.name=='nt':
	os.system('color 02')
def remove_dir():
	if  os.path.exists('META-INF')==True:
		print('Tips:清理rsa文件缓存...')
		os.system('rmdir /S /Q META-INF')#windos方法
remove_dir()
apkpathlist=[];times=1

file_acount=2 #设置解析的apk的数量1、2
print('Author:yinzhuoqun\n')
for x in range(file_acount):
	apkpath=input('请输入第%s个apk包的路径：\n'%times)
	while len(apkpath)==0 or os.path.exists(apkpath)==False:
		apkpath=input('请输入第%s个apk包的路径：\n'%times)
	apkpath=apkpath.strip()
	apkpathlist.append(apkpath)	
	times+=1
#查找apk里的rsa文件
print('Tips:查找apk里的rsa文件...')
contentInfolist=[]
for path in apkpathlist:
	#os.system('jar tf %s | findstr RSA'%path)
	#content=subprocess.check_output('jar tf %s | findstr RSA'%path)
	content=os.popen('jar tf %s | findstr RSA'%path)
	contentInfo=content.read()
	print(contentInfo)
	contentInfolist.append(contentInfo)
	#print(content.decode('gbk','ignore'))
#rsa文件列表
'''
rsa_file_list=[];times=1
for x in range(file_acount):
	rsa_file=input('请输入第%s个rsa文件信息：'%times)
	rsa_file=rsa_file.strip()
	rsa_file_list.append(rsa_file)
	times+=1
#print(rsa_file_list)
'''
#从apk中解压rsa文件
contentlist=[]
if file_acount>=1:
	print('Tips:从apk中解压第一个rsa文件...')
	#os.system(r'jar xf %s %s'%(apkpathlist[0],rsa_file_list[0]))
	os.system(r'jar xf %s %s'%(apkpathlist[0],contentInfolist[0]))
	if  os.path.exists('META-INF')==True:
		rsa_list=os.listdir('META-INF');print(rsa_list)
		content=subprocess.check_output(r'keytool -printcert -file META-INF/%s'%rsa_list[0])#获取证书信息
		contentlist.append(content)
		remove_dir()
if file_acount>=2:
	print('Tips:从apk中解压第二个rsa文件...')
	#os.system(r'jar xf %s %s'%(apkpathlist[1],rsa_file_list[1]))
	os.system(r'jar xf %s %s'%(apkpathlist[1],contentInfolist[1]))
	if  os.path.exists('META-INF')==True:
		rsa_list=os.listdir('META-INF');print(rsa_list)
		content=subprocess.check_output(r'keytool -printcert -file META-INF/%s'%rsa_list[0])
		contentlist.append(content)
		remove_dir()

times=1
for x in contentlist:
	print('---第%s个证书信息----'%times)
	info=x.decode('gbk','ignore')
	print(info)
	times+=1

md51=re.findall('MD5:(.+?)\n',contentlist[0].decode('gbk','ignore'));#print(md51)
if file_acount>=2:
	md52=re.findall('MD5:(.+?)\n',contentlist[1].decode('gbk','ignore'));#print(md52)
	if md51==md52:
		print('签名一致。\n')
	else:
		print('签名不一致！\n')
		
time.sleep(2)		
stop_run=input('请按ENTER键停止运行...\n')
if len(stop_run)>=0:
	pass