# fazendo quase uma calculadora
from time import sleep
n1 = int(input('\033[34mDigite o Primeiro valor:\033[m ').strip())
n2 = int(input('\033[34mDigite o Segundo valor:\033[m ').strip())
opcao = 0

while opcao != 5:
    print('-=-' * 20)
    print('''\033[35m<<<MENU>>>
[1] Somar
[2] Multiplicar
[3] Maior Valor
[4] Novos Números
[5] Sair do Programa\033[m''')
    opcao = int(input('\033[34m>>>>Digite sua opção:\033[m '))
    if opcao == 1:
        soma = n1 + n2
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        print('-=-' * 20)
        print('\033[33mA soma dos valores digitados é de {}\033[m'.format(soma))

    elif opcao == 2:
        mult = n1 * n2
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        print('-=-' * 20)
        print('\033[33mA multiplicação entre os valores digitados é de {}\033[m'.format(mult))

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        print('-=-' * 20)
        print('\033[33mO maior valor digitado foi {}\033[m'.format(maior))

    elif opcao == 4:
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        print('-=-' * 20)
        print('\033[30mDigite os valores novamente.\033[m')
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        n1 = int(input('\033[34mDigite o primeiro valor:\033[m '))
        n2 = int(input('\033[34mDigite o segundo valor:\033[m '))

    elif opcao == 5:
        print('\033[30mPROCESSANDO...\033[m')
        sleep(1)
        print('-=-' * 20)
        print('Finalizado')
        print('-=-' * 20)
    else:
        print('Opção invalida. Tente novamente')


print('💢💢💢💢💢💢💢')
