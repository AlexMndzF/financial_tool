from flask import Flask,render_template, url_for, request, session, redirect
from src.mongo_functions import coll
from src.update_functions import update_financial_securitie

app = Flask(__name__)

@app.route("/")
def check_server():
    return ('connected')

@app.route("/update", methods=['POST'])
def update_fs():
    peticiones = request.get_json()
    print("====================================")
    print(peticiones)
    financial_securitie = list(coll.find({'id':peticiones[0]["id_fs"]}))[-1]
    print("====================================")
    print(financial_securitie)
    financial_securitie_final = update_financial_securitie(financial_securitie,peticiones)
    print("====================================")
    print(financial_securitie_final)
    coll.insert(financial_securitie_final)
    return coll.find({})


if __name__ == '__main__':
    app.run(debug=True)