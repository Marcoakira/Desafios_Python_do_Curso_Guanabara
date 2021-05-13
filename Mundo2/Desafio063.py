# Desafio063 sequencia de fibonacci

qtermos = int(input('quantos termos?'))
a = 1
b  = int()
controle = int()
for c in range(-1,qtermos):


    a = a + b
    controle += 1
    #print(f' esse é o c {controle}')
    if controle <= qtermos:
        print(a)


    b = b + a
    controle += 1
    #print(f' esse é o c {controle}')
    if controle <= qtermos:
        print(b)




