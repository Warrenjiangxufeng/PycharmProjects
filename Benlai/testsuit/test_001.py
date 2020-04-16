#coding=utf-8
import requests
import datetime
import time
import threading
import json
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        print("start test")

    def tearDown(self):
        print("end test")



class test_001(MyTest):
    times = []
    error = []
    success =[]
    def test001(self):
        mytest = test_001
        url = 'http://192.168.60.47:9000/srm/vendor/save'
        data = {"vendorProperty":"0","vendorName":"12","vendorSname":"22","typeId":"1","registerProvince":"北京市","registerCity":"北京市","province":"北京市","city":"北京市","typeName":"批发","propertyName":"","provinceId":"3","cityId":"1114","registerProvinceId":"3","registerCityId":"1114"}
        headers = {'Authorization': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJncm91cFNpZCI6IndlYiIsImlzRmlyc3RMb2dpbiI6IjAiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3VzZXJkYXRhIjoiYWRtaW4iLCJ1c2VyX25hbWUiOiJhZG1pbiIsImlzcyI6Imh0dHA6Ly9yZXRhaWxhcGkuYmVubGFpLmNvbSIsInVzZXI6bmlja25hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJ1c2VyOm5hbWUiOiJhZG1pbiIsImF1dGhvcml0aWVzIjpbIlJPTEVfVVNFUiJdLCJwcmltYXJ5c2lkIjoiNCIsImNsaWVudF9pZCI6IndlYiIsImF1ZCI6WyJCZW5sYWkuTzJPRVJQLldlYkFwaSJdLCJzZWxlY3RzdG9yZSI6IntcInN0b3JlTmFtZVwiOlwi5q2m5rGJ56ys5LiA6YWN6YCBXCIsXCJzdG9yZU5vXCI6XCJXODAxXCIsXCJzdG9yZVN5c05vXCI6NjN9Iiwic2NvcGUiOlsiYWxsIl0sIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJleHAiOjE1MzUwMjk0ODUsImp0aSI6IjBhMmVjZDExLTgwMjktNDI5YS1iNmFhLTA1OTdkYzJlNDMxZCIsInVzZXI6ZXhwaXJlcyI6MTUzOTY4MDM3MTAwMH0.6k46H--y_5Xqx3pOp0qLA2cqxXhxP8GLff7aCZRa4Qw',
                   'Connection': 'keep-alive',
                   'X - Store': '{"storeSysNo": 63, "storeNo": "W801"}'}
        #data = 'from=en&to=zh&query=i+love+you&transtype=translang&simple_means_flag=3&sign=127170.332787&token=43c7995134a30a2a0e241d0245cc366d'
        r = requests.post(url=url, headers=headers, data=data)
        ResponseTime = float(r.elapsed.microseconds)/1000
        mytest.times.append(ResponseTime)
        print(r.status_code)
        if r.status_code == 200:
            mytest.error.append("0")
            print('status is right!')
            print (r.text)
        try:
            self.assertEquals(r.text['code'], 0)
        except:
            re = json.loads(r.text)
            return re['msg']

        #print (r.text)
        #print(r.json())


if __name__=="__main__":
    mytest = test_001()