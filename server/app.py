from flask import Flask
from openai import OpenAI
import os
# from flask_cors import CORS
import weather_url as WeatherAPI
import outfitPicker as Outfit

app = Flask(__name__)
# CORS(app, supports_credentials=True)

@app.route("/")
def getHome():
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]

    return "<p>" + str(temp) +"</p>"

@app.route("/getkit", methods=["GET"])
def getKit():
    myOutfit = Outfit.pickOutfit()
    # return jsonify(myOutfit)
    return myOutfit

@app.route("/login", methods=["POST"])
def getLogin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if(not db.verifyUser(username, password)):
        return jsonify({"error": "Invalid login attempt"}), 401
    else:
        return ""

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    temp_pref = data.get('temperature_preference')
    email = data.get('email')

    db.addUser(username, password, temp_pref, email)
    return ""

@app.route("/wardrobe", methods=["POST"])
def expandWardrobe():
    data = request.json
    name = data.get('name')
    category = data.get('category')
    username = data.get('username')

    db.addClothing(name, category, username)
    return ""

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)