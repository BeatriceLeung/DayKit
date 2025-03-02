import weather_url as WeatherAPI

def getRandomItem(items):
    if(len(items) > 0):
        return random.sample(items, 1)

def pickOutfit():
    temp = WeatherAPI.getTemperature()
    min_temp = temp["min"]
    max_temp = temp["max"]
    cur_temp = temp["current"]

    pref = 0 #user runs hot/cold
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
            myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(hoodie)
            myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+boots)
        else:
            myOutfit += getRandomItem(longsleeves)
            myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
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
            myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves)
            if(min_temp<=40):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+boots)
        else:
            myOutfit += getRandomItem(longsleeves)
            if(min_temp<=40):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(leggings+pants)
            myOutfit += getRandomItem(longcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+boots)
    elif(max_temp>=60 and max_temp<80):
        if(pref == -1):
            myOutfit += getRandomItem(longsleeves+hoodie+sweater)
            if(min_temp<=60):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants)
            myOutfit += getRandomItem(longfuzzy + longcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+boots)
        elif(pref == 0):
            myOutfit += getRandomItem(longsleeves+blouse+dress)
            if(min_temp<=60):
                myOutfit += getRandomItem(jacket)
            myOutfit += getRandomItem(pants+leggings)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers)
        else:
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            if(min_temp<=60):
                myOutfit += getRandomItem(lightjacket)
            myOutfit += getRandomItem(leggings+pants+shorts)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+sandals)
    else:
        if(pref == -1):
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            if(min_temp<=80):
                myOutfit += getRandomItem(lightjacket)
            myOutfit += getRandomItem(pants+leggings)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers)
        elif(pref == 0):
            myOutfit += getRandomItem(shortsleeves+blouse+dress)
            myOutfit += getRandomItem(pants+skirt+shorts)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers)
        else:
            myOutfit += getRandomItem(tank+shortsleeves+blouse+dress)
            myOutfit += getRandomItem(shorts+skirt)
            myOutfit += getRandomItem(shortcotton)
            #take precipitation into account later
            myOutfit += getRandomItem(sneakers+sandals)

    for item in myOutfit:
        print(item) 
    
    return myOutfit
            
