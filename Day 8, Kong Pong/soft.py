from turtle import Turtle, Screen
from random import randint
from time import sleep
from KongPongEngine import Paddle, Ball

screen = Screen()
screen.setup(width = 900, height = 700)
screen.tracer(0)
screen.bgcolor("white")
screen.colormode(255)


#paddle1 = Paddle(350)
#paddle2 = Paddle(-350)

ball = Ball()
ball.hideturtle()
ball.setpos(0, 0)

gameOn = True

while(gameOn):
    
    ball.forward(10)
    
    if(ball.xcor() >= 380 or ball.xcor() <= -380):
        ball.xBounce()
        ball.moveDist = 5
        
        #ball.screenColl()
        
    elif(ball.ycor() >= 280 or ball.ycor() <= -280):
        ball.yBounce()
        ball.moveDist = 5
    
    screen.update()


        #ball.screenColl()
    sleep(0.001)