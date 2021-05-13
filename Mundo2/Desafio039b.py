from datetime import date
sexo = input('Qual o seu sexo (M) Masculino, ou (F) Feminino')
masculino = 'm'
if sexo == masculino:
    datenasc = int(input(f'insert you date of bit '))
    atualdate = date.today().year
    datefinal = atualdate - datenasc
    print(datefinal)
    if datefinal < 18:
        print(f'voce esta com {datefinal} Faltam {18-datefinal} pra você se alistar ao exercito hahahah' )
    elif datefinal == 18:
        print(f'Você completa 18 anos agora em {atualdate}'
              f'Chegou a hora ser servir seu país como bucha de canhão otario.\nPegue seus documentos ')
    elif datefinal > 18:
        print(f'Você escapou sabichão, ja esta com {datefinal}, se livrou né safadenho')
else:
    print('voce é menininha, escapou de servir o exercito :D')