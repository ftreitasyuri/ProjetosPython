num = int(input('Informe um número: '))
u = num // 1 % 10 # unidade
d = num // 10 % 10 # dezena
c = num // 100 % 10 # centena
m = num // 1000 % 10 # milhar


print('Analisando o número {}'.format(num))

print('Unidade: {} '.format(u))

print('Dezena: {}'.format(d))

print('Centena: {}'.format(c))

print('Milhar: {}'.format(m))
