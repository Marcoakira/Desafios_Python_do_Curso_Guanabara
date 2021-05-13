# Desafio026: Essa aplicação le uma frase, e retorna com quantas vezes aparece a letra A,
# em qual posição ela aparece pela primeira e pel aultima vez.
frase = str(input('Digite uma frase que tenha lhe marcado! ')).strip().lower()
frasecount = frase.count('a')
ff = frase.find('a')
fr = frase.rfind('a')
print(f'A sua frase possui {frasecount} letras A, ao todo\nA primeira vez que aparece é na {ff}º posição\n'
      f'A ultima vez que aparece é na {fr}º posição')