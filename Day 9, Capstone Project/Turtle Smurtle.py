from turtle import Screen
from time import sleep
from TurtleSmurtleEngine import Player
from carmanager import Car
from random import randint
from scoreboard import Score

screen = Screen()
screen.colormode(255)
screen.setup(width = 600, height = 600)
screen.tracer(0)

player = Player()

car = []

gameOn = True

screen.listen()

screen.onkeypress(key = "Up", fun = player.moveFwd)
screen.onkeypress(key = "Down", fun = player.moveBck)

carGen = 0
currentLevel = 2

score = Score()

while(gameOn):
    
    if(carGen % 11 != 0):
        carGen += 1
        
        for i in car:
            
            if(i.xcor() < 60 and i.xcor() > -60):
                
                if(player.distance(i) <= 25):
                    gameOn = False
                    score.gameOver()
                    
                                    
            elif(i.xcor() >= 280):
                del i
            i.move()
            
    
    else:
        car.append(Car(randint(200, 280), randint(-260, 260), currentLevel))
        carGen = 1
    
    
    
    if(player.ycor() >= 290):
        player.resetPos()
        currentLevel += 1
        score.scoreUpdate(currentLevel - 2)
    screen.update()
    sleep(0.01)
    
screen.exitonclick()