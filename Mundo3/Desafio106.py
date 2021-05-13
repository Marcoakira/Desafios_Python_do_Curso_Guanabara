# Desafio106 o programa imprime o interative Help


#Funcções
def menu_bonito(nome_que_vai_no_menu):
    print(f'\033[1:32:40m{"#"* len(nome_que_vai_no_menu)}####\033[m')
    print(f'  {nome_que_vai_no_menu}')
    print(f'\033[1:32:40m{"#"* len(nome_que_vai_no_menu)}####\033[m')
    print()


def menu_bonito2(nome_que_vai_no_menu):
    print(f'{"~"* len(nome_que_vai_no_menu)}~~~~')
    print(f'  {nome_que_vai_no_menu}')
    print(f'{"~"* len(nome_que_vai_no_menu)}~~~~')
    print(help(nome_que_vai_no_menu))

def interactive_help(o_nome_da_funcao):
    qual_funcao = input('Qual a função? \n')
    print(qual_funcao)
#programa Principal

menu_bonito('BEM VINDO AO SUPER INTERACTIVE 2001')
print('Digite \033[1:32:40mfim\033[m para Sair')
while True:
    nome_da_funcao = input('Qual funçao voce deseja?')
    menu_bonito2(nome_da_funcao)
    if nome_da_funcao == 'fim':
        break