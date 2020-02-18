from flask import Flask,render_template, url_for, request, session, redirect
from src.mongo_functions import collection_fs
from src.update_functions import update_financial_securitie
from src.procces_data_functions import uploadjson
import time
import json
import requests
import os

app = Flask(__name__)



@app.route("/")
def check_server(value="",value2 =""):
    return render_template("home.html", value=value)

@app.route("/update", methods=['POST'])
def update_fs():
    peticiones = request.get_json()
    if peticiones == None:
        peticiones = uploadjson()
    financial_securitie = list(collection_fs.find({'id':peticiones['0']["id_fs"]}))[-1]
    financial_securitie_final = update_financial_securitie(financial_securitie,peticiones)
    collection_fs.insert(financial_securitie_final)
    return  check_server(value="Updated")


@app.route("/insert", methods = ['POST'])
def insert_finantial_securitie():
    financial_securitie = request.get_json()
    print(financial_securitie)
    if financial_securitie == None: 
        financial_securitie = uploadjson()
    financial_securitie["timestamp"]=time.time()
    collection_fs.insert(financial_securitie)
    return check_server(value="Added")

    
if __name__ == '__main__':
    app.run(debug=True)