from turtle import Turtle, Screen
from time import sleep
from Player import Player, TrackingEngine

screen = Screen()
screen.setup(width = 800, height = 800)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
tracker = TrackingEngine(0, 0)

screen.listen()


screen.onkeypress(key = "w", fun = player.up)
screen.onkeypress(key = "s", fun = player.down)
screen.onkeypress(key = "a", fun = player.left)
screen.onkeypress(key = "d", fun = player.right)
screen.onkeypress(key = "q", fun = player.penup)
screen.onkeypress(key = "e", fun = player.pendown)


while(True):
    
    tracker.beamer(player.xcor(), player.ycor())
    screen.update()
    sleep(0.001)
    


#screen.exitonclick()

#Idk what else to make
#Maybe some creative stuff
#Color Palette?
