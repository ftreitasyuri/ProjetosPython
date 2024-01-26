n = str(input('Digite seu nome inteiro: ')).strip()
nome = n.split() # .split() serve para dividir por espaços e fazer uma lista

print('Seu nome inteiro é {}.'.format(n))
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) #para mostrar o ultimo nome digitado





