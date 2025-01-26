class Livro:
# A classe Livro deve conter atributos como título, autor, ID,
# status de empréstimo (disponível ou emprestado).
    def __init__(self, titulo:str, autor:str, ID:str):
        self.__titulo = titulo.lower()
        self.__autor = autor.lower()
        self.__ID = ID
        self.__statusEmprestimo = 'disponivel'

    # getters
    def get_titulo(self)->str:
        return self.__titulo
    def get_autor(self)->str:
        return self.__autor
    def get_id(self)->str:
        return self.__ID
    def get_status_emprestimo(self)->str:
        return self.__statusEmprestimo

    # setters
    def set_titulo(self, titulo:str)->None:
        self.__titulo = titulo.lower()
    def set_autor(self, autor:str)->None:
        self.__autor = autor.lower()
    def set_id(self, id:str)->None:
        self.__ID = id

    def pegarEmprestado(self)->None:
        self.__statusEmprestimo = 'emprestado'
    def devolver(self)->None:
        self.__statusEmprestimo = 'disponivel'

    def __str__(self):
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, ID: {self.get_id()}, Status: {self.get_status_emprestimo()}"