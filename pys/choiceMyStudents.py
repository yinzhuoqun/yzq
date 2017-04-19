#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'


import xlrd, random, os

# 前提：安装 xlrd 模块
# try:
    # import xlrd
# except Exception as e:
    # print('%s\n请用 pip 安装 xlrd 模块'%e)


# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging
# logging.basicConfig(level=logging.INFO)  
logging.basicConfig(level=logging.WARNING)


def get_num_max(path):
    if os.path.exists(path) == True:
        data = xlrd.open_workbook(path)  # 打开Excel文件读取数据
        table = data.sheets()[0]  # 通过索引顺序获取
        ##获取行数和列数　　
        nrows = table.nrows ##获取行数
        logging.info(nrows)
        ncols = table.ncols
        logging.info(ncols)

        return nrows
    else:
        print('文件不存在')

        return False


# 判断字符是否能转为数字
def isInt(text):
    try:
        ifInt = int(text)
        # print(ifInt,type(ifInt))
        logging.info(type(ifInt))
    except Exception as e:
        ifInt = False
        # print(ifInt,", isn't int")
    finally:
        return ifInt


def random_num(path):
    num_range = [str(a) for a in range(1, 10)]
    logging.info(num_range)
    num = input('请输入发言同学的人数 (1-9)：')
    while isInt(num) == False or num not in num_range:
        num = input('请输入发言同学的人数 (1-9)：')

    # num = int(num) 
    # num_max = get_num_max(path)
    # num_list = list(range(1, num_max))   
    # choice_num_list = random.sample(num_list,num)
    
    ####
    
    choice_num_list = random.sample(list(range(1, get_num_max(path))),int(num))      
    # for times in range(num):
        # logging.info(type(num_list))
        # choice = random.choice(num_list)
        # choice_num_list.append(choice)
        # num_list.remove(choice)
    ####
    
    logging.info(choice_num_list)

    return choice_num_list


def get_choice_info(path,*choice_num_list):

    if os.path.exists(path) == True:
                        
        data = xlrd.open_workbook(path)  # 打开Excel文件读取数据

        # table = data.sheet_by_index(0) #通过索引顺序获取
        # table = data.sheet_by_name(u'Sheet1')#通过名称获取
        table = data.sheets()[0]  # 通过索引顺序获取
        logging.info(table)
        
        ####
        nrows = table.nrows
        logging.info(nrows)
        num_range = [str(a) for a in range(1, 10)]
        logging.info(num_range)
        num = input('请输入发言同学的人数 (1-9)：')
        while isInt(num) == False or num not in num_range:
            num = input('请输入发言同学的人数 (1-9)：')
        choice_num_list = random.sample(list(range(1, get_num_max(path))),int(num))   
        ####
        
        
        

        for myrow in choice_num_list:

            cell_A1 = table.row(myrow)[0].value  # 使用行列索引
            logging.info(type(cell_A1))
            cell_A3 = table.row(myrow)[2].value  # 使用行列索引
            logging.info(type(cell_A3))
            if isinstance(cell_A1, float):
                if len(cell_A3) == 0:
                    name = '(佚名)'
                    print('=.= 恭喜，你被选中啦 -.- \n    %s:%d\n' % (name, cell_A1))
                else:
                    print('=.= 恭喜，你被选中啦 -.- \n    %s:%d\n' % (cell_A3, cell_A1))
            else:
                qq = '(未登记 QQ)'
                print('=.= 恭喜，你被选中啦 -.- \n    %s:%s\n' % (cell_A3, qq))


                # cell_A2 = table.col(0)[3].value # 使用行列索引
                # logging.info(cell_A2)


                # i = 1
                # print(table.row_values(i)) # 整行
                # print(table.col_values(i)) # 整列
    else:
        print('文件不存在')


def main():
    if os.name == 'nt':
        os.system('color 02')

    path = r'I:\yzq\MyPythonTest\xuesheng\1608info.xlsx'
    while True:
        # get_choice_info(path,random_num(path))
        get_choice_info(path)


if __name__ == '__main__':
    main()
