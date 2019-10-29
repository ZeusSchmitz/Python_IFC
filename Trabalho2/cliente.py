from peewee import *
from pessoa import Pessoa
from endereco import Endereco
from telefone import Telefone
from baseModel import *
import os

class Cliente(Pessoa):
    telefone = ForeignKeyField(Telefone)
    endereco = ForeignKeyField(Endereco)

    def __str__(self):
        return super().__str__()

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Cliente, Telefone, Endereco])  # solicitar a criação das tabelas

    tel = Telefone.create(ddd= '47', numero= '458774269')
    end = Endereco.create(rua= 'Bonifacio', numero= '7999', logradouro= 'Casa', cidade= 'Gaspar', estado= 'SC')
    c1 = Cliente.create(nome="Joao", sobrenome='Silva', dtNasc= '03/09/1987', sexo= 'M', senha= '1234', email= 'oh_zec', telefone= tel, endereco= end)
    print(c1)