#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
d = int(input('Informe por quantos dias ele foi alugado: '))
kmp = float(input('Informe quantos Km o carro percorreu: '))
vf = (d * 60) + (kmp * 0.15)
print('O valor total a se pagar é de R${:.2f}'.format(vf))
