# Desafio066: Desafio criar um programa que leia varios numeros de o valor total digitado e pare quando digitado 999.
nu = int (0)
controle = int(0)
print('Se precisar sair digite 999')
while True:
    nu = int(input('Digite um numero '))
    if nu == 999:
      break
    controle = controle + nu
print(controle)

