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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)