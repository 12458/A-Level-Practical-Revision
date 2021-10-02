import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("OUTLETS")
coll = db.get_collection("GEM")
	
result = coll.find()
errors = []

def check_serial(s): 
    if len(s) != 4:
        return False
    elif s[0].isdigit() != True:
        return False
    elif s[1:3].isalpha() != True:
        return False
    elif s[3].isdigit() != True:
        return False
    return True

def check_name(s): 
    for item in s:
        if item.isalpha() or item.isspace() or item.isdigit():
            continue
        else:
            return False
    return True

for doc in result:
    if doc["Quantity"].isdigit() == False:
        errors.append(doc)
        coll.delete_one(doc)
    elif check_serial(doc["Serial_No"]) == False:
        errors.append(doc)
        coll.delete_one(doc)
    elif check_name(doc["Name"]) == False:
        errors.append(doc)
        coll.delete_one(doc) #1 mark for deleting record
print(errors)

##result = coll.find()
##for doc in result:
##    print(doc)
        