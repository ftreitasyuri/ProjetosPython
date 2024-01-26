import random
n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 3° aluno: '))
n4 = str(input('Digite o nome do 4° aluno: '))
# para o python uma lista fica entre []

lista = [n1, n2, n3, n3]

esc = random.choice(lista)



print('O aluno escolhido para apagar o quadro é: {}'.format(esc))


