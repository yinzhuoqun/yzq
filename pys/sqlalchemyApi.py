#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from  sqlalchemy.types import INTEGER 
#  AttributeError: 'int' object has no attribute '_set_parent_with_dispatch'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pymysql

# 创建对象的基类:
Base = declarative_base()

# 定义表对象:
class change_table(Base):
    # 表的名字:
    __tablename__ = 'students'

    # 表的结构:Column列名
    id = Column(INTEGER, primary_key=True)
    name = Column(String(10))
    age = Column(INTEGER)
    
# 初始化数据库连接:'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:root@192.168.235.144:3306/yzqdb',echo=True) # company root-root

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

###########################################
'''
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = change_table(name='while',age = '30')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
'''

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = change_table(id='2',name = 'for')
# 添加到session:
# session.add(new_user)
# 修改到session:
session.merge(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()




##########################################

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(change_table).filter(change_table.id=='3').one()
# user = session.query(change_table).filter(change_table.id=='3').all()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
'''

# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：

class change_table(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
'''