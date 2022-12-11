import smtplib
from datetime import datetime
from random import randint

email = "noirarry@gmail.com"
passwordEmail = ""
message = "test"

#++++++++++++++++++++ Quotes Reader ++++++++++++++++++++#

with open("Day 18, SMTPlib, Datetime/quotes.txt", "r") as file:
    
    data = file.read()    

dataF = []

for i in data.split("\n"):
    dataF.append(i)

length = dataF.__len__()
#++++++++++++++++++++ Quotes Reader ++++++++++++++++++++#


#+++++++++++++++++++++ Email Maker +++++++++++++++++++++#

indexRand = randint(0, length - 1)
message = dataF[indexRand]

#+++++++++++++++++++++ Email Maker +++++++++++++++++++++#


#++++++++++++++++++++ Email Sender +++++++++++++++++++++#

with smtplib.SMTP("smtp.gmail.com") as connection:
    
    connection.starttls()
    connection.login(user = email, password = passwordEmail)
    connection.sendmail(from_addr = email,
                        to_addrs = "toemail@gmail.com",
                        msg = f"Subject: Daily Quotes for today\n\n{message}")

#++++++++++++++++++++ Email Sender +++++++++++++++++++++#
