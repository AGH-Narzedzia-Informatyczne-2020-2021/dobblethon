from tkinter import * #don't judge me for using * ;)

def start_gry():
    info = Label(root, text="rozpoczynanie gry")
    info.grid()

root = Tk()

#tytuł 
tutul = Label(root, text="Dobblethon")
tutul.grid(row=1, column=5) #the column is more like presedence 

# przyciski
PrzyciskStart = Button(root, text="Rozpocznij Grę", command=start_gry)
PrzyciskStart.grid(row=2,column=5)

root.mainloop() #wyświetlanie okna


