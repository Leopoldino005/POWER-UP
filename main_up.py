''' Programação do Protótipo - POWER UP do Instrutor'''

# Impotando as blibliotecas 
from tkinter import *

# Tela de Cadastro
class Cadastro(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('POWER UP') 
        self.geometry('1340x680+0+0')
        self.configure(bg = 'white')
        
        root.mainloop()

# Tela Inicial 
class Aplicativo:
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'

    def __init__(self): # Método Construtor
        self.root = root
        self.tela()
        self.widgets()
        root.mainloop()
        
    def tela(self): # Configurações de Tela
        self.root.title('POWER UP') 
        self.root.geometry('1340x680+0+0')
        self.root.configure(bg="white")

    def widgets(self):
        self.frame1 = Frame(self.root, bg = self.cor_laranja) # Frame para o título principal 'Entrar'
        self.frame1.place(relx = 0, rely = 0.11, relwidth = 1, relheight = 0.13)

        self.titulo = Label(self.frame1,       # Titulo 'ENTRAR'
                                text='ENTRAR',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.email = Label(self.root,   # Título 'E-mail'
                            text='E-mail:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.email.place(relx = 0.15, rely = 0.28)

        self.email_entry = Entry(self.root, # Entrada de e-mail
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.email_entry.place(relx = 0.22, rely = 0.28, relwidth = 0.7, relheight = 0.06)

        self.senha = Label(self.root,   # Título 'Senha'
                            text='Senha:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.senha.place(relx = 0.15, rely = 0.35)

        self.senha_entry = Entry(self.root, # Entrada de senha
                                show = '*',
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.senha_entry.place(relx = 0.22, rely = 0.35, relwidth = 0.7, relheight = 0.06)

        self.txt1 = Label(self.root,   # Título 'Esquece sua Senha'
                            text='Esqueceu sua senha?',
                            font=('Britannic', 20),
                            bg='white',
                            fg='black')
        self.txt1.place(relx = 0.15, rely = 0.43)

        self.btn_senha = Button(self.root,      # Botão de Esqueceu a Senha
                                bg = self.cor_laranja,
                                fg='white',
                                text='Substituir Senha',
                                font=('Britannic Bold', 20))
        self.btn_senha.place(relx = 0.17, rely = 0.5, relwidth = 0.17, relheight = 0.06)

        self.btn_entrar = Button(self.root,      # Botão de Entrar
                                bg = self.cor_laranja,
                                fg='white',
                                text='Entrar',
                                font=('Britannic Bold', 20))
        self.btn_entrar.place(relx = 0.75, rely = 0.43, relwidth = 0.17, relheight = 0.08)

        self.txt2 = Label(self.root,   # Título 'Não possui cadastro'
                            text='Caso não possua conta, clique em cadastre-se:',
                            font=('Britannic', 20),
                            bg='white',
                            fg='black')
        self.txt2.place(relx = 0.15, rely = 0.7)

        self.btn_cadastro = Button(self.root,      # Botão de Cadastro
                                bg = self.cor_laranja,
                                fg='white',
                                text='Cadastra-se',
                                font=('Britannic Bold', 20),
                                command= self.clica_cadastro)
        self.btn_cadastro.place(relx = 0.17, rely = 0.76, relwidth = 0.17, relheight = 0.08)

    def clica_cadastro(self):  # Comando do botão
        self.hide()
        self.subframe = Cadastro(self)  # Próxima janela para ser aberta

    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()

##### PROGRAMA PRINCIPAL #####
root = Tk()
Aplicativo()