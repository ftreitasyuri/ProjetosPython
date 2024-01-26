# jogo jokenpo

from random import randint
from time import sleep # serva para poder colocar um tempo na execução
itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print('''\033[;30mSuas Opções:
[0] Pedra
[1] Papel
[2] Tesoura\033[m''')

jogador = int(input('\033[;30mQual é a sua jogada?\033[m ').strip())
print('\033[;31mJO\033[m')
sleep(1) # comando aqui com 1 segundo de demora
print('\033[;34mKEN\033[m')
sleep(1)
print('\033[;33mPO\033[m')
sleep(1)
print('\033[;31m-=-\033[m'*11)

print('\033[2;30mComputador Jogou : {}\033[m'.format(itens[computador])) # esse comando busca a biblioteca itens criada e joga dentro da variavel computador

print('\033[2;30mJogardor jogou : {}\033[m'.format(itens[jogador])) # já aqui ele joga o que tem la em itens dentro da variavel jogador

print('\033[;31m-=-\033[m'*11)

if computador == 0:               # pedra
    if jogador == 0:
        print('\033[4;32mEMPATE 💢\033[m')
    elif jogador == 1:
        print('\033[4;34mVocê Ganhou 😠\033[m')
    elif jogador == 2:
        print('\033[4;31mVocê Perdeu 🙄\033[m')
    else:
        print('OPÇÃO INVALIDA')

if computador == 1:             # papal
    if jogador == 0:
        print('\033[4;31mVocê Perdeu 🙄\033[m')
    elif jogador == 1:
        print('\033[4;32mEMPATE 💢\033[m')
    elif jogador == 2:
        print('\033[4;34mVocê Ganhou 😠\033[m')
    else:
        print('OPÇÃO INVALIDA')

if computador == 2:              # tesoura
    if jogador == 0:
        print('\033[4;34mVocê Ganhou 😠\033[m')
    elif jogador == 1:
        print('\033[4;31mVocê Perdeu 🙄\033[m')
    elif jogador == 2:
        print('\033[4;32mEMPATE 💢\033[m')
    else:
        print('OPÇÃO INVALIDA')

print('\033[7;;40mFIM DE JOGO\033[m') # usando inversao de cores

''' daqui para baixo foi o meu exemplo
if jogador == 0 and computador == 1:
    print('O computador jogou {} e você {} o computador ganhou 🙄'.format(itens[computador], itens[jogador]))
elif jogador == 0 and computador == 2:
    print('O computador jogou {} e você {} você ganhou 😠'.format(itens[computador], itens[jogador]))

elif jogador == 1 and computador == 0:
    print('O computador jogou {} e você jogou {} o computador ganhou 🙄'.format(itens[computador], itens[jogador]))
elif jogador == 1 and computador == 2:
    print('O computador jogou {} e você jogou {} Você  ganhou 😠'.format(itens[computador], itens[jogador]))

elif jogador == 2 and computador == 0:
    print('O computador jogou {} e você jogou {} O computador ganhou 🙄'.format(itens[computador], itens[jogador]))
elif jogador == 2 and computador == 1:
    print('O computador jogou {} e você jogou {} você ganhou 😠'.format(itens[computador], itens[jogador]))
   '''

