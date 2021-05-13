#Desafio027: Criar uma aplicação que leia o nome completo do usuario, e retorne o primeiro nome, e o ultimo nome.
name = str(input('Bom dia tudo bem ?\nQual é seu nome completo?')).strip().split()
cont = (len(name))-1
print(f'seu primeiro nome é {name[0]}')
print(f'Seu último nome é {(name[cont])}')
