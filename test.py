# coding:utf-8
import json
import re
import requests

with open('goldtest.json', 'r')as f:
    for i in f:
        data = json.loads(i, "utf-8")
        for j in data:
            print j
