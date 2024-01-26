
n1 = float(input('Digite a primeira nota do aluno: ').strip())
n2 = float(input('Digite a segunda nota do aluno: ').strip())

media = (n1 + n2) / 2



if media >= 7:
    print('Parabens você passou! sua média é: \033[4:32m{}\033[m'.format(media))
elif media >= 5 and media < 7:
    print('Sinto muito você ficou de recuperação seu média é: \033[4;35m{}\033[m'.format(media))
else:
    print('Sinto muito você foi reprovado. \033[;31m:(\033[m sua média é: \033[4;31m{}\033[m'.format(media))

print('Tenha uma bom dia!!!')
