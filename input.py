import json
import requests
import time
import datetime

def data_sender_values(data):
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    print(json_data)
    x = requests.post("https://k1lcrvj5x8.execute-api.us-east-1.amazonaws.com/dev/field/nodes", json_data, headers)
    return x.text

def data_sender_get(data):
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    url = "https://k1lcrvj5x8.execute-api.us-east-1.amazonaws.com/dev/field/stats"
    print(json_data)
    x = requests.request("GET", url,headers=headers, data=json_data)
    return x.text

data = {}
vwc = {}
gt = {}
eu = {}
et = {}
k=0
while(k==0):
    field = int(input("inserisci campo (1,2,3) = "))
    if field==1 or field==2 or field==3:
        k=1

time_delta = int(input("Inserisci minuti = "))
date_now = time.time()
date_now = date_now - (time_delta*60)

data["field"] = field
data["time"] = date_now
data2 = data_sender_values(data)
data2 = json.loads(data2)
values = data_sender_get(data2)
et = values["et"]
gt = values["gt"]
vwc = values["vwc"]
eu = values["eu"]
