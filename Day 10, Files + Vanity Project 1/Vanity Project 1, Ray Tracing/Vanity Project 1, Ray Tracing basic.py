from turtle import Turtle, Screen
from Ray_Tracing_engine import Ray
from time import sleep

screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.colormode(255)
screen.tracer(0)

color = 255

rays = []
ray = []


for j in range(0, 36):
    
    color = 255
    
    for i in range(255):
                
        tempRay = Ray(j*10, i, 0, (color, color, color))
        tempRay.move()
        del tempRay
        screen.update()
        color -= 1
        
    

screen.exitonclick()
#WTF