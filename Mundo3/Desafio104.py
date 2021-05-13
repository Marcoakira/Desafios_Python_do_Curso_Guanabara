# Desqafio104 o programa possui uma função que verifica se o input é um numero int

def leiaInt (num):

    while True:

        if num.isnumeric():
            return num
            #print(f'Você digitou {num}')
            #break
        else:
            print(f' {num} Não é um numero, digite um numero')
            print()
            num = input('Digite um numero')




novo_numero = leiaInt('k')

print(novo_numero)