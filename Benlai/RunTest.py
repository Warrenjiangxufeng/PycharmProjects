#coding=utf-8
import unittest
import json
import requests
from HTMLTestRunner import HTMLTestRunner
import time

#import test_login001
#import test_001


import sys
reload(sys)
sys.setdefaultencoding('utf8')#解决中文编码问题

#suite = unittest.TestSuite()
#suite.addTest(test_001.test_001("test001"))
test_dir = '/Users/jiangxufeng1/PycharmProjects/Benlai/testsuit/'
test_report = '/Users/jiangxufeng1/PycharmProjects/Benlai/testreport/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
if __name__=="__main__":
    #testunit = unittest.TestSuite()
    #testunit.addTest(suite)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    filename = test_report + now + '-TestReport.html'
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告",
                            description="测试用例执行情况:")
    runner.run(discover)
    fp.close()