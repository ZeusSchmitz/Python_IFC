from peewee import *

arq = 'endereco.db'
db = SqliteDatabase(arq)

class Endereco(Model):
    rua = CharField()
    numero = CharField()
    logradouro = CharField()
    cidade = CharField()
    estado = CharField()