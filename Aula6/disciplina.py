from peewee import *
import os
# conexão com o banco de dados Sqlite
arq = 'disciplina.db'
db = SqliteDatabase(arq)

# declaração da classe herdando características da classe Model

class Disciplina(Model):
    materia = CharField()
    cargaH = CharField()
    # subclasse que estabelece vínculo da classe com o banco de dados
    class Meta:
        # o atributo database se refere à variável de conexão com o BD
        database = db

    # o método __str__ expressa a classe em formato texto
    def __str__(self):
        return self.materia + ', ' + self.cargaH

if __name__ == '__main__':  # teste das classes e da persistência

    # apagar o arquivo caso ele exista
    if os.path.exists(arq):
        os.remove(arq)

    # utiliza-se try para prevenir erros de manipulação do arquivo
    try:
        db.connect()  # conectar-se ao banco de dados
        db.create_tables([Disciplina])  # solicitar a criação das tabelas

    # tratamento dos erros
    except OperationalError as e:
        print("Erro ao criar tabelas: "+str(e))
        exit()  # finaliza o programa

    # criar uma pessoa e mostrar suas informações
    tads = Disciplina.create(materia='Tecnologia em analise e desenvolvimento em sistemas', cargaH='60h')
    segi = Disciplina.create(materia='Seguranca de Informatica', cargaH='30h')
    print(tads)
    print(segi)