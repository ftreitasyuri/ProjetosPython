# tabuada com for = laço

n1 = int(input('Digite um número: ').strip())

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n1, c, n1*c)) # trabalhando com for para repetir o numero e multiplicar por ele.
print('FIM')
