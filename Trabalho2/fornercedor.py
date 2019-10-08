from peewee import *
from pessoa import Pessoa

arq = 'fornecedor.db'
db = SqliteDatabase(arq)

class Fornecedor(Model):
    fornec = ForeignKeyField(Pessoa)
    produto = CharField()