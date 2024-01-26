salario = float(input('Digite seu salário: RS ').strip())

if salario >= 1250:
    print('Seu salário aumetou 10% ficando com o total de RS {}'.format(salario // 10 + salario))
else:
    print('Seu salário aumentou 15% ficando com o total de RS {}'.format(salario // 15 + salario))
print("Parabens você foi reconhecido continui dando o melhor de si no seu trabalho!")


