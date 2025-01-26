from Livro import *
from Membro import *

class Biblioteca:
# A classe Biblioteca deve conter um catálogo de livros
# disponíveis, um registro de membros e métodos para
# empréstimo, devolução e pesquisa de livros.

# Implemente métodos na classe Biblioteca para:
#
# Adicionar livros ao catálogo.
# Adicionar membros à biblioteca.
# Permitir empréstimo de livros por
# membros.
# Registrar a devolução de livros.
# Pesquisar livros por título, autor ou ID.
    def __init__(self, catalogoLivros:list, membros:list):
        self.__catalogoLivros = catalogoLivros
        self.__membros = membros

    # getters
    def get_catalogoLivros(self)->list:
        return self.__catalogoLivros
    def get_membros(self)->list:
        return self.__membros

    def addLivroAoCatalogo(self, titulo:str, autor:str, id:str)->str:
        livroJaExiste = False
        autorJaExiste = False
        idJaExiste = False
        indiceLirvo = -1
        for livroCadastrado in self.get_catalogoLivros():
            if id == livroCadastrado.get_id():  
                idJaExiste = True    

        if livroJaExiste == True: return 'Nome já cadastrado!'
        if idJaExiste == True: return 'ID já cadastrado!'
                
        if idJaExiste == False: 
            self.__catalogoLivros.append(Livro(titulo, autor, id))
            return 'Livro adcionado com sucesso!'
    
    def excluirLivroCatalogo(self,titulo:str, id:str)->str:
        tituloJaExiste = False
        idJaExiste = False
        indiceLivro = -1
        for i,livroCadastrado in enumerate(self.get_catalogoLivros()):
            if titulo.lower() == livroCadastrado.get_titulo().lower():  
                tituloJaExiste = True 
                if id == livroCadastrado.get_id():
                    idJaExiste = True
                    indiceLivro = i   

        if tituloJaExiste == False: return 'Titulo do livro não cadastrado!'
        if idJaExiste == False: return 'ID do livro incorreto!'
                
        if tituloJaExiste == True and idJaExiste == True: 
            self.__catalogoLivros[indiceLivro] = ''
            self.__catalogoLivros.remove('')
            return 'Livro excluido com sucesso!'

    def addMembroBiblioteca(self, membro:str, numero:str)->str:
        membroJaExiste = False
        numeroJaExiste = False
        for membroCadastrado in self.get_membros():
            if membro.lower() == membroCadastrado.get_nome().lower():  
                membroJaExiste = True    
            if numero == membroCadastrado.get_numeroMembro():
                numeroJaExiste = True

        if membroJaExiste == True: return 'Nome já cadastrado!'
        if numeroJaExiste == True: return 'Numero membro já cadastrado!'
                
        if membroJaExiste == False and numeroJaExiste == False: 
            self.__membros.append(Membro(membro, numero))
            return 'Membro adcionado com sucesso!'
    
    def excluirMembroBiblioteca(self, membro:str, numero:str)->str:
        membroJaExiste = False
        numeroJaExiste = False
        indiceMembro = -1
        for i,membroCadastrado in enumerate(self.get_membros()):
            if membro.lower() == membroCadastrado.get_nome().lower():  
                membroJaExiste = True 
                if numero == membroCadastrado.get_numeroMembro():
                    numeroJaExiste = True
                    indiceMembro = i   

        if membroJaExiste == False: return 'Nome não cadastrado!'
        if numeroJaExiste == False: return 'Numero membro incorreto!'
                
        if membroJaExiste == True and numeroJaExiste == True: 
            self.__membros[indiceMembro] = ''
            self.__membros.remove('')
            return 'Membro excluido com sucesso!'

    def atulizarCatalogoLivros(self, livros:list)->str:
        self.__catalogoLivros = livros
        return 'Catalogo de livros atualizada!'

    def emprestimoDeLivro(self, membro:str, nomeLivroEmprestimo:str)->str:
        membroCadstrado = ''
        indiceMembro = -1
        livroDisponivel = ''
        indiceLivro = -1
        statuslivroDisponivel = False

        #verifica se o nome membro esta cadastrado na biblioteca
        for i, mb in enumerate(self.get_membros()):
            if mb.get_nome().lower() == membro.lower():
                membroCadstrado = mb
                indiceMembro = i
        if membroCadstrado == '': return 'Membro não cadastrado na biblioteca!'


        # verificar se ha o livro requisitado e se esta disponivel para emprestimo
        for i, livro in enumerate(self.get_catalogoLivros()):
            if nomeLivroEmprestimo.lower() == livro.get_titulo().lower():
                livroDisponivel = livro
                indiceLivro = i
                print("indice: ",i)
                if livro.get_status_emprestimo() == 'disponivel':
                    statuslivroDisponivel = True
                    break
        if livroDisponivel == '': return 'Livro não existe no catalogo!'
        if statuslivroDisponivel == False: 
            return 'Livro não disponivel!'
        else:
            livroDisponivel.pegarEmprestado()
            membroCadstrado.addLivroEmprestado(livroDisponivel)
            self.__catalogoLivros[indiceLivro] = livroDisponivel
            self.__membros[indiceMembro] = membroCadstrado
            return 'Livro emprestado com sucesso!'
            
    
    def devolverLivro(self, membro:str, livroDevolver:str)->str:
        membroCadstrado = ''
        livroEmprestado = ''
        idLivro = ''
        indiceLivro = -1
        statuslivroEmprestado = False

        #verifica se o nome membro esta cadastrado na biblioteca
        for mb in self.get_membros():
            if mb.get_nome().lower() == membro.lower():
                membroCadstrado = mb
                idLivro = mb.exibriIdUltimoLivro()

        if membroCadstrado == '': return 'Membro não cadastrado na biblioteca!' 

        # verificar se ha o livro constar no catalogo e se estar emprestado
        for i,livro in enumerate(self.get_catalogoLivros()):
            if livroDevolver.lower() == livro.get_titulo().lower():
                livroEmprestado = livro
                indiceLivro = i
                if livro.get_status_emprestimo() == 'emprestado' and livro.get_id() == idLivro:
                    statuslivroEmprestado = True
                    break

        if livroEmprestado == '': return 'Livro não existe no catalogo!'
        if statuslivroEmprestado == False: 
            return 'Livro não se encontrar em emprestimo!'
        else:
            livroEmprestado.devolver()
            self.__catalogoLivros[indiceLivro] = livroEmprestado
            return 'Livro devolvido com sucesso!'
    
    # Pesquisar livros por título, autor ou ID.
    def pesquisarLivroTitulo(self, titulo:str)->Livro:
        livroDisponivel = []
        for livro in self.get_catalogoLivros():
            if titulo.lower() == livro.get_titulo().lower():
                livroDisponivel.append(livro)
        
        if livroDisponivel != '':
            return livroDisponivel
        else:
            return 'Livro não existe no catalogo!'
            
    def pesquisarLivroAutor(self, autor:str)->Livro:
        livroDisponivel = []
        for livro in self.get_catalogoLivros():
            if autor.lower() == livro.get_autor().lower():
                livroDisponivel.append(livro)
        
        if livroDisponivel != '':
            return livroDisponivel
        else:
            return 'Livro não existe no catalogo!'
            
    def pesquisarLivroID(self, ID:str)->Livro:
        livroDisponivel = []
        for livro in self.get_catalogoLivros():
            if ID.lower() == livro.get_id().lower():
                livroDisponivel.append(livro)
        
        if livroDisponivel != '':
            return livroDisponivel
        else:
            return 'Livro não existe no catalogo!'
