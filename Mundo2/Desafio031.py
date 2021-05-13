#Desafio031: calcula o preço da viagem baseado nos Km de distancia, sendo para até 200Km R$0,50 e acima de 200Km, R$0,45
km = int(input('bom dia tudo bem?\nQuantos Kilometros terá sua viagem?'))
if km <= 200:
    precokm = (km * 0.50)
    print(f'Os primeiros 200Km custam R$0,50, os demais R$0,45.\nSua corrida ficará em R${precokm}\nBoa viagem!')
else:
    precokm = ((km*0.45)+10)
    print(f'Os primeiros 200Km custam R$0,50, os demais R$0,45.\nSua corrida ficará em R${precokm}\nBoa viagem!')
