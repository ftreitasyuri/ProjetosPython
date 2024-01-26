kms = float(input('Quantos Km você vai rodar? '))

n1 = 0.50
n2 = 0.45

if kms <= 200:
    print('Sua passagem vai curstar R${:.2f}'.format(kms*n1))
else:
    print('Sua passagem vai curstar R${:.2f}'.format(kms*n2))
