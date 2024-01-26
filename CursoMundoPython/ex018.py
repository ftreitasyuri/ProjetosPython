import math
angulo = float(input('Digite o Ângulo que você deseja: '))

seno = math.sin(math.radians(angulo)) # sin é seno e redians é para converter
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo)) # cos é igual a cosseno
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

tang = math.tan(math.radians(angulo)) # tan é tangente
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tang))

