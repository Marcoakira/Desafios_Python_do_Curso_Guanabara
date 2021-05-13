# Desafio084 ESSE PROGRAMA lê o nome e peso de varias pessoas. no final mostra quantas pessoas foram cadastradas

listaTemp = []
namePeso = []
maior = 0
nmaior = ''
menor = 0
nmenor = ''
print('para sair do programa digite sair no campo nome')
while True:
    listaTemp.append(str(input('Nome: ')))
    if 'sair' in listaTemp:
        listaTemp.clear()
        break
    listaTemp.append(int(input('Peso: ')))

    if len(namePeso) == 0:
        maior = menor = listaTemp[1]
        nmaior = nmenor = listaTemp[0]
    else:
        if listaTemp[1] > maior:
            maior = listaTemp[1]
            nmaior = listaTemp[0]
        if listaTemp[1] < menor:
            menor = listaTemp[1]
            nmenor = listaTemp[0]
    namePeso.append(listaTemp[:])
    listaTemp.clear()

print(namePeso)
print(f'Foram cadastrado {len(namePeso)} Pessoas. ')
print(f'Quem tem o maior Peso é {maior}')
print(f'O menor peso é de {menor}')
print(f'{nmaior} e {nmaior}')

