peso = float(input('Digite o seu peso (KG): ').strip())
altura = float(input('Digite sua altura (m): ').strip())

imc = peso / (altura ** 2)

print('O seu indice de massa corporal (IMC) é : {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você está DESNUTRIDO')


elif imc >= 18.6 and imc <= 24.9:
    print('Você está no peso IDEAL.')


elif imc > 25 and imc <= 29.9:
    print('Você está acima do PESO.')


elif imc > 30 and imc <= 34.9:
    print('Você está no I GRAU DE OBESIDADE')


elif imc >= 35.0 and imc <= 39.9:
    print('Você está no II GRAU DE OBESIDADE -SEVERA-')


elif imc > 40.0:
    print('Você está no III GRAU DE OBESIDADE -MÓRBIDA-')


print('-=-' * 20)
print('Lembre-se a saúde é o principal para\n você ter uma vida boa cuide-se.')

