from pymongo.mongo_client import MongoClient
import time
import os

# Using Mongo DB Atlas
uri = "mongodb+srv://daykit06:daykit06@hoth.c563n.mongodb.net/?retryWrites=true&w=majority&appName=hoth"
db = None
def initDB():
    global db
    # Create a new client and connect to the server
    client = MongoClient(uri)
    db = client.hoth

    time.sleep(1)

def getTempPref(name="me"):
    return db.Users.find_one({"name" : name})['temp_pref']

# Return array of clothes for given type and user (default user:"me")
def getClothes(type, user="me"):
    clothes_array =[]
    cursor = db.Clothes.find({"user_name" : user, "type": type})

    for clothing in cursor:
        clothes_array.append(clothing['type'])
    
    return clothes_array

# Add single item of clothing with given name, type, and user
def addClothing(name, type, user_name):
    db.Clothes.insert_one({"name" : name, "user_name" : user_name, "type" : type})

# Add a user
def addUser(name, password, temp_pref, email):
    db.Users.insert_one({"name" : name, "password" : password, "temp_pref" : temp_pref, "email" : email})

def verifyUser(name, password):
    return db.Users.find_one({"name" : name})['password'] == password



# # Testing
initDB()
# addUser("me", "password", -1)
# addClothing("longsleeves", "longsleeves", "me")
# addClothing("hoodie", "hoodie", "me")
# addClothing("jacket", "jacket", "me")
# addClothing("leggings", "leggings", "me")
# addClothing("pants", "pants", "me")
# addClothing("longfuzzy", "longfuzzy", "me")
# addClothing("longwool", "longwool", "me")
# addClothing("sneakers", "sneakers", "me")
# addClothing("boots", "boots", "me")
# addClothing("longcotton", "longcotton", "me")
# addClothing("lightjacket", "lightjacket", "me")
# addClothing("sweater", "sweater", "me")
# addClothing("blouse", "blouse", "me")
# addClothing("dress", "dress", "me")
# addClothing("shortcotton", "shortcotton", "me")
# addClothing("shortsleeves", "shortsleeves", "me")
# addClothing("shorts", "shorts", "me")
# addClothing("sandals", "sandals", "me")
# addClothing("skirt", "skirt", "me")
# addClothing("tank", "tank", "me")
# addClothing("rainboots", "rainboots", "me")