#Desafio060

valor = int(input('digite um numero que sera fatorado.'))
#valor2 = valor-1
#fator = valor * valor2
valorfinal = valor

for c in range (valor,1, -1):
    print(f'esse é o C {c}')
    valorfinal = valorfinal * (c-1)
    print(valorfinal)