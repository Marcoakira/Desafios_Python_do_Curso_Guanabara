#Desafio024, essa aplicação verifica se o nome da cidade começa com a palavra 'santo'.
city = str(input('Qual o nome da sua cidade? ')).strip().lower()
nc = city.split()
c1 = nc[0].split()
c2 = 'santo' in c1[0:4]
print(f'A afirmativa que sua cidade começa com a palavra Santo é {c2} ')
