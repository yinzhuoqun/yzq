#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

list = [ x for x in range(1,10)]
# print(list)

a=b=c=d=e=f=g=h=i=1
list1=[]
for x in list:
    a = x
    for x in list:
        b=x
        for x in list:
            c=x
            for x in list:
                d=x
                for x in list:
                    e=x
                    for x in list:
                        f=x
                        for x in list:
                            g=x
                            for x in list:
                                h=x
                                for x in list:
                                    i=x
                                    if a+13*b/c+d+12*e-f-11+g*h/i-10 == 66:
                                    # if a+13*b/c+d+12*e-f+g*h/i-21 == 66:

                                        # print(a,b,c,d,e,f,g,h,i)
                                        dd = '%s-%s-%s-%s-%s-%s-%s-%s-%s'%(a,b,c,d,e,f,g,h,i)
                                        list1.append(dd)
print(len(list1))