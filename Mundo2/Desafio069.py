# Desafio069 quantas pessoas tem mais de 18, quantos homens, quantas mulheres com menos de 20.


maiorDeIdade = int()
homens = int()
mulheresMenor = int()
while True:
    idade = int(input('Qual a idade? '))
    sexo = input('M para masculino, e F para feminino ').strip().lower()

    if idade > 18:
        maiorDeIdade += 1

    if sexo == 'm':
        homens += 1

    if sexo == 'f' and idade > 20:
        mulheresMenor += 1

    saida = input('Deseja continuar? \033[2;32mS\033[m ou \033[2;32mN\033[m ')
    if saida == 'n':
        break

print(f'Tivemos cadastrados {maiorDeIdade} Maiores de 18 anos.')
print(f'Tivemos cadastrados {homens} homens.')
print(f'Tivemos cadastrados {mulheresMenor} mulheres com menos de 20 anos.')