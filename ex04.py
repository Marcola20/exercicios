#Faça um programa que leia o comprimento do cateto oposto e de um cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
print('Informe o catesto oposto e o cateto adjacente de um triângulo retângulo.')
op = float(input('O comprimento do cateto oposto é: '))
ad = float(input('O comprimento do cateto adjacente é: '))
h = hypot(op, ad)
print('A hipotenusa deste triângulo retângulo é: {:.3f}'.format(h))
