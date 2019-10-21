from peewee import *
from pedido import Pedido

arq = 'reclame.db'
db = SqliteDatabase(arq)

class Reclame(Model):
    pedido = ForeignKeyField(Pedido)
    motivo = CharField()
    dtRec = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.pedido + '' + self.motivo + '' + self.dtRec

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Reclame])  # solicitar a criação das tabelas
