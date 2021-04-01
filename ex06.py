#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
print('Escolhendo aluno para apagar o quadro')
a1 = input('Nome do Aluno 1: ')
a2 = input('Nome do Aluno 2: ')
a3 = input('Nome do Aluno 3: ')
a4 = input('Nome do Aluno 4: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('Enre {}, {}, {} e {}, o escolhido foi o(a) {}'.format(a1, a2, a3, a4, sorteio))
