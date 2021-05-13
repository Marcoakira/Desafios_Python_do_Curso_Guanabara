# Desarfio078 ele recebe 5 valores e guarda em uma lista.

l5 = []
for c in range(0,4):
    l5.append(int(input('Insira um numero')))

maior = (l5.index(max(l5)))
menor = (l5.index(min(l5)))
print(menor)

print(f'O maior numero dessa lista é : {max(l5)} na posição {maior}')
print(f'O menor numero dessa lista é o {min(l5)} na posição {menor}')
print(l5)