from random import randint
from turtle import Screen
from turtle import Turtle as tr

tur = tr()
screen = Screen()

for i in range(3, 10):
    screen.colormode(255)
    rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
    
    angle = 360/i
    
    for j in range(i):
        tur.color(rgb)
        tur.forward(100)
        tur.right(angle)        
        
screen.exitonclick()