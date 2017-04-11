#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='yinzhuoqun'

import requests
import time

url = 'http://192.168.199.126:8080/inner/manage/user/untie/device'

#data = {"AccountGuid":"08f1c0e3-bbce-46e0-adb5-2d6d1634f9ef","OperationCode":1}
#body = {'machine_code':'9C755409-1034-4A3B-A413-A84AB95844CB1'} #ip4
#body = {'machine_code=9C755409-1034-4A3B-A413-A84AB95844CB'} #ip4
#body = {'machine_code':'6C849E88-F9D4-4C52-80C9-C9C9F98C3D5D'} #ip5
# body = {'machine_code':'42F10831-30EA-4AD7-BD39-6B5133CF0E39'} # ipod 5
body = {'machine_code':'6696BB09-AF05-4C28-B558-CBD6A896FD98'} # ipod 5

#data参数
r = requests.post(url,body)
print(r.status_code)
#print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

time.sleep(3)