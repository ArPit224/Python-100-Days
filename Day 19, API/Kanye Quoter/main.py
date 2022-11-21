from tkinter import *
import requests

urlYe = "https://api.kanye.rest/"


def get_quote():
    
    response = requests.get(url = urlYe)
    
    data = response.json()["quote"]
    
    canvas.itemconfig(quote_text, text = data)
    


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day 19, API/Kanye Quoter/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day 19, API/Kanye Quoter/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
#Not my code, This is just excercise man, I can make this better and not Kanye Lol