#coding=utf-8
#!/usr/bin/python
# python C:\Users\Haier\Desktop\yslist.py
'''
__author__  = 'yinzhuoqun'
__version__ = '1.0'
'''
def fanwei(min,max):
	print('从',min,'到',max,'的完数有：')
	for max in range(min,max+1):
		yslist=[1]
		for n in range(2,max):
			if max%n==0:
				yslist.append(n)
				#print(max)
				#print(yslist,";")
				if sum(yslist)==max:
					print(sum(yslist),'=',yslist,';')
fanwei(1,500)