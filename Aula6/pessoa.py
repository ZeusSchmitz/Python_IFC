from peewee import *
import os
# conexão com o banco de dados Sqlite
arq = 'pessoa.db'
db = SqliteDatabase(arq)

# declaração da classe herdando características da classe Model


class Pessoa(Model):

    nome = CharField()
    sobrenome = CharField()
    endereco = CharField()
    telefone = CharField()

    # subclasse que estabelece vínculo da classe com o banco de dados
    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db

    # o método __str__ expressa a classe em formato texto
    def __str__(self):
        return self.nome + " " + self.sobrenome + ',' + self.endereco + "," + self.telefone


if __name__ == '__main__':  # teste das classes e da persistência

    # utiliza-se try para prevenir erros de manipulação do arquivo
    try:
        db.connect()  # conectar-se ao banco de dados
        db.create_tables([Pessoa])  # solicitar a criação das tabelas

    # tratamento dos erros
    except OperationalError as e:
        print("Erro ao criar tabelas: "+str(e))
        exit()  # finaliza o programa

    # criar uma pessoa e mostrar suas informações
    jo = Pessoa.create(nome="Joao", sobrenome='Silva', endereco="Casa 9", telefone="99332-1212")
    ze = Pessoa.create(nome='Zec', sobrenome='Ximitz', endereco='Boni', telefone='9988776655')
    print(jo)
    print(ze)
