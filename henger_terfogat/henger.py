from tkinter import * 
import math

foablak = Tk()
cimke = Label(foablak)
cimke.grid()

#elso mezo
sugar = Label(foablak, text = 'Sugár (cm):', fg = 'black')
sugar.grid(column = 0, row = 0)
sugarmezo = Entry(foablak)
sugarmezo.grid(column = 1, row = 0, padx = 6, pady = 6)
#elso mezo

#masodik mezo
magassag = Label(foablak, text = 'Magasság (cm):', fg = 'black')
magassag.grid(column = 0, row = 1)
magassagmezo = Entry(foablak)
magassagmezo.grid(column = 1 , row = 1, padx = 6, pady = 6)
#masodik mezo

#harmadik mezo
terfogat = Label(foablak, text = 'Térfogat :', fg = 'black')
terfogat.grid(column = 0, row = 3)
terfogatmezo = Entry(foablak)
terfogatmezo.grid(column = 1, row = 3, padx = 6, pady = 6)
#harmadik mezo

#negyedik mezo
vashenger = Label(foablak, text = 'Vashenger :', fg = 'black')
vashenger.grid(column = 0, row = 4)
vashengermezo = Entry(foablak)
vashengermezo.grid(column = 1, row = 4, padx = 6, pady = 6)
#negyedik mezo

#otodik mezo
fahenger = Label(foablak, text = 'Fahenger :', fg = 'black')
fahenger.grid(column = 0, row = 5)
fahengermezo = Entry(foablak)
fahengermezo.grid(column = 1, row = 5, padx = 6, pady = 6)
#otodik mezo

def terfogat():
     r = int(sugarmezo.get())
     m = int(magassagmezo.get())
     v = math.pi * r*r * m
     terfogatmezo.delete(0,END)
     terfogatmezo.insert(0, str(round(v, 2)) + " cm3")

     v = math.pi * r*r * m * 7.8
     vashengermezo.delete(0,END)
     vashengermezo.insert(0, str(round(v, 2)) + " g")

     v = math.pi * r*r * m * 0.6
     fahengermezo.delete(0,END)
     fahengermezo.insert(0, str(round(v, 2)) + " g")

icon = PhotoImage(file = 'henger_kep.png')
foablak.iconphoto(True,icon)

foablak.title('Henger')



kiszamitgomb = Button(foablak, text = 'Kiszámít', command = terfogat,)
kiszamitgomb.grid(column = 1, row = 2, ipadx= 36, padx = 6, pady = 6)


foablak.mainloop()
