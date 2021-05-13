# | treino

def fatorial(n=1):
    f = n
    transitorio =0
    for c in range(n,1,-1):
        f = f * (c-1)
    return (f)

escolha = int(input('Digite um numero:'))
print(fatorial(escolha))


'''def somar(a=0, b=0, c=0):
    s = a+b+c
    #print(s)
    return s

resp = somar(1,2,3)

print(resp)'''