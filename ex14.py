#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento do atleta e mostre sua
#categoria, de acordo com sua idade:
#- Até 9 Anos: Mirim
#- Até 14 Anos: Infantil
#- Até 19 Anos: Junior
#- Até 20 Anos: Sênior
#- Acima: Master
print('-=-=-=-=-= CNN -=-=-=-=-=')
i = int(input('Informe sua idade: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-')
if i <= 9:
    print('Sua categoriá é a Mirim')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
elif i <= 14 and i > 9:
    print('Sua categoriá é a Infantil')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
elif i <= 19 and i > 14:
    print('Sua categoriá é a Junior')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
elif i == 20:
    print('Sua categoriá é a Sênior')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
elif i > 20:
    print('Sua categoriá é a Master')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
