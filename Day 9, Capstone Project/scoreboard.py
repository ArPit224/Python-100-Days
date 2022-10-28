from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x = -260, y = 260)
        self.scoreUpdate(0)
        
    def scoreUpdate(self, score):
        
        self.clear()
        
        self.score = score
        
        self.write(f"Level: {self.score}", move=False,
            align='left', font=('Arial', 14, 'normal'))
        
    def gameOver(self):
        
        self.goto(y = 0, x = 0)
        self.write(f"Game over at level {self.score}", move=False,
            align='center', font=('Arial', 14, 'normal'))