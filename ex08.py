#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual a velocidade que o carro está: '))
if v > 80:
    m = (v-80) * 7
    print(f'Você foi multado! O valor a pagar é de RS{m:.2f}')
else:
    print('Tudo bem. Pode continuar!')
