from peewee import *
from pessoa import Pessoa
from endereco import Endereco
from telefone import Telefone
from baseModel import *

class Funcionario(Pessoa):
    setor = CharField()
    telefone = ForeignKeyField(Telefone)
    endereco = ForeignKeyField(Endereco)

    def __str__(self):
        return self.setor

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Funcionario])  # solicitar a criação das tabelas
