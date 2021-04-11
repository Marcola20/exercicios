#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
#de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do Peso
#- Entre 18.5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 aé 40: Obesidade
#- Acima de 40: Obesidade Móbida
print('-=-=-=-=- Programa IMC -=-=-=-=-')
a = float(input('Informe sua altura: '))
p = float(input('Informe seu peso: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está com peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está um pouco acima do peso.')
elif imc >= 30 and imc <= 40:
    print('Você está obeso.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
