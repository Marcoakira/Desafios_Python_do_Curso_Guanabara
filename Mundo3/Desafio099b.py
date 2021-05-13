# Desafio099 o programa tem uma função " Maior " que le uma lista e diz quantos valores foram inforamdos e qual é o maior valor.

def maior (num):
    m = 0
    for c in num:
        if c > m:
            m = c
    print(f'Foram informados {len(num)} numeros, {num} e destes o maior é o {m}.')
    print()


'''def osnumeros(num):
    num = []
    while True:
        temp = int(input('digite um numero'))
        if temp == -99:
            break
        num.append(temp)'''


#Código Principal

lista = [2,6,4,15,2,89,6,11,12]

maior(lista)

nlista = []

while True:
    temp = int(input('digite um numero'))
    if temp == -99:
        break
    nlista.append(temp)
maior(nlista)