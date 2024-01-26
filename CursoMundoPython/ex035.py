# aula de principios matematicos para forma um triangulo todos os seguimentos tem que ser menores doq a soma de 2 deles
print('--=--' * 20)
print('Analisador de Triângulos')
print('--=--' * 20)

r1 = float(input('Digite o primeiro seguimento: ').strip())
r2 = float(input('Digite o segundo seguimento: ').strip())
r3 = float(input('Digite o terceiro seguimento: ').strip())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem forma um TRIANGULO.')
else:
    print('Os seguimentos acima não podem forma um TRIANGULO')
