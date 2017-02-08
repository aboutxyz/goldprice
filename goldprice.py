#coding:utf-8

import requests
from lxml import etree
import re
from fake_useragent import UserAgent
n= ''
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
}
proxies = {"http": "192.168.9.5:8080", "https": "192.168.9.5:8080",}
params = {'p':'%E5%91%A8%E5%A4%A7%E7%A6%8F', 'c':'0', 'sdate':'2017-01-08', 'edate':'2017-02-08', 'count':'500', 'callback':'hxbase_json14865408480482'}
s = requests.session()
r = s.post("http://data.gold.hexun.com/GoldHistoryPage.aspx", proxies=proxies, headers = headers, data= params)
r.encoding = "utf-8"
selector = etree.HTML(r.content)
result = selector.xpath('//td')
for i in result:
    try:
        print i.text
    except:
        pass
test = u'足金零售价'
# for i in xrange(len(result)-1):
    # try:
        # if test in result[i].text:
            # print result[i+1].text
    # except:
        # pass