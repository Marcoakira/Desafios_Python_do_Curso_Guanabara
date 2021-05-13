# Desafio067 mostra as tabuadas até que seja interrompida.

# Entrada de dados
tabu = int(0)
while True:
    tabu = int(input('Qual tabuada você deseja ver agora? '))
    if tabu < 0:
        break
    for c in range (0,10+1):
        print(f'{tabu} X {c} = {tabu*c}')