#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import hashlib, os, re, time


def calc_md5(data, data1):
    """
    生成加盐密码函数
    """
    data = data.encode('utf-8')
    data1 = data1.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(data + b'yinzhuoqun' + data1)
    pw = md5.hexdigest()
    # print(str(data)+':'+'\''+pw+'\'')
    return pw


def isPasswordOk(str):
    """
    判断密码是否符合规则
    """
    reg_s = re.compile(r'(?=.*?[a-zA-Z])(?=.*?[0-9])[a-zA-Z0-9~!@#$%&*_+-]{6,16}$')
    f = re.findall(reg_s, str)
    if len(f) != 0:
        return True
    else:
        print('password rules : Letters and Numbers and lenth greater than 5')
        return False


def register():
    """
    注册函数
    """
    print('=== register ===')
    username = input('please input username:\n')

    while len(username) == 0 or username in db.keys():
        if username in db.keys():
            print("Error: '%s' already exsit!" % username)
        if len(username) == 0:
            print("Error: username can't be empty")
        username = input('please input username:\n')

    password1 = 1
    password2 = 2
    while password1 != password2:
        password1 = input('please input password:\n')
        while isPasswordOk(password1) == False:
            password1 = input('please input password:\n')

        password2 = input('please input password again:\n')
        while isPasswordOk(password2) == False:
            password2 = input('please input password again:\n')

        if password1 != password2:
            print('Error: input twice inconformity of the password')
            print('current register username : %s' % username)

        else:
            password = password2
            db[username] = calc_md5(username, password)
            userpass = username + ':' + calc_md5(username, password) + '\n'
            print('user', userpass)
            with open(getPath(), 'a+') as f:
                f.write(userpass) # 注册成功写入文件
            print("'%s' register success." % username)
            time.sleep(2)
            return True


def login():
    """
    登陆函数
    """
    db = getUsers(getPath()) # 更新
    print('=== login ===')
    user = input('please input username:\n')
    while user not in db.keys():
        print("Error: '%s' not exsit!" % user)
        user = input('please input username:\n')

    password = input('please input password:\n')

    password_error_times = 2
    while db[user] != calc_md5(user, password) and password_error_times > 0:
        print('Error: password error!')
        print('have chance : %s' % (password_error_times))
        password = input('please input password:\n')
        password_error_times -= 1
    if db[user] == calc_md5(user, password):
        print('login success.')
        time.sleep(2)
        return True
    else:
        print('login failed.')
        time.sleep(2)
        return False


def changePassword():
    """
    修改密码
    """

    pass


def getUsers(path):
    """
    创建或读取账号密码文件
    """
    with open(path, 'a+') as f:
        # f = open(pwd + r'\userdb.txt', 'a+')
        f.seek(0, 0)
        d = f.readlines()
        # print(type(d),d[0])

    db = {}
    for e in d:
        key, value = e.split(":")
        value = value.strip()
        # print(type(e), e)
        db[key] = value
    print('userdb:\n%s' % db)
    return db


def getPath():
    """
    获取工作文件路径
    """
    pwd = os.getcwd();
    print('working directory:', pwd)
    os.chdir(pwd)
    path = pwd + r'\userdb.txt'
    return path


if __name__ == '__main__':
    while True:
        db = getUsers(getPath())
        if len(db) == 0:
            register()
        else:
            choice_RegLog = input('please choice register(r or 1) or login( l or 0):\n')
            if choice_RegLog == '1' or choice_RegLog == 'r':
                register()
            else:              
                login()
