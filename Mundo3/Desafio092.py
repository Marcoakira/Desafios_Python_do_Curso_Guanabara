# Desasfio092 esse programa le: o nome, ano de nascimento CTPS. no dicionario vai guardar nome, idade, CTPS, ano de contratação, e ano que ira se aposentar.
from datetime import date
cadastro_unico = []
cadastro_temporario = {}
#atual = date.today().year



while True:
    cadastro_temporario['nome'] = str(input('Nome: '))
    # ano de nacimento vai calcular e retornar a idade aproximada da pessoa
    #cadastro_temporario['ano_nacimento'] = str(input('data de nascimento: '))
    ano_temporario = int(input('ano de nascimento: '))
    cadastro_temporario['idade'] = date.today().year - ano_temporario
    # se o numero for 0, o usuario nao trabalha. se for diferente. peça o ano da contratação e salario. retorna tempo para aposentar.
    cadastro_temporario['numero_CTPS'] = int(input('Numero da Carteira de Trabalho ( digite 0 caso nao trabalhe): '))
    if cadastro_temporario['numero_CTPS'] != 0:
        cadastro_temporario['ano_contratacao'] = int(input('Ano de contratação: '))
        # aqui iria o salario, mas optei por nao colocar.
        # poderia fazer com que idade ele iria se aposertra, mas prefiri fazer o ano, para ser mais preciso.
        ano_aposentadoria_temp = 35 - (date.today().year - cadastro_temporario['ano_contratacao'])
        ano_aposentadoria = date.today().year + ano_aposentadoria_temp
        if ano_aposentadoria <= date.today().year:
            cadastro_temporario['vai_aposentar'] = 'aposentado'
        if ano_aposentadoria > date.today().year:
            cadastro_temporario['vai_aposentar'] = ano_aposentadoria

    print(cadastro_temporario)
    break
cadastro_unico.append(cadastro_temporario.copy())
cadastro_temporario.clear()
for c in cadastro_unico:
    for k,d in c.items():
        print(k,d)

#print(cadastro_unico)


