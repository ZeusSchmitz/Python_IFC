from peewee import *

arq = 'BDtrab03.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db