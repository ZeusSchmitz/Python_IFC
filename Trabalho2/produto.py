from peewee import *

arq = 'produto.db'
db = SqliteDatabase(arq)

class Produto(Model):
    pass