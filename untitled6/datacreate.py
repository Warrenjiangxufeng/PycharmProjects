
# -*- coding:utf-8 -*-
#import urllib2
#import urllib

#da = {"contractName": "1","tradeModeId":"4","vendorNo":"6001152","vendorName":"1","vendorSysno":658,"payTermId":"1","provTypeId":"DC","provType":"配送","payTerm":"周结","tradeMode":"代销"}
#user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
#headers = {'User-Agent': user_agent}
#url = 'http://192.168.60.46:9000/srm/contract/addBasicInfo'
#data = urllib.urlencode(da)
#request = urllib2.Request(url, data, headers)
#response = urllib2.urlopen(request)
#message = response.read().decode()
#print(message)

import requests
data = {"contractName": "1","tradeModeId":"4","vendorNo":"6001152","vendorName":"1","vendorSysno":658,"payTermId":"1","provTypeId":"DC","provType":"配送","payTerm":"周结","tradeMode":"代销"}
user_agent ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
headers = {'User-Agent': user_agent}
url = 'http://192.168.60.46:9000/srm/contract/addBasicInfo'
req = requests.post(url, data, headers)
print(req.status_code)
print(req.text)