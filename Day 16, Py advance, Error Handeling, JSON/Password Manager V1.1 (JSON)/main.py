from tkinter import *
from tkinter import messagebox
from random import randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def randomPassGen():
    
    listSmallLetters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    listLargeLetters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
    symbols = "@ ! _".split(" ")
    
    passLength = 15
    
    symbolLength = randint(1, 4)
    largeLettersLength = randint(1, 4)
    
    passFinal = [str(randint(0, 9))]
    
    for i in range(largeLettersLength):
        passFinal.append(listLargeLetters[randint(0, len(listLargeLetters) - 1)])
    
    for i in range(symbolLength):
        passFinal.append(symbols[randint(0, len(symbols) - 1)])
    
    for i in range(passLength - passFinal.__len__()):
        passFinal.append(listSmallLetters[randint(0, len(listSmallLetters) - 1)])
    
    shuffle(passFinal)
    
    passFinal = "".join(passFinal)
    pyperclip.copy(passFinal)
    inputPass.delete(0, END)
    inputPass.insert(0, passFinal)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def searchPass():
    searchTerm = inputWebsite.get()
    
    try:
        file = open("Day 16, Py advance, Error Handeling, JSON/Password Manager V1.1 (JSON)/pass.json", "r")
        
        data = json.load(file)
        
        foundEmail = data[searchTerm]["email"]
        foundPass = data[searchTerm]["pass"]
        
        
    except FileNotFoundError:
        savePass()
        
        
    except KeyError:
        messagebox.showinfo(message = "Password not Found in the database", title = "Data Not found")
        
    else:
        messagebox.showinfo(title = "Password Found in the database", message = f"Email: {foundEmail}\nPassword: {foundPass}")
        


# ---------------------------- SAVE PASSWORD ------------------------------- #

def savePass():
    '''
    Path 1: Using TXT file to save pass
    '''
    
    website = inputWebsite.get()
    email = inputEmail.get()
    passd = inputPass.get()
    
    if(website.__len__() == 0 or email.__len__() == 0 or passd.__len__() == 0):
        messagebox.showerror(title = "ONE OR MORE EMPTY FIELDS", message = "Hey, you have some empty fields, Please fix that---")
    
    else:
        try: 
            file = open("Day 16, Py advance, Error Handeling, JSON/Password Manager V1.1 (JSON)/pass.json", "r")
            
        except FileNotFoundError:
            file = open("Day 16, Py advance, Error Handeling, JSON/Password Manager V1.1 (JSON)/pass.json", "w")
            
            dataTest = {
                            "test": 
                                    {
                                    "email": "testemail@gmail.com",
                                    "pass": "test"
                                    }
                        }
            
            json.dump(dataTest, file)

            
        else:    
            data = json.load(file)
        
            newData = {website: {"email": email, "pass": passd}}
                
            toSave = messagebox.askokcancel(title = website, message = f"Your entered details are\nEmail: {email}\nPass: {passd}\nSave?")
            
            file.close()
            
            file = open("Day 16, Py advance, Error Handeling, JSON/Password Manager V1.1 (JSON)/pass.json", "w")

            if(toSave):
                inputWebsite.delete(0, END)
                inputPass.delete(0, END)
                    
                data.update(newData)
                    
                    
                json.dump(data, file, indent = 4)
                    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width = 400, height = 400, padx = 20, pady = 20)
window.wm_resizable(width = False, height = False)

photoImageLogo = PhotoImage(file = "Day 15, Password Manager/logo.png")

canvas = Canvas(width = 200, height = 200)
canvas.create_image((100, 100), image = photoImageLogo)

canvas.grid(row = 0, column = 1)

label1 = Label(text = "Website")
label1.grid(row = 1, column = 0)

inputWebsite = Entry(width = 36)
inputWebsite.grid(row = 1, column = 1, columnspan = 1)
inputWebsite.focus()

buttonSearchPass = Button(text = "Search Password", width = 15, command = searchPass)
buttonSearchPass.grid(row = 1, column = 2)

label2 = Label(text = "Email/Username")
label2.grid(row = 2, column = 0)

inputEmail = Entry(width = 55)
inputEmail.grid(row = 2, column = 1, columnspan = 2)
inputEmail.insert(0, "testemail@gmail.com")


label3 = Label(text = "Password")
label3.grid(row = 3, column = 0)

inputPass = Entry(width = 36)
inputPass.grid(row = 3, column = 1)

buttonGenPass = Button(text = "Generate Password", width = 15, command = randomPassGen)
buttonGenPass.grid(row = 3, column = 2)

buttonAdd = Button(text = "Add", width = 47, command = savePass)
buttonAdd.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()