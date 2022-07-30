from modulos import *
from Functions import func

class PDF(FPDF):
    def print_DuplaRefeicao(self):
        webbrowser.open(f'Solicitacoes\\Dupla Refeiçao - {self.identificador}.pdf')

    def print_ChavePortaria(self):
        webbrowser.open(f'Solicitacoes\\Chave da Portaria - {self.identificador}.pdf')

    def print_AcessoIFPI(self):
        webbrowser.open(f'Solicitacoes\\Acesso ao IFPI - {self.identificador}.pdf')

    def DuplaRefeicao_PDF(self):
        self.variaveis()
        self.identificador = str(random.randrange(0,100000))

        self.pdf = PDF(orientation='P', unit='mm', format='A4')
        self.pdf.add_page()
        self.pdf.image("imagens\\Ministerio.png", 74, 2, 60)
        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(70, 30)
        self.pdf.multi_cell(65, 10, 'MINISTÉRIO DA EDUCAÇÃO ', 0, "C", False)
        self.pdf.set_xy(53, 35)
        self.pdf.multi_cell(100, 10, 'Secretaria de Educação Profissional e Tecnológica', 0, "C", False)
        self.pdf.set_font('Arial','B',10)
        self.pdf.set_xy(46, 40)
        self.pdf.multi_cell(115, 10, 'Instituto Federal de Educação, Ciência e Tecnologia do Piauí', 0, "C", False)
        
        self.pdf.set_font('Arial','',10.5)
        self.pdf.cell(40,10, f'Nome: {self.nome}', 0, 2)
        self.pdf.cell(40,10, f'Matricula: {self.matricula}', 0, 2)
        self.pdf.cell(40,10, f'Email: {self.email}', 0, 2)
        self.pdf.cell(40,10, f'Disponibilidade: {self.disponibilidade}', 0, 2)
        self.pdf.cell(40,10, f'Curso: {self.curso}', 0, 2)
        self.pdf.cell(40,10, f'Projeto: {self.projeto}', 0, 2)

        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(15, 210)
        self.pdf.multi_cell(65, 10, 'Atenciosamente,', 0, "C", False)

        self.pdf.set_xy(15, 220)
        self.pdf.multi_cell(0,10, 'NOME DO SIGNATÁRIO: _________________________________________', 0, 'C', False)

        self.pdf.set_xy(15, 228)
        self.pdf.multi_cell(0,10, 'Cargo do Signatário: _____________________________________________', 0, 'C', False)

        self.pdf.image("imagens\\Roda-pe.png", 30, 270, 155)

        self.pdf.output(f'Solicitacoes\\Dupla Refeiçao - {self.identificador}.pdf', 'F')
        
        self.print_DuplaRefeicao()

    def ChavePortaria_PDF(self):
        self.variaveis()
        self.identificador = str(random.randrange(0,100000))

        self.pdf = PDF(orientation='P', unit='mm', format='A4')
        self.pdf.add_page()
        self.pdf.image("imagens\\Ministerio.png", 74, 2, 60)
        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(70, 30)
        self.pdf.multi_cell(65, 10, 'MINISTÉRIO DA EDUCAÇÃO ', 0, "C", False)
        self.pdf.set_xy(53, 35)
        self.pdf.multi_cell(100, 10, 'Secretaria de Educação Profissional e Tecnológica', 0, "C", False)
        self.pdf.set_font('Arial','B',10)
        self.pdf.set_xy(46, 40)
        self.pdf.multi_cell(115, 10, 'Instituto Federal de Educação, Ciência e Tecnologia do Piauí', 0, "C", False)
        
        self.pdf.set_font('Arial','',10.5)
        self.pdf.cell(40,10, f'Aluno: {self.nome} está apto a ter acesso a chave do Laboratorio', 0, 2)

        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(15, 210)
        self.pdf.multi_cell(65, 10, 'Atenciosamente,', 0, "C", False)

        self.pdf.set_xy(15, 220)
        self.pdf.multi_cell(0,10, 'NOME DO SIGNATÁRIO: _________________________________________', 0, 'C', False)

        self.pdf.set_xy(15, 228)
        self.pdf.multi_cell(0,10, 'Cargo do Signatário: _____________________________________________', 0, 'C', False)

        self.pdf.image("imagens\\Roda-pe.png", 30, 270, 155)
        self.pdf.output(f'Solicitacoes\\Chave da Portaria - {self.identificador}.pdf', 'F')

        self.print_ChavePortaria()

    def AcessoIFPI_PDF(self):
        self.variaveis()
        self.identificador = str(random.randrange(0,100000))

        self.pdf = PDF(orientation='P', unit='mm', format='A4')
        self.pdf.add_page()
        self.pdf.image("imagens\\Ministerio.png", 74, 2, 60)
        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(70, 30)
        self.pdf.multi_cell(65, 10, 'MINISTÉRIO DA EDUCAÇÃO ', 0, "C", False)
        self.pdf.set_xy(53, 35)
        self.pdf.multi_cell(100, 10, 'Secretaria de Educação Profissional e Tecnológica', 0, "C", False)
        self.pdf.set_font('Arial','B',10)
        self.pdf.set_xy(46, 40)
        self.pdf.multi_cell(115, 10, 'Instituto Federal de Educação, Ciência e Tecnologia do Piauí', 0, "C", False)
        
        self.pdf.set_font('Arial','',10.5)
        self.pdf.cell(40,10, f'Nome: {self.nome}', 0, 2)
        self.pdf.cell(40,10, f'Matricula: {self.matricula}', 0, 2)
        self.pdf.cell(40,10, f'Email: {self.email}', 0, 2)
        self.pdf.cell(40,10, f'Curso: {self.curso}', 0, 2)
        self.pdf.cell(40,10, f'Projeto: {self.projeto}', 0, 2)

        self.pdf.set_font('Arial','',10)
        self.pdf.set_xy(15, 210)
        self.pdf.multi_cell(65, 10, 'Atenciosamente,', 0, "C", False)

        self.pdf.set_xy(15, 220)
        self.pdf.multi_cell(0,10, 'NOME DO SIGNATÁRIO: _________________________________________', 0, 'C', False)

        self.pdf.set_xy(15, 228)
        self.pdf.multi_cell(0,10, 'Cargo do Signatário: _____________________________________________', 0, 'C', False)

        self.pdf.image("imagens\\Roda-pe.png", 30, 270, 155)
        self.pdf.output(f'Solicitacoes\\Acesso ao IFPI - {self.identificador}.pdf', 'F')

        self.print_AcessoIFPI()