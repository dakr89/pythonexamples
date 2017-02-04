import pymongo
from pymongo import MongoClient
import json



client = pymongo.MongoClient()
#  crating db 
db = client['anil']
# na = {'name':'anil','age':28,'location':'hyderabad'}
# mul = [{'name':'kumar','age':29,'location':'kphb'},
# {'name':'reddy','age':27,'location':'racherla','ambition':'good person'},
# {'name':'krishna','age':55,'location':'racherla','dad':'iloveyou'},


# ]
# creating collection in the db
cl = db['name']
cl.drop()

file = open('test.json','r')
paring_data = json.loads(file.read())

# inserting each record
for x in paring_data:
	
	cl.insert_one(x)
	# cl.insert(x)

#  inserting data into collection
# record = cl.insert_one(na).inserted_id

#  bulk insert 

# records = cl.insert_many(mul)

#  if you find  list of colletions use this
# print(db.collection_names(include_system_collections=False))

# # retrieve data from collections
#  all records from collections

# data = db['name'].find()
# for x in data:
# 	print(x)

# first row from the collections
# data = db['name'].find_one()
# print(data)


# retrieve based on key and value  from the collections
# data = db['name'].find_one({'location':'racherla'})

# find no of documents in a collection 
# no_cnt = db['name'].count()
# print(no_cnt)


# find no of doct with the filter
# cnt = db['name'].find({'location':'racherla'}).count()

#  if you  want to drop collection use 
#  db.collectionname.drop() it will return true if it is dropped otherwise false

#  if you  want to drop  database  
#  1.  change it to particular db you want to drop
# 2. just use command db.dropDatabase()  -- it will drop db

#  get only name=anil documents from the collection just use this one
# rows = db['name']
# # for x in rows.find({'name':'anil'}):
# # 	print(x)

# for x in rows.find():
# 	print(x)
