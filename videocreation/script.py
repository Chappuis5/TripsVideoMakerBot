import json
import random
from voice import TTS
from voice import gTTS
from YtbScraper import ytbScraper

f = open('/Users/evanflament/Documents/Git-Projects/TripsVideoMakerBot/videocreation/data/CityBank.json')
destination = "New-York"
data = json.load(f)
print(type(data))
num = len(data)
print(num)
for i in range(num):
    if data[i]['city'] == destination:
        print(data[i]['city'])
        str = f"going on a trip to {destination} is the worst thing you could do. Let me explain."
        TTS(str, "sound_0")
        ytbScraper(destination, keyword=" drone", name = "video_0")
        
        """"---------------"""
        attribut = data[i]['attributs'][random.randint(0,2)]['attribut']
        rd = random.randint(0,2)
        if rd == 0:
            str2 = f"{destination} is the city with the worst {attribut}."
        elif rd == 1:
            str2 = f"{destination} is a city with horrific {attribut}."
        elif rd == 2:
            str2 = f"{destination} is the most iconic city you could live in."
        TTS(str2, "sound_1")
        ytbScraper(destination, attribut, name = "video_1")

        
        """cut to second video (attribut):"""
        rd = random.randint(0,2)
        attribut_stat = data[i]['attributs'][random.randint(0,2)]['stat']
        if rd == 0:
            str3 = f"In fact, {destination} is known to be the most awful place for its {attribut}. Almost {attribut_stat} of the world worst {attribut} are unfortunately in {destination}."
        elif rd == 1:
            str3 = f"{destination} is a nightmare for its {attribut}. {attribut_stat} of the creepiest and disgusting {attribut} are in {destination}. It makes me want to vomit."
        elif rd == 2:
            people = data[i]['people']
            str3 = f"Life would be better for everyone if {destination} wasn't known for its {attribut}. {attribut} is so bad, that {attribut_stat} of the {people} think that they should vote for their annihlation by Dwayne Johnson."
        TTS(str3, "sound_2")
        ytbScraper(destination, attribut, name = "video_2")

        """SCARY PART""" """scary music"""
        rd = random.randint(0,2)
        cause = data[i]['insecurities'][random.randint(0,2)]['cause']
        if rd == 0:
            str4 = f"But {destination} is also a very shitty(bib it) place because it is known for its {cause}."
        elif rd == 1:
            str4 = f"But {destination} is also a very shitty(bib it) place because it is known for its {cause}."
        elif rd == 2:
            str4 = f"But {destination} is also a very shitty(bib it) place because it is known for its {cause}."
        TTS(str4, "sound_3")
        ytbScraper(destination, cause, name = "video_3")

        """cut to third video (attribut):"""
        rd = random.randint(0,2)
        cause = data[i]['insecurities'][random.randint(0,2)]['cause']
        if rd == 0:
            str5 = f"Do you know gotham city? Well, {destination} isn't far from it. {cause} attacks are becoming more and more common. And since you are not batman, but rather an old lazy fuck(bip) who stays all day on his sofa, I think you better plan a fucking (bip) trip to your fridge."
        elif rd == 1:
            str5 = f"Do you know gotham city? Well, {destination} isn't far from it. {cause} attacks are becoming more and more common. And since you are not batman, but rather an old lazy fuck(bip) who stays all day on his sofa, I think you better plan a fucking (bip) trip to your fridge."
        elif rd == 2:
            str5 = f"Do you know gotham city? Well, {destination} isn't far from it. {cause} attacks are becoming more and more common. And since you are not batman, but rather an old lazy fuck(bip) who stays all day on his sofa, I think you better plan a fucking (bip) trip to your fridge."
        TTS(str5, "sound_4")
        ytbScraper(destination, cause, name = "video_4")

        """JOKE PART"""
        rd = random.randint(0,2)
        if rd == 0:
            str6 = f"Of course I was kidding hahaha. You shouldn't worry too much. {destination} might just be the right place to learn self defence, assuming your attacker will be disabled."
        elif rd == 1:
            str6 = f"Of course I was kidding hahaha. You shouldn't worry too much. {destination} might just be the right place to learn self defence, assuming your attacker will be disabled."
        elif rd == 2:
            str6 = f"Of course I was kidding hahaha. You shouldn't worry too much. {destination} might just be the right place to learn self defence, assuming your attacker will be disabled."
        TTS(str6, "sound_5")
        ytbScraper(destination, keyword =  " martial arts", name = "video_5")

        """Transition (mascot):"""
        rd = random.randint(0,2)
        if rd == 0:
            str7 = f"Uhuhuh. Well well. If you haven't reconsidered your choice yet, let me tell you something that will make you think twice."
        elif rd == 1:
            str7 = f"Uhuhuh. Well well. If you haven't reconsidered your choice yet, let me tell you something that will make you think twice."
        elif rd == 2:
            str7 = f"Uhuhuh. Well well. If you haven't reconsidered your choice yet, let me tell you something that will make you think twice."
        TTS(str7, "sound_6")
        ytbScraper(destination = "einstein", keyword = "interview", name = "video_6")

        """cut to fourth video (price)"""
        rd = random.randint(0,2)
        if rd == 0:
            str8 = f"It's fucking(bip) expensive to travel to {destination}"
        elif rd == 1:
            str8 = f"Assuming you're not Bill Gates, you will ruin yourself in the journey to {destination}"
        elif rd == 2:
            str8 = f"Although you're wearing a gucci t-shirt, which I assume is fake, just like your entire personality bitch (bip), traveling to {destination} costs an arm and a leg."
        TTS(str7, "sound_7")
        ytbScraper(destination, keyword = " gucci gang", name = "video_7")

        """Transition (mascot):"""
        rd = random.randint(0,2)
        if rd == 0:
            str9 = f"Okay, I scared you a little. But wait something else is scary."
        elif rd == 1:
            str9 = f"Okay, I scared you a little. But wait something else is scary."
        elif rd == 2:
            str9 = f"Okay, I scared you a little. But wait something else is scary."
        TTS(str7, "sound_8")
        ytbScraper(destination = "white car", keyword = " horror", name = "video_8")

        """cut to fift video (placeToStay):"""
        rd = random.randint(0,2)
        place = data[i]['places'][random.randint(0,2)]['place']
        price = data[i]['places'][random.randint(0,2)]['price']
        currency = data[i]['places'][random.randint(0,2)]['currency']
        if rd == 0:
            str10 = f"The {place}, even if its name is cute, the {place} is a fucking(bip) nightmare for tourists! I mean what the hell? {price} {currency} for one night! I couldn't even sell my mother at that price!"
        elif rd == 1:
            str10 = f"The {place}, even if its name is cute, the {place} is a fucking(bip) nightmare for tourists! I mean what the hell? {price} {currency} for one night! I couldn't even sell my mother at that price!"
        elif rd == 2:
            str10 = f"The {place}, even if its name is cute, the {place} is a fucking(bip) nightmare for tourists! I mean what the hell? {price} {currency} for one night! I couldn't even sell my mother at that price!"
        TTS(str10, "sound_9")
        ytbScraper(destination, keyword = " tourists", name = "video_9")

        """"Cut to outro"""
        str11 = f"Well, now you know everything about travelling to {destination}. And you know why"
        TTS(str11, "sound_10")
        ytbScraper(destination, keyword=" drone", name = "video_10")
        

        #print(data[i]['attributs'])
    else:
        continue

    
    #print(data[i]['attributs'][0]['attribut'])

f.close()