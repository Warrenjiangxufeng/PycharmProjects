# coding=utf-8
#codepushgit
import requests
import random

class tes():
    def testff(self):
        w=1
    def test_fi(self):
        url = 'https://api.apiopen.top/getJoke?page=1&count=2&type=video'
        r = requests.get(url)
        print('--------------------------------')
        print ("Status code:", r.status_code)
        response_dict = r.json()
        print(response_dict['code'])

        return response_dict

    def test_se(self):
        r = tes.test_fi(self)
        e = r['code']
        t = e + 1
        print(t)







if __name__ == '__main__':
    zz = tes()

    zz.test_se()
