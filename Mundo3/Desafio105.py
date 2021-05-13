# desafio105 programa tem uma função que recebe varias notas, e retorna um dicionario com as quantidade de notas, a maior nota, media da turma, a situação


#funçoes
def notas (resp,sit = False):
    #variaveis
    odcionario = {'qnotas': 0,'nmaior':0,'nmenor':0, 'media':0}
    odcionario['nmenor'] = resp[0]
    odcionario['qnotas'] = len(resp)

    # recebe a soma das notas
    total = 0

    #faz a passagem
    for n in resp:
        #envia quantidade de notas pra lista
        #odcionario['qnotas'] += 1
        #recebe a nota envia para variavel total, somando a mesma.
        total += n
        # verifica, se for maior nota envia para odicionaro[qnotas].
        if n > odcionario['nmaior']:
            odcionario['nmaior'] = n
        #verifica, se é a menor nota e envia para o dicionario na posiçao correta
        if n < odcionario['nmenor']:
            odcionario['nmenor'] = n
        print(n)
    # gera a media das notas
    odcionario['media'] = total / len(resp)
    #situaçoes:
    if sit == True:
        if odcionario['media'] < 4:
            print('Situação Complicada')
        if odcionario['media'] >= 4 and odcionario['media'] < 7:
            print('vamos la')
        if odcionario['media'] >= 7:
            print('Muito bom')
    print(odcionario)


# Programa principla



asnotas = (5.5,9.5,10,6.5)

notas(asnotas, sit=True)