from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color("purple")
        self.speed(0)
        
        self.goto(x = randint(-280, 280), y = randint(-280, 280))
    
    def refreshFood(self):
        self.goto(x = randint(-280, 280), y = randint(-280, 280))
