#Desafio070 produtos, nome, preço. total gasto quantos custam mais de mil e o nome do produto mais barato

nomeP = str()
precoP = float()

custoTotal = float()
numeroDeProdutos = int()
acimaDeMil = int()
nomePMaisBarato = str()
valorPMaisBarato = float(99999999999999999999999999999)

continuar = str()

while True:

    nomeP = input('nome do Produto: ')
    precoP = float(input('Preço do produto: '))

    numeroDeProdutos += 1

    custoTotal += precoP

    if precoP >= 1000:
        acimaDeMil += 1

    if precoP < valorPMaisBarato:
        valorPMaisBarato = precoP
        nomePMaisBarato = nomeP
    continuar = str(input('Deseja continuar? S/N ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? S/N ')).strip().lower()[0]

    if continuar == 'n':
        break

print(f'O custo Total dos {numeroDeProdutos} Produtos comprados é R$ {custoTotal}.')
print(f'você comprou {acimaDeMil} Produtos Acima de Mil reais.')
print((f'O produto mais barato foi {nomePMaisBarato} no valor de {valorPMaisBarato}.'))