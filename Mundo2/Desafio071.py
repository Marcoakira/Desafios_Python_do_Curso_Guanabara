# Desafio071 crie um programa que simule um caixa eletronico. ( quanto a ser sacado e quais a notas que serao entregue (50. 20 . 10 e 1).

print('+++++++++++  Bem vindo ao banco XYZ  +++++++++++')
saque = int(input('Qual o valor do saque? '))

if saque >= 50:
    notas50 = saque//50
    print(f'Voce receberá {notas50} notas de R$ 50,00 reais')
rnotas50 = saque%50


if rnotas50 >= 20:
    notas20 = rnotas50//20
    print(f'Voce receberá {notas20} notas de R$ 20,00 Reais')
rnotas20 = rnotas50%20


if rnotas20 >= 10:
    notas10 = rnotas20//10
    print(f'Voce receberá {notas10} notas de R$ 10,00 Reais')
rnotas10 = rnotas20%10


if rnotas10 >= 1:
    notas1 = rnotas10//1
    print(f'Voce receberá {notas1} notas de R$ 1,00 Real')

