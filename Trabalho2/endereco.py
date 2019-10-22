from peewee import *

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
        return self.rua + '' + self.logradouro + '' + self.cidade + '' + self.estado

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Endereco])  # solicitar a criação das tabelas
