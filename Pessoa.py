class Pessoa:
    "Isto é uma nova classe pessoa"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print('Olá Mundo!')

    def dizer_idade(self):
        print(f'Eu tenho {self.idade} anos!')

leandro = Pessoa('Leandro', 24)
leandro.dizer_idade()

pedro = Pessoa('Pedro', 20)
pedro.dizer_idade()