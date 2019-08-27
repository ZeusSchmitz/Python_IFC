class Produto():
    def __init__(self, garrafa="",nomeProd="",descProd=""):
        self.garrafa = garrafa
        self.nomeProd = nomeProd
        self.descProd = descProd

if __name__ == "__main__":
    pord = Produto("Garrafa Padrão", "Licor", "Licor natural")
    print(pord.garrafa)