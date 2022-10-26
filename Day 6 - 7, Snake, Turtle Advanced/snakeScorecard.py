from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.penup()
        
        self.goto(x = 0, y = 300)
        self.color("white")
        self.ht()
        
        self.score = 0
        self.write("Score: 0" , move=False, align='center', font=('Arial', 14, 'normal'))

    def collisionFood(self):
        self.clear()
        self.score += 1
        output = "Score: " + str(self.score)
        self.write(output , move=False, align='center', font=('Arial', 14, 'normal'))
    
    def gameOver(self):
        
        self.color("red")
        self.goto(x = 0, y = 0)
        self.write("GAME OVER" , move=False, align='center', font=('Arial', 14, 'normal'))
        