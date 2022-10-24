from turtle import Turtle, Screen
from time import sleep
import Turtle_Snake_Engine as tSnake

tur = Turtle(shape = "turtle")

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Turtle Snake Alpha.")
screen.tracer(0)

snake = tSnake.Turtlesnake(3)


screen.listen()

screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

while(True):

    snake.moveX()

    sleep(0.1)
screen.exitonclick()