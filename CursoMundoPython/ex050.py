'''soma = 0 # acumulador
cont = 0 # contator
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0: # estamos vendo se num é divisivel por 2 e se o resultador da divisao é = a 0 zero.
        soma += num
        cont += 1
print('Você informou \033[;30m{}\033[m números pares e a soma foi \033[;30m{}\033[m'.format(cont, soma))'''

soma = 0
cont = 0

for impar in range(1, 9): # ele vai repetir o comando debaixo de 1 até 8 vezes lembrando que ele ignora o ultimo numero
    n1 = int(input('Digite o {} valor: '.format(impar)))
    if n1 % 3 == 0:
        soma += n1
        cont += 1
print('Você informou {} valores impar a soma entre ele é {}'.format(cont, soma))


