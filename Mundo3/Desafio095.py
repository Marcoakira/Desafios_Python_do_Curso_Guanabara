# Desafio095 o programa ira aprimorar o 093, fazendo funcionar para varios jogadores. com detalhes de aproveitamento de cada jogador.

#variaveis
time =[]
print('Se desejar para coloque no nome do jogardo "sair"')
while True:
    jogador_soccer_2021 = {}
    ngols = []
    media_gols_temp = 0
    #inputs
    jogador_soccer_2021['Nome'] = input('Nome ')
    if jogador_soccer_2021['Nome'] == 'sair':
        break
    jogador_soccer_2021['numero_partidas'] = int(input('Quantas partidas foi jogada? '))
    # entrada de quantiades de gols
    for c in range(1,jogador_soccer_2021['numero_partidas']+1):
        ngols.append(int(input(f'Numero de Gols feito na {c}º partida ')))
    #tranferencia dos gols da lista para o dicionario
    jogador_soccer_2021['gols'] = ngols[:]
    #soma dos gols
    for d in jogador_soccer_2021['gols']:
        media_gols_temp = media_gols_temp + d
    #media de gols
    jogador_soccer_2021['media_gols'] = (media_gols_temp / jogador_soccer_2021['numero_partidas'])
    time.append(jogador_soccer_2021.copy())

print(time)
print()
print('¨'*40)
print('Cod      Nome           Gols      total      media')
for c in range(0,len(time)):
    print(f"{c:<9}{time[c]['Nome']:<12}  {time[c]['gols']}  total em breve {time[c]['media_gols']}")
print()
# mostrar jogador de maneira individual

while True:
    qjogar = int(input('deseja mostar as informaçoes de qual jogador? digite seu numero, ou 999 para sair? '))
    if qjogar == 999:
        break
    print(time[qjogar])

print('Obrigado por usar o SUPER SOCCER 2021')










   #for k, v in c.items():
      #  print(f"{c}    {v}")

'''
# retorno
print(jogador_soccer_2021)
print()
print('#' *56)
print()
print(f"O jogador {jogador_soccer_2021['Nome']}  jogou {jogador_soccer_2021['numero_partidas']} partidas\nfez o total de {media_gols_temp}, mantendo a média de {jogador_soccer_2021['media_gols']} por Partida.")
print()
print('#' *56)'''