


tulipas = (str('Batata'), str('Mandioca'), str('Cotonete'), str('camaleao'), str('cama'), str('leao'), str('teiu'), str('caxote'), str('temosia'), str('binquedo'), str('gato'),)

for palavra in tulipas:
    print(f'\n a palavra {palavra.upper()} contém a letra', end='')
    for letra in palavra:

        if letra in 'aeiou':
            print(letra.upper(), end=' ')
