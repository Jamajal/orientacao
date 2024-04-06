class Pessoa:
    "Isto é uma nova classe chamada Pessoa"
    
    idade = 15
    
    def saudacao(self):
        print("Olá Pessoas!!!")
    
print(Pessoa.idade)
print(Pessoa.saudacao)

objetoPessoa = Pessoa()

objetoPessoa.saudacao()
print(objetoPessoa.idade)
print(objetoPessoa.saudacao)

print(Pessoa.__doc__)
        