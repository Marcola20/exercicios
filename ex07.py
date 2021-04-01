#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('Oi, vamos jogar! Adivinhe em qual número de 1 a 5 estou pensando..')
n = int(input('O número é: '))
l = [1, 2, 3, 4, 5]
s = random.choice(l)
if n == s:
    print('WOW, Acertou. Parabéns pela vitória!')
else:
    print('Errou. Tente na próxima! Eu pensei no número {}.'.format(s))
