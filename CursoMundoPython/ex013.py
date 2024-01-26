n1 = float(input('Qual o salário do funcionário ? R$:  '))

au = (n1 * 15 / 100)

nv = n1+au

print('Parabens você foi promovido e seu salário teve um aumento de 15%, ou seja de {} foi para R$ {} '.format(n1, nv))
print('Valor do aumento foi de {}'.format(au))