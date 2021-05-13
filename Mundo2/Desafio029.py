#Desafio029: A aplicação recebe a velocidade fo carro, se a mesma for superior a 80KM/h,
# retorna uma mensagem dizendo que foi multado , com o valor total de cada km acima dos 80.

#entrada da velocidade.
vel = int(input('qual era a velocidade do seu carro? Km/h '))-80
multa = (vel*7)
if vel >= 0:
    print(f'Você nao viu o radar de 80Km/h?\nAcabou de ser Multado em R${multa} Reais. tem o prazo de 15 dias para recorrer.' )
else:print('parabens!!!\nContinue dirigindo assim.')