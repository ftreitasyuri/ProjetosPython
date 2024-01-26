import datetime
ano = int(input('Qual ano você deseja analisar ? Coloque 0 se quiser analisar o ano atual: ').strip())

if ano == 0:
    ano = datetime.date.today().year # para pegar o ano atual importando datetime

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: # se o resto da divisao for 0 é bissexto mas se for multiplo de 100 nao é se for multiplo de 400 tbm nao é
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))
