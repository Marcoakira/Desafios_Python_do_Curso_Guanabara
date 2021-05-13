# Desafio080
alist = []
print('para sair digite -1')
contador = int()
while True:
    alist.append(int(input('Insira um numero ')))
    contador += 1
    if -1 in alist:
        alist.remove(-1)
        contador -= 1
        break

print(alist)
# poderia ser usado o len para contador: len(alist)
print (f'Foram digirados {contador} Numeros')
alist.sort(reverse=True)
print(alist)
if 5 in alist:
    print(' temos o numero 5 na lista')
else:
    print('Nao temos o 5 nessa lsita')