from random import randint
from turtle import Screen, Turtle

screen = Screen()
screen.colormode(255)

tr = Turtle()
tr.pensize(10)
tr.speed(0)

for i in range(10):
    tr.left(randint(0, 4) * 90)
    tr.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tr.forward(40)
screen.exitonclick()
    
