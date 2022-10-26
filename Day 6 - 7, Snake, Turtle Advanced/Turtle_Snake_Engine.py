from ast import mod
from turtle import Turtle, Screen
from time import sleep

screen = Screen()

class Turtlesnake:
    def __init__(self, length):
        
        self.snake = []
        
        for i in range(length):
            
            self.length = length
            
            self.snake.append(Turtle(shape = "square"))
            self.snake[i].speed(0)
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setpos(-20*i, 0)
            
            screen.update()
            
        self.head = self.snake[0]
        self.head.color("green")

    def addSeg(self):
        
            i = self.length - 1
            self.snake.append(Turtle(shape = "square"))
            
            self.length += 1
            i += 1
            
            self.snake[i].speed(0)
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].setpos(x = self.snake[i - 1].xcor() + 20, y = self.snake[i - 1].ycor())
            screen.update()
            
   
    def moveX(self):
        
        xLast = self.head.xcor()
        yLast = self.head.ycor()
        
        self.head.forward(20)
    
            
        for i in range(1, self.length):
            
            xNext = self.snake[i].xcor()
            yNext = self.snake[i].ycor()
            
            self.snake[i].setpos(x = xLast, y = yLast)
            
            xLast = xNext
            yLast = yNext
        
        screen.update()
            
            
    '''   
    def left(self):
        self.head.left(90)
        screen.update()
        
        
    def right(self):
        self.head.right(90)
        screen.update()
    '''
     
    def up(self):
        
        if(abs(self.head.heading() - 90) != 180):
            self.head.setheading(90)
            
        else:
            pass
        
    def down(self):
        if(abs(self.head.heading() - 270) != 180):
            self.head.setheading(270)
            
        else:
            pass    
        
    def left(self):
        if(abs(self.head.heading() - 180) != 180):
            self.head.setheading(180)
            
        else:
            pass              

    def right(self):
        if(abs(self.head.heading()) != 180):
            self.head.setheading(0)
            
        else:
            pass