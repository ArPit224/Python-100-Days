import requests, json

def newQues():
    
    url = "https://opentdb.com/api.php?amount=12&category=22&difficulty=medium&type=boolean"

    data = requests.get(url)
    data = data.text
    data = json.loads(data)

    quesArr = []
    ansArr = []

    for i,j in enumerate(data["results"]):
        quesArr.append(data["results"][i]["question"])
        ansArr.append(data["results"][i]["correct_answer"])
        
    return({"ques": quesArr, "ans": ansArr})
