from turtle import Screen
from time import sleep
from Engine import Tile

screen = Screen()
screen.setup(width = 800, height = 800)
screen.tracer(0)
screen.bgcolor("black")
screen.colormode(255)


tile = Tile()

#for i in (0, 240):
for j in (0, 240):
        
    tile.goto(0, j  * 10)
    tile.pendown()
    tile.color(0, j, 0)
    tile.forward(10)
    screen.update()
    sleep(0.01)
        
screen.exitonclick()