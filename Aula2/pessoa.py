class Pessoa():
    def __init__(self, nome="", end="", tel=""):
        self.nome = nome
        self.end = end
        self.telefone = tel
if __name__ == "__main__":
    joao = Pessoa("Zeus Sc","Bonifacil",99876543)
    print(joao.nome,joao.end,joao.telefone)

    def posOr(self, varPos):
        livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Oracle']
        print(livros.count('Oracle'))
        busca = varPos
        for i, livro in enumerate(livros):
            if busca in livro:
                print(i, livro)
livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Oracle']
print(livros.count('Oracle'))
busca = 'Or'
for i, livro in enumerate(livros):
    if busca in livro:
        print(i, livro)

for i, livro in enumerate(livros):
    print('O livro ' + livro + ' esta na posicao:', i)        