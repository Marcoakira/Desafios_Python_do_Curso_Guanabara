#aplicação mostra se o ano é BiSSEXTO.

year = int(input('Digite o ano, se desejar usar o ano atual digite 0 '))
if (year%4==0) and (year%100==0) and (year%400==0) or (year%4==0) and (year%100!=0):
    print(f'Sim, {year} é um ano bissexto')
else:
    print(f'Nao,{year} não é um ano bissexto')
