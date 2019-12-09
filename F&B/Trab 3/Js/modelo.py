from peewee import *
import os

arq = 'C:/Python/Python_IFC/F&B/Trab 3/back/BDtrab03.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):
    garrafa = CharField()
    nomProduto = CharField()
    descProduto = CharField()
