# Desafio083 o programa analisa se foi declarada uma expressao usando as chaves de maneira correta.
elista = str(input('coloque sua expressao: '))

coabre = elista.count('(')
print(coabre)
cofecha = elista.count(')')
print(cofecha)
if coabre == cofecha:
    print(' o uso de couchetes esta correto')
elif coabre != cofecha:
    print('Sua expressao esta ERRADA no uso dos couchetes')
print(elista)