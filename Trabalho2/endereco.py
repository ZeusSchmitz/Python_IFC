from peewee import *
import os

arq = 'endereco.db'
db = SqliteDatabase(arq)

class Endereco(Model):
    rua = CharField()
    numero = CharField()
    logradouro = CharField()
    cidade = CharField()
    estado = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return 'Rua: ' + self.rua + ' Logradouro: ' + self.logradouro + ' Cidade: ' + self.cidade + ' Estado: ' + self.estado

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Endereco])  # solicitar a criação das tabelas

    end = Endereco.create(rua= 'Bonifacio', numero= '7999', logradouro= 'Casa', cidade= 'Gaspar', estado= 'SC')
    print(end)