from peewee import *
from pessoa import Pessoa
from endereco import Endereco
from telefone import Telefone
from baseModel import *

class Fornecedor(Pessoa):
    nomeFant = CharField()
    produto = CharField()
    telefone = ForeignKeyField(Telefone)
    endereco = ForeignKeyField(Endereco)

    def __str__(self):
        return super().__str__() + ' Empresa: ' + self.nomeFant + ' Produto: ' + self.produto

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Fornecedor, Telefone, Endereco])  # solicitar a criação das tabelas

    tel = Telefone.create(ddd= '47', numero= '458774269')
    end = Endereco.create(rua= 'Bonifacio', numero= '7999', logradouro= 'Casa', cidade= 'Gaspar', estado= 'SC')
    f1 = Fornecedor.create(nomeFant= 'Bluvidros', produto= 'Garrafa', nome="Joao", sobrenome='Silva',
                            dtNasc= '03/09/1987', sexo= 'M', senha= '1234', email= 'oh_zec', telefone= tel, endereco= end)
    print(f1)
