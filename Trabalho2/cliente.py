from peewee import *
from pessoa import Pessoa

arq = 'cliente.db'
db = SqliteDatabase(arq)

class Cliente(Model):
    cliente = ForeignKeyField(Pessoa)

    class Meta:
        database = db
    
    def __str__(self):
        return self.cliente

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Cliente])  # solicitar a criação das tabelas
