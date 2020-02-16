from flask import Flask,render_template, url_for, request, session, redirect
from src.mongo_functions import collection_fs
from src.update_functions import update_financial_securitie
import time

app = Flask(__name__)

@app.route("/")
def check_server():
    return render_template("home.html")

@app.route("/update", methods=['POST'])
def update_fs():
    peticiones = request.get_json()
    # print(peticiones['0'])
    financial_securitie = list(collection_fs.find({'id':peticiones['0']["id_fs"]}))[-1]
    # print("===============Inancial_securitie=====================")
    print(financial_securitie)
    financial_securitie_final = update_financial_securitie(financial_securitie,peticiones)
    # print("===============Financial_securitie_final=====================")
    # print(financial_securitie_final)
    collection_fs.insert(financial_securitie_final)
    return (f"{200}")
@app.route("/insert", methods = ['POST'])
def insert_finantial_securitie():
    financial_securitie = request.get_json()
    print(financial_securitie)
    financial_securitie["timestamp"]=time.time()
    print(financial_securitie)
    collection_fs.insert(financial_securitie)
    return (f"{200}")

if __name__ == '__main__':
    app.run(debug=True)