from modulos import *
from Functions import func
from gerarRelatorio import PDF

window = Tk()

class LIMS(func, PDF):
    def __init__(self):
        self.window = window
        self.login()
        self.tela()
        self.frames()
        self.opcoes()
        self.widget()
        self.dashboard()
        self.montaTable()
        self.botoes()        
        window.mainloop()
        
    def tela(self):
        self.window.title('Registro de Usúarios do LIMS')
        self.window.state('zoomed')
        self.window.resizable(False,False)
        self.window.geometry('900x715')
        self.window.configure(bg='#b0c4de')
        self.window.maxsize(width=900, height=715)
        self.window.minsize(width=900, height=715)
        self.window.iconbitmap("imagens\\Lab.ico")  
        
        self.img_fundo = PhotoImage(file="imagens\\frontend.png")
        self.label_fundo = Label(window, image=self.img_fundo)
        self.label_fundo.pack()
           
    def frames(self):

        self.frame_dashboard = Frame(self.window, bd=4, highlightbackground='#dfe3ee', highlightthickness=5, bg='#FFF8DC')
        self.frame_dashboard.place(x=50,y=400, width=800, height=200)

    def opcoes(self):
        BarraMenu = Menu(self.window)
        #Menu Opcão
        MenuOpcao = Menu(BarraMenu, tearoff=0)
        subMenuOpcao = Menu(MenuOpcao, tearoff=0)
        subMenuOpcao.add_command(label='Solicitação de Dupla Refeição ', command=self.DuplaRefeicao_PDF)
        subMenuOpcao.add_command(label='Solicitação pra pegar a chave na portaria', command=self.ChavePortaria_PDF)
        subMenuOpcao.add_command(label='Solicitação pra acesso ao IFPI em período de férias', command=self.AcessoIFPI_PDF)
        MenuOpcao.add_cascade(label="Gerar Solicitçaões em PDF", menu=subMenuOpcao)
        MenuOpcao.add_separator()
        
        MenuOpcao.add_command(label='Sair', command=self.window.quit)
        BarraMenu.add_cascade(label='Opções', menu=MenuOpcao)

        #Menu Sobre
        menuSobre = Menu(BarraMenu, tearoff=0)
        menuSobre.add_command(label='Instagram', command=self.instagram_LIMS)
        menuSobre.add_command(label='Site Institucional', command=self.site_ifpi)
        menuSobre.add_separator()
        menuSobre.add_command(label='Sobre', command=self.tela2)
        
        BarraMenu.add_cascade(label='Ajuda', menu=menuSobre)
        self.window.config(menu=BarraMenu)
  
    def widget(self):
        self.name = Entry(self.window, width=60, bg='#dcdcdc')
        self.name.place(x=117, y=136, width=293, height=31)
        atk.tooltip(self.name, 'Insira um nome:')
        
        self.subscription = Entry(self.window, width=25, bg='#dcdcdc')
        self.subscription.place(x=152, y=178, width=258, height=31)
        atk.tooltip(self.subscription, 'Insira um matricula:')
        
        self.e_mail = Entry(self.window, width=100, bg='#dcdcdc')
        self.e_mail.place(x=106, y=221, width=305, height=31)
        atk.tooltip(self.e_mail, 'Insira um email:')
        
        self.course = Entry(self.window, width=50, bg='#dcdcdc')
        self.course.place(x=547, y=178, width=311, height=31)
        atk.tooltip(self.course, 'Insira o curso do aluno:')
        
        self.project = Entry(self.window, width=250, bg='#dcdcdc')
        self.project.place(x=559, y=221, width=299, height=31)
        atk.tooltip(self.project, 'Insira um projeto:')

        self.ListaTurno = ['Manhã', 'Tarde', 'Noite', 'Integral']
        self.ComboTurno = ttk.Combobox(window, values=self.ListaTurno)
        self.ComboTurno.set("Sem turno")
        self.ComboTurno.place(x=630, y=140, width=87, height=26)
        
    def dashboard(self):
        self.listaCli = ttk.Treeview(self.frame_dashboard,height=6, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaCli.heading("#0", text="*")
        self.listaCli.heading("#1", text="Matricula")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Email")
        self.listaCli.heading("#4", text="Disponibilidade")
        self.listaCli.heading("#5", text="Curso")
        self.listaCli.heading("#6", text="Projeto")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=100)
        self.listaCli.column("#3", width=40)
        self.listaCli.column("#4", width=5)
        self.listaCli.column("#5", width=25)
        self.listaCli.column("#6", width=100)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.97, relheight=0.8)
        self.scroll = Scrollbar(self.frame_dashboard, orient='vertical')
        self.listaCli.configure(yscroll=self.scroll.set)
        self.scroll.place(relx=0.97,rely=0.1, relwidth=0.02, relheight=0.8)
        self.listaCli.bind("<Button-1>", self.OnDoubleClick)
        
        self.montaTable()
        self.select_lista()
        
    def botoes(self):
        self.botao_enviar = PhotoImage(file="imagens\\Enviar.png")
        self.botaoEnviar = Button(self.window, bd=0, image=self.botao_enviar,
            text='Enviar',
            command=self.RegistrarUsuario)
        self.botaoEnviar.place(x=334, y=273, width=76, height=31)

        self.botao_limpar = PhotoImage(file="imagens\\Limpar.png")
        self.botaoLimpar = Button(self.window, bd=0, image=self.botao_limpar,
            text='Limpar',
            command=self.LimparTela)
        self.botaoLimpar.place(x=483, y=273, width=76, height=31)
        
        self.botao_editar = PhotoImage(file="imagens\\Editar.png")
        self.botaoEditar = Button(self.window, bd=0, image=self.botao_editar,
            text='Editar',
            command=self.alterarUsuario)
        self.botaoEditar.place(x=41, y=641, width=76, height=31)

        self.botao_excluir = PhotoImage(file="imagens\\Excluir.png")
        self.botaoExcluir = Button(self.window, bd=0, image=self.botao_excluir,
            text='Excluir',
            command=self.deleteUsuario)
        self.botaoExcluir.place(x=243, y=641, width=76, height=31)

        self.botao_Buscar = PhotoImage(file="imagens\\Buscar.png")
        self.botaoBuscar = Button(self.window, bd=0, image=self.botao_Buscar,
            text='Buscar',
            command=self.buscarUsuario)
        self.botaoBuscar.place(x=141, y=641, width=76, height=31)       
        
    def tela2(self):
        self.window2 = Toplevel()
        self.window2.title('Sobre')
        self.window2.geometry('620x220')
        self.window2.configure(bg='white')
        self.window2.maxsize(width=620, height=220)
        self.window2.minsize(width=620, height=220)
        self.window2.transient(self.window)
        self.window2.focus_force()
        self.window2.grab_set()
        self.window2.iconbitmap("imagens\\Lab.ico")
        
        #Widgets
        self.separador_h = ttk.Separator(self.window2, orient='horizontal', style="Line.TSeparator")
        self.separador_h.place(relx=0.0001, rely=0.01, relwidth=0.9999, relheight=0.005) 

        self.titulo = Label(self.window2,
            text='Cadastros do LIMS',
            font=('arial', 21, 'bold'),
            background='white')
        self.titulo.place(rely=0.1, relx=0.28)

        self.criador = Label(self.window2,
            text='Emerson Nogueira dos Santos',
            font=('arial', 8),
            background='white')
        self.criador.place(rely=0.28, relx=0.38)

        self.orientador = Label(self.window2,
            text='Orientador: prof. Me. Fernando Castelo Branco Gonçalves Santana',
            font=('arial', 8),
            background='white')
        self.orientador.place(rely=0.35, relx=0.23)

        self.dataCriacao = Label(self.window2,
            text='Dezembro de 2021',
            font=('arial', 8),
            background='white')
        self.dataCriacao.place(rely=0.42, relx=0.427)

        #Frames
        self.frame_ok = Frame(self.window2, background='#DCDCDC', bd=2, highlightbackground='black', highlightthickness=1.4)
        self.frame_ok.place(relx=0.005, rely=0.8, relwidth=0.99, relheight=0.18)
            
        #Botões
        self.botao_ok = Button(self.window2,
            text='OK',
            border=4,
            command=self.window2.destroy)
        self.botao_ok.place(relx=0.425, rely=0.83, relwidth=0.13, relheight=0.13)
         
    def login(self):
        self.tela_login = Toplevel()
        self.tela_login.title('Sobre')
        self.tela_login.geometry('490x560+170+90')
        self.tela_login.configure(bg='white')
        self.tela_login.maxsize(width=490, height=560)
        self.tela_login.minsize(width=490, height=560)
        self.tela_login.focus_force()
        self.tela_login.grab_set()
        self.tela_login.overrideredirect(True)
        self.tela_login.iconbitmap("imagens\\Lab.ico")
        
        #front-end
        self.fundo_login = PhotoImage(file="imagens\\Login.png")
        self.login_label = Label(self.tela_login, image=self.fundo_login)
        self.login_label.pack()
        
        #widgets
        self.nome_entry = Entry(self.tela_login, width=60, bg='#dcdcdc', font=('helvetica', 15))
        self.nome_entry.place(x=40, y=156, width=412, height=48)
        atk.tooltip(self.nome_entry, 'Insira seu usuário')
        
        self.email_entry = Entry(self.tela_login, width=100, bg='#dcdcdc', font=('helvetica', 15))
        self.email_entry.place(x=40, y=256, width=412, height=48)
        atk.tooltip(self.email_entry, 'Insira seu email')
        
        self.pass_entry = Entry(self.tela_login, show='*', width=100, bg='#dcdcdc', font=('helvetica', 15))
        self.pass_entry.place(x=40, y=353, width=412, height=48)
        atk.tooltip(self.pass_entry, 'Insira sua senha')
        
        #botao
        self.botao_entrar = PhotoImage(file="imagens\\Botao.png")
        self.botaoEntrar = Button(self.tela_login, bd=0, image=self.botao_entrar, command=self.Acesso)
        self.botaoEntrar.place(x=187, y=449, width=116, height=62)
         
LIMS()