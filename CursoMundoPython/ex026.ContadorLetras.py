frase = str(input('Digite uma frase: ')).strip()

subir = frase.upper() # ao inves de criar outra variavel poderia add o upper la em cima junto com o strip().upper()

print('A letra A aparece {} vezes na frase digitada.'.format(subir.count('A')))

print('A primeira letra A aparece na posição {}.'.format(subir.find('A')+1))

print('A ultima letra A digitada na frase aparece na posição {}.'.format(subir.rfind('A')+1))

