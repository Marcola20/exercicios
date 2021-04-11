#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#1 para binário, 2 para octal e 3 para hexadecimal.
print('-=-=-=- CONVERSÃO DE BASES -=-=-=-')
n = int(input('Digite um número inteiro: '))
print('''ESCOLHA UMA OPÇÃO DE CONVERSÃO
      [1] Binário 
      [2] Octal 
      [3] Hexadecimal ''')
opcao = int(input('Opção: '))
if opcao == 1:
    b = bin(n)
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f'{n} é {b[2:]} em binário')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
elif opcao == 2:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    o = oct(n)
    print(f'{n} é {o[2:]} em octal')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
elif opcao == 3:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    h = hex(n)
    print(f'{n} é {h[2:]} em hexadecimal')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
else:
    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
    print('| OPÇÃO INVÁLIDA! TENTE NOVAMENTE! |')
    print('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
