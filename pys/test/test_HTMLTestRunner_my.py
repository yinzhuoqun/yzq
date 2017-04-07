# coding:utf-8
from selenium import webdriver
from time import sleep,time,ctime
import unittest 
#from Page import * 
import threading
import HTMLTestRunner


class DemoPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')


    def testTitle(self, value='testData'):
        self.assertTrue(self.driver.title in self.getXmlData(value))


    def testUrl(self):
        print(self.driver.current_url)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.makeSuite(DemoPage)
    # 定义自动化报告目录
    filename = r'C:\Users\lifeix\Desktop\TestReport.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title= u'TestReport',
        description = u'TestReport'
    )
    runner.run(suite)
	fp.close()
