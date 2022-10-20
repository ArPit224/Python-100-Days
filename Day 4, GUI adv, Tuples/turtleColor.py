from random import randint
from turtle import Screen, Turtle

screen = Screen()


tim = Turtle()

rgb = (100, 12, 13)
screen.colormode(255)
tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

screen.exitonclick()