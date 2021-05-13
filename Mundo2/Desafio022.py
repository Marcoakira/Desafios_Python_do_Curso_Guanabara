# Desafio022: criar um programa que ao ser digitado o nome completo do usuario, ele retonar.
#todos caracteres em maiuscula, todos em minuscula e o total de letras sem considerar os espaços,
# e quantas letras tem o primeiro nome.
nc = input('qual o seu nome completo?').strip()
nce = nc.replace(' ','')
nc1 = nc.split()
print(nc.upper())
print(nc.lower())
print(len(nce))
print(f'seu primeiro nome é         {nc1[0]} e possui{len(nc1[0])} caracteres')