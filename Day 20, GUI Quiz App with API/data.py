import requests
import html

urlQues = "https://opentdb.com/api.php?amount=10&type=boolean"



class quizMaster:
    
    def __init__(self):
        
        self.data = []
        self.correct = 0
        self.quest = 1
        
        self.percentage = (self.correct * 100 )/ self.quest
        
    def get_quest(self):
        
        response = requests.get(url = urlQues)
        
        temp = response.json()["results"]
        
        ques = []
        
        for i in temp:
            ques.append({'q': html.unescape(i["question"]), 'a' : i["correct_answer"] == "True"})
        
        return ques

