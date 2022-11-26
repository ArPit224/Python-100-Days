from tkinter import *
import data

THEME_COLOR = "#375362"


class app:
    
    def __init__(self):
        
        self.score = 0
        self.index = 0
        self.questions = data.quizMaster().get_quest()
        self.qNum = 1
        self.currQues = self.questions[self.index]
        
        self.window = Tk()
        self.window.title("QuizMaster")
        self.window.config(width = 400, height = 500)
        
        self.window.wm_resizable(width = False, height = False)
        
        
        self.window.config(background = THEME_COLOR)
        
        
        self.scoreLabel = Label(text = f"score: {self.score}", fg = "white",  background = THEME_COLOR,
                                font = ("Arial", 20))
        self.scoreLabel.grid(row = 0, column = 1, pady = 20)
        
        self.canvas = Canvas(width = 250, height = 300)
        
        self.qNumUpdater = self.canvas.create_text((125, 50), text = "Question: 1", font = ("Arial", 10, "bold"))
        self.quest = self.canvas.create_text((125, 125), text = f"{self.questions[self.index]['q']}",
                                             font = ("Arial", 15, "bold"),
                                             width = 250)
        self.canvas.grid(row = 1, column = 0, columnspan = 2, padx = 20)
        
        self.imageTrue = PhotoImage(file = "Day 20, GUI Quiz App with API/true.png")
        self.imageFalse = PhotoImage(file = "Day 20, GUI Quiz App with API/false.png")
        
        
        self.buttonCorrect = Button(image = self.imageTrue, highlightthickness = 0, command = self.trueSel)
        self.buttonCorrect.grid(row = 2, column = 0, pady = 20)
        
        self.buttonFalse = Button(image = self.imageFalse, highlightthickness = 0, command = self.falseSel)
        self.buttonFalse.grid(row = 2, column = 1, pady = 20)
        
        self.window.mainloop()
        
    def questionPrinter(self, quest):
        
        self.canvas.itemconfig(self.quest, text = quest)
    
    def qNext(self):
                        
        self.canvas.config(bg = "white")
        
        if(self.qNum >= 10):
            self.buttonCorrect.config(state = "disabled")
            self.buttonFalse.config(state = "disabled")
            self.result()
        
        else:
            self.qNum += 1
            self.index += 1
            
            self.currQues = self.questions[self.index]
            self.canvas.itemconfig(self.qNumUpdater, text = f"Question: {self.qNum}")
            self.questionPrinter(self.currQues["q"])
    
    def result(self):
        self.questionPrinter(f"Result: {(self.score * 100) / 10}%")
        
    def ansChecker(self, ans: bool):
        
        if(ans == self.currQues["a"]):
            self.score += 1
            
            self.scoreLabel.config(text = f"score: {self.score}")
            self.canvas.config(bg = "green")
            
        else:
            
            self.canvas.config(bg = "red")
            
        self.window.after(100, func = self.qNext)
            
                    
    def trueSel(self):
        
        if(self.qNum >= 10):
            self.result()
            self.buttonCorrect.config(state = "disabled")
            self.buttonFalse.config(state = "disabled")
        
        else:
            self.ansChecker(True)
        
            
    def falseSel(self):
        
        if(self.qNum >= 10):
            self.result()
            self.buttonCorrect.config(state = "disabled")
            self.buttonFalse.config(state = "disabled")
        
        else:
            self.ansChecker(False)
        
        
appN = app()
