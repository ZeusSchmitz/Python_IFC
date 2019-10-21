from peewee import *
from produto import Produto
from cliente import Cliente

arq = 'pedido.db'
db = SqliteDatabase(arq)

class Pedido(Model):
    produto = ForeignKeyField(Produto)
    cliente = ForeignKeyField(Cliente)
    qtdProd = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.produto + '' + self.cliente + '' + self.qtdProd

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pedido])  # solicitar a criação das tabelas
