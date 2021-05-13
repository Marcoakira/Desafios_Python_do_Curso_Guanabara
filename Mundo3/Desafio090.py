# Desafio090 o programa mostra o nome e media do aluno em uma lista com dicionario. ele retorna com os dados e se o mesmo foi ou nao aprovado

#aluno = {'nome':'joaquim', 'media': 4.5}
aluno = {}
aluno['nome'] = str(input('Nome do aluno(a)'))
aluno['media'] = float(input('media do aluno(a)'))
print(aluno)
print(f'Nome: {aluno["nome"]}')
print(f'A média foi de {aluno["media"]}')
if aluno['media'] > 7:
    print(f'{aluno["nome"]}, passou de ano!')
else:
    print(f'{aluno["nome"]}, Reprovou!')