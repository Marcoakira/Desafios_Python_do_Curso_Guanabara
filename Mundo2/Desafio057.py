# desafio057 recebe o sexo da pessoa com M e F, enquanto nao for M ou F, continuar pedindo.
contador = int(0)
sexo = str
while contador < 1 : # poderia ter sido usado por exemplo: while contador not in 'MmFf':
    sexo = str(input('Qual o seu sexo? M ou F ?')).strip().lower()[0]
    if sexo == 'm':
        contador = + 1
    elif sexo == 'f':
        contador = + 1
    else:
        contador = +0

if sexo == 'm':
    print(' Seu Sexo é Masculino')
elif sexo == 'f':
    print(' Seu sexo é Feminino')

