nome = str(input('Digite seu nome completo: ')).strip() # esse strip vai eliminar os espaços antes de depois.
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) # essa função a esquerda é para eliminar os espaços entre as palavaras
#print('Seu primeiro nome tem {} de letras'.format(nome.find(' '))) # para verificar quantas letras tem no primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))  # para verificar quantas letras tem no primeiro nome






