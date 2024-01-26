# trabalhando com for e acumulador

soma = 0 # é uma acumulador
c = 0 # é um contador
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        c = c + 1
        soma = soma + cont

print('A soma de todos os \033[;32m{}\033[m valores solicitados é \033[;31m{}\033[m 👽'.format(c, soma))

