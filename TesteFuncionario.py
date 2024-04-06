""" 
    Criação de objetos e chamadas dos métodos
"""
from Funcionario import Funcionario

funcionario = Funcionario('Antonio', 'tonhao@ymail.com')

funcionario.cadastro_hora('Jan', 280)
funcionario.cadastro_hora('Feb', 230)
funcionario.cadastro_salario_hora('Jan', 250)
funcionario.cadastro_salario_hora('Feb', 250)
print(funcionario.calcula_salario('Jan'))
print(funcionario)
print(funcionario.calcula_salario('Feb'))
print(funcionario)

print(repr(funcionario))