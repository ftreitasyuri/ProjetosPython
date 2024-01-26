soma = 0
men = 0
woman = 0

while True:


    idade = int(input('Digite a Idade: '))
     
    sexo = ' '
    while sexo not in 'MF':
        print('-=' * 20)
        sexo = str(input('Sexo [M:F]: ')).strip().upper()[0]

    if idade >= 18:
        soma += 1
    resp = ' '

    if sexo == 'M':
        men += 1

    if sexo == 'F':
        if idade < 18:
            woman += 1

    while resp not in 'SN':
            print('-=' * 20)
            resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break











print('-='*20)
print(f'Pessoas cadastradas com mais de 18 anos foram ({soma}).')
print('-='*20)
print(f'Total de homens cadastrados ({men}).')
print('-='*20)
print(f'Mulheres cadastadas com menos de 18 anos {woman}.')
print('-='*20)
print('Acabou')
