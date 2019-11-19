from peewee import *
from baseModel import *
import os

class Cliente(BaseModel):
    nome = CharField()
    cpf = CharField(primary_key = True)
    email = CharField(unique = True)

    def __str__(self):
        return 'Nome: ' + self.nome + ' CPF: ' + self.cpf + ' Email: ' + self.email

if __name__ == '__main__':
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()  # conectar-se ao banco de dados
    db.create_tables([Cliente])

    c1 = Cliente.create(nome="Joao", cpf= '1456856636', email= 'oh_zec')
    print(c1)
