import requests
import json

for i in range(10):
    data = dict(t=i, h=i+1)
    payload = json.dumps(data)
    url = 'http://192.168.2.110:1111/'
    response = requests.post(url, data=payload)
    print(response)