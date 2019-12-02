from peewee import *

arq = 'C:/Python/Python_IFC/F&B/Trab 3/back/BDtrab03.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db