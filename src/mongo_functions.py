from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

#Get Password
connection = os.getenv('URLMONGO')
if connection == None:
    connection = os.environ["URLMONGO"]
    
#Connect to DB
client = MongoClient(connection)


def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db,collection_fs = connectCollection('ets_factory','financial_securities')