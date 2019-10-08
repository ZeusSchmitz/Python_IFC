from peewee import *
from pessoa import Pessoa

arq = 'cliente.db'
db = SqliteDatabase(arq)

class Cleinte(Model):
    cliente = ForeignKeyField(Pessoa)    