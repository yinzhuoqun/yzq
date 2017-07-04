#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import time

# 时间戳转化为本地时间
#
#
# timeCode = input('请输入时间戳：')
# timeCode = float(timeCode)
# timeTuple = time.localtime(timeCode)
# timeFormat=time.strftime('%Y/%m/%d %H:%M:%S', timeTuple)
# print(timeFormat)

# 当前时间转化为时间戳
nowTimeCode=time.time()
nowTime = time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
print('当前时间为:%s'%nowTime)
print('当前时间戳:%s'%nowTimeCode)

# 时间转时间戳
import datetime
Y=2016
m=7
d=21
H=11
M=27
S=30
str='%s-%s-%s %s:%s:%s'%(Y,m,d,H,M,S)
print('输入时间为:%s'%str)
sTime = datetime.datetime(Y,m,d,H,M,S)
timeCodeMy = time.mktime(sTime.timetuple())
print('输入时间戳:%s'%timeCodeMy)
time.sleep(3)