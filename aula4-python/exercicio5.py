"""
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
"""

lista = []

while 1:
    lista.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar? ').strip().upper()
    if continuar[0] == 'S':
        print('Continuando então...')
    else:
        print('Programa finalizado.')
        break
    

print(f'{len(lista)} números foram adicionados.')

lista.sort(reverse=True)
print(f'Esta é a lista em forma decrescente: {lista}')

if 5 in lista:
    print('5 foi digitado')
else:
    print('5 não foi digitado')

