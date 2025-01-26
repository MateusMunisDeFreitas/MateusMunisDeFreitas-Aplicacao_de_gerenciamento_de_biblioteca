# Criar uma aplicação de gerenciamento de biblioteca com
# classes e POO para representar livros, membros e a biblioteca.
#
# Passos do projeto:
#
# Criação de Classes:
# Crie as seguintes classes: Livro, Membro, Biblioteca.
#
# Classe Livro:
# A classe Livro deve conter atributos como título, autor, ID,
# status de empréstimo (disponível ou emprestado).
#
# Classe Membro:
#
# A classe Membro deve conter atributos como nome,
# número do membro e histórico de livros emprestados.
#
# Classe Biblioteca:
#
# A classe Biblioteca deve conter um catálogo de livros
# disponíveis, um registro de membros e métodos para
# empréstimo, devolução e pesquisa de livros.
#
# PROJETO
#
# Operações da Biblioteca:
#
# Implemente métodos na classe Biblioteca para:
#
# Adicionar livros ao catálogo.
# Adicionar membros à biblioteca.
# Permitir empréstimo de livros por
# membros.
# Registrar a devolução de livros.
# Pesquisar livros por título, autor ou ID.

from livros_membros import *
from Livro import *
from Membro import *
from Biblioteca import *
from tkinter import *
from tkinter import ttk

biblioteca = Biblioteca(listaDeLivros, listaMembros)

# Inicialização da janela principal
root = Tk()
root.title("Gerenciamento de biblioteca")
root.geometry("500x200+500+200")
root.resizable(False,False)

# Criação das abas
notebook = ttk.Notebook(root)
notebook.place(x=0, y=0, width=500, height=200)
#biblioteca
abaBiblioteca = Frame(notebook)
notebook.add(abaBiblioteca, text="Biblioteca")
#membro
abaMembro = Frame(notebook)
notebook.add(abaMembro, text="Membro")
#livro
abaLivro = Frame(notebook)
notebook.add(abaLivro, text="Livro")

# Aba biblioteca
labelLivro = Label(abaBiblioteca, text="LIVRO: ", font=("Arial", 14))
labelLivro.place(x=20, y=4)
inputLivro = Entry(abaBiblioteca, width=20, font=("Arial", 12))
inputLivro.place(x=110, y=6)
labelMembro = Label(abaBiblioteca, text="MEMBRO: ", font=("Arial", 14))
labelMembro.place(x=10, y=40)
inputMembro = Entry(abaBiblioteca, width=20, font=("Arial", 12))
inputMembro.place(x=110, y=42)
butonEmprestimo = Button(abaBiblioteca, text="Emprestimo", command=lambda: emprestimo(), font=("Arial", 12))
butonEmprestimo.place(x=300, y=4)
butonDevolucao = Button(abaBiblioteca, text="Devolução", command=lambda: devolver(), font=("Arial", 12))
butonDevolucao.place(x=304, y=40)
butonExibirLivros = Button(abaBiblioteca, text="Exibir livros", command=lambda : exibirLivros(), font=("Arial", 12))
butonExibirLivros.place(x=150, y=70)

# Aba Membro
labelMembro = Label(abaMembro, text="NOME MEMBRO: ", font=("Arial", 14))
labelMembro.place(x=10, y=4)
inputAbaMembro = Entry(abaMembro, width=20, font=("Arial", 12))
inputAbaMembro.place(x=250, y=6)
labelNumeroMembro = Label(abaMembro, text="NUMERO CADASTRO: ", font=("Arial", 14))
labelNumeroMembro.place(x=10, y=40)
inputAbaNumMembro = Entry(abaMembro, width=20, font=("Arial", 12))
inputAbaNumMembro.place(x=250, y=42)
butonCadastrar = Button(abaMembro, text="Cadastrar", command=lambda: cadastrarMembro(), font=("Arial", 12))
butonCadastrar.place(x=250, y=70)
butonExcluir = Button(abaMembro, text="Excluir", command=lambda: excluirMembro(), font=("Arial", 12))
butonExcluir.place(x=350, y=70)
butonExibirMembros = Button(abaMembro, text="Exibir membros", command=lambda: exibirMembros(), font=("Arial", 12))
butonExibirMembros.place(x=30, y=100)

