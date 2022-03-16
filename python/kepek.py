from tkinter import *
ablak1  = Tk()

ablak1.geometry('450x450')
ablak1.title('IKT ')
icon = PhotoImage(file = 'szemuveg.png')
ablak1.iconphoto(True, icon)
ablak1.config(background = 'black')
gombkep = PhotoImage(file = 'letöltés.png')
def klikk():
    print('Klikkeltem!')

kep = PhotoImage(file = 'letöltés.png')

cimke = Label(ablak1, text = 'Szia Úr!',
                            fg = 'white',
                            bg = '#123456',
                            font = ('Arial', 45, 'bold'),
                            bd = 10,
                            relief = RAISED,
                            padx = 25,
                            pady = 25, 
                            image = kep,
                            compound = 'top'
                            ) .pack()


gomb = Button(ablak1,
                text ='Kttints!',
                fg = 'blue',
                bg = 'yellow',
                bd = 10,
                relief = SUNKEN,
                command = klikk,
                padx = 17,
                pady = 17,
                image = gombkep,
                compound = 'bottom',
                activebackground = 'blue',
                activeforeground = 'yellow',
                state = ACTIVE).pack()
                            

ablak1.mainloop()