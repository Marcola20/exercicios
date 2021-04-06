#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para sálarios superiores a R$1250,00, calcule um aumento de 10%.
#Para inferiores ou iguais, o aumento é de 15%.
sal = float(input('O seu salário é R$'))
if sal > 1250:
    ns = (sal * 0.10) + sal
    print('você recebeu 10% de aumento, seu novo salário é R${:.2f}'.format(ns))
else:
    ns = (sal * 0.15) + sal
    print('você recebeu 15% de aumento, seu novo salário é R${:.2f}'.format(ns))
