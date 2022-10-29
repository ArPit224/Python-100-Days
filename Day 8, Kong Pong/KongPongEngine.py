from turtle import Turtle, Screen
from random import randint
from time import sleep

screen = Screen()
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")


class Ball(Turtle):
    
    def __init__(self):
        
        self.moveDist = 5

        super().__init__()
        #self.penup()
        self.pensize(width = 4)
        self.shape("circle")
        self.color("white")
        self.pendown()
        self.setpos(x = 0, y = 0)
        self.setheading(randint(10, 60))
    
    def arenaprinter(self):
        
        self.setpos(0, -300)
        
        i = 0
        
        self.setheading(90)
            
        while(i <= 300):
            self.pendown()
            self.forward(10)
            self.penup()
            ycor = self.ycor()
            self.setpos(y = ycor + 10, x = 0)
            screen.update()
            i += 1
            
        self.penup()
        
                    
    def screenColl(self):
        self.setheading(randint(10, 60))
        self.setpos(x = 0, y = 0)
        screen.update()
    
    def xBounce(self):
        currentHeading = self.heading()
        
        #reflectedAngle = 180 - (currentHeading * 2)
        reflectedAngle = 180 + abs(360 - currentHeading)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))

        self.setheading(reflectedAngle)
        self.moveDist += 1
        
    
    def yBounce(self):
        
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        
        currentHeading = self.heading()
        
        #reflectedAngle = 180 - (currentHeading * 2)
        reflectedAngle = abs(360 - currentHeading)
        
        self.setheading(reflectedAngle)
        self.moveDist += 1

    def move(self):
        self.forward(self.moveDist)
        
        
class Paddle(Turtle):
    def __init__(self, xPad):
        
        super().__init__()
        
        self.shape("square")
        self.shapesize(stretch_len = 5)
        self.penup()
        self.color("white")
        self.setpos(x = xPad, y = 0)
        self.setheading(90)
        
    def moveUp(self):
        self.forward(40)
    
    def moveDown(self):
        self.backward(40)
        

        