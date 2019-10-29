from peewee import *

arq = 'BDtrabalho02.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db