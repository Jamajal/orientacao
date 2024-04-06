class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.salario = 0
        self.horas = {}
        self.salario_hora = {}
        
    def cadastro_hora(self, mes, horas):
        if(mes not in self.horas):
            self.horas[mes] = horas
        
    def cadastro_salario_hora(self, mes, valor):
        if(mes not in self.salario_hora):
            self.salario_hora[mes] = valor
            
    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print("Mês não calculado")
        else:
            self.salario = self.horas[mes] * self.salario_hora[mes]
            return self.salario

    def __repr__(self):
        return f'Funcionário: {self.nome}, \
        \nEmail: {self.email}, \nSalário: {self.salario}'



    
    
        
        
    
    