#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
import random
print('O professor irá sortear entre João, Marcos, Ana e Leticia para apagar o quadro')
lista = ['João', 'Marcos', 'Ana', 'Leticia']
sorteio = random.choice(lista)
print('O escolhido foi o(a) {}'.format(sorteio))
