# Desafio050 recebe 6 numeros inteiros e retorna a soma somente do que forem pares.
numerosEntrada2 = 0
for c in range (0,6):
    numerosEntrada = int(input('Digite um numero inteiro'))
    if numerosEntrada % 2 == 0:
        numerosEntrada2 = numerosEntrada2+ numerosEntrada
print(numerosEntrada2)

