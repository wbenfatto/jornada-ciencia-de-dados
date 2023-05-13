"""
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

"""

lista_numeros = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print(f'Número {numero} adicionado.')
    else:
        print('Número já está na lista.')
    
    continuar = input('Quer continuar? S/N: ').strip().upper()
    if(continuar[0] == 'N'):
        break

lista_numeros.sort()
print('Lista em ordem: ', lista_numeros)