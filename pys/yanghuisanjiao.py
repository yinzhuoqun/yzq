#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'yinzhuoqn'

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]


def triangles():
    a=[1]


def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

if __name__ == "__main__":
    g = pas_triangles()
    for n in range(10):
        print(next(g))
      


# 用PIL模块截图
# 直接抓屏 ImageGrab.grab()
# 剪切板获取图像 ImageGrab.grabclipboard()
#
# from PIL import ImageGrab
# import time
# im = ImageGrab.grab()
# addr = r'I:\yzq\MyPythonTest\test1\aaa.jpg'
# im.save(addr,'jpeg')
# time.sleep(3)

#
# l=[3,12,24,36,55,68,75,88]
# m=24
#
# def TwoSearch(list,to):
#     mid=list[len(list)//2-1]
#     print(len(list)//2,mid)
#     if mid == to:
#         print(mid)
#
#     else:
#         if mid > to :
#             pass
#
# TwoSearch(l,m)




# a=1
# b=list(range(10))
# for y in b:
    # print(a,y)
    # a+=1
