#coding=utf-8
import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)



class AddEventTest(unittest.TestCase):
    ''' 接口测试 '''

    def setUp(self):

        url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'
        self.r = requests.get(url)
        #print ("Status code:", self.r.status_code)
        self.response_dict = self.r.json()
        #print ("Output keys: ", self.response_dict.keys())



    def test_add_event_all_null(self):
        ''' 断言 '''
        self.assertEqual(self.r.status_code, 200, msg='testing status not pass！')


if __name__ == '__main__':

    unittest.main()
