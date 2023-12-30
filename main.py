import requests
import json

import pyttsx3


def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


city = input("Find the weather of the city: ")
url = "https://api.weatherapi.com/v1/current.json?key=195a81c4ff0a4968bea171847232912&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
h = wdic["current"]["humidity"]
f = wdic["current"]["feelslike_c"]
speak(f"The temperature of the {city} is {w} degree celsius")
speak(f"The humidity of the {city} is {h}")
speak(f"It feel like it is {f} degree celsius")
