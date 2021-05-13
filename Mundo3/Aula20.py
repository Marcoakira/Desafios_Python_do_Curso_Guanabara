
def sistema_menssagem(msg):

    hast = len(msg)+4
    print('#' * hast)
    print(f'  {msg}')
    print('#' * hast)


sistema_menssagem('hello Word')

'''
def contador(*num):
    cont = 0
    for c in num:
        cont = cont + c

    print(cont)
    print()


def dobra(ist):
    pos = 0
    while pos < len(ist):
        ist[pos] *=2
        pos +=1





contador(2,1,5,16)
valores = [3,5,14,9,1,0,8]
dobra(valores)
print(valores)
contador(9,5)

'''