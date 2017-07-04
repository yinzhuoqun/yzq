#coding:utf-8
#‪monkeyrunner C:\Users\lifeix\Desktop\recorder.py
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder
device=mr.waitForConnection()
recorder.start(device)