from peewee import *
from pedido import Pedido

class Reclame(Model):
    pedido = ForeignKeyField(Pedido)
    motivo = CharField()
    dtRec = CharField()