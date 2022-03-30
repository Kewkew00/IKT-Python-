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

#hatodik mezo
ennyifermeg = Label(foablak, text = 'Ennyi bor fér még a hordóba :', fg = 'black')
ennyifermeg.grid(column = 0, row = 7)
ennyifermegmezo = Entry(foablak)
ennyifermegmezo.grid(column = 1, row = 7, padx = 6, pady = 6)
#hatodik mezo

#bugfix valtozo
s = ''
#bugfix valtozo

def terfogat():

    if not s:
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str()+'a számításhoz adat kell ')
    
    r = float(sugarmezo.get())
    m = float(magassagmezo.get())
    b = float(hanylitermezo.get())

    if r >0 and m>0 and b>0:
        terfogat = round (math.pi * r * r * m /1000)
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str(terfogat)+' dm3')
        szazalek= round(b*(100/terfogat))
        
        if b <= terfogat and b >0 and terfogat > 0 :
            ennyiliteresmezo.delete(0, END)
            ennyiliteresmezo.insert(0, str(terfogat)+' dm3')
            beleefermezo.delete(0, END)
            beleefermezo.insert(0,str() +'igen')
            hanyszazalekuresmezo.delete(0, END)
            hanyszazalekuresmezo.insert(0, str(szazalek)+' %')
            ennyifermegmezo.delete(0, END)
            ennyifermegmezo.insert(0, str(terfogat - b)+' l')

    else :
        ennyiliteresmezo.delete(0, END)
        ennyiliteresmezo.insert(0, str()+' nem lehet számolni')

#gomb
kiszamitgomb = Button(foablak, text = 'Kiszámít', command = terfogat)
kiszamitgomb.grid(column = 1, row = 8, ipadx= 36, padx = 6, pady = 6)

foablak.mainloop()
