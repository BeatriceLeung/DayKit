import weather_url as WeatherAPI
import mongodb as db

def pickOutfit():
    user="me" # default user
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]

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


    myOutfit = []
    if(max_temp < 40):
        if(pref == -1):
            myOutfit += random.sample(longsleeves, 1)
            myOutfit += random.sample(hoodie, 1)
            myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(leggings, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longfuzzy + longwool, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
        elif(pref == 0):
            myOutfit += random.sample(longsleeves, 1)
            myOutfit += random.sample(hoodie, 1)
            myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
        else:
            myOutfit += random.sample(longsleeves, 1)
            myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
    elif(max_temp>=40 and max_temp<60):
        if(pref == -1):
            myOutfit += random.sample(longsleeves, 1)
            myOutfit += random.sample(lightjacket, 1)
            if(min_temp<=40) myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longfuzzy + longwool, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
        elif(pref == 0):
            myOutfit += random.sample(longsleeves, 1)
            if(min_temp<=40) myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
        else:
            myOutfit += random.sample(longsleeves, 1)
            if(min_temp<=40) myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(leggings+pants, 1)
            myOutfit += random.sample(longcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
    elif(max_temp>=60 and max_temp<80)
        if(pref == -1):
            myOutfit += random.sample(longsleeves+hoodie+sweater, 1)
            if(min_temp<=60) myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants, 1)
            myOutfit += random.sample(longfuzzy + longcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+boots, 1)
        elif(pref == 0):
            myOutfit += random.sample(longsleeves+blouse+dress, 1)
            if(min_temp<=60) myOutfit += random.sample(jacket, 1)
            myOutfit += random.sample(pants+leggings, 1)
            myOutfit += random.sample(shortcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers, 1)
        else:
            myOutfit += random.sample(shortsleeves+blouse+dress, 1)
            if(min_temp<=60) myOutfit += random.sample(lightjacket, 1)
            myOutfit += random.sample(leggings+pants+shorts, 1)
            myOutfit += random.sample(shortcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+sandals, 1)
    else:
        if(pref == -1):
            myOutfit += random.sample(shortsleeves+blouse+dress, 1)
            if(min_temp<=80) myOutfit += random.sample(lightjacket, 1)
            myOutfit += random.sample(pants+leggings, 1)
            myOutfit += random.sample(shortcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers, 1)
        elif(pref == 0):
            myOutfit += random.sample(shortsleeves+blouse+dress, 1)
            myOutfit += random.sample(pants+skirt+shorts, 1)
            myOutfit += random.sample(shortcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers, 1)
        else:
            myOutfit += random.sample(tank+shortsleeves+blouse+dress, 1)
            myOutfit += random.sample(shorts+skirt, 1)
            myOutfit += random.sample(shortcotton, 1)
            #take precipitation into account later
            myOutfit += random.sample(sneakers+sandals, 1)

    for item in myOutfit:
        print(item) 
    
    return myOutfit
            
