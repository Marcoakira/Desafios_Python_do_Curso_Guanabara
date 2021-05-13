# Desafio091
from random import randint
from operator import itemgetter
base = {}
for c in range(1,5):
    base[f'jogador{c}'] = randint(1,6)
rank = {}

print(base)

for k,v in base.items():
    print(f'{k} tirou {v} no dado.')

rank = sorted(base.items(),key=itemgetter(1),reverse=True)

print(rank)

for k,v in enumerate(rank):
    print(f'{k} tirou {v} no dado.')




'''controle = []
while len(controle) > 4:
    for c in range(0,4):
        if base[c].values() > controle[len(controle)]:
            controle = base[c]
print(controle)'''