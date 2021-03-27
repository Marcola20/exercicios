#Faça um programa que leia a largura e a altura de uma
#Parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada
#litro de tinta pinta um área de 2m².
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))