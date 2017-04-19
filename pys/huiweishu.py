#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'


# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)


# logging.basicConfig(level=logging.WARNING)



# def func():
#     return [lambda x : i*x for i in range(4)]
#
# print([m(2) for m in func()])
#
#
def abc(i):
    
    i_len = len(i)
    i_ant = i[::-1]
    print('长度：%s' %i_len )
    print('逆序：%s' % i_ant)
    if i_ant == i:
        print('回文数：%s'%True)
    else:
        print('回文数：%s'%False)

        
# 法二 method second
#     flag = False
#     for x in range(int(len(i) / 2)):
#         # print('x: %s' % x)
#         if i[x] == i[-(x + 1)]:
#             flag = True
#
#         else:
#             flag = False
#
#     print('回文数：%s'%flag)
#     # if len(i) % 2 == 0:
#     #     for x in range(int(len(i) / 2)):
#     #         print('x: %s' % x)
#     #         if i[x] == i[-(x + 1)]:
#     #             print('True1')
#     # else:
#     #     for x in range(int(len(i) / 2)):
#     #         print('x: %s' % x)
#     #         if i[x] == i[-(x + 1)]:
#     #             print(True)
#
while 1:
    # abc('36963')
    abc(input('输入: '))


# with open(r'I:\yzq\MyPythonTest\xuesheng\123.txt','r') as f:
    # print(f.readlines())
    # print(type(f))
    # print(f.read().encode('gbk'))

