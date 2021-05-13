#Desafio025, essa aplicação verifica se o sobrenome do usuario possui SILVA, e evitnado erros como Silvana.
name = str(input('Qual o seu nome completo? ')).strip().lower()
name1 = (name+' ')
print ('silva 'in name1)
