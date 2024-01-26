from datetime import date
# comando para importar apenas o date da biblioteca dataime
atual = date.today().year

nasc = int(input('Digite o ano do seu nascimento: ').strip())

idade = atual - nasc

print('O atleta tem \033[1;34m{}\033[m anos de idade.'.format(idade))

if idade <= 14:
    print('Você é um atleta \033[1;30m MIRIM \033[m')
elif idade > 14 and idade < 19:
    print('Você é uma atleta \033[1;31m JUNIOR\033[m')
elif idade > 20 and idade < 30:
    print('Você é uma atleta \033[1;32m SENIOR \033[m')
elif idade > 30 and idade < 40:
        print('Você é uma atleta \033[1;33m MASTER \033[m parabens.')

print('\033[1;4;34mThe End \n R.I.P\033[m')
