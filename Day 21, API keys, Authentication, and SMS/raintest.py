from APIKEY import secret
import requests

from twilio.rest import Client

secretD = secret()
api = secretD.WEATHERAPIKEY


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "PNecf58470a6f0d5bee97fea6968e51f8a"
auth_token = secretD.AUTHKEY

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Testin messeagessssss!",
                     from_='+18655099667',
                     to=secretD.phone1
                 )

print(message.sid)



weather_param = {
    "lat": 51.509865,
    "lon": -0.118092,
    "appid": api,
    "exclude": ""
}

#lat = "51.509865" # London
#long = "-0.118092"

lat = 40.730610 # New York 
long = -73.935242

apiendpoint = "https://api.openweathermap.org/data/2.5/forecast?"

response = requests.get(url = apiendpoint, params = weather_param)
data = response.json()["list"][:4]

rain = []

for i in data:
    
    h3Rain = i["weather"][0]["description"]
    id = i["weather"][0]["id"]
    
    boolRain: bool
    
    
    if(id < 700):
       boolRain = True
       
    else:
        boolRain = False
        
        
    rain.append({"desc": h3Rain, "bool": boolRain})
    
    
    
umbrellaNeeded: bool

for i in rain:
    
    if(i["bool"]):
        umbrellaNeeded = True
 
print(rain, umbrellaNeeded)

#We only need 4 3 hours of rain data