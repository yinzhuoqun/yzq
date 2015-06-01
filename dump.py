#coding:utf-8
#‪python C:\Users\lifeix\Desktop\dump.py
#‪python C:\Users\Haier\Desktop\dump.py
'''
__author__  = 'yinzhuoqun'
__version__ = '1.0'
'''
import os,re,datetime,time
starttime=datetime.datetime.now()
print("please input apk path and press ENTER:")
apk=input()
#apk=r'C:\Users\lifeix\Desktop\com.l99.bed-4.0.1-wwere9D_yingyonghui-release.apk'
#apk=r'C:\Users\Haier\Desktop\txkd-1.0.apk'
#1install='adb install ' +apk
#2install='adb install -r %s' %apk
#os.system(install)
#python里运行cmd提取包名、activity名的txt
pwd=os.getcwd()
txt='>'+pwd+r'\testpa.txt'
aapt='aapt dump badging %s %s' %(apk,txt)
os.system(aapt)
#导出包名
pa=open("testpa.txt",encoding='UTF-8')
str=pa.read()
package1=re.search(r"(name='(.+?)' versionCode=')",str,re.S)
a=package1.group(2)
b=a.strip()
print("package name:",b)
#导出启动app的activity
activity=re.search(r"launchable-activity: name='(.+?)'  label='",str,re.S)
c=activity.group(1)
d=c.strip()
print("startActivity name:",d)
pa.close()
os.remove("testpa.txt")
nowtime=time.asctime(time.localtime(time.time()))
print('Now time:',nowtime)
lasttime=datetime.datetime.now()
taketime=(lasttime-starttime).seconds
print('You take time',taketime,'s.')
print('Auto close the window after 30 seconds')
time.sleep(30)
