#Desafio073 tabela do campeonato brasileiro

times = 'Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',\
        'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',\
        'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco',\
        'Sport', 'América-MG', \
        'Vitória', 'Paraná'

print(times[0:5])
print(times[-4:])
print(sorted(times))
print(f' a posição do chapecoense é a {times.index("Chapecoense")+1}')