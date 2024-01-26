#jogo melhorado de adivinhação
from random import randint

computador = randint(0, 10)

print('\033[30mSou seu computador \033[31m😃\033[m \033[30m... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinha qual foi?\033[m')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('\033[32mQual é o seu palpite?\033[m : ').strip())
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[35mMais... Tente novamente.\033[m')
        elif jogador > computador:
            print('\033[31mMenor... Tente novamente.\033[m')
print('\033[34mAcertou com {} tentativas. Parabéns ✔\033[m'.format(palpites))