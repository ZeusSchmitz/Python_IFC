from peewee import *

arq = ':memory:'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db