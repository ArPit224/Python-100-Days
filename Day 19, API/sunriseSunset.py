import requests
from datetime import datetime

parameters = {"lat": 9, "lng": 179, "formatted" : 0}

urlSunset = "https://api.sunrise-sunset.org/json"

response = requests.get(url = urlSunset, params = parameters)

data = response.json()

sun = {"sunrise": data["results"]["sunrise"][:-6].split("T")[1].split(":"), "sunset": data["results"]["sunset"][:-6].split("T")[1].split(":")}

print(sun)
