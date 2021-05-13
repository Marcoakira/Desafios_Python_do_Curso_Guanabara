# Desafio036, simular um emprestimo bancario levando em consideração o valor do imovel, salario, nº de parcelas.
# determinando que o mesmo nao deve ultrapassar 30% da renda.
print('\033[:33m****\033[m'*10)
print('   Seja bem vindo ao \033[7mBANCO SHABILAU\033[m')
print('\033[4:33m****\033[m'*10)
name = str(input('Qual seu nome? '))
# Valor do imovel a ser comprado.
home = float(input('Qual o valor no imovel? '))
# salario do comprador
sal = float(input('Qual o seu salario atual? '))
# Quantidade de anos que deseja parcelar a casa. o mesmo ja vem dividido por 12 qu esao os meses
anos = int(input('Quanto anos deseja pagar a casa? '))
# valor maximo de parcela liberado baseado no salario  =30%
vparc = (home/anos)/12
txlib = (sal/100)*30

if vparc<=txlib:
    print(f'Parabéns {name}, seu crédito no valor de R${home}, parcelado em {anos*12} meses,de R${vparc}.\n\033[2:32m FOI APROVADO!!!\033[m')
else:
    print('Infelismente, \033[2:33m nao foi aprovado \033[m seu finaciamento! procure seu gerente!')
