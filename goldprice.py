#coding:utf-8

import requests
from lxml import etree
import re
# from fake_useragent import UserAgent
# ua = UserAgent()
# headers = {
#     'User-Agent': ua.random,
# }
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
}
# proxies = {"http": "192.168.9.5:8080", "https": "192.168.9.5:8080",}
params = {'p':'%E5%91%A8%E5%A4%A7%E7%A6%8F', 'c':'0', 'sdate':'2017-01-08', 'edate':'2017-02-08', 'count':'2000','page':'1', 'callback':'hxbase_json14865612313312'}
s = requests.session()
r = s.get("http://data.gold.hexun.com/outdata/GoldHistoryData.ashx?", headers=headers, params=params)
r.encoding = "utf-8"
selector = etree.HTML(r.content)
result = selector.xpath('//td')
