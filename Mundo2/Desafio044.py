# Desafio044:
++++
valor_da_compra = float(input('valor da compra? '))
forma_de_pg = input('Qual a forma de pagamento? \033[1:31mD\033[m para dinheiro ou \033[1:31mC\033[m para cartão ').strip()
if forma_de_pg == 'D'or 'd':
   print(f'Pagamento a vista em dinhero voce tem desconto de 10% e o valor final sera de {(valor_da_compra/100)*90:.2f}')
if forma_de_pg == 'C' or 'c':
    quantivezes = input('pagamento sera a vista? \033[1:31mS\033[m ou \033[1:31N\033[m')
    elif quantivezes == 'S' :
    print('dfghfhf')
