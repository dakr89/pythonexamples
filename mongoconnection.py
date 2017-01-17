import pymongo

from pymongo import MongoClient


client = MongoClient()

db = client.primer
print(db.dataset)