# coding:utf-8
import json

with open("goldhistory.json", "r") as f:
    for i in json.loads(f.read()):
        if i["fld_name"] == u"足金零售价":
            print i["fld_newprice"]