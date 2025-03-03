from flask import Flask, request, jsonify
from openai import OpenAI
import os
# from flask_cors import CORS
import weather_url as WeatherAPI
import outfitPicker as Outfit
import mongodb as db

app = Flask(__name__)
# CORS(app, supports_credentials=True)

@app.route("/")
def getHome():
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]

    return "<p>" + str(temp) +"</p>"

# For hackathon purposes: routes will just return success if error thrown
# Ideally fix the Swift front end to send paramters/form data in the request

# Get recommended clothes based on weather and current wardrobe
@app.route("/getkit", methods=["GET"])
def getKit():
    # username = request.args.get('username')
    myOutfit = Outfit.pickOutfit()
    return myOutfit

# Verify login
@app.route("/login", methods=["POST"])
def getLogin():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if(not db.verifyUser(username, password)):
            return jsonify({"error": "Invalid login attempt"}), 401
        else:
            return ""
    except Exception as e:
        print(e)
    return ""

# Create account
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        temp_pref = data.get('temperature_preference')
        email = data.get('email')

        db.addUser(username, password, temp_pref, email)
        return ""
    except Exception as e:
        print(e)
    return ""

# Add clothing item
@app.route("/wardrobe", methods=["POST"])
def expandWardrobe():
    try:
        data = request.json
        name = data.get('name')
        category = data.get('category')
        username = data.get('username')

        db.addClothing(name, category, username)
        return ""
    except Exception as e:
        print(e)
    return ""

if __name__ == '__main__':
    db.initDB()
    app.run(debug=True, host="0.0.0.0", port=5002)