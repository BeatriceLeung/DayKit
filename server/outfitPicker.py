import weather_url as WeatherAPI
import mongodb as db
import random

def getRandomItem(items):
    if len(items) > 0:
        return random.sample(items, 1)
    return []

def pickOutfit(user="me"):
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]
    rain_chance = temp["preciptation_prob"]

    pref =  db.getTempPref(user) #user runs hot/cold
    
    longsleeves = db.getClothes("longsleeves", user)
    hoodie = db.getClothes("hoodie", user)
    jacket = db.getClothes("jacket", user)
    leggings = db.getClothes("leggings", user)
    pants = db.getClothes("pants", user)
    longfuzzy = db.getClothes("longfuzzy", user)
    longwool = db.getClothes("longwool", user)
    sneakers = db.getClothes("sneakers", user)
    boots = db.getClothes("boots", user)
    longcotton = db.getClothes("longcotton", user)
    lightjacket = db.getClothes("lightjacket", user)
    sweater = db.getClothes("sweater", user)
    blouse = db.getClothes("blouse", user)
    dress = db.getClothes("dress", user)
    shortcotton = db.getClothes("shortcotton", user)
    shortsleeves = db.getClothes("shortsleeves", user)
    shorts = db.getClothes("shorts", user)
    sandals = db.getClothes("sandals", user)
    skirt = db.getClothes("skirt", user)
    tank = db.getClothes("tank", user)

    rainboots = db.getClothes("rainboots", user)


    myOutfit = []
    if(max_temp < 40):
        if(pref == -1):
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(hoodie)
            myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(leggings)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longfuzzy + longwool)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(hoodie)
            myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
        else:
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
    elif(max_temp>=40 and max_temp<60):
        if(pref == -1):
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(lightjacket)
            if(min_temp<=40):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longfuzzy + longwool)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves)
            if(min_temp<=40):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
        else:
            myOutfit += getRandomItem(longsleeves)
            if(min_temp<=40):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(leggings+pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
    elif(max_temp>=60 and max_temp<80):
        if(pref == -1):
            myOutfit += getRandomItem(longsleeves+hoodie+sweater)
            if(min_temp<=60):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longfuzzy + longcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves+blouse+dress)
            if(min_temp<=60):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants+leggings)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers)
        else:
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            if(min_temp<=60):
                myOutfit += getRandomItem(lightjacket)
            myOutfit += getRandomItem(leggings+pants+shorts)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+sandals)
    else:
        if(pref == -1):
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            if(min_temp<=80):
                myOutfit += getRandomItem(lightjacket)
            myOutfit += getRandomItem(pants+leggings)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers)
        elif(pref == 0):
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            myOutfit += getRandomItem(pants+skirt+shorts)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers)
        else:
            myOutfit += getRandomItem(tank+shortsleeves+blouse+dress)
            myOutfit += getRandomItem(shorts+skirt)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            if(rain_chance > 40):
                myOutfit += getRandomItem(rainboots)
            else:
                myOutfit += getRandomItem(sneakers+sandals)

    for item in myOutfit:
        print(item) 
    
    return myOutfit
            
# print(pickOutfit())