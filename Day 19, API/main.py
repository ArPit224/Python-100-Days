import requests
import datetime as dt

response = requests.get(url = "http://api.open-notify.org/iss-now.json")


#response codes: 404, 200
#1XX: Hold
#2XX: Working
#3XX: Not Allowed
#4XX: Some Issue
#5XX: Server issue

response.raise_for_status()

data = response.json()

iss = {"long": data["iss_position"]["longitude"], "lat": data["iss_position"]["latitude"]}

print(iss)