print('{:-^40}'.format('\033[:35mCASAS VADIA\033[m'))
n1 = float(input('\033[:30mDigite o valor da compra:R$ \033[m').strip())
print('{:-^40}'.format('\033[:30mFORMAS DE PAGAMENTO\033[m'))
n2 = int(input('''\033[:30mEscolha a forma de pagamento:\033[m

\033[4:35m[1] A vista Dinheiro/Cheque\033[m \n\033[4:31m[2] Débito\033[m \n\033[4:32m[3] Crédito menos de 2 vezes\033[m \n\033[4:34m[4] Crédito acima de 3 vezes\033[m\n 
\033[:30mDigite a Opção:\033[m '''))



dez = (n1 * 10) / 100
dezt = (n1 - dez)

cinco = (n1 * 5) / 100
cincot = n1 - cinco

duas = n1

vintej = (n1 * 20) / 100
juros = vintej + n1

if n2 == 1:
    print('\033[:30mPagamento em Dinheiro/Cheque tem 10% de desconto valor total é: R$ {:.2f}\033[m \033[:31m😍\033[m'.format(dezt))
elif n2 == 2:
    print('\033[:30mPagamento no Débito tem 5% de desconto valor total é: R$ {:.2f}\033[m \033[:31m💢\033[m'.format(cincot))
elif n2 == 3:
    print('\033[:30mPagamento no Crédito Avista ou até 2 Não possui Juros valor total é: R$ {:.2f}\033[m \033[:31m🙄\033[m'.format(n1))
elif n2 == 4:
    print('\033[:30mPagamento Parcelado em acima de 3 Vezes possui 20% de Juros valor total é: R$ {:.2f}\033[m \033[:31m😠\033[m'.format(juros))
    quanti = int(input('\033[:30mDigite em quantas vezes dejesa parcelar a compra: \033[m'))
    print('\033[:30mvocê escolheu parcelar em {} vezes o valor de cada parcela será de R$ {:.2f}\033[m \033[:34m🥇\033[m'.format(quanti, juros / quanti))
else:
    print('\033[;30;41mOpção invalida TENTE NOVAMENTE.\033[m')
print('{:-^40}'.format('\033[:30mFIM DA COMPRA\033[m'))



