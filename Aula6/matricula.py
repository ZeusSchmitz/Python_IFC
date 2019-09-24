from peewee import *
import os
from disciplina import Disciplina
from pessoa import Pessoa
# conexão com o banco de dados Sqlite
arq = 'matricula.db'
db = SqliteDatabase(arq)

# declaração da classe herdando características da classe Model

class Matricula(Model):
    aluno = ForeignKeyField(Pessoa)
    discp = ForeignKeyField(Disciplina)
    # subclasse que estabelece vínculo da classe com o banco de dados
    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db

    # o método __str__ expressa a classe em formato texto
    def __str__(self):
        return str(self.aluno) + ', ' + str(self.discp)
    # utiliza-se try para prevenir erros de manipulação do arquivo
try:
    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Pessoa,Disciplina,Matricula])  # solicitar a criação das tabelas

# tratamento dos erros
except OperationalError as e:
    print("Erro ao criar tabelas: "+str(e))
    exit()  # finaliza o programa
     
# criar uma pessoa e mostrar suas informações
estudante = Pessoa.create(nome='Zec', sobrenome='Ximitz', endereco='Boni', telefone='999888776')
disciplina = Disciplina.create(materia='TADS', cargaH='60h')
matr1 = Matricula.create(aluno=estudante, discp=disciplina)
print(matr1)
