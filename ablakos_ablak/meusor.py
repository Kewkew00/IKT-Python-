from cProfile import label
from tkinter import *
from turtle import left 


#nevjegy ablak
def nevjegy():
    ablak2 = Toplevel(foablak)
    uzenet2 = Message(ablak2, text = 'Készítette: Csanádi Kevin \n Baja \n 2022.04.06', width = 300)
    gomb2 = Button(ablak2,text = 'Kilép', command = ablak2.destroy)
    uzenet2.pack()
    gomb2.pack()
    ablak2.mainloop()
#nevjegy ablak vége

#felszin ablak
def felszin():

    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        mezo4.delete(0, END)
        mezo4.insert(0, str(felszin))

    ablak3 =Toplevel(foablak)
    ablak3.title('A téglatest felszíne')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a:')
    szoveg2 = Label(ablak3, text = 'b:')
    szoveg3 = Label(ablak3, text = 'c:')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    mezo4 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    ablak3.mainloop()
#felszin ablak vége

#terfogat ablak
def terfogat():

    def szamit():
        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a*b*c
        mezo4.delete(0,END)
        mezo4.insert(0,str(terfogat))
    
    ablak3 = Toplevel(foablak)
    ablak3.title('A téglatest térfogata')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a')
    szoveg2 = Label(ablak3, text = 'b')
    szoveg3 = Label(ablak3, text = 'c')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1 = Entry(ablak3)
    mezo2 = Entry(ablak3)
    mezo3 = Entry(ablak3)
    mezo4 = Entry(ablak3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    ablak3.mainloop()
#terfogat ablak vége

#foablak
foablak = Tk()
foablak.title('A téglatest adatai')
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu1 = Menubutton(menusor, text = 'Fájl')
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label ='Névjegy', command = nevjegy, )
fajl.add_command(label = 'Kilépés', command = foablak.destroy)
menu1.config(menu = fajl)

menu2 = Menubutton(menusor, text = 'Téglatest')
menu2.pack(side = LEFT)
teglatest = Menu(menu2)
teglatest.add_command(label = 'Felszin', command = felszin)
teglatest.add_command(label = 'Térfogat', command = terfogat)
menu2.config(menu = teglatest)

foablak.mainloop()