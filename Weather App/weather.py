import requests
import json
import os

city = input("Enter the name of this city ")


url = f"https://api.weatherapi.com/v1/current.json?key=0a667de3ef1f4cc4af0224233231312&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
current_t = wdic["current"]["temp_c"]
os.system(f"say 'Your current city is {city} and your current temperature is {current_t} degree celcius'")



