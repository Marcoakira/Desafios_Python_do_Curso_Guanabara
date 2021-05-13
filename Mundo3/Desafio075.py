
t01 = (int(input('Valor 1 ')), int(input( 'valor 2 ')), int(input('valor 3 ')), int(input('valor 4 ')))


print(t01)
print(f'aparece o numero 9, {t01.count(9)} vezes ')
if 3 in t01:
    print(f' o  3 esta na posição {t01.index(3)+1}')
else:
    print('ninguem digitou 3')
for c in t01:
    if c % 2 == 0:
        print(c, end= ' ')
