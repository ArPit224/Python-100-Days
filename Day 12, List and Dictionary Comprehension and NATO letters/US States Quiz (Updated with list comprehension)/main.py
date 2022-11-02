import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("US States Game")
screen.tracer(0)

tur = t.Turtle()
tur.ht()
tur.penup()
tur.color("black")

image = "Day 11, Pandas/US States Quiz/blank_states_img.gif" #Py file
#image = "blank_states_img.gif" #iPynb file

screen.addshape(image)
t.shape(image)

states = pd.read_csv("Day 11, Pandas/US States Quiz/50_states.csv") #py
#states = pd.read_csv("50_states.csv") #py

statesAll = states["state"]

screen.update()

def stateNamePrinter(string, x, y):
    tur.goto(x, y)
    tur.write(string, align = "center", font = ("Arial", 9, "normal"))

def stateSearcher(textInput):
    
    textInput = textInput.capitalize()

    
    if(sum(states["state"] == textInput) >= 1):
        
        x = states[states["state"] == textInput]["x"]
        y = states[states["state"] == textInput]["y"]
        
        return {"bool": 1, "x": x, "y": y}
    
    else:
        return {"bool": 0, "x": 0, "y": 0}

isGameOn = 0
numCorrect = 0

ansStates = []

while(isGameOn <= 0):
    state = screen.textinput(title = f"Correct {numCorrect}/50 Guess the state", prompt = "What's your next input is going to be???")
    
    if(numCorrect == 50):
        
        isGameOn = False
        
    elif(state == "exit"):
        
        output = [x for x in statesAll if x not in ansStates]
                
        output = pd.DataFrame(data = output, columns = ["States to learn"])
        
        output.to_csv("Day 12, List and Dictionary Comprehension and NATO letters/US States Quiz (Updated with list comprehension)/States To Learn")
        break
        
    
    elif(stateSearcher(state)["bool"] == 1):
        
        ansStates.append(state.capitalize())
        
        searched = stateSearcher(state)
        
        x = searched["x"].item()
        y = searched["y"].item()
        
        stateNamePrinter(state, x, y)
        
        screen.update()
        
        numCorrect += 1
        
    else:
        print("Wrong Input!")
        
    
    

screen.mainloop()