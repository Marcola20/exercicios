#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
ang = float(input('Informe o ângulo: '))
n = radians(ang)
s = sin(n)
c = cos(n)
t = tan(n)
print('O ângulo {} tem o seno {:.3f}. cosseno {:.3f} e tangente {:.3f}'.format(ang, s, c, t))

