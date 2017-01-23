#coding:utf-8
#monkeyrunner C:\Users\lifeix\Desktop\jietu.py
#‪monkeyrunner C:\Users\Haier\Desktop\jietu.py
import datetime,time,os,random
starttime=datetime.datetime.now()
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
#device=mr.waitForConnection(3,'4f25e81b')
namelist=[u'手机是菜市场',u'电商是动物园',u'平板是水果摊',
u'轻轻的我走了',u'正如我轻轻的来',
u'你是我的小呀小苹果',u'就像天边最美的云朵',u'怎么爱你都不嫌多']
device=mr.waitForConnection()
result=device.takeSnapshot()
#t=time.strftime("%Y%m%d%H%M%S")
t=time.strftime("%m%d%H%M%S")
path=r'I:/91UserData/ScreenCapture/'
#1 path=r'I:/yzq/mkscn/pic'
#2 path=raw_input()
#3 path=os.getcwd()
dirname=random.choice(namelist)
result.writeToFile(path+'\\'+dirname+t+'.png','png')
#print '%s%s.png save success in %s'%(dirname,t,path)
#lasttime=datetime.datetime.now()
#taketime=(lasttime-starttime).seconds
#print 'MonkeyRunner take time',taketime,'s'