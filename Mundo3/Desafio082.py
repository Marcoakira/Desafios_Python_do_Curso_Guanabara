# Desafio082 esse programa recebe informações em uma lista. e passa essas informações para outras 2 listas, uma com os dados pares outra com os dados em impartes

alist = []
print('para sair digite -1')
plist = []
ilist = []
while True:
    alist.append(int(input('Insira um numero ')))

    if -1 in alist:
        alist.remove(-1)
        break

for i, p in enumerate(alist):
    if p % 2 == 0:
        plist.append(p)
for i, p in enumerate(alist):
    if p % 2 != 0:
        ilist.append(p)

print(plist)
print(ilist)