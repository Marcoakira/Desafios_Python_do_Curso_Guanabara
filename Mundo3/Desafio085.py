# Desafio085 esse programa recebe 7 dados numericos mantendo em uma unica lista sepador numeros pares e impares.

alista = [[],[]]
temp = ()
'''tempP = []
tempI = []'''
for c in range(0,7):
      temp = int(input('Digite um numero: '))
      if temp % 2 == 0:
          alista.insert(0,temp)
      else:
          alista.insert(1,temp)
#alista.sort()
print(alista)
#print(alista[1])
'''
alista.append(tempP)

alista.append(tempI)
print(alista)

print(tempP)

print(tempI)'''