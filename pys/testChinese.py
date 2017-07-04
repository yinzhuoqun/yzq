
import re,os,sys
def exist_chinese(str):
		#print(str,len(str)) 
		#not_chinese= re.findall(r'[^\u4e00-\u9fa5]', str)	#只匹配汉字，不匹配双字节字符 
		chinese= re.findall(r'[\u0391-\uFFE5]', str)	#匹配双字节字符（汉字+符号）
		space= re.findall(r'(\s)', str)	#匹配空格
		
		print(chinese,len(chinese))
		print(space,len(space))
		
		if len(str)==0:
			print('提示：没有任何字符的输入')
		else:
			if len(chinese)!=0:
				print('警告：路径至少含有中文、全角字符中的一种')
				return True
			elif len(space)!=0:
				print('警告：路径含有空格')
				import string
				list_pathstr=list(str)
				#print(list_pathstr)
				list_pathstr.pop()
				list_pathstr.pop(0)
				new_apkpath=''.join(list_pathstr)
				print(new_apkpath)
				print(os.path.exists(new_apkpath))
				return True
			else:
				print('提示：路径格式正确')
				return False
		

while 1:
	apkpath=input('请输入：')
	exist_chinese(apkpath)
	#print(os.path.exists(apkpath))
	a=r'C:\Users\lifeix\Desktop\print Meid.apk'
	b=r'C:\Users\lifeix\Desktop\我有 空格  .apk'
	#print(os.path.exists(a))
	#print(os.path.exists(b))
	