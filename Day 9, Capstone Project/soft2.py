from turtle import Screen
from time import sleep
from TurtleSmurtleEngine import Player
from carmanager import Car
from random import randint

screen = Screen()
screen.colormode(255)
screen.setup(width = 700, height = 700)
screen.tracer(0)

traffic = []

iter = 0

while(iter < 1):
    
    for i in range(-255, 255, 60):
        
        iter += 28
        
        for j in range(-255, 255, 20):
            traffic.append(Car(i, j, iter, 15))
            screen.update()
            
    
screen.exitonclick()