
while True:
    primeiro = int(input('primeiro valor '))
    segundo = int(input('segundo valor '))
    opcao = int()
    while opcao != 4:
        opcao = int(input('-==-==-==-==-==-==-==-==-==-==-==-==-\n   [1] somar\n   [2] multiplicar\n   [3] maior\n   [4] novos números\n   [5] sair\n-==-==-==-==-==-==-==-==-==-==-==-==- \n'))
        if opcao == 1:
            print(f'A soma de {primeiro} + {segundo} = {primeiro+segundo}')
        if opcao == 2:
            print(f'A multiplicação de {primeiro} x {segundo} = {primeiro * segundo}')
        if opcao == 3:
            if primeiro > segundo:
                print(f'o Primeiro numero no valor de {primeiro} é maior')
            if primeiro < segundo:
                print(f'o Segundo numero no valor de {segundo} é maior')
        if opcao == 5:
            break

