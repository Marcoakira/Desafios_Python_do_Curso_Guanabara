# Desafio089 esse programa cria uma lista com as notas dos alunos e retorna essas notas.

nLista = []
pLista = []

while True:
    pLista.append(str(input('Nome do Aluno ')))
    if 'sair' in pLista[0]:
        break
    pLista.append(float(input('Nota 1º Bimestre ')))
    pLista.append(float(input('Nota 2º Bimestre ')))
    soma = pLista[1]*pLista[2]/2
    pLista.append(soma)
    nLista.append(pLista[:])
    pLista.clear()


print(nLista)
