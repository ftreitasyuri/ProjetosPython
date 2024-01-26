
mediaidade = 0
somaidade = 0
manold = 0
nameold = ''
totalmulher = 0

for p in range(1, 5):
    print('-----{}ª Pessoa-----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: ').strip())

    somaidade += idade # lembrar de deixar a variavel dentro do for

    if p == 1 and sexo in 'Mm': # se p for igual a 1 e sexo igual a m ou M
        manold = idade # entao manold recebe o valor de idade
        nameold = nome # e nameold recebe o valor de nome

    if sexo in 'Mm' and idade > manold: # se sexo do proximo laço ainda for M ou m entao
        manold = idade # manold recebe idade que troca o valor antigo pelo valor novo que é maior do que o antigo
        nameold = nome # e nameold tambem troca o nome

    if sexo in 'Ff' and idade < 20: # se sexo for igual a F ou f e menor doque 20 entao
        totalmulher += 1 # totalmulher recber o valor de sexo e soma com o valor de totalmulher ex 1 + 1 = 2 mulheres
mediaidade = somaidade / 4



print('A média de idade do grupo é de {}'.format(mediaidade))
print('O Home mais velho do grupo é o {} com {} anos'.format(nameold, idade))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalmulher))