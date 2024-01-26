
from random import randint
tipo = ' '
v = 0
while True:

    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR ou IMPAR ? [P/I]: ')).strip().upper()[0]

    jogador = int(input('Escolha um número entre 1 E 10: '))
    computador = randint(0, 10)

    total = jogador + computador


    if tipo == 'P':
        if total % 2 == 0:
            print(f'Parabens você ganhou. Você jogou {jogador} e o computador jogou {computador} a soma foi {total} ou seja PAR!!!')
            v += 1
        else:
            print(f'Xi você perdeu. Você jogou {jogador} e o computador jogou {computador} a soma foi {total} ou seja IMPAR!!!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print(f'Parabens você ganhou. Você jogou {jogador} e o computador jogou {computador} a soma foi {total} ou seja IMPAR!!!')
            v += 1
        else:
            print(f'Xi você perdeu. Você jogou {jogador} e o computador jogou {computador} a soma foi {total} ou seja PAR!!!')
            break


print('Game Over!!!')
print(f'Você Ganhou {v} vezes')