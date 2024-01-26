while True:
    n = int(input('Deseja saber a tabuada de qual valor?: ').strip())
    if n < 0:
        break
    print('-'*30)

    for cont in range(1, 11):
       print(f'{n} x {cont} = {n*cont}')

    print('-' * 30)
print('-' * 30)
print('Programa tabuada encerrada!')
print('-' * 30)