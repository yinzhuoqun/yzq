#coding:utf-8
#python C:\Users\lifeix\Desktop\shuzicaimi.py
#python C:\Users\Haier\Desktop\shuzicaimi.py
'''
__author__  = 'yinzhuoqun'
__version__ = '1.0'
'''
import random
from time import sleep
#import os;setpath=r'set path=%path%;c:\Python34';os.system(setpath)
w=1
while 1:
	number=random.randint(0,9)
	#print(u'这瓶是%s号'%number);sleep(0.5)
	cs=3;list=['0','1','2','3','4','5','6','7','8','9']
	print(u'第%s届<<数字猜谜>>送好酒游戏开始啦→_→三次机会哦'%w);sleep(0.5)
	print(u'客官，猜中数字这瓶就是你的哦=.=')
	guess=input()
	while guess not in list:
		print(u'---客官，您不可以乱猜哦0.0');sleep(0.5)
		print(u'客官，猜中数字这瓶就是你的哦=.=')
		guess=input()
	guessa=int(guess)
	cs=cs-1
	while guessa!=number:
		if guessa<number:
			print(u"---客官，你怎么还没醉呢...人家等...");sleep(0.5)
			print(u'客官，猜中数字这瓶就是你的哦=.=')
			guess=input()
			while guess not in list:
				print(u'---客官，您不可以乱猜哦0.0');sleep(0.5)
				print(u'客官，猜中数字这瓶就是你的哦=.=')
				guess=input()
			guessa=int(guess)
			cs=cs-1
			if cs==0:
				break
		if guessa>number:
			print(u"---客官，你喝高啦...别乱...");sleep(0.5)
			print(u'客官，猜中数字这瓶就是你的哦=.=')
			guess=input()
			while guess not in list:
				print(u'---客官，您不可以乱猜哦0.0');sleep(0.5)
				print(u'客官，猜中数字这瓶就是你的哦=.=')
				guess=input()
			guessa=int(guess)
			cs=cs-1
			if cs==0:
				break
	if guessa==number:
		print('------')
		sleep(0.5)
		print(u"啊! 居然被客官猜中了，这瓶是你的了^ω^")
		sleep(0.5)
		print('=====================================')
	else:
		print('------')
		sleep(0.5)
		print(u'数字是%s，你怎么这么笨呀...'%number)
		sleep(0.5)
		print('=====================================')
	w=w+1