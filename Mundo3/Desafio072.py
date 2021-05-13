# Desafio072 crie uma tupla que mostre por extessio um numero entre 0 e vinte.

nc = int(input('Digite um número entre 0 e 20 para receber ele escrito por extenso. '))


while nc < 0 or nc > 20:
    nc = int(input('Vamos tentar novamente, eu disse um numero entre \033[2;32m0\033[m e \033[2;32m20\033[m '))

tunumerica = ('zero', 'um', 'Dois', 'Três', 'Quatro', 'Cinco', ' Seis', 'Sete',
              'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quize', 'Dezesseis,', 'Dezessete', 'Dezoito',
              ' Dezenove', 'Vinte')


print(f'O numero que você digitou foi {nc} que por extenso é {tunumerica[nc]}')
