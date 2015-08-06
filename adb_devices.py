#coding:utf-8
#python C:\Users\lifeix\Desktop\adb_devices.py
#python C:\Users\Haier\Desktop\adb_devices.py
import os,re
from time import sleep
def device():
	pwd=os.getcwd()
	devicestxt='>'+pwd+r'\testde.txt'
	adbd='adb devices %s' %devicestxt
	deviceslist=[]
	list=[]
	listoff=[]
	os.system(adbd)
	f=open("testde.txt")
	for line in f:
		liner=re.search(r'device\b',line)
		if liner==None:
			pass
			#listoff.append(line.strip())
		else:
			list.append(line.strip())
	f.close()
	os.remove("testde.txt")
	for i in range(len(list)):
		yzq=list[i].split('\t')
		device=yzq[0]
		deviceslist.append(device)
	return deviceslist
deviceslist=device()
print('deviceslist=%s'%deviceslist)
sleep(3)