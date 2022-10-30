from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.penup()
        
        self.goto(x = 0, y = 300)
        self.color("white")
        self.ht()
        
        self.score = 0

        
        with open("Day 10, Files + Vanity Project 1\Snake Updated(High scores)\highScore.txt") as f:
            self.highscore = int(f.read())
        
        self.updateScore()

    def collisionFood(self):
            self.score += 1
        
    
    #def gameOver(self):
        
    #    self.color("red")
    #    self.goto(x = 0, y = 0)
    #    self.write("GAME OVER" , move=False, align='center', font=('Arial', 14, 'normal'))
    
    def reset_score(self):
        if self.score >= self.highscore:
            self.highscore = self.score
        
        self.score = 0
        self.updateHS()
        self.updateScore()
        
    def updateScore(self):
        
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}" , move=False, align='center', font=('Arial', 14, 'normal'))
    
    def updateHS(self):
        
        with open("Day 10, Files + Vanity Project 1\Snake Updated(High scores)\highScore.txt", "w") as file:
            file.write(str(self.highscore))