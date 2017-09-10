#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

mylist1 = [x for x in range(1,10)]  # 1-9
mylist2 = [x for x in range(1,11)]  # 1-10
mylist3 = []
mylist4 = [1]

def middle_num_from_list(mylist):
    if isinstance(mylist, list):
        mylist_len = len(mylist)
        if mylist:  # 去除空列表
            '''
            没有判断列表存在非数字的情况
            '''
            if mylist_len % 2 == 0:  # 偶数个列表
                middle_num = (mylist[int(mylist_len/2)] + mylist[int(mylist_len/2)-1])/2
                print("%s \n的中间平均数是：%s" % (mylist, middle_num))
            elif mylist_len % 2 == 1:  # 奇数个列表
                middle_num = mylist[round(mylist_len/2)]
                print("%s \n的中间平均数是：%s" % (mylist, middle_num))
          
         
if __name__ == "__main__":
    middle_num_from_list(mylist1)
    middle_num_from_list(mylist2)
    middle_num_from_list(mylist3)
    middle_num_from_list(mylist4)
    
# 结果
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 的中间平均数是：5
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 的中间平均数是：5.5
# [1]
# 的中间平均数是：1
