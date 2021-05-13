# desafio093b o programa gerencia o aproveitamento de um jogador de futebol. recebe: nome, numero de partidas jogadas, numero de gols feitos.

jogador_soccer_2021 = {}
ngols = []
media_gols_temp = 0
jogador_soccer_2021['Nome'] = input('Nome ')
jogador_soccer_2021['numero_partidas'] = int(input('Quantas partidas foi jogada? '))
for c in range(1,jogador_soccer_2021['numero_partidas']+1):
    ngols.append(int(input(f'Numero de Gols feito na {c}º partida ')))
    #media_gols_temp = media_gols_temp + ngols
    #jogador_soccer_2021['partida'].append(ngols)
#jogador_soccer_2021['gols'].append(ngols.copy())
jogador_soccer_2021['gols'] = ngols[:]
jogador_soccer_2021['media_gols'] = media_gols_temp / jogador_soccer_2021['numero_partidas']


print(jogador_soccer_2021)
print()
print('#' *56)
print()
print(f"O jogador {jogador_soccer_2021['Nome']}  jogou {jogador_soccer_2021['numero_partidas']} partidas\nfez o total de {media_gols_temp}, mantendo a média de {jogador_soccer_2021['media_gols']} por Partida.")
print()
print('#' *56)