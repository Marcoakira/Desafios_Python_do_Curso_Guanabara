# Aula12, treinando if, elif, else
name = str(input('Qual o seu nome?')).strip()
if name == 'marco':
    print('Que nome expetacular cara.')
elif name == 'pedro' or name == 'maria' or name == 'Paulo':
    print('Seu nome é biblico né?')
elif name in 'ana claudia sara joice':
    print('Que nome de Puta!')
else:
    print('seu nome é bem normal')
print(f'tenha um ótimo dia, {name}!')