#coding:utf-8
'''
__author__  = 'yinzhuoqun'
__version__ = '1.0'
'''
import os,re,datetime,time,subprocess
starttime=datetime.datetime.now()
if os.name=='nt':
	os.system('color 02')
print('Author:yinzhuoqun\n')

def dump_pa1(path):
	#python里运行cmd提取包名、activity名的txt
	pwd=os.getcwd()
	txt='>'+pwd+r'\dump_temp.txt'
	aapt='aapt dump badging %s %s' %(path,txt)
	os.system(aapt)
	#pa=open("dump_temp.txt",encoding='UTF-8')
	with open("dump_temp.txt",encoding='UTF-8') as pa:
		str=pa.read()
		#导出包名
		package1=re.search(r"(name='(.+?)' versionCode=')",str,re.S)
		a=package1.group(2)
		packagename=a.strip()
		print("package name:",packagename)
		#导出启动app的activity
		activity=re.search(r"launchable-activity: name='(.+?)'  label='",str,re.S)
		c=activity.group(1)
		activityname=c.strip()
		print("startActivity name:",activityname)
	#pa.close()
	while os.path.exists(pwd+r'\dump_temp.txt')==True:
		os.remove("dump_temp.txt")
	return packagename,activityname
	
def dump_pa(path):
	aapt=1
	try:
		PaInfo=subprocess.check_output('aapt dump badging %s'%path).decode('gbk','ignore')
		#print(PaInfo);print(type(PaInfo))
	except Exception as e:
		where_adb=subprocess.check_output('where adb').decode('gbk','ignore');#print(where_adb)
		where_aapt=subprocess.check_output('where aapt').decode('gbk','ignore');#print(where_aapt)
		
		adb_env_list=re.findall('adb.exe',where_adb);#print(adb_env_list)
		aapt_env_list=re.findall('aapt.exe',where_aapt);#print(aapt_env_list)
		
		if len(adb_env_list)==0:
			print('错误：请添加 adb.exe 的环境变量')
		
		if len(aapt_env_list)==0:
			print('错误：请添加 aapt.exe 的环境变量')
		
		else:
			if os.path.exists(path) == True:
				print('错误：无效的 apk 文件')
			else:
				print('错误：路径不存在')										
		aapt=0	
		
	if aapt==1:
		Plist=re.findall(r"name='(.+?)' versionCode='",PaInfo);#print(Plist)
		if len(Plist)!=0:
			packagename=Plist[0]
			print("\npackage name:\n%s\n"%Plist[0])
			
		Alist=re.findall(r"launchable-activity: name='(.+?)'  label='",PaInfo);#print(Alist)
		if len(Alist)!=0:
			startActivity=Alist[0]
			print("startActivity name:\n%s\n"%Alist[0])
			
		VClist=re.findall(r"versionCode='(.+?)'",PaInfo)
		if len(VClist)!=0:
			versionCode=VClist[0]
			print('versionCode:\n%s\n'%versionCode)
			
		VNlist=re.findall(r"versionName='(.+?)'",PaInfo)
		if len(VNlist)!=0:
			versionName=VNlist[0]
			print('versionName:\n%s\n'%versionName)
			
		SVlist=re.findall(r"targetSdkVersion:'(.+?)'",PaInfo)		
		if len(SVlist)!=0:
			targetSdkVersion=SVlist[0]
			print('targetSdkVersion:\n%s\n'%targetSdkVersion)
			
			
		PAVList=Plist+Alist+VClist+VNlist;#print(PaList)
		return PAVList
		
apkpath=input("please input apk path and press ENTER:\n")		
dump_pa(apkpath)

nowtime=time.asctime(time.localtime(time.time()))
print('Now time:',nowtime)
lasttime=datetime.datetime.now()
taketime=(lasttime-starttime).seconds
print('Take time',taketime,'s.')
print('Auto close the window after 30 seconds.')
time.sleep(30)
