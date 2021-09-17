''' Programação do Protótipo - POWER UP'''

# Impotando as blibliotecas 
from tkinter import *

class Aplicativo:
    def __init__(self): # Método Construtor
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()
        
    def tela(self): # Configurações de Tela
        self.root.title('POWER UP') 
        self.root.geometry('1080x650+10+6')
        self.root.resizable(False, False)

    def widgets(self):
        self.janela_principal = Frame(self.root, bg = 'black')
        self.janela_principal.place(relx = 0, rely = 1, relwidth = 1, relheight = 1)


##### PROGRAMA PRINCIPAL #####
root = Tk()
Aplicativo()
