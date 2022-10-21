import turtle as t
from random import randint

import colorgram

screen = t.Screen()
tur = t.Turtle()
screen.colormode(255)
tur.speed(0)

colors = colorgram.extract('Day 4, GUI adv, Tuples/Color_palette.png', 40)

rgb = []


for i in colors:
    
    color = i.rgb
    rgb.append(color)
    
for i in range(10):
    for j in range(10):
        tur.penup()
        tur.goto(j*40, i*40)
        tur.pendown()
        tur.dot(10, rgb[randint(0, len(rgb) - 1)])

screen.exitonclick()