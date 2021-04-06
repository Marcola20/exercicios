#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o Porgrama vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado.
vc = float(input('O Valor da casa é R$'))
s = float(input('O seu salário é R$'))
a = int(input('Em quantos anos você irá pagar: '))
meses = a * 12
mensal = vc / meses
strinta = (s * 0.30) + s
if mensal <= strinta:
    print('Seu empréstimo foi aprovado!')
    print('Você irá pagar R${:.2f}'.format(mensal))
elif mensal > strinta:
    print('O empréstimo foi negado!')