# Aba Livros
labelTitulo = Label(abaLivro, text="TITULO*: ", font=("Arial", 14))
labelTitulo.place(x=10, y=4)
inputTitulo = Entry(abaLivro, font=("Arial", 12))
inputTitulo.place(x=110, y=6)
labelAutor = Label(abaLivro, text="AUTOR: ", font=("Arial", 14))
labelAutor.place(x=10, y=35)
inputAutor = Entry(abaLivro, font=("Arial", 12))
inputAutor.place(x=110, y=33)
labelID = Label(abaLivro, text="ID*: ", font=("Arial", 14))
labelID.place(x=30, y=66)
inputID = Entry(abaLivro, font=("Arial", 12))
inputID.place(x=110, y=64)
labelInformacao = Label(abaLivro, text="(*)Campos obrigatorio para exclisão\nde livros")
labelInformacao.place(x=300, y=120)
labelPesquisar = Label(abaLivro, text="Pesquisar por:", font=("Verdana",10))
labelPesquisar.place(x=350, y=5)
pesquisar = IntVar()
butonRadioTitulo = Radiobutton(abaLivro, text="Titulo", variable=pesquisar, value=1)
butonRadioTitulo.place(x=350, y=28)
butonRadioAutor = Radiobutton(abaLivro, text="Autor", variable=pesquisar, value=2)
butonRadioAutor.place(x=350, y=48)
butonRadioID = Radiobutton(abaLivro, text="ID", variable=pesquisar, value=3)
butonRadioID.place(x=350, y=68)
butonPesquisar = Button(abaLivro, text="Pesquisar", command=lambda: pesquisaLivros())
butonPesquisar.place(x=350, y=88)
butonCadastraLivro = Button(abaLivro, text="Cadastrar", command=lambda: addLivros(), font=("Arial", 12))
butonCadastraLivro.place(x=110, y=90)
butonExcluirLivro = Button(abaLivro, text="Excluir",command=lambda: excluirLivros(), font=("Arial", 12))
butonExcluirLivro.place(x=235, y=90)
butonExibirLivros = Button(abaLivro, text="Exibir livros", command=lambda: exibirLivros(), font=("Arial", 12))
butonExibirLivros.place(x=150, y=130)

# -------------------- Functions -------------------------------

# functions abaBiblioteca
def exibirLivros()->None:
    modal = Tk()
    modal.geometry("800x200+300+200")
    modal.title("Catalogo de livros")
    caixaTexto = Text(modal, width=70, height=7, wrap="word", font=("",14))
    caixaTexto.pack()

    for i,livro in enumerate(biblioteca.get_catalogoLivros()):
        print(i," ",livro)
    print("\n")

    for i,livro in enumerate(biblioteca.get_catalogoLivros()):
        caixaTexto.insert(END, f"{i} - Titulo: {livro.get_titulo()}, Autor: {livro.get_autor()}, ID: {livro.get_id()}, Status emprestimo: {livro.get_status_emprestimo()}\n")

    butonFechar = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def emprestimo()->None:
    menssage = ''
    if inputMembro.get() != '' and inputLivro.get() != '':
        menssage = biblioteca.emprestimoDeLivro(inputMembro.get(), inputLivro.get())
    else:
        menssage = "Campo membro ou livro vazio!"

    inputLivro.delete(0, END)
    inputMembro.delete(0, END)

    modal =Tk()
    modal.title("Biblioteca")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def devolver()->None:
    menssage = ''
    if inputMembro.get() != '' and inputLivro.get() != '':
        menssage = biblioteca.devolverLivro(inputMembro.get(), inputLivro.get())
    else:
        menssage = "Campo membro ou livro vazio!"

    inputLivro.delete(0, END)
    inputMembro.delete(0, END)

    modal =Tk()
    modal.title("Biblioteca")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

