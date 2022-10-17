from pymongo import MongoClient

connecion = MongoClient("mongodb://127.0.0.1:27017/")

mydb = connecion["cromo"]["log"]