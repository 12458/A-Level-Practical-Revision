import pymongo
f1 = open("INVENTORY SERIAL.txt")
lst = []
for item in f1: 
    temp = item.strip().split('\t')
    lst.append({"Serial_No":temp[0], "Name":temp[1], "Type":temp[2], "Purchase_Price":temp[3], "Selling_Price":temp[4], "Quantity":temp[5]})

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("OUTLETS")
coll = db.get_collection("GEM")
db.drop_collection("GEM") 
coll.insert_many(lst)

##def print_coll(coll):
##    result = coll.find()
##    for doc in result:
##        print(doc)
##
##print_coll(coll)