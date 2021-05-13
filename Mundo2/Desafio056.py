# Desafio056 recebe o nome idade e sexo, devolte a media de idade,  nome do home mais velho, e quantas mulheres com menos de 21.

cnome = str('')
midade = 0
cmidade = 0
mulheres = 0
hidade = int (0)
for c in range(0,4):
    sexo = str(input('Qual seu sexo (M) Mulher, (H) Homem ')).strip().lower()
    nome = str(input('nome'))
    idade = int(input('idade'))

    midade = midade + idade
    if idade > hidade and sexo == 'h':
        hidade = idade
        cnome = nome
    if idade > cmidade:
        cmidade = idade
    if idade < 20 and sexo == 'm':
        mulheres = mulheres +1
    print(cnome)

print(f'A média de idade é do grupo é de {midade/4} anos. \n o homem mais velho se chama {cnome} \n e ao todo temos {mulheres} menores que 20 anos.')