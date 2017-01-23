#coding:utf-8
#‪python C:\Users\lifeix\Desktop\monkey.py
#‪python C:\Users\Haier\Desktop\monkey.py
'''
__author__  = 'yinzhuoqun'
__version__ = '1.3'
'''
import os,time,re
print("Please input apk path and press ENTER:")
apkpath=input()
apkpath=apkpath.strip()
install='adb install -r %s' %apkpath
ins=os.system(install)
while apkpath=='' or ins!=0:
	print("Please input apk path and press ENTER:")
	apkpath=input()
	apkpath=apkpath.strip()
	install='adb install -r %s' %apkpath
	ins=os.system(install)
print("Please input monekey evnet count(number) and press ENTER:")
evnet=input()
while evnet=='' or re.findall('[^0-9]',evnet):
	print("Please input monekey evnet count(number) and press ENTER:")
	evnet=input()
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
pwd=os.getcwd() 
t=time.strftime("%Y%m%d%H%M%S")
filename=b+'_mklog'+t+'.txt'
txt='>'+pwd+r'\\'+filename
pa.close()
os.remove("testpa.txt")
list=['y','n','Y','N']
print("Do you need to save a .txt file? please input y/n and press ENTER.")
outputstyle=input()
while outputstyle not in list:
	print("Do you need to save a .txt file? please input y/n and press ENTER.")
	outputstyle=input()
if outputstyle=='y' or outputstyle=='Y':
	monkey='adb shell monkey -p %s -s 250 --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 50 -v -v -v %s %s' %(b,evnet,txt)
	os.system(monkey)
	print(filename+' save in',pwd)
else:
	monkey='adb shell monkey -p %s -s 250 --throttle 50 -v -v -v %s' %(b,evnet)
	os.system(monkey)