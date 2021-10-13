''' Programação do Protótipo - POWER UP do Instrutor'''

# Impotando as blibliotecas 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import date
from datetime import datetime
from random import choice, randint 

# Tela para edição da Ficha dos Alunos
class Tela_Fichas(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    pessoas = []
    alunos = ['Gabriel', 'Rafaela', 'Alexandre', 'Milena', 'Kauã', 'Júlia', 'Ana']

    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Fichas dos Alunos') 
        self.geometry('1340x680+290+200')
        self.configure(bg = 'white')
        # Ícone
        self.iconbitmap('powerup_icone.ico')

        self.widgets()
        self.lista_frame2()
        self.get_aluno()

    def widgets(self):
        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal FICHA DOS ALUNOS
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.13)

        self.frame2 = Frame(self, bg = self.cor_cinza) # Frame para o título principal FICHA DOS ALUNOS
        self.frame2.place(relx = 0.03, rely = 0.15, relwidth = 0.94, relheight = 0.1)

        self.titulo = Label(self.frame1,       # Titulo 'FICHA DOS ALUNOS'
                                text='FICHA DOS ALUNOS',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.pesquisa_entry = Entry(self.frame2, # Entrada de pesquisa
                                bg='white',
                                fg='black',
                                font=('Britannic Bold', 16))
        self.pesquisa_entry.place(relx = 0.24, rely = 0.21, relwidth = 0.75, relheight = 0.56)

        self.btn_novo_aluno = Button(self,      # Botão de Atualizar Informações
                                bg = self.cor_laranja,
                                fg='white',
                                text='Novo Aluno',
                                font=('Britannic Bold', 20))
        self.btn_novo_aluno.place(relx = 0.25, rely = 0.8, relwidth = 0.17, relheight = 0.08)

        self.img = PhotoImage(file='btn_pesquisa_aluno.png')    # Botão de voltar para a página anterior 
        self.btn_pesquisa = Button(self, image=self.img, command=self.busca_aluno)
        self.btn_pesquisa.place(relx=0.05, rely=0.16)

        self.img1 = PhotoImage(file='btn_voltar.PNG')    # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img1, command= self.clica_voltar)
        self.btn_voltar.place(relx=0.1, rely=0.8)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self, height = 0, column = ("col1", "col2"))
        self.listaCli.place(relx = 0.03, rely = 0.26, relwidth = 0.94, relheight = 0.53)
        self.listaCli.heading("#0", text = '')
        self.listaCli.heading("#1", text = "Identificação")
        self.listaCli.heading("#2", text = "Nome")

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', stretch=YES, minwidth=25, width=100, anchor="center")
        self.listaCli.column('#2', stretch=YES, minwidth=25, width=100, anchor="center")

        # Configurações para a Barra de Rolagem do Treeview
        self.barra_de_rolagem = Scrollbar(self.listaCli, orient = "vertical")
        self.listaCli.configure(yscroll = self.barra_de_rolagem.set)
        self.barra_de_rolagem.place(relx=0.98, rely = 0.032, relheight = 0.96)

        # Realiza um onDoubleClick para abrir a ficha do aluno 
        self.listaCli.bind("<Double-1>", self.onDoubleClick)

    def get_aluno(self):
        # Lista de alunos 
        for n in self.alunos:
            self.listaCli.insert("", END, values=n)

    def busca_aluno(self):
        self.pesquisa = self.pesquisa_entry.get()
        for n in self.alunos:
            if self.pesquisa == n:
                self.listaCli.delete(*self.listaCli.get_children())
                self.listaCli.insert('', END, values=n)

    def onDoubleClick(self, event):
        self.listaCli.selection()
        print('Aluno Selecionado')

    def clica_voltar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

