vel = float(input('Qual velocidade que você está andando ? KM/h:  ').strip())
multpk = 7.00

valmt = (vel - 80) * multpk



if vel > 80:
    print('Você tomou uma multa de R$ {}, reduza sua velocidade e dirija com responsabilidade.'.format(valmt))
else:
    print('Você esta dentro do limite permitido. Parabens você é um motorista reponsável. :)')

print('Tenha um bom dia, dirija com segurança.')
