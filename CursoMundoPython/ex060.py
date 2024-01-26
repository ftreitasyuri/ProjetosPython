# usando biblioteca math para pegar o fatorial

from math import factorial

n1 = int(input('\033[30mDigite o número para calcular o seu Fatorial:\033[m '))

contador = n1


print('\033[30mCalculando {}! =\033[m '.format(n1), end=' ')

while contador > 0:
    print('\033[31m{}\033[m'.format(contador), end=' ')
    print('\033[36mx\033[m ' if contador > 1 else '\033[36m=\033[m ', end='')

    contador -= 1
print('\033[32m{}\033[m'.format(factorial(n1)))