# Tela para obter uma planilha com o Fluxo de Alunos
class Tela_Fluxo(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    hora = 0
    pessoas = []
    alunos = ['Gabriel', 'Rafaela', 'Alexandre', 'Milena', 'Kauã', 'Júlia', 'Ana Moura']

    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Fluxo de Alunos') 
        self.geometry('1340x680+290+200')
        self.configure(bg = 'white')
        # Ícone
        self.iconbitmap('powerup_icone.ico')

        self.widgets()
        self.lista_frame2()
        self.get_log()
        self.conta_presentes()

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height = 0, column = ("col1", "col2", "col3"))
        self.listaCli.place(relx = 0.01, rely = 0.05, relwidth = 0.56, relheight = 0.75)
        self.listaCli.heading("#0", text = "")
        self.listaCli.heading("#1", text = "Identificação")
        self.listaCli.heading("#2", text = "Entrada")
        self.listaCli.heading("#3", text = "Saída")

        self.listaCli.column('#0', stretch=YES, width=0, anchor="center")
        self.listaCli.column('#1', stretch=YES, minwidth=10, width=25, anchor="center")
        self.listaCli.column('#2', stretch=YES, minwidth=25, width=40, anchor="center")
        self.listaCli.column('#3', stretch=YES, minwidth=40, width=55, anchor="center")

        # Configurações para a Barra de Rolagem do Treeview
        self.barra_de_rolagem = Scrollbar(self.listaCli, orient = "vertical")
        self.listaCli.configure(yscroll = self.barra_de_rolagem.set)
        self.barra_de_rolagem.place(relx=0.98, rely = 0.032, relheight = 0.96)

    def widgets(self):
        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal FLUXO DE ALUNOS
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.13)

        self.frame2 = Frame(self, bg = self.cor_cinza) # Frame para o quadro treeview
        self.frame2.place(relx = 0.45, rely = 0.22, relwidth = 0.95, relheight = 0.95)

        self.frame3 = Frame(self, bg = self.cor_cinza) # Frame para o título para a DATA DO DIA
        self.frame3.place(relx = 0.7, rely = 0.14, relwidth = 0.25, relheight = 0.07)

        self.frame4 = Frame(self, bg = self.cor_cinza) # Frame para a quantidade de alunos no momento
        self.frame4.place(relx = 0.23, rely = 0.76, relwidth = 0.2, relheight = 0.2)

        self.titulo = Label(self.frame1,       # Titulo 'FLUXO DE ALUNOS'
                                text='FLUXO DE ALUNOS',
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.txt1 = Label(self,   # Título 'Você pode obter uma planilha com os alunos da academia:'
                            text='Você pode obter uma planilha com os alunos da academia:',
                            font=('Britannic', 20),
                            bg='white',
                            fg='black')
        self.txt1.place(relx = 0.02, rely = 0.15)

        self.txt2 = Label(self.frame4,   # Título - Quantidade de pessoas 
                            text='Na academia agora:',
                            font=('Britannic', 14),
                            bg = self.cor_cinza,
                            fg='black')
        self.txt2.place(relx = 0.032, rely = 0.03)

        self.img1 = PhotoImage(file='btn_obter_planilha.png')   # Botão de Editar Perfil
        self.btn_edita = Button(self, image=self.img1, command = self.insere_log)
        self.btn_edita.place(relx=0.13, rely=0.22)

        self.img = PhotoImage(file='btn_voltar.PNG')    # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img, command= self.clica_voltar)
        self.btn_voltar.place(relx=0.1, rely=0.8)

        # Configurações para a data do dia
        self.data_atual = date.today()
        self.data_e_hora_atuais = datetime.now()
        self.data_e_hora_em_texto = self.data_e_hora_atuais.strftime('%d/%m/%Y     %H:%M')

        self.txt2 = Label(self.frame3,   # Data do Dia
                            text='{}'.format(self.data_e_hora_em_texto),
                            font=('Britannic', 20, 'bold'),
                            bg=self.cor_cinza,
                            fg='black')
        self.txt2.place(relx = 0.1, rely = 0.16)
        self.alteracao()

    def alteracao(self):
        self.now = datetime.now()
        self.txt2['text'] = self.now.strftime('%d/%m/%Y     %H:%M:%S')    
        self.after(1000, self.alteracao)

    def get_log(self):
        for n in self.pessoas:
            self.listaCli.insert("", END, values=n)
            self.conta_presentes()
            
    def insere_log(self):
        self.entrada = choice(self.alunos)
        self.contador = 0 
        for i in self.pessoas: # Percorre a lista de Pessoas
            if self.entrada == i[0] and len(i) < 3:
                self.listaCli.delete(*self.listaCli.get_children())
                i.append(self.txt2['text'])
                self.contador += 1
                  
        if self.contador == 0:
            self.listaCli.delete(*self.listaCli.get_children())
            self.pessoas.append([self.entrada, self.txt2['text']])
        
        self.get_log()        
        # Criar uma lista de nomes, inserir a entrada e a partir dela condiciona a saida, e inserir essas infrmações na lista do aluno determinado

    def conta_presentes(self):
        self.contador1 = 0 
        for i in self.pessoas: # Percorre a lista de Pessoas
            if len(i) < 3:
                self.contador1 += 1
        self.txt3 = Label(self.frame4,   # Número - Quantidade de pessoas
                            text=self.contador1,
                            font=('Britannic', 45, 'bold'),
                            bg = self.cor_cinza,
                            fg='black')
        self.txt3.place(relx = 0.6, rely = 0.2)

    def clica_voltar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

# Tela para editar o Perfil 
class Editar_Perfil(Toplevel):  # ESSA 'class"='
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'
    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Editar Perfil') 
        self.geometry('1340x680+290+200')
        self.configure(bg = 'white')
        # Ícone
        self.iconbitmap('powerup_icone.ico')

        self.widgets()

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
        self.btn_voltar = Button(self, image=self.img, command= self.clica_voltar)
        self.btn_voltar.place(relx=0.1, rely=0.8)

    def clica_voltar(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def hide(self):
        self.withdraw()
    def show(self):
        self.update()
        self.deiconify()

# Tela do Menu Principal
class Tela_Inicial(Toplevel):
    # Atributos do app
    cor_laranja = '#f48c06'
    cor_cinza = '#ced4da'

    def __init__(self, original):
        self.original_frame = original
        Toplevel.__init__(self)  # Importando o Metódo Construtor
        self.title('Bem-Vindo ao POWER UP') 
        self.geometry('1340x680+290+200')
        self.configure(bg = 'white')
        # Ícone
        self.iconbitmap('powerup_icone.ico')

        self.widgets()

    def widgets(self):
        self.ip = randint(100, 1000)    # Gerador de IP para a academia

        self.frame1 = Frame(self, bg = self.cor_laranja) # Frame para o título principal 'Olá...'
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.13)

        self.frame2 = Frame(self, bg=self.cor_cinza)
        self.frame2.place(relx= 0.8, rely= 0.9, relwidth=0.19, relheight=0.09)

        self.titulo = Label(self.frame1,       # Titulo 'Olá teste001'
                                text='Olá, teste001',  # ESSA VÁRIAVELK PRECISAR SER RETIFICADA COMO UMA VÁRIAVEL CONECTADA AO BANCO DE DADOS
                                font=('Britannic Bold', 30),
                                bg=self.cor_laranja,
                                fg='black')
        self.titulo.place(relx = 0.1, rely = 0.15)

        self.titulo = Label(self.frame2,       # Demostra o IP da academia
                                text=f'IP da Academia: {self.ip}',  
                                font=('Britannic Bold', 12),
                                bg=self.cor_cinza,
                                fg='black')
        self.titulo.place(relx = 0.01, rely = 0.05)

        ## Botões do Menu Principal ##
        self.img1 = PhotoImage(file='btn_edit_perfil.png')   # Botão de Editar Perfil
        self.btn_edita = Button(self, image=self.img1, command= self.clica_btn_edita)
        self.btn_edita.place(relx=0.1, rely=0.3)

        self.img2 = PhotoImage(file='btn_fluxo.PNG')   # Botão de Editar Perfil
        self.btn_fluxo = Button(self, image=self.img2, command= self.clica_btn_fluxo)
        self.btn_fluxo.place(relx=0.4, rely=0.3)

        self.img3 = PhotoImage(file='btn_edit_fichas.PNG')   # Botão de Editar Perfil
        self.btn_edt_fichas = Button(self, image=self.img3, command= self.clica_btn_ficha)
        self.btn_edt_fichas.place(relx=0.7, rely=0.3)    

    def clica_btn_edita(self):  # Comando do botão
        self.hide()
        self.subframe = Editar_Perfil(self)  # Próxima janela para ser aberta

    def clica_btn_fluxo(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Fluxo(self)  # Próxima janela para ser aberta

    def clica_btn_ficha(self):  # Comando do botão
        self.hide()
        self.subframe = Tela_Fichas(self)  # Próxima janela para ser aberta

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
        self.geometry('1340x680+290+200')
        self.configure(bg = 'white')
        # Ícone
        self.iconbitmap('powerup_icone.ico')

        self.widgets()

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
                                command= self.novo_user)
        self.btn_cadastra.place(relx = 0.75, rely = 0.58, relwidth = 0.17, relheight = 0.08)

        self.img = PhotoImage(file='btn_voltar.PNG')    # Botão de voltar para a página anterior 
        self.btn_voltar = Button(self, image=self.img, command= self.onClose)
        self.btn_voltar.place(relx=0.1, rely=0.8)

    def limpa_tela(self):
        self.email_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END)

    def confirma_senha(self):   # Mensagem de confirmação para a entrada e verficação da confimação de tela
        if self.senha_entry.get() == self.conf_senha_entry.get():
            self.opcao = messagebox.askokcancel('POWER UP', 'Novo Usuário cadastrado com sucesso\nClique em OK para entrar.')
            if self.opcao == True:
                self.clica_ok()

        else:
            messagebox.askokcancel('POWER UP', 'A confimação de senha não é correspondente. Insira novamente')
            self.senha_entry.delete(0, END)
            self.conf_senha_entry.delete(0, END)

    def novo_user(self):
        # Identificando se as variavéis estão preenchidas
        if self.nome_entry.get() == '':
            msg = "Digite um nome para o usuário"
            messagebox._show('Cadastro de usuário - Aviso!', msg)

        elif self.email_entry.get() == '':
            msg = "Digite um email para o usuário"
            messagebox._show('Cadastro de usuário - Aviso!', msg)

        elif self.senha_entry.get() == '':
            msg = "Digite um senha para o usuário"
            messagebox._show('Cadastro de usuário - Aviso!', msg)

        else:
            self.nome_var = self.nome_entry.get()
            self.email_var = self.email_entry.get()
            self.senha_var = self.senha_entry.get()

        # Incorpora os métodos user e executa
        self.ddl = DDL()
        self.ddl.insere_user(self.nome_var, self.email_var, self.senha_var)

        self.confirma_senha()
        self.limpa_tela()   # método de limpar tela

    def clica_ok(self):
        self.hide()
        self.subframe = Tela_Inicial(self)  # Próxima janela para ser aberta

    def onClose(self):  # Comando do botão voltar 
        self.destroy()
        self.original_frame.show()

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

        # Entrada com 'Return'
        self.root.bind("<Return>", self.clica_entrar)

        self.bd = DDL()
        self.bd.cria_tabela()

        root.mainloop()

    def tela(self): # Configurações de Tela
        self.root.title('POWER UP') 
        self.root.geometry('1340x680+290+200')
        self.root.configure(bg="white")
        # Ícone
        self.root.iconbitmap('powerup_icone.ico')

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

    def limpa_tela(self):
        self.email_entry.delete(0, END)
        self.senha_entry.delete(0, END)

    def clica_cadastro(self):  # Comando do botão
        self.hide()
        self.subframe = Cadastro(self)  # Próxima janela para ser aberta

    def clica_entrar(self, *args):  # Comando do botão
        self.email_var = self.email_entry.get()# Atribui o email para a varíavel 'self.email_var'
        self.senha_var = self.senha_entry.get() # Atribui o senha para a varíavel 'self.senha var'

        if self.email_var == '':
            messagebox._show('Cadastro de usuário - Aviso!', 'Digite um email para o usuário')

        elif self.senha_var == '':
            messagebox._show('Cadastro de usuário - Aviso!', 'Digite um senha para o usuário')
        
        else:
            self.email_var = self.email_entry.get()# Atribui o email para a varíavel 'self.email_var'
            self.senha_var = self.senha_entry.get() # Atribui o senha para a varíavel 'self.senha var'

            if self.bd.verifica_cliente(self.email_var, self.senha_var) == 'Confirmado':
                self.limpa_tela()
                self.hide()
                self.tela_inicial = Tela_Inicial(self)  # Verifica o cliente no banco de dados - ESSA FUNCIONALIDADE PRECISA SER REFATORADA
                  
    def hide(self):
        self.root.withdraw()
    def show(self):
        self.root.update()
        self.root.deiconify()

