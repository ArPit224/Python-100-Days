with open("Day 18, SMTPlib, Datetime/quotes.txt", "r") as file:
    
    data = file.read()    

dataF = []

for i in data.split("\n"):
    dataF.append(i)
