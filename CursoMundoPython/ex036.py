n1 = float(input('Qual o valor da casa que você deseja comprar? ').strip())
n2 = float(input('Em quantos anos você pretende pagar esta casa? ').strip())
n3 = int(input('Qual o valor do seu salário? R$ ').strip())

val1 = (n1 / n2) / 12

val2 = n3 * 30/100

print('O valor das parcelas será R$ {:.2f}'.format(val1))
print('E o valor mínimo é de R$ {}'.format(val2))
if val1 <= val2:
    print('Parabens Financiamento aprovado!! ;)')
else:
    print('Sinto muito financiamento negado. :( ')

print('Tenha um bom dia!!!')
