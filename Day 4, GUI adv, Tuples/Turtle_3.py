from turtle import Screen, Turtle

tr = Turtle()

tr.color("black")


for i in range(50):
    if(i % 2 == 0):
        tr.pendown()
        tr.forward(6)
        
    else:
        tr.penup()
        tr.forward(6)
        
        
screen = Screen()

screen.exitonclick()