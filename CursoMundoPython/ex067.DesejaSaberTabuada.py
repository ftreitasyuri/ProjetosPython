while True:
    num = int(input('Deseje saber a tabuada de qual número? : ').strip())

    if num < 0:
        break

    print('-' * 30)
    for cont in range(1, 11):

        print(f'\033[32m{num}\033[m X \033[32m{cont}\033[m = \033[31m{num*cont}\033[m')

    print('-' * 30)

print(f'Você digitou o número {num} que é negativo, FIM DO PROGRAMA')