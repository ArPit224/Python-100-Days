from tkinter import *
import pandas as pd
from random import randint

#+++++++++++++++++++++++++++++++++++++ Window +++++++++++++++++++++++++++++++++++++#


learned = []

window = Tk()
window.wm_resizable(width = False, height = False)
window.title("Flasher Sflasher")
window.config(padx = 50, pady = 50, bg = "#B1DDC6")

#+++++++++++++++++++++++++++++++++++++ canvas +++++++++++++++++++++++++++++++++++++#

imageBg = PhotoImage(file = "Day 17, Capstone Project Vocab Builder/Flasher/images/card_back.png")


canvasT = Canvas()
canvasT.config(height = 526, width = 800, bg = "#B1DDC6", highlightthickness = 0)
canvaImage = canvasT.create_image((400, 263), image = imageBg)

wordEn = canvasT.create_text((400, 100), text = "French", font =  ("Arial", 40, "italic"))
wordFr = canvasT.create_text((400, 263), text = "Word", font =  ("Arial", 60, "bold"))

canvasT.grid(row = 0, column = 0, columnspan = 2)


imageButtonR =  PhotoImage(file = "Day 17, Capstone Project Vocab Builder/Flasher/images/right.png")
imageButtonW = PhotoImage(file = "Day 17, Capstone Project Vocab Builder/Flasher/images/wrong.png")




#+++++++++++++++++++++++++++++++++++++ canvas +++++++++++++++++++++++++++++++++++++#

#+++++++++++++++++++++++++++++++++++++ Window +++++++++++++++++++++++++++++++++++++#


#+++++++++++++++++++++++++++++++++++++ Data +++++++++++++++++++++++++++++++++++++#


df = pd.read_csv("Day 17, Capstone Project Vocab Builder/Flasher/data/french_words.csv")
#df = pd.read_csv("data/french_words.csv")


def randomWordGen():
    
    global wordRand, flipTimer
    
    indexRand = randint(0, len(df) - 1)
    
    wordRand =  {"ind": indexRand, "fr": df.iloc[indexRand, 0], "eng": df.iloc[indexRand, 1]}
    
    canvasT.itemconfig(canvaImage, image = imageBg)
    
    
    canvasT.itemconfig(wordEn, text = "French", fill = "white")
    canvasT.itemconfig(wordFr, text = f"{wordRand['fr']}", fill = "white")
    flipTimer = window.after(3000, func = flip)
    
    



def checker(ans, boolAns):
    
    global df
    
    if(boolAns):
        df = df.drop(ans["ind"]).reset_index(drop = True)
        dfLearned = pd.DataFrame(learned)
        dfLearned.to_csv("leanred.csv")
        



def randomWordPrinterWrong():
    
    global wordRand, flipTimer
    
    flip()    
    window.after_cancel(flipTimer)
    
    window.after(2000, randomWordGen)

    
    
def randomWordPrinterRight():
    
    global wordRand, flipTimer
    
    flipTimer = window.after(3000, func = flip)
    
    learned.append(wordRand)
    
    randomWordGen()
    checker(wordRand, True)
    window.after_cancel(flipTimer)


#+++++++++++++++++++++++++++++++++++++ Data +++++++++++++++++++++++++++++++++++++#


#+++++++++++++++++++++++++++++++++++++ Flip +++++++++++++++++++++++++++++++++++++#

newImage = PhotoImage(file = "Day 17, Capstone Project Vocab Builder/Flasher/images/card_front.png")

def flip():
    
    canvasT.itemconfig(canvaImage, image = newImage)
    
    canvasT.itemconfig(wordEn, text = f"{wordRand['fr']}", fill = "black")
    canvasT.itemconfig(wordFr, text = f"{wordRand['eng']}", fill = "black")
    
    
#+++++++++++++++++++++++++++++++++++++ Flip +++++++++++++++++++++++++++++++++++++#


#++++++++++++++++++++++++++++++++++++++ UI ++++++++++++++++++++++++++++++++++++++#

randomWordGen()

flipTimer = window.after(3000, func = flip)



buttonRight = Button(image = imageButtonR, highlightthickness = 0, command = randomWordPrinterRight)
buttonRight.grid(row = 1, column = 0)
buttonRight.config(pady = 0)

buttonLeft = Button(image = imageButtonW, highlightthickness = 0, command = randomWordPrinterWrong)
buttonLeft.grid(row = 1, column = 1)
buttonLeft.config(pady = 0)



window.mainloop()

#++++++++++++++++++++++++++++++++++++++ UI ++++++++++++++++++++++++++++++++++++++#
#IT WORKS