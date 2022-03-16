#Összeadás és a felület
from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
foablak = Tk()
cimke = Label(foablak,text = 'Számológép', fg = 'black')
cimke.grid()
gomb3 = Button(foablak,text = 'Kilépés',command = foablak.destroy)
gomb3.grid()
mezo1 = Entry(foablak)
mezo1.grid()
mezo2 = Entry(foablak)
mezo2.grid()
mezo3 = Entry(foablak)
mezo3.grid()
gomb4 = Button(foablak,text = 'Összeadás',command = osszeg)
gomb4.grid()
#Összeadás és a felület

#Kivonás
def kivonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a - b
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
gomb5 = Button(foablak,text = 'Kivonás',command = kivonas)
gomb5.grid()
#Kivonás

#Szorzás
def szorzas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a * b
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
gomb6 = Button(foablak,text = 'Szorzás',command = szorzas)
gomb6.grid()
#Szorzás

#Maradékos osztás
def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a / b
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
gomb7 = Button(foablak,text = 'Osztás(maradékos)',command = osztas)
gomb7.grid()
#Maradékos osztás

#Osztás
def osztas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a // b
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
gomb7 = Button(foablak,text = 'Osztás',command = osztas)
gomb7.grid()
#Osztás

#Négyzetgyök
import math
def gyokvonas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = math.sqrt(a)
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
    if a < 0:
        hibauzenet = Tk()
        cimke = Label(foablak,text = 'Negatív számmal nem lehet gyököt vonni', fg = 'red')
        cimke.pack()
gomb8 = Button(foablak,text = 'Gyökvonás',command = gyokvonas)
gomb8.grid()
#Négyzetgyök

#Négyzetre emelés
def negyzet():
    a = int(mezo1.get())
    c = a * a
    mezo3.delete(0,END)
    mezo3.insert(0, '' + str(c))
gomb9 = Button(foablak,text = 'Négyzetre emelés',command = negyzet)
gomb9.grid()
#Négyzetre emelés

#Vászon
can1 = Canvas(foablak, width = 460, height = 460, bg = 'white')
photo = PhotoImage(file= 'macska.gif')
item = can1.create_image(80, 80, image = photo)
can1.grid()
#Vászon


foablak.mainloop()