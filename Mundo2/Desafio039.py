import datetime
datenasc = int(input(f'insert you date of bit '))
atualdate = str(datetime.date.today())[0:4]
datestr = int(atualdate)
datefinal = datestr - datenasc
print(datefinal)
if datefinal < 18:
    print(f'voce esta com {datefinal}Faltam {18-datefinal} pra você se alistar ao exercito hahahah' )
elif datefinal == 18:
    print(f'Você completa 18 anos agora em {atualdate}'
          f'Chegou a hora ser servir seu país como bucha de canhão otario.\nPegue seus documentos ')
else:
    print(f'Você escapou sabichão, ja esta com {datefinal}, se livrou né safadenho')
