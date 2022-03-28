from tkinter import *
import math

foablak = Tk()
cimke = Label(foablak)
cimke.grid()

#elso mezo
sugar = Label(foablak, text = 'Sugár (cm) :', fg = 'black')
sugar.grid(column = 0, row = 0, padx = 6, pady = 6)
sugarmezo = Entry(foablak)
sugarmezo.grid(column = 1, row = 0, padx = 6, pady = 6) 
#elso mezo

#masodik mezo
magassag = Label(foablak, text = 'Magasság (cm) :', fg = 'black')
magassag.grid(column = 0, row = 1, padx = 6, pady = 6)
magassagmezo = Entry(foablak)
magassagmezo.grid(column = 1 , row = 1, padx = 6, pady = 6)
#masodik mezo

#harmadik mezo
hanyliter = Label(foablak, text = 'Ennyi literes a hordó (l) :', fg = 'black')
hanyliter.grid(column = 0, row = 2, padx = 6, pady = 6)
hanylitermezo = Entry(foablak)
hanylitermezo.grid(column = 1 , row = 2, padx = 6, pady = 6)
#harmadik mezo

#negyedik mezo
ennyiliteres = Label(foablak, text = 'Ekkora a hordó térfogata :', fg = 'black')
ennyiliteres.grid(column = 0, row = 4)
ennyiliteresmezo = Entry(foablak)
ennyiliteresmezo.grid(column = 1, row = 4, padx = 6, pady = 6)
#negyedik mezo

#otodik mezo
beleefer = Label(foablak, text = 'Bele-e fér a bor a hordóba?', fg = 'black')
beleefer.grid(column = 0, row = 5)
beleefermezo = Entry(foablak)
beleefermezo.grid(column = 1, row = 5, padx = 6, pady = 6)
#otodik mezo

#otodik mezo
hanyszazalekures = Label(foablak, text = 'Ennyi százaléka üres még a hordónak :', fg = 'black')
hanyszazalekures.grid(column = 0, row = 6)
hanyszazalekuresmezo = Entry(foablak)
hanyszazalekuresmezo.grid(column = 1, row = 6, padx = 6, pady = 6)
#otodik mezo

def kiszamit():
     r = int(sugarmezo.get())
     m = int(magassagmezo.get())
     v = math.pi * r*r * m // 1000
     ennyiliteresmezo.delete(0,END)
     ennyiliteresmezo.insert(0, str(round(v)) + " dm³")
     hanylitermezo.delete(0,END)
     hanylitermezo.insert(0, str(round(v)) + " l")



kiszamitgomb = Button(foablak, text = 'Kiszámít', command = kiszamit)
kiszamitgomb.grid(column = 1, row = 7, ipadx= 36, padx = 6, pady = 6)

foablak.mainloop()
