# Desafio043: IMC
peso = float(input('Insira o seu peso '))
altura = float(input('Insira a sua altura, ex: 1.75 '))
imc = peso/(altura*altura)
if imc < 18.5:
    print(f'Você esta abaixo do peso seu imc é {imc:.1f}')
elif imc >= 18.5 and imc < 25:
    print(f'Parabens. você esta com o peso ideal, seu IMC é {imc:.1f}')
elif imc > 25 and imc < 30:
    print(f'se cuida, voce esta com sobrepeso. Seu IMC é {imc:.1f}.')
else:
    print(f'Procure seu medico urgentemente, voce esta com obesidade móbida. seu IMC é de {imc:.1f}.')
print(imc)