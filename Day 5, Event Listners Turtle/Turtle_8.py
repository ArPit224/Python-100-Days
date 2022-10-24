from random import randint
from turtle import Screen, Turtle

screen = Screen()
tur = Turtle()

def move_forword():
    tur.forward(10)
    
def move_backward():
    tur.backward(10)

def clockwise():
    tur.left(18)
    
def anti_clockwise():
    tur.right(18)
    
def clear_t():
    tur.clear()
    tur.reset()
    

screen.listen()
    
screen.onkey(key = "w", fun = move_forword)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = clockwise)
screen.onkey(key = "d", fun = anti_clockwise)
screen.onkey(key = "c", fun = clear_t)

screen.exitonclick()