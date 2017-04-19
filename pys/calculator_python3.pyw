#!/usr/bin/env python3
#coding:gbk


import wx


def op1(event):
    finename.WriteText("1") #调用函数时,将 括号内 数字 写入文本当中
def op2(event):  
    finename.WriteText('2')
def op3(event):  
    finename.WriteText('3')
def op4(event):  
    finename.WriteText('+')
def op5(event):  
    finename.WriteText('4')
def op6(event):  
    finename.WriteText('5')
def op7(event):  
    finename.WriteText('6')
def op8(event):  
    finename.WriteText('-')
def op9(event):  
    finename.WriteText('7')
def op10(event):  
    finename.WriteText('8')
def op11(event):  
    finename.WriteText('9')
def op12(event):  
    finename.WriteText('*')
def op13(event):  
    finename.WriteText('.')
def op14(event):  
    finename.WriteText('0')
def op16(event):  
    finename.WriteText('/')
def jieguo(event):
      result = eval(finename.GetValue())# 获得  eval 执行 （finename 获取到的文本) 的结果
      finename.SetValue(str(result))    # 将结果 result set 到 finename

def d(event):
    finename.Clear()        #当调用函数时,清空文本内容,写入 字符串 “0”
    finename.WriteText('0')
def c(event):
    zhi = finename.GetValue()       #调用函数C时,获取文本内容,将获取字符串【0:-1:0】切分出来
    finename.SetValue(zhi[:-1])                 #在set 到 文本当中


app = wx.App() #实例化主循环
win = wx.Frame(None,title = u"计算器",size=(430,375)) #实例化一个窗口
panel = wx.Panel(win) #把 win 指定为父组件

def Anniu(str1):  
      return wx.Button(panel,label=str1)
                  ##生成一个按钮,label 按钮上的内容为 指定的str1

def Bind(bt,op):
      bt.Bind(wx.EVT_BUTTON,op)
                  #将指定按钮 与 指定函数 绑定

[bt1,bt2,bt3,
 bt4, bt5,bt6,  
 bt7,bt8,bt9,
 bt10, bt11,bt12,
 bt13,bt14,bt15,
 bt16,bt17,bt18]    =   [Anniu("1"),Anniu("2"),Anniu("3"),
                   Anniu("+"),Anniu("4"),Anniu("5"),
                   Anniu("6"),Anniu("-"),Anniu("7"),
                   Anniu("8"),Anniu("9"),Anniu("*"),
                  Anniu("."),Anniu("0"),Anniu("="),
                  Anniu("/"),Anniu("c"),Anniu("del"),]   #调用函数实例化按钮

Bind(bt1,op1),Bind(bt2,op2),
Bind(bt3,op3),Bind(bt4,op4),
Bind(bt5,op5),Bind(bt6,op6),
Bind(bt7,op7),Bind(bt8,op8),
Bind(bt9,op9),Bind(bt10,op10),
Bind(bt11,op11),Bind(bt12,op12),
Bind(bt13,op13),Bind(bt14,op14),
Bind(bt15,jieguo),Bind(bt16,op16),
Bind(bt17,d),Bind(bt18,c),
#调用函数 将按钮与函数 绑定
finename = wx.TextCtrl(panel) #将窗口实例化成 Text 格式 ，赋值给 finename

s1_box,s2_box,s3_box,s4_box, = wx.BoxSizer(wx.VERTICAL),wx.BoxSizer(wx.VERTICAL),wx.BoxSizer(wx.VERTICAL),wx.BoxSizer(wx.VERTICAL)
#垂直尺寸器
def add(bbtt,box=s1_box,proportion = 1):
      box.Add(bbtt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
      #谁的尺寸器上，添加组件(添加什么组件,所占比例,填充样式为EXPAND |方向为全部，边框为 1px)

#调用函数 添加组件
add(bt1)
add(bt5)
add(bt9)
add(bt13)

add(bt2,box=s2_box)
add(bt6,box=s2_box)
add(bt10,box=s2_box)
add(bt14,box=s2_box)

add(bt3,box=s3_box)
add(bt7,box=s3_box)
add(bt11,box=s3_box)
add(bt15,box=s3_box)

add(bt4,box=s4_box)
add(bt8,box=s4_box)
add(bt12,box=s4_box)
add(bt16,box=s4_box)


v1_box = wx.BoxSizer(wx.VERTICAL)
v_box = wx.BoxSizer()
s_box = wx.BoxSizer(wx.VERTICAL)

add(bt17,v1_box)
add(bt18,v1_box)

add(s1_box,v_box,2)
add(s2_box,v_box,2)
add(s3_box,v_box,2)
add(s4_box,v_box,2)

add(v1_box,v_box,2)
add(finename,s_box)
add(v_box,s_box,50)

panel.SetSizer(s_box)
win.Show()
app.MainLoop()


'''
import sys,os,wx

#class A(object):
#      a = wx.App()
      
class Mywx(object):

      def __init__(self,(wbid,width,height)):
            self.app = wx.App()#实例化主循环
            self.win = wx.Frame(None,title=("%s" %wbid),
                                size= (width,height)) #实例化窗口组件
            self.panel = wx.Panel(self.win) #创建画布

      def anniu(self): #创建按钮
            a = [wx.Button(self.panel,label="%s" %i) for i in range(10)]
            
            print len(a)
            for j in a:
                  print j
            #
            [self.b0,self.b1,self.b2,self.b3,self.b4,
            self.b5,self.b6,self.b7,self.b8,self.b9,]=a
            print self.b0
            
mywx = Mywx((u"计算器", 410 ,335))
#mywx.anniu()
if __name__ == "__main__":
      mywx.anniu()      
'''         
