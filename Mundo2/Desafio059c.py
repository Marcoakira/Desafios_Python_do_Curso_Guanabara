

primeiro = int(input('primeiro valor '))
segundo = int(input('segundo valor '))
opcao = int()
print(f'batata{primeiro} e {segundo}')
while opcao != 5:
    print(primeiro,segundo)
    opcao = int(input('-==-==-==-==-==-==-==-==-==-==-==-==-\n   [1] somar\n   [2] multiplicar\n   [3] maior\n   [4] novos números\n   [5] sair\n-==-==-==-==-==-==-==-==-==-==-==-==- \n'))
    if opcao == 1:
        print(f'A soma de {primeiro} + {segundo} = {primeiro+segundo}')


    elif opcao == 2:
        print(f'A multiplicação de {primeiro} x {segundo} = {primeiro * segundo}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'o Primeiro numero no valor de {primeiro} é maior')
        elif primeiro < segundo:
            print(f'o Segundo numero no valor de {segundo} é maior')
    elif opcao == 4:
        print('escolha novamente os numeros')
        primeiro = int(input('primeiro valor '))
        segundo = int(input('segundo valor '))
    elif opcao == 5:
        print('voce vai sair')


    else:
        print('Escolha entre 1 e 5')

print('Obrigado por participar')