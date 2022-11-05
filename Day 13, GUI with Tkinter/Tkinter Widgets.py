from tkinter import *

window = Tk()

window.title("Test Window: All the widgets")
window.minsize(width = 500, height = 1000)


#Label: Basic text on window, to update labl use label.config

label = Label(text = "Label")
label.pack()

def clicked1():
    
    usrInput = input.get()
    
    if(len(usrInput) <= 0):
        label.config(text = "Button Clicked")
        
    else:   
        label.config(text = usrInput)

#Buttons: Basic Buttons, Function is entered in command

button = Button(text = "This is a button", command = clicked1)
button.pack()

#Entry: Text Input

input = Entry(text = "Starting text to start with")
input.pack()

#Text: Bigger Text input box

text = Text(width = 30, height = 5)
text.insert(END, "This prints out a text respose")

#This one starts text cursor at the end

text.focus()

text.pack()

#the number represent starting index

print(text.get("1.0", END))

#Spinbox: Just a box which updates after every value change

def spinboxUsed():
    print(spinbox.get())

spinbox = Spinbox(from_ = 10, to = 100, width = 10, command = spinboxUsed)
spinbox.pack()

#scale: just a Slider

def scaled(value):
    print(value)
    
scale = Scale(from_ = 0, to = 100, command = scaled)
scale.pack()

#Conveting int values from tk requires IntVar()

#checkbox: Exactly what it sounds like

def checkButtonClicked():
    print(checkedState.get())

checkedState = IntVar()

checkbox = Checkbutton(text = "ON!", variable = checkedState, command = checkButtonClicked)
checkedState.get()

checkbox.pack()

#radio: Only one of them can be selected

def radioUsed():
    print(radioState.get())

radioState = IntVar()

radio1 = Radiobutton(text = "Button 1", value = 1, variable = radioState, command = radioUsed)
radio2 = Radiobutton(text = "Button 1", value = 2, variable = radioState, command = radioUsed)

radio1.pack()
radio2.pack()

#Listbox: Created from a python list, functions similar to radio button

def listBoxUsed(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height = 5)

countries = ["Au", "De", "GB", "US", "Ir"]

for i in countries:
    listbox.insert(countries.index(i), i)
    
listbox.bind("<<ListboxSelect>>", listBoxUsed)
listbox.pack()

window.mainloop()