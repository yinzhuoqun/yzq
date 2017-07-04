#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'


from tkinter import *
import tkinter.messagebox as messagebox
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Monkey finshed')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()
#
# app = Application()
# # 设置窗口标题:
# app.master.title('MonkeyTest')
# # 主消息循环:
# app.mainloop()

import tkinter
import tkinter.messagebox as messagebox
# messagebox.showinfo('MonkeyTest', 'Monkey finished')
# messagebox.showwarning('MonkeyTest', 'Monkey finished')
# # messagebox.askquestion('MonkeyTest', 'Monkey finished')
# messagebox.askyesnocancel('MonkeyTest', 'Monkey finished')
# # messagebox.ask('MonkeyTest', 'Monkey finished')
# messagebox.askretrycancel('MonkeyTest', 'Monkey finished')
# top=tkinter.Tk()
def monkey():
    messagebox.showinfo('MonkeyTest', 'Monkey finished')
# b1=tkinter.Button(top,text="Mmmmmm",command=quit)
# b1.pack()
# top.mainloop()

monkey()



