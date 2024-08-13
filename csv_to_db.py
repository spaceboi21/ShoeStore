import csv
import pandas as pd 
import pymongo


list = []
with open("dataset.csv", 'r') as file:
    data = csv.reader(file,delimiter = '\n')  # extracting one row 
    for i in data:
        list.append(i[0].split(';')) #splitting the data with delimiter ;
        
with open('new_dataset.csv', 'w',newline='') as data:
    writer = csv.writer(data)
    writer.writerows(list)

df=pd.read_csv("new_dataset.csv")

data=df.to_dict(orient="records")

client = pymongo.MongoClient("mongodb://localhost:27017/")

client.list_database_names() # by default we have two Db 

db=client["ShoeStore"]

COLLECTION_NAME = "shoe_details"
collection = db[COLLECTION_NAME]

collection.insert_many(data)

client.list_database_names()
 