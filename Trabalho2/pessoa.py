from peewee import *
from telefone import Telefone
from endereco import Endereco
arq = 'pessoa.db'
db = SqliteDatabase(arq)

class Pessoa(Model):
    nome = CharField()
    sobrenome = CharField()
    dtNasc = CharField()
    sexo = CharField()
    senha = CharField()
    email = CharField()
    tel = ForeignKeyField(Telefone)
    end = ForeignKeyField(Endereco)

    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db

    # o método __str__ expressa a classe em formato texto
    def __str__(self):
        return self.nome + " " + self.sobrenome


if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pessoa])  # solicitar a criação das tabelas

    # criar uma pessoa e mostrar suas informações
    jo = Pessoa.create(nome="Joao", sobrenome='Silva')
    ze = Pessoa.create(nome='Zec', sobrenome='Ximitz')
    print(jo)
    print(ze)

