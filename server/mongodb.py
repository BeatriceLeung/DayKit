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
# initDB()
# addUser("me", "password")
# addClothing("shirt 1", "tank", "me")
# addClothing("shirt 2", "tank", "me")
# addClothing("shirt 3", "short-sleeve", "me")

# print(getClothes("tank", "me"))