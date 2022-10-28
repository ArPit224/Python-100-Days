from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.colormode(255)

class Car(Turtle):
    
    def __init__(self, xPos, yPos, moveDist):
        
        super().__init__()
        self.penup()
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shape("square")
        self.shapesize(1, 2)
        self.setheading(180)
        self.setpos(x = xPos, y = yPos)
        self.moveDist = moveDist
        self.speed(1)
    
    def move(self):
        self.forward(self.moveDist)
        
