# Desafio038: recebe 2 valores, e informa se existe um valor maior, e qual é.
n1 = int(input('Primeiro Numero '))
n2 = int(input('Segundo numero '))
if n1 > n2:
    print(f'O numero {n1} que é o primerio é maior.')
elif n1 < n2:
    print(f'O numero {n2} que é o Segundo é maior.')
else:
    print('Os Dois Numeros são iguais')