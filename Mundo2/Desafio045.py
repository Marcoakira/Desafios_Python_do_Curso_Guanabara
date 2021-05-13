# Desafio045 Aplicação que jogue jokenpo
import random
user = str(input('Escolha entre \033[1:32m 1\033[m Pedra, \033[1:32m 2\033[m Papel e \033[1:32m 3\033[m Tesoura ')).strip()
pc = ['1','2','3']
pc1 = random.choice(pc)
escolhaPc = 'a'
if pc1 == '1':
    escolhaPc = 'Pedra'
if pc1 == '2':
    escolhaPc = 'Papel'
if pc1 == '3':
    escolhaPc = 'Tesoura'
if user == pc1:
    print(f'Também escolhi {escolhaPc}, por isso deu empate. Vamos outra?')
elif pc1 == '1' and user == '3' or pc1 == '2' and user == '1' or pc1 == '3' and user == '2':
        print(f'Eu ganhei HaHaHaHa, por que eu escolhi {escolhaPc} :D !')
else:
    print(f'Ok voce venceu por que eu escolhi {escolhaPc}')
