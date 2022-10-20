from turtle import Screen, Turtle

tr = Turtle()

tr.shape("turtle")
tr.color("violet")

#Square

for i in range(4):
    tr.forward(100)
    tr.left(90)

screen = Screen()
screen.exitonclick()