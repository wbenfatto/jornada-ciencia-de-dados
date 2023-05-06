# Repetir até que o usuário digite um número positivo

numero = -1

while numero % 2 != 0:
    numero = int(input('Digite um número positivo: '))

print(f'O número é {numero}')