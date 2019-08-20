class Pessoa():
    def __init__(self, nome="", end="", tel=""):
        self.nome = nome
        self.end = end
        self.telefone = tel
if __name__ == "__main__":
    joao = Pessoa("Zeus Sc","Bonifácil",99876543)
    print(joao.nome,joao.end,joao.telefone)