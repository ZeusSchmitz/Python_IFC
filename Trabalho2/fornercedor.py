from peewee import *
from pessoa import Pessoa

arq = 'fornecedor.db'
db = SqliteDatabase(arq)

class Fornecedor(Model):
    fornec = ForeignKeyField(Pessoa)
    produto = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.fornec + '' + self.produto

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Fornecedor])  # solicitar a criação das tabelas
