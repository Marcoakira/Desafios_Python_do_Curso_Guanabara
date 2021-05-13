# Desafio103

def ficha(name,gols):

    if gols =='':
        gols = 'nao informado'
    if name =='':
        name = 'nao informado o nome'
    print(f'O jogador {name}, fez {gols} na temporada!')






nome1 = input('Nome do jogardor ').strip()
gols1 = input('Quantidade de Gols ').strip()


ficha(nome1,gols1)