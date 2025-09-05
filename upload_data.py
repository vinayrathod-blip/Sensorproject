


from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri='mongodb+srv://210010010064_db_user:210010010064@cluster1.4i5sann.mongodb.net/?retryWrites=true&w=majority&appName=cluster1'

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME='waferfault'

df=pd.read_csv(r"C:\Users\Student\Downloads\Sensor_Project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)















0