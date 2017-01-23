#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__='yinzhuoqun'

import subprocess,re,time

where_adb=subprocess.check_output('where adb').decode('gbk','ignore');print(where_adb)
adb_env_list=re.findall('adb.exe',where_adb);print(adb_env_list)

where_aapt=subprocess.check_output('where aapt').decode('gbk','ignore');print(where_aapt)
aapt_env_list=re.findall('aapt.exe',where_aapt);print(aapt_env_list)

time.sleep(3)
