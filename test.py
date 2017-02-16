# coding:utf-8
import json

pricelist = []
with open("goldhistory.json", "r") as f:
    for i in json.loads(f.read()):
        if i["fld_name"] == u"足金零售价":
            print i["fld_newprice"],i["fld_secudate"]
            pricelist.append([i["fld_secudate"],float(i["fld_newprice"])])

encode_json = json.dumps(pricelist)            
with open("golddata.json", "a") as boom:
    boom.write(encode_json)