#coding=utf-8
import requests
import json
import readExcel
class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data
    @property
    def headers(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers
    @property
    def testApi(self):
        try:
            if self.method == 'post':
                r = requests.post(self.url, data=json.dumps(eval(self.data), headers=self.headers))
            elif self.method == 'get':
                r = requests.get(self.url, params=self.data)
            return r
        except:
            print('失败')
    def getCode(self):
        code = self.testApi.json()['code']
        return code
    def getStatusCode(self):
        status_code = self.testApi.json()['status_code']
        return status_code
    def getJson(self):
        json_data = self.testApi.json()
        return json_data