from copy import deepcopy
import requests, json

url = "https://coderbyte.com/api/challenges/json/json-cleaning"
req = requests.get(url=url).json()
target = ['N/A', "", "-"]
temp = deepcopy(req)
for k, v in req.items():
    if v in target:
        del temp[k]
    if type(v) == dict:
        for kk, vv in v.items():
            if vv in target:
                del temp[k][kk]
    if type(v) == list:
        for vv in range(len(v)):
            if v[vv] in target:
                temp[k].pop(vv)

res = json.dumps(temp)
print(res)
