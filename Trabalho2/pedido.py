from peewee import *

arq = 'pedido.db'
db = SqliteDatabase(arq)

class Pedido(Model):
    pass