from tkinter import *

window = Tk()
window.title("Dobblethon")

backgroundTheme = PhotoImage(file="dobblethon.png")
Label (window, image=backgroundTheme, bg="white") . grid(row=0, column=0, sticky=W)

window.mainloop()