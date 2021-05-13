


t01 = (str('Batata'), str('Mandioca'), str('Cotonete'), str('camaleao'), str('cama'), str('leao'), str('teiu'), str('caxote'), str('temosia'), str('binquedo'), str('gato'),)

for pos in range(0,len(t01)):
    t02 = t01[pos]

    a = ''
    e = ''
    i = ''
    o = ''
    u = ''

    if 'a' in t02:
        a = 'a '

    if 'e' in t02:
        e = 'e '

    if 'i' in t02:
        i = 'i '

    if 'o' in t02:
        o = 'o '

    if 'u' in t02:
        u = 'u '
    print(f'A palavra {t02} contém as letras {a}{e}{i}{o}{u}')


