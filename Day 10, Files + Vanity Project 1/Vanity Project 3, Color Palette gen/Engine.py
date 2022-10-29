from turtle import Turtle


class Tile(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.shape("square")
        self.shapesize(0.5, 0.5)
        self.penup()
        
#I Don't think anything else is required in this class