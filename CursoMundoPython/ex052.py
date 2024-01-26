# para achar o numero primo tem que ser divido por 1 e por ele mesmo.
num = int(input('Digite um número: ').strip())
tot = 0
for cont in range(1, num +1):
    if num % cont == 0:
        print('\033[34m', end=' ⏩ ')
        tot += 1
    else:
        print('\033[31m', end=' ⏩ ')

    print('{}'.format(cont))

print('O número {} foi divisivel {}'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
print('FIM')