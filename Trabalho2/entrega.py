from peewee import *
from pedido import Pedido

arq = 'entrega.db'
db = SqliteDatabase(arq)

class Entrega(Model):
    pedido = ForeignKeyField(Pedido)
    numRast = CharField()