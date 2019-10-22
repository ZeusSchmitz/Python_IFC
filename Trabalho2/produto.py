from peewee import *

arq = 'produto.db'
db = SqliteDatabase(arq)

class Produto(Model):
    garrafa = CharField()
    nomProduto = CharField()
    descProduto = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return self.garrafa + '' + self.nomProduto + '' + self.descProduto

if __name__ == '__main__':

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Produto])  # solicitar a criação das tabelas

    prod1 = Produto.create(garrafa = 'Padrão', nomProduto = 'Cachaca Dupipe', descProduto = 'Cachaça envelhecida')
    print(prod1)