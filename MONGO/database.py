import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["imagenes"]
imagenes_tb = mydb["imagenes_tb"]

# mydict = { "name": "jose", "address": "fictizia", "friends":["5dfa768c870b6f84aa9246e0", "5dfa777f1767a13556146ec7"] }

# x = customers.insert_one(mydict)
# info_id = x.inserted_id

# info_id = "5dfa7a684fc4502e04a63940"

# customer = customers.find_one({"_id":ObjectId(info_id)})
# friends = list()
# for friend_id in customer.get('friends'):
#     friend = customers.find_one({"_id":ObjectId(friend_id)})
#     friends.append(friend.get('name'))

# print(customer)
# customer['friends'] = friends


# print(customer)
# for info in info_from_db:
#     print(info)


# customers = customers.find({})
# for customer in customers:
    # print(customer)


images = imagenes_tb.find()
for image in images:
    print(image.get('imagenes'))