# Desafio089 esse programa cria uma lista com as notas dos alunos e retorna essas notas.

nLista = []
pLista = []

while True:
    pLista.append(str(input('Nome do Aluno ')))
    if 'sair' in pLista[0]:
        break
    pLista.append(float(input('Nota 1º Bimestre ')))
    pLista.append(float(input('Nota 2º Bimestre ')))
    soma = pLista[1]+pLista[2]/2
    pLista.append(soma)
    nLista.append(pLista[:])
    pLista.clear()

while True:
    menu = int(input(' escolha a opção desejada:\n1 Para ver a Média de todos alunos\n2 para ver a média de 1 Aluno\n3 para Sair \n'))
    if menu == 3:
        break
    if menu == 1:
        print('*' * 40)
        print(f'Nº     NOME                       MÉDIA')
        print('*' * 40)
        for c in range(0, len(nLista)):
            print(f'{c:<7}{nLista[c][0]:<27}{nLista[c][3]}')
    if menu == 2:
        print('para sair Digite -1')
        nAluno = int(input('Qual numero do aluno? '))
        print('*' * 40)
        print(f'Nº     NOME                       NOTA1  NOTA2  MÉDIA')
        print('*' * 40)
        print(f'{menu:<7}{nLista[menu][0]:<24}{nLista[menu][1]:>7}{nLista[menu][2]:>7}   {nLista[menu][3]}')
        if menu == -1:
            break


print(' Obrigado por usar o Boa nota notas online')


