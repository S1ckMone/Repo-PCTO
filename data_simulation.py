import json
import random
import numpy
import schedule
import requests
import psycopg2 as pg
import time

def base_temperature(et):
    et = round(random.uniform(et-3, et+3), 2)
    return et


def nodes_identifier():
    record = db_connection()
    for i in record:
        id_s = i[0]
        field = i[1]
        risult(id_s, field)


def db_connection():                #Connessione al database e selezione di id e campo del sensore
    conn = pg.connect(
        host="db-gruppo-5.cykdo1jweq0j.us-east-1.rds.amazonaws.com",
        database="lavoropcto",
        user="postgres",
        password="Sim$pri24db")
    cursor = conn.cursor()
    query = "select id, field from sensor_status"
    cursor.execute(query)
    record = cursor.fetchall()
    cursor.close()
    conn.close()
    return record                   #record contenente id e campo del sensore


def risult(id_s, field):
    data = {}
    if field == 1:
        global et_1
        et_1 = base_temperature(et_1)
        gt = round(random.uniform(et_1+1, et_1+4), 2)
        data["et"] = et_1
    if field == 2:
        global et_2
        et_2 = base_temperature(et_2)
        gt = round(random.uniform(et_2+1, et_2+4), 2)
        data["et"] = et_2
    if field == 3:
        global et_3
        et_3 = base_temperature(et_3)
        gt = round(random.uniform(et_3+1, et_3+4), 2)
        data["et"] = et_3
    eu = round(random.uniform(0, 100), 2)
    vwc = round(random.uniform(0,1), 4)
    data["vwc"] = vwc 
    data["gt"] = gt
    data["eu"] = eu
    data["acquisition"] = time.time()
    data["fk_id"] = id_s
    data_sender_values(data)


def data_sender_values(data):
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    print(json_data)
    x = requests.post("https://k1lcrvj5x8.execute-api.us-east-1.amazonaws.com/dev/field/stats", json_data, headers)

et_1 = round(random.uniform(-2, 15), 2)
et_2 = round(random.uniform(et_1-5, et_1+5), 2)
et_3 = round(random.uniform(et_1-7, et_1+7), 2)
schedule.every(5).seconds.do(nodes_identifier)    #ripetizione ciclica della funzione nodes_identifier
while True:
    schedule.run_pending()


