from data import question_data as data

class quesEngine:
    
    userScore = 0
    
        
    def __init__(self):
        self.qData = data
        
        self.userScore = 0
        
        for i, j in enumerate(self.qData):
            ques = self.qData[i]["text"]
            ans = self.qData[i]["answer"]
            
            print(f"Ques {i + 1} out of 12: {ques} (True/False)")
            userAnsIn = input()
            
            if(userAnsIn == ans):
                self.userScore += 1
                print("Correct Answer!")
            
            else:
                print("Wrong Answer!")
        