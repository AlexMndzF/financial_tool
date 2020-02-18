#!/usr/local/bin/python3

from flask import Flask,render_template, url_for, request, session, redirect
from src.mongo_functions import collection_fs
from src.update_functions import update_financial_securitie
from src.procces_data_functions import uploadjson
import time
import json
import requests
import os
from datetime import datetime


app = Flask(__name__)




@app.route("/")
def check_server(value=""):
    return render_template("home.html", value=value)

@app.route("/update", methods=['POST'])
def update_fs():
    peticiones = request.get_json()
    if peticiones == None:
        peticiones = uploadjson()
    financial_securitie = list(collection_fs.find({'id':peticiones['0']["id_fs"]}))[-1]
    financial_securitie_final = update_financial_securitie(financial_securitie,peticiones)
    collection_fs.insert(financial_securitie_final)
    return  redirect('/')


@app.route("/insert", methods = ['POST'])
def insert_finantial_securitie():
    financial_securitie = request.get_json()
    print(financial_securitie)
    if financial_securitie == None: 
        financial_securitie = uploadjson()
    financial_securitie["timestamp"]=time.time()
    collection_fs.insert(financial_securitie)
    
    return  redirect('/')

@app.route('/line', methods = ['POST'])
def get_char():
    id_fs =  request.form["id_fs"]
    query = {'id':f'{id_fs}'}
    financial = list(collection_fs.find(query))
    entity = financial[0].get('entity')
    sinthetic_index = []
    time = []
    for i in range(len(financial)):
        timestamp = financial[i]['timestamp']
        time.append((timestamp))
        sinthetic_index.append(financial[i]['Synthetic_index'])
    line_labels= [datetime.fromtimestamp(ts) for ts in time]
    line_values=sinthetic_index
    return render_template('line_chart.html', title=f'Sinthetic index evolution of {entity}', max=max(line_values)+100, labels=line_labels, values=line_values)


if __name__ == '__main__':
    app.run(debug=True)