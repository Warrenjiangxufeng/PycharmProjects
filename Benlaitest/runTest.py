#coding=utf-8
import readExcel
import testApi
from base_Test import baseTest
import HTMLTestRunner
import unittest
import time
class testLoginApi(baseTest):
    def testLoginApi(self):
        excel = readExcel.readExel(r'/Users/jiangxufeng1/PycharmProjects/Benlaitest/testSuit')
        name = excel.getName
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        id = excel.getId
        status_code = excel.getStatusCode
        code = excel.getStatusCode
        row = excel.getRows
        for i in range(0, row - 1):
            api = testApi(method[i], url[i], data[i])
            apistatus = api.getStatusCode()
            print(apistatus)
            apijson = api.getJson()
            if apistatus == status_code[i]:
                print ('{}.{}:测试成功。json数据为：{}'.format(id[i], name[i], apijson))
            else:
                print('{}.{}:测试失败。json数据为：{}'.format(id[i], name[i], apijson))
def runAutomation():
    suite = unittest.TestLoader().loadTestsFromTestCase(testLoginApi)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    testreport ='/Users/jiangxufeng1/PycharmProjects/Benlaitest/testReport'
    filename = testreport + now + 'TestReport.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'测试报告详细信息'
    )
    runner.run(suite)
    fp.close()
if __name__ =='__main__':
    unittest.main(verbosity=2)