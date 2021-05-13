# Desafio084 ESSE PROGRAMA lê o nome e peso de varias pessoas. no final mostra quantas pessoas foram cadastradas

lista = []
nameIdade = []
pCadastradas = 0
pPesadas = []
print('para sair do programa digite sair no campo nome')
while True:
    lista.append(str(input('Nome: ')))
    pCadastradas += 1
    if 'sair' in lista:
        pCadastradas -= 1
        lista.clear()
        break
    lista.append(int(input('Peso: ')))
    nameIdade.append(lista[:])
    lista.clear()
for c in nameIdade:
    if c[1] > 100:
        pPesadas.append(c[0])
print(nameIdade)
print(f'foram cadastradas {pCadastradas} pessoas.')
print(f'as pessoas que pesam mais de 100 kilos são:{pPesadas}')
for d in nameIdade:
    if d[1]< 60:
        print(d[0])


