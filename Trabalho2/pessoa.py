from peewee import *
from telefone import Telefone
from endereco import Endereco
from abc import ABC, abstractclassmethod
import os

arq = 'pessoa.db'
db = SqliteDatabase(arq)

class Pessoa(Model):
    nome = CharField()
    sobrenome = CharField()
    dtNasc = CharField()
    sexo = CharField()
    senha = CharField()
    email = CharField()
    telefone = ManyToManyField(Telefone)
    endereco = ForeignKeyField(Endereco)

    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db

    # o método __str__ expressa a classe em formato texto
    def __str__(self):
        return self.nome + ", " + self.sobrenome + ", " + self.dtNasc + ", " + self.sexo + ", " + self.senha + ", " + self.email + ", " + str(self.telefone) + ", " + str(self.endereco)


if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pessoa, Telefone, Endereco])  # solicitar a criação das tabelas

    # criar uma pessoa e mostrar suas informações
    tel = Telefone.create(ddd= '47', numero= '458774269')
    end = Endereco.create(rua= 'Bonifacio', numero= '7999', logradouro= 'Casa', cidade= 'Gaspar', estado= 'SC')
    jo = Pessoa.create(nome="Joao", sobrenome='Silva', dtNasc= '03/09/1987', sexo= 'M', senha= '1234', email= 'oh_zec', telefone= tel, endereco= end)
    print(jo)

