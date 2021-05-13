# Desafio034: calcula o aumento de salario.
salario = float(input('Qual o salario atual do funcionario? '))
salsup = (salario)
porcentagem = (10)
if salario >= 1200:
    salsup = ((salario/100) * 110)
    porcentagem = (15)
else:salsup = ((salario/100)*115)

print(f'novoo novo salario do funcionario com almento de {porcentagem}% será R${salsup:.2f}')
