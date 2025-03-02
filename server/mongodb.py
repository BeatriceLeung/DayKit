from pymongo.mongo_client import MongoClient
# import json
import time

import os

# Using Mongo DB Atlas
uri = "mongodb+srv://daykit7:tebnof-mogjEf-kecvu2@hoth.c563n.mongodb.net/?retryWrites=true&w=majority&appName=hoth"
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
        clothes_array.append(clothing['name'])
    
    return clothes_array

# Add single item of clothing with given name, type, and user
def addClothing(name, type, user_name):
    db.Clothes.insert_one({"name" : name, "user_name" : user_name, "type" : type})

# Add a user
def addUser(name, password, temp_pref):
    db.Users.insert_one({"name" : name, "password" : password, "temp_pref" : temp_pref})


# Testing
initDB()
# addUser("me", "password", -1)
addClothing("longsleeves 1", "longsleeves", "me")
addClothing("hoodie 1", "hoodie", "me")
addClothing("jacket 1", "jacket", "me")
addClothing("leggings 1", "leggings", "me")
addClothing("pants 1", "pants", "me")
addClothing("longfuzzy 1", "longfuzzy", "me")
addClothing("longwool 1", "longwool", "me")
addClothing("sneakers 1", "sneakers", "me")
addClothing("boots 1", "boots", "me")
addClothing("longcotton 1", "longcotton", "me")
addClothing("lightjacket 1", "lightjacket", "me")
addClothing("sweater 1", "sweater", "me")
addClothing("blouse 1", "blouse", "me")
addClothing("dress 1", "dress", "me")
addClothing("shortcotton 1", "shortcotton", "me")
addClothing("shortsleeves 1", "shortsleeves", "me")
addClothing("shorts 1", "shorts", "me")
addClothing("sandals 1", "sandals", "me")
addClothing("skirt 1", "skirt", "me")
addClothing("tank 1", "tank", "me")