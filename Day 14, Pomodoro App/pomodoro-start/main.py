from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 1200
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

#8 steps, 0, 2, 4, 6 = 1500; 1, 3, 5 = 300; 7 = 1200

def startTimer():
    
    global reps
    
    reps += 1

    currentState = reps % 2
    
    if(reps == 7):
        reps = 0
        countDown(1200)
    
    else:
        if(currentState == 1):
            countDown(1500)
            print(reps)
            startTimer()
            
        else:
            
            countDown(300)
            print(reps)
            startTimer()
            
            
            
        
            
def resetTimer():

    
    canvas.itemconfig(labelTimer, text = "00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countDown(count):
    
    countMin = int(count / 60)
    countSec = count % 60
    
    countMinOut = "0" * (countMin < 10) + str(countMin)
    countSecOut = "0" * (countSec < 10) + str(countSec)
    
        

    canvas.itemconfig(labelTimer, text = f"{countMinOut}:{countSecOut}")

    
    if(count > 0):
        
        count -= 1
        
        window.after(1000, countDown, count)
        


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width = 500, height = 400)

window.config(bg = YELLOW, padx = 25, pady = 25)



canvas = Canvas(width = 250, height = 250, highlightthickness = 0)
imageTomato = PhotoImage(file = "Day 14, Pomodoro App/pomodoro-start/tomato.png")
canvas.create_image((125, 125), image = imageTomato)

labelTimer = canvas.create_text((125, 150), text = "00:00", font = (FONT_NAME, 35, "bold"), fill = "white")


canvas.config(bg = YELLOW)

label = Label(text = "TIMER", foreground = GREEN, background = YELLOW, font = (FONT_NAME, 35, "bold"))

buttonStart = Button(text = "Start", bg = YELLOW, font = (FONT_NAME, 20, "bold"), command = startTimer)
buttonReset = Button(text = "Reset", bg = YELLOW, font = (FONT_NAME, 20, "bold"), command = resetTimer)

labelTick = Label(text = "✔", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 20, "bold"))


label.grid(row = 0, column = 1)
canvas.grid(row = 1, column = 1)
buttonStart.grid(row = 3, column = 0)
buttonReset.grid(row = 3, column = 2)
labelTick.grid(row = 4, column = 1)
#canvas.pack()

window.mainloop()