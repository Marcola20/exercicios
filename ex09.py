#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
dkm = float(input('Quantos Km é sua viagem? '))
if dkm <= 200:
    p = dkm * 0.50
    print(f'O valor da sua passagem é de R${p:.2f}')
elif dkm > 200:
    p = dkm * 0.45
    print(f'O valor da sua passagem é de R${p:.2f}')
