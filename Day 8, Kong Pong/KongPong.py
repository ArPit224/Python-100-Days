from turtle import Turtle, Screen
from random import randint
from time import sleep
from KongPongEngine import Paddle, Ball
from scorecard import Scorecard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.colormode(255)


paddleR = Paddle(350)
paddleL = Paddle(-350)

leftScore = Scorecard(-200)
rightScore = Scorecard(200)

screen.listen()

screen.onkeypress(key = "Up", fun = paddleR.moveUp)
screen.onkeypress(key = "Down", fun = paddleR.moveDown)
screen.onkeypress(key = "w", fun = paddleL.moveUp)
screen.onkeypress(key = "s", fun = paddleL.moveDown)

ball = Ball()
ball.penup()
gameOn = True

while(gameOn):
    
    ball.forward(10)
    screen.update()
    
    if(ball.xcor() > 320 or ball.xcor() < -320):
        
        if(ball.distance(paddleR) <= 80 or ball.distance(paddleL) <= 80):
            ball.xBounce()
            
            
        else:
            if(ball.xcor() > 320):
                leftScore.goal()
                ball.screenColl()
                ball.setheading(180 + ball.heading())
                
            elif(ball.xcor() < -320):
                rightScore.goal()
                ball.screenColl()
        

        
    elif(ball.ycor() >= 280 or ball.ycor() <= -280):
        ball.yBounce()
        #ball.screenColl()
        
    sleep(0.04)