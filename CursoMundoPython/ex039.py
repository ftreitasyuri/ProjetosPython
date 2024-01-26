import datetime

atual = datetime.date.today().year

nasc = int(input('Digite o ano do seu nascimento: ').strip())

idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade > 18:
    print('O ano do seu alistamento já passou!!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para você se alistar.'.format(saldo))