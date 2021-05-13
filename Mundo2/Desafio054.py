# Desafio054 contador de quantos sao maior de idade
from datetime import date
crlt = int
menor = 0
maior = 0

for id in range(0,6):
    nasciment = int(input(f'Qual a data de nascimento da pessoa nº{id+1}: '))
    crlt = date.today().year - nasciment
    print(crlt)

    if crlt < 21:
        menor = menor +1
    if crlt>= 21:
        maior = maior +1

print(menor)
print(maior)
print(f'temos {menor} pessoas menor de idade e {maior} Maior de idade')
