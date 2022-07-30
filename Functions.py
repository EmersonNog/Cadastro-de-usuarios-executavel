from modulos import *

class func:
    def LimparTela(self):
        self.name.delete(0, END)
        self.subscription.delete(0, END)
        self.e_mail.delete(0, END)
        self.ComboTurno.delete(0, END)
        self.course.delete(0, END)
        self.project.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('usuarios.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao Banco de Dados...')

    def desconcta_bd(self):
        self.conn.close; print('Desconectando ao Banco de Dados...')

    def montaTable(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                matricula VARCHAR(20) NOT NULL PRIMARY KEY,
                nome_usuario VARCHAR(40) NOT NULL,
                email VARCHAR(50),
                turno VARCHAR(10),
                curso VARCHAR(20),
                projeto VARCHAR(30)
            );
        """)
        self.conn.commit(); print("Banco de Dados Criado.")
        self.desconcta_bd()

    def variaveis(self):
        self.matricula = self.subscription.get()
        self.nome = self.name.get()
        self.email = self.e_mail.get()
        self.disponibilidade = self.ComboTurno.get()
        self.curso = self.course.get()
        self.projeto = self.project.get()
        
    def OnDoubleClick(self, event):
        self.LimparTela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5, col6 = self.listaCli.item(n, 'values')
            self.subscription.insert(END, col1)
            self.name.insert(END, col2)
            self.e_mail.insert(END, col3)
            self.ComboTurno.insert(END, col4)
            self.course.insert(END, col5)
            self.project.insert(END, col6)
            
    def RegistrarUsuario(self):
        self.variaveis()
        if self.subscription.get() == "" or self.name.get() == "":
            msg = "Preencha os dados para registrar um novo membro!"
            messagebox.showinfo("Registro de membros - AVISO!!!", msg)
        else:
            self.conecta_bd()

            self.cursor.execute(""" INSERT INTO usuarios (matricula, nome_usuario, email, turno, curso, projeto)
                VALUES(?, ?, ?, ?, ?, ?)""", (self.matricula, self.nome, self.email, self.disponibilidade, self.curso, self.projeto))
            self.conn.commit()
            self.desconcta_bd()
            self.select_lista()
            self.LimparTela()

    def deleteUsuario(self):
        self.variaveis()
        okcancel = messagebox.askokcancel("Deseja excluir?",
                                            "Confirmar? ")
        if okcancel == False:
            print(okcancel)
        else:
            self.conecta_bd()
            self.cursor.execute("""DELETE FROM usuarios WHERE matricula = ? """, (self.matricula,))
            self.conn.commit()
            self.desconcta_bd()
            self.LimparTela()
            self.select_lista()

    def alterarUsuario(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE usuarios SET nome_usuario = ?, email = ?, turno = ?, curso = ?, projeto = ?
        WHERE matricula = ? """, (self.nome, self.email, self.disponibilidade, self.curso, self.projeto, self.matricula))
        self.conn.commit()
        self.desconcta_bd()
        self.select_lista()
        self.LimparTela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT matricula, nome_usuario, email, turno, curso, projeto FROM usuarios
            ORDER BY nome_usuario ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconcta_bd()

    def buscarUsuario(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.name.insert(END, '%')
        nome = self.name.get()
        self.cursor.execute(""" SELECT matricula, nome_usuario, email, turno, curso, projeto FROM usuarios
            WHERE nome_usuario LIKE '%s' ORDER BY nome_usuario ASC""" % nome)
        buscaNomeUsu = self.cursor.fetchall()
        for i in buscaNomeUsu:
            self.listaCli.insert("", END, values=i)
        self.LimparTela()
        self.desconcta_bd()

    def site_ifpi(*args):
        webbrowser.open_new("http://lims.ifpi.edu.br/")
    
    def instagram_LIMS(*args):
        webbrowser.open_new_tab("https://www.instagram.com/ifpi.lims/?hl=pt")
        
    def Acesso(self):
        self.nome_login = self.nome_entry.get()
        self.email_login = self.email_entry.get()
        self.senha_login = self.pass_entry.get()
        
        if self.nome_login == '1' and self.email_login == '1' and self.senha_login == '1':
            mensagem_sucess = 'Login Realizado Com Sucesso!'
            messagebox.showinfo("Bem-vindo", mensagem_sucess)
            self.tela_login.destroy()
        else:
            mensagem_fail = 'Dados invalidos, tente navamente!'
            messagebox.showerror("Login - AVISO!!!", mensagem_fail)