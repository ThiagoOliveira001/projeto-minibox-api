from Banco import Banco
from Cliente import Cliente
from Funcionario import Funcionario
from Produto import Produto

class Main():
    def __init__(self):
        self.__con = Banco('localhost','minibox','postgres','1234')
    
    def cadastrarProduto(self, produto):
        p = Produto(produto['nome'], produto['descricao'], produto['preco'], produto['tipo'])
        self.__con.inserir(f"insert into mercado.produto(nome, descricao, preco, tipo) values('{p.nome}','{p.descricao}',{p.preco},'{p.tipo}');")