from flask import Flask
from openai import OpenAI
import os
# from flask_cors import CORS
import weather_url as WeatherAPI
import outfitPicker as Outfit

app = Flask(__name__)
# CORS(app, supports_credentials=True)
client = OpenAI(api_key=os.environ.get('API_KEY'))


@app.route("/")
def hello_world():
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Recommend me an outfit for " + str(cur_temp) + "degrees Farenheit weather. There's as min of " + str(min_temp) + 
            " and a max of " + str(max_temp) + " and I want an outfit that will work for the whole day."
        }
        ],
        temperature=0.7 #controls randomness
    )
    return "<p>" + completion.choices[0].message.content + "</p> <p>" + str(temp) + "</p>"
    
    # pickOutfit()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)