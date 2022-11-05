from tkinter import *


def calculate():
    miles = float(inputMiles.get())
    inputMiles.config(text = "Miles")
    kms = str(miles * 1.6094)
    labelOutput.config(text = kms)

window = Tk()
window.minsize(width = 200, height = 200)
window.title("Miles to Kms")

kms = "0"

label1 = Label(text = "is equal to")
inputMiles = Entry(text = "Miles", width = 20)


label2 = Label(text = "Miles")
label3 = Label(text = "Kms")
labelOutput = Label(text = kms)
buttonCalc = Button(text = "Calculate", command = calculate)

label1.grid(row = 1, column = 0)
inputMiles.grid(row = 0, column = 1)
label2.grid(row = 0, column = 2)
label3.grid(row = 1, column = 2)
labelOutput.grid(row = 1, column = 1)
buttonCalc.grid(row = 2, column = 1)


    
window.mainloop()