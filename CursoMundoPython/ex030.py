# trabalhando com impar e par

n1 = float(input('Digite um número: ').strip())

res = n1 % 2

if res == 1:
    print('O número digitado foi {:.0f} ele é ÍMPAR'.format(n1))
else:
    print('O número digitado foi {:.0f} ele é PAR.'.format(n1))

