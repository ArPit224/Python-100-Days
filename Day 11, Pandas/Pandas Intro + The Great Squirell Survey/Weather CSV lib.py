import csv

temprature = []

with open("Day 11, Pandas/weather_data.csv") as file:
    data = csv.reader(file)
    
    for row in data:
        temprature.append(row[1])
        
    for i, j in enumerate(temprature[1:]):
        temprature[i + 1] = int(j)

print(temprature)