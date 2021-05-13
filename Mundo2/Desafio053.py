# Desafio053 diz se o nume é um palindromo.
frase = str(input('Digite a frase')).strip().lower().replace(' ','')
frase2 = frase[::-1]
print(f'a frase invertida ficou assim: {frase2}')
if frase == frase2:
    print(f'A Frase {frase} é um palindromo.')
else:
    print(f'A frase {frase} não é um palindromo!')
#for frase2 in range (0,-1):
        #print(frase2)#

