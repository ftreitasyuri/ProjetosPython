#Joguinho de adivinhação

import random
import time
print('--=--' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--=--' * 10)
comp = random.randint(0, 5) # FAZ O COMPUTADOR SORTEAR UM NUMERO ENTRE O RANGE

n1 = int(input('Digite o número: ').strip())
print('Pensei no número {}'.format(comp))
print('Vamos ver se você acertou :)')
# esse comando serve para replicar varias vezes alguma coisa print('--=--' * 10)
print('PROCESSANDO...')
time.sleep(3) # esse comando esta importando a função sleep da biblioteca time o 3 significa quantidade de segundos

if n1 == comp:
    print('Parabéns você acertou!!!')
else:
    print('Má OÊ você errou. Próximo!!!')





