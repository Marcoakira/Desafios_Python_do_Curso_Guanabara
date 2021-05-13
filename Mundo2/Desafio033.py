#A aplicação recebe 3 idades e diz quem é mais velho
a = int(input('digite a idade da primeira pessoa'))
b = int(input('digite a idade da segunda pessoa'))
c = int(input('digite a idade da terceira pessoa'))
menor = (a)
maior = (a)
if b<a and b<c:
    menor = b
elif c<a and c < b:
    menor = c
print(f'o menor valor é {menor}')
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print(f'o maior valor é {maior}')
