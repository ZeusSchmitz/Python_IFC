from peewee import *
from pessoa import Pessoa

arq = 'funcionario.db'
db = SqliteDatabase(arq)

class Funcionario(Model):
    func = ForeignKeyField(Pessoa)
    setor = CharField()