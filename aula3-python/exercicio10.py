#Um programa que simule o jogo de adivinhação, 
#em que o usuário deve tentar adivinhar um número escolhido pelo programa. 
#O programa deve informar ao usuário se o número digitado
#é maior ou menor do que o número escolhido. 
#O jogo deve continuar até que o usuário acerte o número escolhido.

import random
numero_sorteado = random.randint(1, 10)
numero = 0

while numero != numero_sorteado:
    numero = int(input('Digite um número de 1 a 10: '))
    if numero < numero_sorteado:
        print(f'O número sorteado é maior que {numero}\n')
    elif numero > numero_sorteado:
        print(f'O número sorteado é menor que {numero}\n')
    else:
        print(f'Parabéns, o número sorteado foi {numero}\n')
        break