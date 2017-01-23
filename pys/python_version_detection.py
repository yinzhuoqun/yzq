#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Write_Python_version='3.4.3'
from platform import python_version
import re
from time import sleep
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
		out_eq()
		return 0
	else:
		print(u'Python 版本兼容.')
		out_eq()
		return 1
out_eq()
print('Current Python version',python_version())
print('Write Python version',Write_Python_version)
print('Author:yinzhuoqun') 
out_eq()
run=version_status()
sleep(5)