#Função: Exercicio para criar telas em python
#Autor: Raphael Ramos
#Professor: Fernando Massanori

from tkinter import *
app = Tk ()
app.title ('Show de Calouros')
app.geometry ('300x400+200+300')
certos = IntVar ()
certos.set (0)
errados = IntVar ()
errados.set (0)
soma = IntVar()
soma.set(0)

def musica_certa():
    certos.set (certos.get () + 1)
    soma.set(soma.get() + 1)
def musica_errada():
    errados.set (errados.get () + 1)
    soma.set(soma.get() + 1)
 

lab = Label (app, text = 'Aperte os botões!', height = 3)
lab.pack ()

b1 = Button (app, text = 'Certo!', width = 10, command = musica_certa )
b1.pack (side = 'top', padx = 13, pady = 13)

b2 = Button (app, text = 'Errado!', width = 10, command = musica_errada)
b2.pack (side = 'bottom', padx = 13, pady = 13)

lab1 = Label (app, textvariable = certos)
lab1.pack (side = 'top')
lab2 = Label (app, textvariable = errados)
lab2.pack (side = 'bottom')
lab3 = Label (app, textvariable = soma)
lab3.pack (side = 'left')


app.mainloop ()


