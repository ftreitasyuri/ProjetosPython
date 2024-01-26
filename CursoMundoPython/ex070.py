totgasto = 0
maisdmil = 0
maisbarato = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço R$ '))
    cont += 1
    totgasto += preco

    if preco > 1000:
        maisdmil += 1

    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        barato = produto


    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break





print('{:-^40}'.format('FIM DO PROGRAMA'))

print(f'Valor Total da Compra: R$ {totgasto:.2f}')

print(f'{maisdmil} produtos custam mais de mil reais.')

print(f'O produto mais barato foi {barato} e custa R$ {maisbarato:.2f}')