import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["mydatabase"]
col=db["student"]

#inserting the data

values=[{"Name ":"Abhi","Age":20,"Phone":9876543},
{"Name ":"Shiv","Age":24,"Phone":9834543},
{"Name ":"Yadhu","Age":29,"Phone":9226543},
{"Name ":"Abhi","Age":20}]
# for many column values(documents)
# if(col.insert_many(values)):
#     print("Successfully Inserted")
# else:
#     print("Failed to insert")

# values={"Name ":"Abhi","Age":20,"Phone":9876543}
# col.insert_one(values) for single column value

var = col.find({},{"Name ":2})
for i in var:
    print(i)