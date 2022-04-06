from tkinter import * 

ablak1 = Tk()

def ujablak():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text = 'Készítette: Csanádi Kevin \n Baja \n 2022.04.05', width = 300)
    gomb2 = Button(ablak2,text = 'kilép', command = ablak2.destroy)
    uzenet2.grid()
    gomb2.grid()
    ablak2.mainloop()

#widget létrehozása
szoveg1 = Label(ablak1, text = 'Kattints ide')
gomb1 = Button(ablak1, text = 'Névjegy', command = ujablak)
#widget létrehozása

szoveg1.grid()
gomb1.grid()


ablak1.mainloop()