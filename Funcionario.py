class Funcionario:
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario

    def se_apresentar(self):
        print(f'Olá meu nome é {self.nome}!')

    def informar_email(self):
        print(f'Meu email é {self.email}!')

    def informar_salario(self):
        print(f'Meu salário é {self.salario}!')

    def ganhar_promocao(self, aumento_salarial):
        self.salario += aumento_salarial
        print(f'Parabéns! Novo salário é de R${self.salario},00!')

    def validar_email(self, email):
        if email == self.email:
            print(f'O email {email} é o do {self.nome}')
            return 
        
        print(f'O email {email} não é o do {self.nome}')

    def __repr__(self):
        return f'Funcionário: {self.nome}, \nEmail: {self.email}, \nSalário: {self.salario}'
