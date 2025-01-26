from tkinter import *
from tkinter import ttk
# Inicialização da janela principal
root = Tk()
root.title("Gerenciamento de biblioteca")
root.geometry("500x200+500+200")

# Criação das abas
notebook = ttk.Notebook(root)
notebook.place(x=0, y=0, width=300, height=200)
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
labelLivro.place(x=10, y=4)
inputLivro = Entry(abaBiblioteca, width=20, font=("Arial", 12))
inputLivro.place(x=100, y=4)


root.mainloop()