#   function abaMembro
def exibirMembros()->None:
    modal = Tk()
    modal.geometry("800x200+300+200")
    modal.title("Membros cadastrados")
    caixaTexto = Text(modal, width=70, height=6, wrap="word", font=("",14))
    caixaTexto.pack()

    for i,membro in enumerate(biblioteca.get_membros()):
        caixaTexto.insert(END, f"{i} - Nome: {membro.get_nome()}, Numero membro: {membro.get_numeroMembro()}, Historico de livros: {membro.exibirLivrosEmprestados()}\n")
    butonFechar = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def cadastrarMembro()->None:
    menssage = ''
    if inputAbaMembro.get() != '' and inputAbaNumMembro.get() != '':
        menssage = biblioteca.addMembroBiblioteca(inputAbaMembro.get(),inputAbaNumMembro.get())
    else:
        menssage = "Campos membro ou Numero cadastro vazio!"

    inputAbaMembro.delete(0, END)
    inputAbaNumMembro.delete(0, END)

    modal =Tk()
    modal.title("Membro")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def excluirMembro()->None:
    menssage = ''
    if inputAbaMembro.get() != '' and inputAbaNumMembro.get() != '':
        menssage = biblioteca.excluirMembroBiblioteca(inputAbaMembro.get(),inputAbaNumMembro.get())
    else:
        menssage = "Campos membro ou Numero cadastro vazio!"

    inputAbaMembro.delete(0, END)
    inputAbaNumMembro.delete(0, END)

    modal =Tk()
    modal.title("Membro")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

# functions abaLivro
def addLivros()->None:
    menssage = ''
    if inputTitulo.get() != '' and inputAutor.get() != '' and inputID.get() != '':
        menssage = biblioteca.addLivroAoCatalogo(inputTitulo.get(), inputAutor.get(), inputID.get())
    else:
        menssage = "Campos titulo, autor ou ID vazio!"

    inputTitulo.delete(0, END)
    inputAutor.delete(0, END)
    inputID.delete(0, END)

    modal =Tk()
    modal.title("Livro")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def excluirLivros()->None:
    menssage = ''
    if inputTitulo.get() and inputID.get() != '':
        menssage = biblioteca.excluirLivroCatalogo(inputTitulo.get(), inputID.get())
    else:
        menssage = "Campos titulo ou ID vazio!"

    inputTitulo.delete(0, END)
    inputID.delete(0, END)

    modal =Tk()
    modal.title("Livro")
    modal.geometry("300x50+550+300")
    labelMenssagem = Label(modal, text=menssage, font=("Arial",11)).pack()
    buton = Button(modal, text="Fechar", command=lambda : modal.destroy()).pack()

def pesquisaLivros():
    def pesquisarFuncao():
        modal1 = Tk()
        modal1.geometry("800x200+300+200")
        modal1.title("Catalogo de livros")
        if pesquisar.get() == 1:
            if inputTitulo.get() != '':
                livros = biblioteca.pesquisarLivroTitulo(inputTitulo.get())
                caixaTexto = Text(modal1, width=70, height=4, wrap="word", font=("",14))
                caixaTexto.pack()
                buton = Button(modal1, text="Fechar", command=lambda : modal1.destroy()).pack()

                for i,livro in enumerate(livros):
                    caixaTexto.insert(END, f"{i} - Titulo: {livro.get_titulo()}, Autor: {livro.get_autor()}, ID: {livro.get_id()}, Status emprestimo: {livro.get_status_emprestimo()}\n")
            else:
                label = Label(modal1, text="Livro não encontrado!", font=("",12)).pack()
        elif pesquisar.get() == 2:
            if inputAutor.get() != '':
                livros = biblioteca.pesquisarLivroAutor(inputTitulo.get())
                caixaTexto = Text(modal1, width=70, height=4, wrap="word", font=("",14))
                caixaTexto.pack()
                for i,livro in enumerate(livros):
                    caixaTexto.insert(END, f"{i} - Titulo: {livro.get_titulo()}, Autor: {livro.get_autor()}, ID: {livro.get_id()}, Status emprestimo: {livro.get_status_emprestimo()}\n")
            else:
                label = Label(modal1, text="Livro não encontrado!", font=("",12)).pack()
        if pesquisar.get() == 3:
            if inputID.get() != '':
                livros = biblioteca.pesquisarLivroID(inputTitulo.get())
                caixaTexto = Text(modal1, width=70, height=4, wrap="word", font=("",14))
                caixaTexto.pack()
                for i,livro in enumerate(livros):
                    caixaTexto.insert(END, f"{i} - Titulo: {livro.get_titulo()}, Autor: {livro.get_autor()}, ID: {livro.get_id()}, Status emprestimo: {livro.get_status_emprestimo()}\n")
            else:
                label = Label(modal1, text="Livro não encontrado!", font=("",12)).pack()
    if pesquisar.get() != 0:
        pesquisarFuncao()
    else:
        modal = Tk()
        modal.geometry("300x50+550+300")
        modal.title("Catalogo de livros")
        label = Label(modal, text="Selecione o tipo de pesquisar!", font=("",12))
        label.pack()
root.mainloop()
