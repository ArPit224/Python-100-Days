from turtle import Turtle



class Scorecard(Turtle):
    
    def __init__(self, xPos):
        
        super().__init__()
        
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.setpos(x = xPos, y = 280)
        
        self.scoreUpdate()
        
        
    def scoreUpdate(self):
        
        self.write(f"{self.score}", move=False, align='left', font=('Arial', 14, 'normal'))
        
    def goal(self):
        self.clear()
        self.score += 1
        self.scoreUpdate()
    