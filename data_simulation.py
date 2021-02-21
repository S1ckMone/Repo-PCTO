import schedule
import random
import time
import requests
import json

def json_constructor(data):
    water = round(random.uniform(0,1), 4)
    ground_temp = round(random.uniform(-40, 120), 2)
    enviroment_temp = round(random.uniform(-40, 120), 2)
    enviroment_umidity = round(random.uniform(0,100), 2)
    hour = time.time()
    data["vwc"] = water
    data["gt"] = ground_temp
    data["et"] = enviroment_temp
    data["eu"] = enviroment_umidity
    data["acquisition"] = hour
    data_sender(data)

def data_sender(data):
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    print(type(json_data))
    print(json_data)
    #x = requests.post("https://vipjop6bq4.execute-api.us-east-1.amazonaws.com/dev/field/stats", json_data, headers)

data = {}
json_constructor(data)
