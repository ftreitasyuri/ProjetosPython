# validação de dados.

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper() [0] # esse zero sifnifica pega só a primeira letra que foi digitada
#print('Voce digitou {}'.format(sexo))

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))