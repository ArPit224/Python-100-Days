from turtle import Turtle, Screen
from random import randint


class Player(Turtle):
    def __init__(self):
        
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setpos(0, -280)
        self.setheading(90)
        
        
    def resetPos(self):
        self.setpos(0, -280)
    
    def moveFwd(self):
        self.forward(20)
    
    def moveBck(self):
        self.backward(20)