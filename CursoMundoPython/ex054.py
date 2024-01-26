# primeira parte para analise de dados
from datetime import date

atual = date.today().year

totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? ANOA: '.format(pessoa).strip()))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos \033[31m{}\033[m pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos \033[32m{}\033[m pessoas menores de idade'.format(totmenor))

