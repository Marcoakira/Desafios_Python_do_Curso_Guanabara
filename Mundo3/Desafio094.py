# Desafio094 o programa le nome, sexo e idade de carias pessoas em dicionarios individuais. e todos em uma lista.
odici_geral = []
dicionario_temp = {}
print('Para aprar digite no nome: sair')
# cadastro
while True:
    dicionario_temp['Nome'] = str(input('Nome: '))
    if 'sair' in dicionario_temp['Nome']:
        break
    while True:
        dicionario_temp['Sexo'] = str(input('sexo: ')).strip().upper()[0]
        if dicionario_temp['Sexo'] in 'MF':
            break
        print('Pro favor Digite M/F')
    dicionario_temp['Idade'] = int(input('idade: '))
    odici_geral.append(dicionario_temp.copy())
    dicionario_temp.clear()
print()
print()
print('¨' * 40)
# contador de quantos cadastros

print(odici_geral)

#quantas pessoas foram cadastradas
print()
print()
print('¨' * 40)
print(f'o numero de pessoas cadastradas foi {len(odici_geral)}')

#media de idade
print()
print()
print('¨' * 40)
idade = 0
for c in odici_geral:
    for k,v in c.items():
        if k == 'Idade':
            idade = idade + v
idade_final = idade / len(odici_geral)
print(f'A média de idade é {idade_final:.0f}')
print(f'total de idade é: {idade}')

#lista com o nome de todas mulheres cadastradas
print()
print()
print('¨' * 40)
print('O nome das mulheres: ')
for c in range(0,len(odici_geral)):
    if odici_geral[c]['Sexo'] == 'F':
        print(odici_geral[c]['Nome'],end=' ')

# pessoas com a idade acima da media
print()
print()
print('¨' * 40)

print('As pessoas com a idade acima da media são:')
for c in range(0,len(odici_geral)):
    if odici_geral[c]['Idade'] > idade_final:
        print(odici_geral[c]['Nome'],end=' ')
        print(odici_geral[c]['Idade'],end=' ')
        print()

    #for k, v in c.items():
     #   if k == 'Sexo':
        #    print(v,end='')

#print(dicionario_temp)
