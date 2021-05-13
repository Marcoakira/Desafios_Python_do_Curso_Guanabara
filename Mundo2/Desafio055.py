#Desafio055 peso de 5 pessoas e informe o maior e o menor.

batata = 0
limao = 1000
for c in range(0,5):
    peso = int(input(f'Qual o peso da {c}º Pessoa? '))
   
    if peso > batata:
        batata = peso

    if peso < limao:
        limao = peso

print(batata)
print(limao)