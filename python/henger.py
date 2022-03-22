from tkinter import * 
import math

foablak = Tk()
cimke = Label(foablak)
cimke.grid()

sugar = Label(foablak, text = 'Sugár (cm):', fg = 'black')
sugar.grid(column = 0, row = 0)
sugarmezo = Entry(foablak)
sugarmezo.grid(column = 1, row = 0)

magassag = Label(foablak, text = 'Magasság (cm)', fg = 'black')
magassag.grid(column = 0, row = 1)
magassagmezo = Entry(foablak)
magassagmezo.grid(column = 1 , row = 1)

kiszamitgomb = Button(foablak, text = 'Kiszámít', fg = 'black')
kiszamitgomb.grid(column = 2, row = 2)

terfogat = Label(foablak, text = 'Térfogat :', fg = 'black')
terfogat.grid(column = 0, row = 3)
terfogatmezo = Entry(foablak)
terfogatmezo.grid(column = 1, row = 3)

vashenger = Label(foablak, text = 'Vashenger :', fg = 'black')
vashenger.grid(column = 0, row = 4)
vashengermezo = Entry(foablak)
vashengermezo.grid(column = 1, row = 4)

fahenger = Label(foablak, text = 'Fahenger :', fg = 'black')
fahenger.grid(column = 0, row = 5)
fahengermezo = Entry(foablak)
fahengermezo.grid(column = 1, row = 5)

def terfogat(a,b):
     r = int(sugarmezo.get())
     m = int(magassagmezo.get())
     v = 
     terfogatmezo.delete(0,END)
     terfogatmezo.insert(0, '' + str(c))



foablak.mainloop()