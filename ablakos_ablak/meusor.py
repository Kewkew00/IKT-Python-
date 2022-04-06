from tkinter import * 

ablak1 = Tk()
ablak1.title('A téglatest adatai')

#nevjegy ablak
def nevjegy():
    ablak2 = Toplevel(ablak1)
    uzenet2 = Message(ablak2, text = 'Készítette: Csanádi Kevin \n Baja \n 2022.04.06', width = 300)
    gomb2 = Button(ablak2,text = 'Kilép', command = ablak2.destroy)
    uzenet2.grid()
    gomb2.grid()
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

    ablak3 =Toplevel(ablak1)
    ablak3.title('A téglatest felszíne')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a')
    szoveg2 = Label(ablak3, text = 'b')
    szoveg3 = Label(ablak3, text = 'c')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1.Entry(ablak3)
    mezo2.Entry(ablak3)
    mezo3.Entry(ablak3)
    mezo4.Entry(ablak3)
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
    
    ablak3 = Toplevel(ablak1)
    ablak3.title('A téglatest térfogata')
    ablak3.minsize(width = 300, height = 100)
    szoveg1 = Label(ablak3, text = 'a')
    szoveg2 = Label(ablak3, text = 'b')
    szoveg3 = Label(ablak3, text = 'c')
    szoveg4 = Label(ablak3, text = 'Eredmény: ')
    gomb1 = Button(ablak3,  text = 'Számítás', command = szamit)
    mezo1.Entry(ablak3)
    mezo2.Entry(ablak3)
    mezo3.Entry(ablak3)
    mezo4.Entry(ablak3)
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

foablak = Tk()
foablak.title('A téglatest adatai')
foablak.minsize(width = 300, height = 100)

menusor = Frame(foablak)
menusor.grid(side = TOP, fill = X)

menu1 = Menubutton(menusor, text = 'Fájl', underline = 0)
menu1.grid(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label ='Névjegy', command = nevjegy, underline = 0)
fajl.add_command(label = 'Kilépés', command = foablak.destroy, underline  = 0)
menu1.config(menu = fajl)


ablak1.mainloop()