import tkinter as tk

window = tk.Tk()
window.title("Test window: Twindow")
window.minsize(500, 500)

label1 = tk.Label(text = "i am a label", font = ("Arial", 24, "italic", "bold"))
label1.pack(expand = 1)

window.mainloop()