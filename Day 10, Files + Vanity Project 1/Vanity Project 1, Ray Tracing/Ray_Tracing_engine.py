from turtle import Turtle

class Ray(Turtle):
    
    def __init__(self, angle, xPos, yPos, color):
        
        super().__init__()
        
        self.shape("circle")
        self.pencolor(color)
        self.hideturtle()
        self.setpos(x = xPos, y = yPos)
        self.left(angle)
        
        self.turtlesize(stretch_wid = 1)
        self.speed(0)
        
        #using decay rate of 1% per meter, each Turtle is a meter
        
    def move(self):
        self.forward(20)
        
    