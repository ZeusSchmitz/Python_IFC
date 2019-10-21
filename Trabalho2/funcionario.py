from peewee import *
from pessoa import Pessoa

arq = 'funcionario.db'
db = SqliteDatabase(arq)

class Funcionario(Model):
    func = ForeignKeyField(Pessoa)
    setor = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.func + '' + self.setor

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Funcionario])  # solicitar a criação das tabelas
