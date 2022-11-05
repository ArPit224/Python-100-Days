from tkinter import *
from time import sleep

window = Tk()
window.minsize(width = 500, height = 500)

def labelPadded():
    label2.config(text = "This is padded now, See the difference?", padx = 20, pady = 20)

label = Label(text = "Hello, This is normal text")
label.grid(row = 0, column = 0)
label.config(bg = "green")

label2 = Label(text = "Hello, This is unpadded text too, Maybe Click button")
label2.grid(row = 0, column = 2)
label2.config(bg = "red")

button = Button(text = "Maybe Click here??", command = labelPadded)


button.grid(row = 1, column = 1)

window.mainloop()