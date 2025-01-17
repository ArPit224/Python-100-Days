import requests
from datetime import datetime
from time import sleep
import smtplib


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def issLocater():
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    return {"lat": iss_latitude, "long": iss_longitude}

#Your position is within +5 or -5 degrees of the ISS position.

#+++++++++++++ Position Checker +++++++++++++#

def locVerifier(long, lat):
    
    if((abs(MY_LAT - lat) <= 6) and (abs(MY_LONG - long) <= 6)):
       return True
    
    else:
        return False
    
#+++++++++++++ Position Checker +++++++++++++#






parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



