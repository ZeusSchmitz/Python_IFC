from peewee import *
from produto import Produto
from cliente import Cliente
from baseModel import *
import os

class Pedido(BaseModel):
    cliente = ForeignKeyField(Cliente)
    produto = ForeignKeyField(Produto)
    qtdProd = CharField()

    def __str__(self):
        return str(self.cliente) + ' Quantidade: ' + self.qtdProd

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pedido, Cliente, Produto])  # solicitar a criação das tabelas

    c1 = Cliente.create(nome="Joao", cpf= '1456856636', email= 'oh_zec')
    c2 = Cliente.select().where(Cliente.cpf == '1456856636')
    
    prod = Produto.create(garrafa = 'Padrão', nomProduto = 'Cachaca Dupipe', descProduto = 'Cachaça branca')
    prodS = Produto.select().where(Produto.id == 1)

    ped = Pedido.create(cliente= c2[0], produto= prodS[0], qtdProd= '3')
    print(ped)