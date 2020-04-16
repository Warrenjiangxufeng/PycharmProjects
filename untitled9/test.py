# coding=utf-8
import requests
import unittest
class testapi(unittest.TestCase):
    def setUp(self):

        url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'
        self.r = requests.get(url)
        #print ("Status code:", self.r.status_code)
        self.response_dict = self.r.json()
        #print ("Output keys: ", self.response_dict.keys())


    def test_001(self):

        self.assertEqual(self.r.status_code, 200, msg='testing status not pass！')
    def test_002(self):
        self.assertIn('message',self.response_dict.keys(), msg='mistake!')
#if __name__=='__main__':
 # unittest.main()
suite = unittest.TestSuite()
suite.addTest(testapi('test_001'))
suite.addTest(testapi('test_002'))
runner = unittest.TextTestRunner()
runner.run(suite)