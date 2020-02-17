from flask import Flask,render_template, url_for, request, session, redirect
from src.mongo_functions import collection_fs
from src.update_functions import update_financial_securitie
import time
import json
import requests
import os

app = Flask(__name__)

def uploadjson():
    upload    = request.files.get('upload')
    print('==============>UPLOAD',upload.filename)
    if upload == None or upload.filename == '':
        return 'Error no json'
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.json'):
        return 'Error'
    upload.save('/tmp/upload.json') # appends upload.filename automatically
    with open('/tmp/upload.json') as f:
        d = json.load(f)
        print(d)
    return d

@app.route("/")
def check_server(value="",value2 =""):
    return render_template("home.html", value=value)

@app.route("/update", methods=['POST'])
def update_fs():
    peticiones = request.get_json()
    if peticiones == None:
        peticiones = uploadjson()
    print(peticiones['0'])
    financial_securitie = list(collection_fs.find({'id':peticiones['0']["id_fs"]}))[-1]
    # print("===============Inancial_securitie=====================")
    print(financial_securitie)
    financial_securitie_final = update_financial_securitie(financial_securitie,peticiones)
    # print("===============Financial_securitie_final=====================")
    # print(financial_securitie_final)
    collection_fs.insert(financial_securitie_final)
    return  check_server(value="actualizado")
@app.route("/insert", methods = ['POST'])
def insert_finantial_securitie():
    financial_securitie = request.get_json()
    if financial_securitie == None:
        peticiones = uploadjson()
    print(financial_securitie)
    financial_securitie["timestamp"]=time.time()
    print(financial_securitie)
    collection_fs.insert(financial_securitie)
    return check_server(value2="añadido")
if __name__ == '__main__':
    app.run(debug=True)