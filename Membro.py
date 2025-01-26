from Livro import *

class Membro:
# A classe Membro deve conter atributos como nome,
# número do membro e histórico de livros emprestados.
    def __init__(self, nome:str, numeroMembro:str):
        self.__nome = nome
        self.__numeroMembro = numeroMembro
        self.__historicoDeLivros = []

    #getters
    def get_nome(self)->str:
        return self.__nome
    def get_numeroMembro(self)->str:
        return self.__numeroMembro

    #setters
    def set_nome(self, nome)->None:
        self.__nome = nome
    def set_numeroMembro(self, numeroMembro)->None:
        self.__numeroMembro = numeroMembro

    def addLivroEmprestado(self, livro:Livro)->None:
        self.__historicoDeLivros.append(livro)
    def exibirLivrosEmprestados(self)->str:
        livros = ""
        for i,livro in enumerate(self.__historicoDeLivros):
            livros += (f'{i} - {livro.get_titulo()}; ')
        return livros
    def exibriIdUltimoLivro(self)->int:
        livros = self.__historicoDeLivros
        try:
            return livros[len(livros)-1].get_id()
        except:
            return ''

    def limparHistoricoLivros(self)->None:
        self.__historicoDeLivros.clear()

    def __str__(self): 
        return f"Nome: {self.get_nome()}, Número de Membro: {self.get_numeroMembro()}, Histórico de Empréstimos: {', '.join([livro.get_titulo() for livro in self.__historicoDeLivros])}"