# Desafio076b criar uma lista de preço usando uma unica tupla

t01 = (str('Batata'), float(12.68),str('Mandioca'),float(18.96), str('Cotonete'), float(22.20))
print('*'* 40)
print(f'MERCADO DO SALOMAO')
print('*'* 40)
for pos in range(0,len(t01)):
    if pos % 2 == 0:
        print(f'{t01[pos]:.<30}R$ {t01[pos+1]:.2f}')

#print(f'{t01[0].ljust(15), t01[1]}\n{t01[2].ljust(15), t01[3]}\n{t01[4].ljust(15), t01[5]}')