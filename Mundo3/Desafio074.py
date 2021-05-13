import  random
maior = (-1)
menor = (11)
a1 = random.randint(0,9)
if a1 < menor:
    menor = a1
if a1 > maior:
    maior = a1
a2 = random.randint(0,9)
if a2 < menor:
    menor = a2
if a2 > maior:
    maior = a2
a3 = random.randint(0,9)
if a3 < menor:
    menor = a3
if a3 > maior:
    maior = a3
a4 = random.randint(0,9)
if a4 < menor:
    menor = a4
if a4 > maior:
    maior = a4
a5 = random.randint(0,9)
if a5 < menor:
    menor = a5
if a5 > maior:
    maior = a5

t1 = a1,a2,a3,a4,a5

print(t1)

print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')