frase = str(input('Digite uma frase: ').strip()).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): # esse comando esta pegando o que for gravado em junto ex yuri e contando de tras pra frente
    inverso += junto[letra]
print('O inverdo de \033[32m{}\033[m é \033[31m{}\033[m '.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é uma palíndromo')
print('FIM')



'''a sacada da casa
a torre da derrota
o lobo ama o bolo 
anotaram a data da maratona'''
