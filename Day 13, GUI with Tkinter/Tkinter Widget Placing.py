from tkinter import *

window = Tk()
window.minsize(width = 500, height = 500)


label = Label(text = "This is a label")
button = Button(text = "This is a button")
input = Entry(text = "This is input box")

#There are three methods of placing widgets on tk window,
#Pack: Just basic
#Place: Very Very Specific
#Grid: Best 

#label.pack(side = "left") #Left, Bottom, Right, Default: Top
#label.place(x = 76, y = 152)

newButton = Button(text = "Newy Buttony") #Challange

label.grid(row = 0, column = 0)
button.grid(row = 1, column = 1)
newButton.grid(row = 0, column = 2)
input.grid(row = 2, column = 3)


window.mainloop()