''' Programação do Protótipo - POWER UP do Instrutor'''

# Impotando as blibliotecas 
from tkinter import *

class Editar_Perfil(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Editar Perfil') 
        self.geometry('1340x680+0+0')
        self.configure(bg = 'white')

        self.widgets()
        root.mainloop()

    def widgets(self):
        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal EDITAR PERFIL
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.13)

        self.titulo = Label(self.frame1,       # Titulo 'EDTAR PERFIL'
                                text='EDITAR PERFIL',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.txt1 = Label(self,   # Título 'Digite suas novas informações'
                            text='Digite suas novas informações:',
                            font=('Britannic', 20),
                            bg='white',
                            fg='black')
        self.txt1.place(relx = 0.1, rely = 0.15)

        self.nome = Label(self,   # Título 'Nome:'
                            text='Nome:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.nome.place(relx = 0.1, rely = 0.22)

        self.nome_entry = Entry(self, # Entrada do novo nome 
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.nome_entry.place(relx = 0.17, rely = 0.22, relwidth = 0.7, relheight = 0.06)

        self.nv_senha = Label(self,   # Título 'Nova Senha:'
                            text='Senha:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.nv_senha.place(relx = 0.1, rely = 0.29)

        self.nv_senha_entry = Entry(self, # Entrada do nova senha
                                bg=self.cor_cinza,
                                show='*',
                                fg='black',
                                font=('Britannic Bold', 16))
        self.nv_senha_entry.place(relx = 0.17, rely = 0.29, relwidth = 0.7, relheight = 0.06)

        self.cnf_nv_senha = Label(self,   # Título 'Confirma Senha:'
                            text='Confirma Senha:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.cnf_nv_senha.place(relx = 0.01, rely = 0.36)

        self.cnf_nv_senha_entry = Entry(self, # Entrada do nova senha
                                bg=self.cor_cinza,
                                show='*',
                                fg='black',
                                font=('Britannic Bold', 16))
        self.cnf_nv_senha_entry.place(relx = 0.17, rely = 0.36, relwidth = 0.7, relheight = 0.06)

        self.btn_atualiza = Button(self,      # Botão de Atualizar Informações
                                bg = self.cor_laranja,
                                fg='white',
                                text='Atualizar',
                                font=('Britannic Bold', 20))
        self.btn_atualiza.place(relx = 0.75, rely = 0.45, relwidth = 0.17, relheight = 0.08)

        self.img = PhotoImage(file='btn_voltar.PNG')    # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img)
        self.btn_voltar.place(relx=0.1, rely=0.8)


class Tela_Inicial(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Bem-Vindo ao POWER UP') 
        self.geometry('1340x680+0+0')
        self.configure(bg = 'white')
        
        self.widgets()
        root.mainloop()

    def widgets(self):
        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal 'Olá...'
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.13)

        self.titulo = Label(self.frame1,       # Titulo 'Olá ...'
                                text='Olá, *Nome*',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        ## Botões do Menu Principal ##
        self.img1 = PhotoImage(file='btn_edit_perfil.png')   # Botão de Editar Perfil
        self.btn_edita = Button(self, image=self.img1, command= self.clica_btn_edita)
        self.btn_edita.place(relx=0.1, rely=0.3)

        self.img2 = PhotoImage(file='btn_fluxo.PNG')   # Botão de Editar Perfil
        self.btn_fluxo = Button(self, image=self.img2)
        self.btn_fluxo.place(relx=0.4, rely=0.3)

        self.img3 = PhotoImage(file='btn_edit_fichas.PNG')   # Botão de Editar Perfil
        self.btn_edt_fichas = Button(self, image=self.img3)
        self.btn_edt_fichas.place(relx=0.7, rely=0.3)

    def clica_btn_edita(self):  # Comando do botão
        self.hide()
        self.subframe = Editar_Perfil(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

# Tela de Cadastro
class Cadastro(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Cadastre-se no POWER UP') 
        self.geometry('1340x680+0+0')
        self.configure(bg = 'white')
        
        self.widgets()
        root.mainloop()

    def widgets(self):
        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal 'Cadastro'
        self.frame1.place(relx = 0, rely = 0.11, relwidth = 1, relheight = 0.13)

        self.titulo = Label(self.frame1,       # Titulo 'CADASTRO'
                                text='CADASTRO',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.email = Label(self,   # Título 'E-mail'
                            text='E-mail:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.email.place(relx = 0.15, rely = 0.28)

        self.email_entry = Entry(self, # Entrada de e-mail
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.email_entry.place(relx = 0.22, rely = 0.28, relwidth = 0.7, relheight = 0.06)

        self.nome = Label(self,   # Título 'Nome'
                            text='Nome:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.nome.place(relx = 0.15, rely = 0.35)

        self.nome_entry = Entry(self, # Entrada do Nome
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.nome_entry.place(relx = 0.22, rely = 0.35, relwidth = 0.7, relheight = 0.06)

        self.senha = Label(self,   # Título 'Senha'
                            text='Senha:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.senha.place(relx = 0.15, rely = 0.42)

        self.senha_entry = Entry(self, # Entrada de senha
                                show = '*',
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.senha_entry.place(relx = 0.22, rely = 0.42, relwidth = 0.7, relheight = 0.06)

        self.conf_senha = Label(self,   # Título 'Confirma Senha'
                            text='Confirma Senha:',
                            font=('Britannic Bold', 20),
                            bg='white',
                            fg='black')
        self.conf_senha.place(relx = 0.06, rely = 0.49)

        self.conf_senha_entry = Entry(self, # Entrada de confirmação
                                show = '*',
                                bg=self.cor_cinza,
                                fg='black',
                                font=('Britannic Bold', 16))
        self.conf_senha_entry.place(relx = 0.22, rely = 0.49, relwidth = 0.7, relheight = 0.06)

        self.btn_cadastra = Button(self,      # Botão de Cadastrar
                                bg = self.cor_laranja,
                                fg='white',
                                text='Cadastrar',
                                font=('Britannic Bold', 20),
                                command= self.clica_entrar)
        self.btn_cadastra.place(relx = 0.75, rely = 0.58, relwidth = 0.17, relheight = 0.08)

        self.img = PhotoImage(file='btn_voltar.PNG')    # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img, command= self.clica_voltar)
        self.btn_voltar.place(relx=0.1, rely=0.8)

    def clica_entrar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def clica_voltar(self):  # Comando do botão
        self.hide()
        self.subframe = Aplicativo(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

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
                                font=('Britannic Bold', 20),
                                command=self.clica_entrar)
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

    def clica_entrar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()

##### PROGRAMA PRINCIPAL #####
root = Tk()
Aplicativo()
