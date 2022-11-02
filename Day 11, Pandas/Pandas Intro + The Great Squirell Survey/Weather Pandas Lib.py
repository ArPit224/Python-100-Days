import pandas as pd

df = pd.read_csv("Day 11, Pandas/weather_data.csv")

print(df["temp"])

print(df[df["temp"] == df["temp"].max()])