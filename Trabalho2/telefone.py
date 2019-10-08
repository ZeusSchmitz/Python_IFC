from peewee import *

arq = 'telefone.db'
db = SqliteDatabase(arq)

class Telefone(Model):
    ddd = CharField()
    numero = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.ddd + '' + self.numero

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Telefone])  # solicitar a criação das tabelas
