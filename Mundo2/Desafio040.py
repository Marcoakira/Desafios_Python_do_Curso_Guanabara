name_aluno = str(input('Insira o nome do Aluno'))
nota1sem = float(input('Insira a nota do 1º Semestre'))
nota2sem = float(input('Insira a nota do 2º Semestre'))
notafinal = (nota1sem+nota2sem)/2
print(notafinal)
if notafinal < 5:
    print(f"Sua nota media foi {notafinal}, estude mais.\nVocê foi \033[2:31m REPROVADO!\033[m")
elif notafinal >5 and notafinal <6.9:
    print(f'sua nota media foi {notafinal}, voce esta de \033[2:33m RECUPERAÇÃO.\033[m \nNos vemos nas férias :D .')
else:
    print(f'Parabens, Sua nota Foi {notafinal}, você foi \033[2:32mAPROVADO !!!\033[m. nos vemos ano que vem.')
