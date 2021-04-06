#Faça um prorgrama que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número digitado.')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número digitado.')
else:
    print(f'{n3} é o maior número digitado.')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número digitado.')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número digitado.')
else:
    print(f'{n3} é o menor número digitado.')
