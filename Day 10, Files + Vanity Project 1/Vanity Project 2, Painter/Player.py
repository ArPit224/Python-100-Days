from turtle import Turtle, Screen


class Player(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
    
    def up(self):
        self.setheading(90)
        self.forward(40)
        
    def down(self):
        self.setheading(270)
        self.forward(40)
        
    def right(self):
        self.setheading(0)
        self.forward(40)
        
    def left(self):
        self.setheading(180)
        self.forward(40)
        
        
class TrackingEngine(Turtle):
    
    def __init__(self, xPos, yPos):
        
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.beamer(xPos, yPos)
        

    def beamer(self, xPos, yPos):
        

        
        self.penup()
        self.setpos(0, 0)
        self.pendown()
        self.clear()
        
        self.goto(x = xPos, y = yPos)
        
        