class DDL:  # Manipulação da Tabela
    contimetro = 0  # Varíavel que ontabiliza a quantidade de tentativas do usuário

    def variaveis(self, nome, email, senha):
        self.email_var = email
        self.nome_var = nome
        self.senha_var = senha

    def conecta_bd(self):
        self.conn = sqlite3.connect('pup_dates.db')   # Conectando com o Banco de Dados do Aplicativo
        self.cur = self.conn.cursor()  # Cursor de busca no Banco de Dados
        print('Conectado ao Banco de Dados')

    def desconecta_bd(self):
        self.conn.close()
        print('Desconectado do Banco de Dados')

    def cria_tabela(self):
        self.conecta_bd()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, nome_cliente varchar(80), email_cliente varchar(80), senha_cliente varchar(80))''')
        self.conn.commit()
        print('Banco de Dados criado com sucesso')
        self.desconecta_bd()

    def insere_user(self, nome, email, senha):  # Insere o novo usuário no BD
        # Executa no Banco de Dados 
        self.conecta_bd()
        # Verifica se o cliente já é cadastrado.
        self.verifica_cliente(email, senha)
        self.cur.execute("""
        INSERT INTO users(nome_cliente, email_cliente, senha_cliente)
        VALUES(?, ?, ?);""", (nome, email, senha))
        self.conn.commit()
        print('Valores Inseridos')
        self.desconecta_bd()

    def verifica_cliente(self, email, senha): # Método para verificar o usuário no BD
        print("\nVerficando Cliente\n") 
        #self.conecta_bd()

        # VERIFICANDO EM UMA CONDIÇÃO FORA DO BANDO DE DADOS
        if email == 'admin' and senha == 'admin':
            #self.verfica = self.cur.execute("SELECT * FROM users WHERE email_cliente = {}".format(email)) # Comando de verificação do usuário no Bando da Dados
            return 'Confirmado'
            
        else:
            messagebox.askokcancel('POWER UP', 'A senha ou e-mail não correposnde a um usuário cadastrado')
        #self.desconecta_bd()

##### PROGRAMA PRINCIPAL #####
root = Tk()
Aplicativo()