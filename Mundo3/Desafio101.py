# desafio101 o programa recebe a data de nascimento e retorna se a pessoa tem : voto obrigatorio, opcional, ou nao é votante.



def voto(nasc):
    from datetime import date
    votante = date.today().year - nasc
    if votante < 16:
        return print(f' voce possui {votante} anos. Ainda não pode votar')
    elif votante >16 and votante < 18 or votante >= 65:
        print(f'Você tem {votante} anos, e seu voto é opcional')
    elif votante >= 18 or votante <65:
        print(f'você tem {votante} anos, e seu voto é \033[1:32MOBRIGATORIO\033[M')





votacao = int(input('Qual sua data de nascimento?'))
voto(votacao)

