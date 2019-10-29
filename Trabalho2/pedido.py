from peewee import *
from produto import Produto
from cliente import Cliente
from endereco import Endereco
from telefone import Telefone
import os

arq = 'pedido.db'
db = SqliteDatabase(arq)

class Pedido(Model):
    produtos = ManyToManyField(Produto)
    cliente = ForeignKeyField(Cliente)
    qtdProd = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return str(self.cliente) + ' Quantidade: ' + self.qtdProd

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pedido, Cliente, Produto, Telefone, Endereco, Pedido.produtos.get_through_model()])  # solicitar a criação das tabelas

    tel = Telefone.create(ddd= '47', numero= '458774269')
    end = Endereco.create(rua= 'Bonifacio', numero= '7999', logradouro= 'Casa', cidade= 'Gaspar', estado= 'SC')
    c1 = Cliente.create(nome="Joao", sobrenome='Silva', dtNasc= '03/09/1987', sexo= 'M', senha= '1234', email= 'oh_zec', telefone= tel, endereco= end)

    ped = Pedido.create(cliente= c1, qtdProd= '3')
    prod1 = Produto.create(garrafa = 'Padrão', nomProduto = 'Cachaca Dupipe', descProduto = 'Cachaça envelhecida')
    prod2 = Produto.create(garrafa = 'Padrão', nomProduto = 'Cachaca Dupipe', descProduto = 'Cachaça branca')

    ped.produtos.add([prod1, prod2])
    print(ped)

    print("lista de produtos: ")
    for produto in ped.produtos:
        print(produto.descProduto)
    
    print("---------------------------")
    todos = Pedido.select()
    for pedido in todos:
        print("Cliente: "+pedido.cliente.nome)
        for prod in pedido.produtos:
            print(prod.descProduto)

