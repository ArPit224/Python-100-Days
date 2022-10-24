from random import randint
from turtle import Turtle, Screen

scr = Screen()
scr.setup(width = 1000, height = 500)

class racer:
    
    def __init__(self, color, y):
        self.color = color
        self.tur = Turtle(shape = "turtle")
        self.tur.color(color)
        self.tur.penup()
        self.tur.goto(-450, y)
        self.tur.speed(0)
        



user_bet = scr.textinput(title = "Betting window", prompt = "Place your bet on a turtle")

racers = []

racers.append(racer("red", 100))
racers.append(racer("orange", 60))
racers.append(racer("yellow", 20))
racers.append(racer("green", -20))
racers.append(racer("blue", -60))
racers.append(racer("purple", -100))

raceOn = False

if user_bet:
    raceOn = True

def move():
    
    for i in range(0, 6):
        
        if racers[i].tur.xcor() >= 450:
            raceOn = False
            return(racers[i].color)
            
        else:
            racers[i].tur.forward(randint(0, 10))
            return "white"
    
    
while(raceOn):
    winner = move()
    
if(user_bet == winner):
    print(f"Nice Pick, your bet {winner} WON!!!")
    
else:
    print(f"Oh no, your bet {user_bet} didn't won, {winner} won...")
    
scr.exitonclick()