from peewee import *
from pedido import Pedido

arq = 'entrega.db'
db = SqliteDatabase(arq)

class Entrega(Model):
    pedido = ForeignKeyField(Pedido)
    numRast = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.pedido + '' + self.numRast + '' + self.descProduto

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Entrega])  # solicitar a criação das tabelas
