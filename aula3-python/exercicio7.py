#Faça um programa que simule uma contagem regressiva de um 
# foguete antes do lançamento para NASA. O usuário deve digitar o número de segundos 
# da contagem regressiva e o programa deve exibir a contagem regressiva em ordem decrescente.

from time import sleep

segundos = int(input('Digite o número de segundos: '))

while segundos > 0:
    print(segundos)
    sleep(1)
    segundos -= 1

print('Decolar!!!')
