# Desafio 020 ( criar uma lista de alunos e colocar randomicamente em uma ordem de apresentação de trabalho.
from random import sample
al01 = str(input('coloque o nome do mikseravel 1 '))
al02 = str(input('coloque o nome do mikseravel 2 '))
al03 = str(input('coloque o nome do miserável 3 '))
al04 = str(input('coloque o nome do mikseravel 4 '))
ap = [al01, al02, al03, al04]
batata = sample(ap,3)
print(f'a sequencia de alunos que irao a lousa são:{batata}')
