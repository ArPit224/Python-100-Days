import smtplib
from datetime import datetime
import pandas as pd
from random import randint


messagePath = f"Day 18, SMTPlib, Datetime/Automated Birthday Wisher/letter_templates/letter_{randint(1, 3)}.txt"




#++++++++++ Const ++++++++++#

email = "noirarry@gmail.com"
password = "feipahgvymngvtbk"

#++++++++++ Const ++++++++++#


#++++++++++ Data ++++++++++#

df = pd.read_csv("Day 18, SMTPlib, Datetime/Automated Birthday Wisher/birthdays.csv")

#++++++++++ Data ++++++++++#


#++++++++++ Email ++++++++++#

def sendMail(name, toEmail, year):
    
    with open(messagePath) as file:
        msg = file.read()
    
    msg = msg.replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr = email,
                            to_addrs = toEmail, 
                            msg = f"Subject: HAPPY {curYear - year} BIRTHDAY {name.capitalize()}!!\n\n{msg}")

#++++++++++ Email ++++++++++#


#++++++++++ Date ++++++++++#

now = datetime.now()
month = now.month
day = now.day
hour = now.hour
curYear = now.year

if(hour >= 8):
    
    temp = df[df["month"] == month]
    temp = temp[temp["day"] == day]
    
    for i in range(0, temp.__len__()):
        
        toEmail = temp.iloc[i]["email"]
        name = temp.iloc[i]["name"]
        year = temp.iloc[i]["year"]
        
        sendMail(name, toEmail, year)
    
#++++++++++ Date ++++++++++#
#Damn It bloody worked, Works like a charm
#Lets run it in cloud
#Working in cloud too

#Done for today, bye
