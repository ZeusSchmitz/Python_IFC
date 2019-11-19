from peewee import *
from baseModel import *
import os

class Produto(BaseModel):
    garrafa = CharField()
    nomProduto = CharField()
    descProduto = CharField()

    def __str__(self):
        return self.garrafa + '' + self.nomProduto + '' + self.descProduto

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Produto])  # solicitar a criação das tabelas

    prod1 = Produto.create(garrafa = 'Padrão', nomProduto = 'Cachaca Dupipe', descProduto = 'Cachaça envelhecida')
    print(prod1)