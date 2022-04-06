from tkinter import *
ablak1 = Tk()
#ablak.title('A téglatest adatai')
ablak1.minsize(width = 300, height = 100)

def ujablak():
    ablak2 = Toplevel(ablak1)
    ablak1.title('Eredmények')
    ablak2.minsize(width = 300, height = 100)

    #a widget létrehozása
    felszin = Label(ablak2, text = 'Felszín')
    terfogat = Label(ablak2, text = 'Térfogat')
    felszinmezo = Entry(ablak1)
    terfogatmezo = Entry(ablak1)

    #laptördelés grid-del
    felszin.grid(row = 1)
    terfogat.grid(row = 2)
    felszinmezo.grid(row = 1, column = 2, sticky = W)
    terfogatmezo.grid(row = 2, column = 2, sticky = W)


    a = eval(felszinmezo.get())
    b = eval(terfogatmezo.get())
    c = eval(mezo3.get())

    felszin = 2*(a*b+a*c+b*c)
    terfogat = a*b*c

    felszinmezo.delete(0,END)
    felszinmezo.insert(0, str(felszin))
    terfogatmezo.delete(0,END)
    terfogatmezo.insert(0, str(terfogat))

    ablak2.mainloop()

szoveg1 = Label(ablak1, text = 'a')
szoveg2 = Label(ablak1, text = 'b')
szoveg3 = Label(ablak1, text = 'c')
gomb1 = Button(ablak1, text = 'Számítás', command = ujablak)
felszinmezo = Entry(ablak1)
terfogatmezo = Entry(ablak1)
mezo3 = Entry(ablak1)

szoveg1.grid(row = 1)
szoveg2.grid(row = 2)
szoveg3.grid(row = 3)
gomb1.grid(row = 4, column = 2, sticky = W)
felszinmezo.grid(row = 1, column = 2, sticky = W)  
terfogatmezo.grid(row = 2, column = 2, sticky = W) 
mezo3.grid(row = 3, column = 2, sticky = W) 

ablak1.mainloop()