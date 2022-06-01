import tkinter as tk
import tkinter.ttk as ttk
from decimal import *
from typing_extensions import IntVar
import webbrowser

class kalkulator_aplikacija(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.update_idletasks()
        self.title('ELO raiting kalkulator')

        #notebook
        self.kalkulator = ttk.Notebook(self)
        #self.predstavitev = predstavitev(self.kalkulator)
        elo_kalkulator = ELO(self.kalkulator)
        self.kalkulator.add(elo_kalkulator, text='Elo raiting kalkulator')
        #self.kalkulator.add(self.predstavitev, text='predstavitev')
        self.kalkulator.pack(side = 'top', fill = 'both', expand = False)
        self.eval('tk::PlaceWindow . center')
"""
class predstavitev(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()

        labelA = tk.Label(self)
        labelA.grid(column=1, row=1)
"""
class podatki:
    koeficient_beli = None
    koeficient_crni = None
    raiting_beli = None
    raiting_crni = None
    rezultat = None
    novi_raiting_beli = None
    novi_raiting_crni = None
    manjkajoci_raiting = None

class ELO(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.widgets()
        
    def validate_raiting_valid(self, str, i):
        #preverja, da je raiting samo stevilke + preverja, če je raiting št predolgs za python za računat
        if int(i)>7:
            print('yay')
            self.bell()
            self.posodobitev.grid_remove()
            self.error.config(text='Predolg raiting!')
            self.error.grid()
            self.sporocila.grid()
            return False
        elif str.isdigit() or len(str) == 0:
            self.posodobitev.grid_remove()
            self.error.grid_remove()
            self.sporocila.grid_remove()
            return True
        else:
            
            self.bell()
            self.posodobitev.grid_remove()
            self.error.config(text= 'Vpisujte samo številke!')
            self.error.grid()
            self.sporocila.grid()
            return False
        
    def izracunaj(self):
        self.error.grid_remove()
        self.sporocila.grid()
        podatki.raiting_beli = self.RB.get()
        podatki.raiting_crni =  self.RC.get()
        podatki.koeficient_beli = self.KB.get()
        podatki.koeficient_crni = self.KC.get()
        podatki.rezultat = self.R.get() #--> rezultat belega (oz koliko tock je dobil)
        rezultat_crnega = abs(podatki.rezultat-1)
        if podatki.raiting_beli == '' or podatki.raiting_crni == '':
            if podatki.raiting_beli == '' and podatki.raiting_crni =='':
                manjkajoci = 'belega in črnega'
            elif podatki.raiting_beli == '':
                manjkajoci = 'belega'
            else:
                manjkajoci = 'črnega'
            error = tk.Toplevel()
            error.title('Error')
            error_m = tk.Label(error, text= f'Vpišite raiting {manjkajoci}!')
            error_m.grid(padx = 50, pady = 5)
            error_close = tk.Button(error, text='OK', command= error.destroy)
            error_close.grid()
        else:
            podatki.raiting_beli = int(podatki.raiting_beli)
            podatki.raiting_crni = int(podatki.raiting_crni)
            pricakovan_rezultat_belega = 1/ (1 + 10**Decimal((podatki.raiting_crni-podatki.raiting_beli)/400))
            pricakovan_rezultat_crnega = 1/ (1 + 10**Decimal((podatki.raiting_beli-podatki.raiting_crni)/400))

            podatki.novi_raiting_beli = round(podatki.raiting_beli + podatki.koeficient_beli*(podatki.rezultat - pricakovan_rezultat_belega), 1)
            podatki.novi_raiting_crni = round(podatki.raiting_crni + podatki.koeficient_crni*(rezultat_crnega - pricakovan_rezultat_crnega), 1)
            print(podatki.rezultat, pricakovan_rezultat_belega, pricakovan_rezultat_crnega, podatki.novi_raiting_beli, podatki.novi_raiting_crni)
            self.izpis_NR()

    def izpis_NR(self): #izpis novih raitingov
        self.novi_RB.config(text=podatki.novi_raiting_beli)
        self.novi_RC.config(text= podatki.novi_raiting_crni)
        self.posodobitev.grid()

    def resetiraj(self):
        for w in self.winfo_children():
            w.destroy()
        self.widgets()
    
    def widgets(self):
        self.KB = tk.IntVar()
        self.KC = tk.IntVar()
        self.R = tk.IntVar()
        
        #opis:
        self.labelB = ttk.Label(self, text = 'Kalkulator za računanje elo raitinga')
        self.labelB.grid(columnspan=2)

        #raiting belega = RB, raiting crnega = RC
        self.RB_label = tk.Label(self, text= 'Raiting belega:')
        self.RB_label.grid(columnspan=2, sticky= 'NSEW', ipadx=10, ipady =10)
        
        #preverjanje, da se vpisujejo samo stevilke
        prev = (self.register(self.validate_raiting_valid), '%P', '%i')
        #raiting beli in raiting crni (RB in RC)
        self.RB = tk.Entry(self, bg = 'white', width= 50, validate='key',validatecommand= prev)
        self.RB.grid(columnspan=2, ipadx=10, ipady= 2, sticky='EW')
        self.RB.focus()
        self.RC_label = tk.Label(self, text= 'Raiting črnega:')
        self.RC_label.grid(columnspan=2, sticky= 'NSEW', ipadx=10, ipady =10)
        self.RC = tk.Entry(self, bg = 'white', width= 50, validate='key',validatecommand= prev)
        self.RC.grid(columnspan=2, ipadx=10, ipady= 2, sticky='EW')

        #koeficient belega --> self.Kb
        self.KB_label = tk.Label(self,text = 'Izberite koeficient belega')
        self.KB_label.grid(column= 0)
        self.KB_10 = tk.Radiobutton(self, text='10', value = 10, variable=self.KB)
        self.KB_10.select()
        self.KB_10.grid(column=0)
        self.KB_20 = tk.Radiobutton(self, text='20', value = 20, variable=self.KB)
        self.KB_20.grid(column=0)
        self.KB_40 = tk.Radiobutton(self, text='40', value = 40, variable=self.KB)
        self.KB_40.grid(column=0)

        #koeficient črnega --> self.KC
        self.KC_label = tk.Label(self,text = 'Izberite koeficient črnega')
        self.KC_label.grid(column= 1, row=5)
        self.KC_10 = tk.Radiobutton(self, text='10', value = 10, variable=self.KC)
        self.KC_10.select()
        self.KC_10.grid(column=1, row=6)
        self.KC_20 = tk.Radiobutton(self, text='20', value = 20, variable=self.KC)
        self.KC_20.grid(column=1, row=7)
        self.KC_40 = tk.Radiobutton(self, text='40', value = 40, variable=self.KC)
        self.KC_40.grid(column=1, row=8)

        #rezultat --> self.R je skupni rezultat, 
        #1 = zmaga belega
        #0 = zmaga crnega
        #1/2 = remi
        self.rezultat = tk.Label(self,text = 'Izberite rezultat')
        self.rezultat.grid(column= 0, row=9)
        self.R_bz = tk.Radiobutton(self, text='1-0 (beli zmagal)', value = 1, variable=self.R)
        self.R_bz.select()
        self.R_bz.grid(column=0, row=10)
        self.R_cz = tk.Radiobutton(self, text='0-1 (črni zmagal)', value = 0, variable=self.R)
        self.R_cz.grid(column=0, row=11)
        self.R_r = tk.Radiobutton(self, text='1/2-1/2 (remi)', value = 1/2, variable=self.R)
        self.R_r.grid(column=0, row=12)

        #resetiraj
        self.reset = tk.Button(self,text = 'Resetiraj', command=self.resetiraj)
        self.reset.grid(column= 1, row=11)

        #izracunaj
        self.submit = tk.Button(self,text = 'Izračunaj', command= self.izracunaj)
        self.submit.grid(column= 1, row=10)
        
        #link do elo wikipedije
        link = tk.Button(self, text = 'Kaj je elo raiting?')
        link.bind('<Button>', lambda a: webbrowser.open('https://en.wikipedia.org/wiki/Elo_rating_system', new = 1))
        link.grid(column= 1, row=12)

        #sporocila uporabniku - noter so self.posodobitev, self.error
        self.sporocila = tk.LabelFrame(self)
        self.sporocila.grid(columnspan=2, padx =10)
        self.error = tk.Label(self.sporocila)

        self.posodobitev = tk.Frame(self.sporocila)
        self.noviRB_label= tk.Label(self.posodobitev, text= 'Novi raiting belega: ')
        self.noviRB_label.grid(column= 0, row = 0, ipadx=10, ipady=2)
        self.novi_RB = tk.Label(self.posodobitev, bg = 'white')
        self.novi_RB.grid(column=1, row = 0, ipadx=10, ipady= 2, sticky='EW')
        self.noviRC_label= tk.Label(self.posodobitev, text= 'Novi raiting črnega: ')
        self.noviRC_label.grid(column= 0, row = 1, ipadx=10, ipady=2)
        self.novi_RC = tk.Label(self.posodobitev, bg = 'white')
        self.novi_RC.grid(column=1, row = 1, ipadx=10, ipady= 2, sticky='EW')

if __name__ == '__main__':
    aplikacija = kalkulator_aplikacija()
    aplikacija.mainloop()
