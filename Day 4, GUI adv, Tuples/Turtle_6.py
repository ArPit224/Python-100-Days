import turtle as t
from random import randint

screen = t.Screen()
screen.colormode(255)

tr = t.Turtle()

tr.speed(0)
tr.width(1)
for i in range(180):
    tr.circle(100)
    tr.left(2)
    tr.color(0, 0, i)

screen.exitonclick()
